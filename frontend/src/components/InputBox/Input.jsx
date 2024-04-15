import { useRef } from "react";
import axios from "axios";
import "./input.css";

const Input = () => {
  const promptRef = useRef();
  const backend_API_URL = import.meta.env.VITE_backend_API_URL;

  const handlePrompt = async (e) => {
    e.preventDefault();
    try {
      const prompt = promptRef.current.value.trim();
      if (!prompt) {
        promptRef.current.value = "";
        return;
      }
      const res = await axios.post(
        `${backend_API_URL}/intentResponse?query=${prompt}`
      );
      promptRef.current.value = "";
      console.log(res);
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
        <button type="submit">
          <span className="material-symbols-outlined">send</span>
        </button>
      </form>
    </div>
  );
};

export default Input;
