import { Navbar, Input } from "../../components";
import { messages } from "../../dummyMessages";
import "./chat.css";

const Chat = () => {
  return (
    <main className="main">
      <Navbar />
      <div className="message-list">
        {messages.map((message) => (
          <>
            <div className="prompt-container">
              <div className="prompt">
                <p>{message[0]}</p>
              </div>
            </div>
            <div className="response-container">
              <div className="response">
                <p>{message[1]}</p>
              </div>
            </div>
          </>
        ))}
      </div>
      <Input />
    </main>
  );
};

export default Chat;
