import "./input.css";

const Input = () => {
  return (
    <div className="input-container">
      <div className="input-field">
        <input type="text" placeholder="Enter a prompt here" />
        <span className="material-symbols-outlined">send</span>
      </div>
    </div>
  );
};

export default Input;
