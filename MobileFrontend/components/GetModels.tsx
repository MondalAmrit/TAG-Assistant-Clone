import * as onnx from 'onnxruntime-react-native';
import * as bertTokenizer from './bert-tokenizer/tokenizers';
import { Alert } from 'react-native';
import { Asset } from 'expo-asset';

////////////////////////////////////////////
// GPT Model
export async function getGPTModel(): Promise<{ model: onnx.InferenceSession | null }> {
  let model = null, tokenizer = null;
  try {
    console.log('loading the model...');
    const assets = await Asset.loadAsync(require('@/assets/models/GPT_MODEL.with_runtime_opt.ort'));
    
    const modelUri = assets[0].localUri;
    if (!modelUri) {Alert.alert('No Such model found');}
    else {
      // MobileFrontend\assets\models\GPT_MODEL.with_runtime_opt.ort
      model = await onnx.InferenceSession.create(modelUri);
      if (model)
      console.log('Model Loaded Successfully');
    }
  } catch(e) {Alert.alert('Error in loading the Model'); console.log(e);}
  return { model }
}

export async function gptGenerate(model: onnx.InferenceSession | null , tokenizer: bertTokenizer.BertTokenizer | null, text: string) {
    if (model === null) {Alert.alert('Onnx version Model must be present'); return null;}
    if (tokenizer === null) {Alert.alert('Tokenizer is not loaded'); return null;}
    // Convert text into tensor
    let seq_len = 128;
    let generation = tokenizer.encode([101] + text + [tokenizer.getToken('[QUES]')],
                                null,  {add_special_tokens:false});
    let new_generation = [];
    // Generate the tokens until we hit [SEP] token (ID: 102)
    var new_x = -1, r = null;
    while (new_x !== 102 || new_generation.length < 200) {
        // Run the model with the last `seq_len` tokens from the `generation` array
        r = await model.run({ input: new onnx.Tensor(
          'float32',
          new Float32Array(generation.slice(-seq_len)),
          [1, Math.max(seq_len, generation.length)]
        )});
        // Extract logits from the result
        const logits = r.logits; // Assuming the logits are directly accessible from the result
        // Convert logits tensor data to an array
        const logitsDataArray = Array.from(logits.data as Iterable<number>);
        const maxLogit = Math.max(...logitsDataArray);

        // Get the new_x from the logits
        const new_x_index: number = logitsDataArray.indexOf(maxLogit); // Find the index of the token with the highest probability
        new_x = new_x_index + 1; // Convert index to token ID (assuming token IDs start from 1)
        // Add new_x to the `generation` array
        generation.push(new_x);
        if (new_x != 102) new_generation.push(new_x);
    }
    return tokenizer.decode(new_generation);
}