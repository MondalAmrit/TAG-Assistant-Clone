import execute_command from "@/components/CommandExecutor";
import React, { useState, useCallback } from "react";
import {
  View,
  TextInput,
  Pressable,
  ScrollView,
  Text,
  StyleSheet,
  useColorScheme,
} from "react-native";

interface Message {
  sender: "user" | "bot";
  message: string;
}

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState<string>("");
  const [isFirstMessage, setIsFirstMessage] = useState<boolean>(false);
  const colorScheme = useColorScheme();

  const sendMessage = useCallback(() => {
    if (inputText.trim() === "") return;

    // Add user message to the chat
    setMessages([...messages, { sender: "user", message: inputText }]);

    // Execute the command.
    execute_command(inputText);

    setInputText("");

    // Handle sending message to backend and bot's response here
  }, [inputText, messages]);

  const handleKeyPress = useCallback(
    (event: any) => {
      if (event.nativeEvent.key === "Enter") {
        sendMessage();
      }
    },
    [sendMessage]
  );

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
          onKeyPress={handleKeyPress} // Call handleKeyPress function on key press
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
