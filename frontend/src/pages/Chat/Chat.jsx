import { Navbar, Main, Message } from "../../components";
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
                <Message message={message[0]} />
              </div>
            </div>
            <div className="response-container">
              <div className="response">
                <Message message={message[1]} />
              </div>
            </div>
          </>
        ))}
      </div>
      <Main />
    </main>
  );
};

export default Chat;
