/* eslint-disable react/prop-types */
import { useRef } from "react";
import axios from "axios";
import "./input.css";

const backend_API_URL = import.meta.env.VITE_backend_API_URL;

const Input = ({ time, setIsGenerating, setMessages, isGenerating }) => {
  const promptRef = useRef();

  const handlePrompt = async (e) => {
    e.preventDefault();
    try {
      const prompt = promptRef.current.value.trim();
      if (!prompt) {
        promptRef.current.value = "";
        return;
      }
      promptRef.current.value = "";
      setMessages((prev) => [
        ...prev,
        {
          user: true,
          msg: prompt,
          time: time(),
        },
      ]);
      setIsGenerating(true);
      const response = await axios.post(`${backend_API_URL}/intentResponse`, {
        query: prompt,
      });
      const msg = response.data;
      setIsGenerating(false);
      setMessages((prev) => [
        ...prev,
        {
          user: false,
          msg: msg.response,
          time: time(),
        },
      ]);
    } catch (error) {
      console.log("Error in handlePrompt:", error);
    }
  };

  return (
    <div className="input-container">
      <form onSubmit={handlePrompt} className="input-field">
        <input
          ref={promptRef}
          type="text"
          placeholder="Enter a prompt here..."
        />
        <button type="submit" disabled={isGenerating}>
          <span className="material-symbols-outlined">send</span>
        </button>
      </form>
    </div>
  );
};

export default Input;
