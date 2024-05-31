import execute_command from '@/components/CommandExecutor';
import React, { useState, useCallback, useEffect } from 'react';
import { View, TextInput, Pressable, ScrollView, Text, StyleSheet, useColorScheme,Alert } from 'react-native';
import { router } from 'expo-router';

// ML Imports
import * as Model from '@/components/GetModels';
import * as onnx from 'onnxruntime-react-native';
import * as bertTokenizer from '@/components/bert-tokenizer/tokenizers';
import * as samplingTech from '@/components/getMultinomialSamples';
import * as vocabJson from '@/assets/nova_tokenizer/tokenizer.json';
import * as configJson from '@/assets/nova_tokenizer/tokenizer_config.json';

interface Message {
  sender: "user" | "bot";
  message: string;
}

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState<string>("");
  const [isFirstMessage, setIsFirstMessage] = useState<boolean>(true);
  const colorScheme = useColorScheme();
  const seq_len: number = 128;
  const vocab_size: number = 30523;
  // ML state Managers
  const [model, setModel] = useState<onnx.InferenceSession | null>(null); // State to hold the model
  const tokenizer = new bertTokenizer.BertTokenizer(vocabJson, configJson);

  // Load the GPT model when the component mounts
  useEffect(() => {
    const loadModel = async () => {
      try {
        const r = await Model.getGPTModel();
        setMessages([...messages,{ sender: 'bot', message: 'Hi, How can I help you?'}])
        setModel(r.model);
      } catch (error) {
        Alert.alert('Error in loading the Model');  router.replace('/');
      }
    };
    loadModel(); // Call the function to load the model
  }, []); // Empty dependency array ensures this effect runs only once, when the component mounts
  
  async function autoGenerateTokens(arr:number[], num_tokens: number): Promise<number[]> {
    if (!model || !tokenizer) {
      if (!tokenizer) console.log("Tokenizer not present");
      else console.log("Model not present");
      console.log("Either model or tokenizer is not present"); return [];}
    let generatedTokens = [];
  
    for (let i = 0; i < num_tokens; i++) {
      arr = arr.slice(-seq_len);  // Slice the array to the latest generation
      let tens = new onnx.Tensor("int64", arr, [1,arr.length]);
      let res = (await model.run({ "x": tens }))["logits"];
      let [B, S, V] = res.dims;
      let d = res.data.slice(((S - 1) * V), ((S) * V));
      let sfRes = samplingTech.applySoftmax(Object.values(d));
      let mltiNomRes = samplingTech.multinomial(sfRes);
  
      // Check if the generated token is the [SEP] token (102)
      if (mltiNomRes[0] === 102) break;
      
      generatedTokens.push(mltiNomRes[0]);
      arr.push(mltiNomRes[0])
  
    }
  
    return generatedTokens;
  }

  const sendMessage = useCallback(async () => {
    if (inputText.trim() === '') return;

    // Add user message to the chat
    setMessages((prevMessages) => [...prevMessages, { sender: 'user', message: inputText }]);
    if (!tokenizer || !model) {
      if (!tokenizer) console.log("Tokenizer not present");
      else console.log("Model not present");
      console.log("Something is wrong"); return ;}
    let arr = tokenizer.encode('[CLS] ' + inputText + ' [QUES] ',null,{add_special_tokens:false}).slice(-seq_len);
    if (arr.length < 1) return ;
    let res = await autoGenerateTokens(arr, 100);
    let ans = 'There is some internal error';
    if (res.length > 0)  ans = tokenizer.decode(res);            

    // Add bot message to the chat
    setMessages((prevMessages) => [...prevMessages, { sender: 'bot', message: ans }]);
    execute_command(inputText);
    setInputText('');

    // Handle sending message to backend and bot's response here
  }, [inputText, messages]);

  return (
    <View
      style={[
        styles.container,
        { backgroundColor: colorScheme === "dark" ? "black" : "white" },
      ]}
    >
      {isFirstMessage ? (
        <ScrollView style={styles.chatContainer}>
          {messages.map((msg, index) => (
            <View
              key={index}
              style={[
                styles.messageContainer,
                msg.sender === "user" ? styles.userMessage : styles.botMessage,
              ]}
            >
              <Text>{msg.message}</Text>
            </View>
          ))}
        </ScrollView>
      ) : (
        <View style={styles.chatInfoContainer}>
          <View style={styles.chatInfo}></View>
          <View style={styles.chatInfo}></View>
          <View style={styles.chatInfo}></View>
        </View>
      )}
      <View style={styles.inputContainer}>
        <TextInput
          style={[
            styles.input,
            colorScheme === "dark" ? { color: "white" } : { color: "black" },
          ]} // Set text color based on color scheme
          value={inputText}
          onChangeText={setInputText}
          placeholder="Type your message..."
        />
        <Pressable onPress={sendMessage} style={styles.button}>
          <Text>Send</Text>
        </Pressable>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    flexDirection: "column",
    justifyContent: "space-between",
  },
  chatContainer: {
    flex: 1,
    marginBottom: 20,
    marginTop: 30,
  },
  messageContainer: {
    maxWidth: "80%",
    padding: 10,
    marginBottom: 10,
    borderRadius: 10,
  },
  chatInfoContainer: {
    flex: 0.95,
    gap: 20,
    flexDirection: "column",
    justifyContent: "space-between",
  },
  chatInfo: {
    flex: 1,
    borderWidth: 1,
    borderColor: "#fff",
    borderRadius: 5,
    backgroundColor: "transparent",
  },
  userMessage: { alignSelf: "flex-end", backgroundColor: "#e0e0e0" },
  botMessage: { alignSelf: "flex-start", backgroundColor: "#aed581" },
  inputContainer: { flexDirection: "row", alignItems: "center" },
  input: {
    flex: 1,
    marginRight: 10,
    padding: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
  },
  button: { padding: 10, backgroundColor: "#007BFF", borderRadius: 5 },
});

export default ChatInterface;
