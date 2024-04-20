import { Fragment, useEffect, useRef, useState } from "react";
import { Navbar, Input } from "../../components";
import "./chat.css";

const time = () => {
  return new Date().toString().split(" ")[4].substring(0, 5);
};

const conversation = {
  user: false,
  msg: "Hi, I am TAG chatbot. How can I assist you?",
  time: time(),
};

const Chat = () => {
  const chatRef = useRef(null);
  const [messages, setMessages] = useState([conversation]);
  const [isGenerating, setIsGenerating] = useState(false);

  useEffect(() => {
    chatRef.current.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <main className="main">
      <Navbar />
      <div className="message-list">
        {messages.map((message, index) => (
          <Fragment key={index}>
            <div
              className={
                message.user ? "prompt-container" : "response-container"
              }
            >
              <div className={message.user ? "prompt" : "response"}>
                <p>{message.msg}</p>
                <p
                  style={{
                    textAlign: "end",
                    fontSize: "10px",
                    marginBottom: "-10px",
                  }}
                >
                  {message.time}
                </p>
              </div>
            </div>
          </Fragment>
        ))}
        {isGenerating && (
          <p
            style={{
              display: "flex",
              gap: "1.2rem",
              color: "rgb(10, 180, 183)",
              width: "20%",
            }}
          >
            Generating<span className="loader"></span>
          </p>
        )}
      </div>
      <Input
        time={time}
        setIsGenerating={setIsGenerating}
        setMessages={setMessages}
        isGenerating={isGenerating}
      />
      <div ref={chatRef}></div>
    </main>
  );
};

export default Chat;
