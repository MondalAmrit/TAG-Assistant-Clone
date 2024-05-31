from transformers import BertTokenizer

class SlotFillingAnnotations:
    @staticmethod
    def generate_annotations(prompt, slot_values):
        # Initialize BERT tokenizer
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        
        # Pre-process the prompt to extract slot placeholders
        slot_placeholders = {}
        for word in prompt.split():
            if "{" in word and "}" in word:
                slot_label = word.replace("{", "").replace("}", "")
                slot_placeholders[slot_label] = slot_values.get(slot_label, "")
        
        # Tokenize all slot values simultaneously
        slot_tokens = []
        for slot_value in slot_placeholders.values():
            slot_tokens.append(SlotFillingAnnotations.tokenize_slot_value(tokenizer, slot_value))
        
        # Tokenize the prompt
        tokens = SlotFillingAnnotations.tokenize_sentence(tokenizer, prompt, slot_placeholders.keys(), slot_tokens)
        
        return tokens
    
    @staticmethod
    def tokenize_sentence(tokenizer, sentence, slot_labels, slot_tokens):
        # Replace slot placeholders with special tokens
        for slot_label, slot_token in zip(slot_labels, slot_tokens):
            sentence = sentence.replace("{" + slot_label + "}", slot_token)
        
        # Tokenize the entire sentence
        tokens = tokenizer.tokenize(sentence)
        
        # Annotate slot tokens
        annotated_tokens = []
        in_slot = False
        for token in tokens:
            if token.startswith("[SLOT]") and token.endswith("[/SLOT]"):
                slot_label = token.split("_")[1]
                if in_slot:
                    annotated_tokens.append("I-" + slot_label)
                else:
                    annotated_tokens.append("B-" + slot_label)
                    in_slot = True
            else:
                annotated_tokens.append("O")
                in_slot = False
        
        return annotated_tokens
    
    @staticmethod
    def tokenize_slot_value(tokenizer, slot_value):
        # Tokenize slot value
        tokens = tokenizer.tokenize(slot_value.replace("#", ""))
        
        # Wrap tokens with special symbols
        return "[SLOT] " + " ".join(tokens) + " [/SLOT]"

if __name__ == "__main__":
    example = "What's the weather like in {Location} today?"
    slot_values = {"Location": "Delhi"}
    
    annotated_tokens = SlotFillingAnnotations.generate_annotations(example, slot_values)
    print("Annotated Tokens:", annotated_tokens)
