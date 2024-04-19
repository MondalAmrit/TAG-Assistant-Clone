import { useState } from "react";
import "./SimpleChat.css";

export default function SimpleChat() {
  const [conversations, setConversations] = useState([
    {
      user: false,
      msg: "Hi I am TAG - chatbot. How can I help you?",
      time: Date.now(),
    },
  ]);
  const [prompt, setPrompt] = useState("");
  const [bgClr, setBgClr] = useState("");
  const [generating, setGenerating] = useState(false);
  const sendMsg = async () => {
    if (prompt === "") return;
    let msgObj = { user: true, msg: prompt, time: Date.now() };
    setConversations((conversation) => [...conversation, msgObj]);
    setPrompt("");

    setBgClr(getRandomColor(shapesColors));

    setGenerating(true);
    // Send the message to backend
    const res = await fetch("http://127.0.0.1:8000/api/v1/intentResponse", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: prompt }),
    })
      .then((resp) => resp.json())
      .then((resp) => resp["response"]);
    setGenerating(false);
    msgObj = { user: false, msg: res, time: Date.now() };
    setConversations((conversation) => [...conversation, msgObj]);
  };
  const shapesColors = [
    "10,10,210,",
    "10,210,10",
    "210,10,10",
    "200,100,10",
    "10,100,200",
    "200,10,100",
  ];

  function getRandomColor(array) {
    const randomIndex = Math.floor(Math.random() * array.length);
    return array[randomIndex];
  }
  const enterClicked = (k) => {
    if (k === "Enter") {
      sendMsg();
    }
  };
  return (
    <div className="mainWrapper">
      {/* Containes the background Shapes */}
      <div className="bgShapesContainer">
        <div
          className="diffShape"
          style={{
            top: "17%",
            left: "29%",
            width: "350px",
            height: "200px",
            background: `radial-gradient(rgba(${bgClr},0.9), rgba(${bgClr},0.5))`,
            boxShadow: `0 0 20px rgba(${bgClr},0.5)`,
          }}
        ></div>
        <div
          className="diffShape"
          style={{
            top: "24%",
            left: "27%",
            width: "200px",
            height: "270px",
            background: `radial-gradient(rgba(${bgClr},0.9), rgba(${bgClr},0.5))`,
            boxShadow: `0 0 20px rgba(${bgClr},0.5)`,
          }}
        ></div>
        <div
          className="diffShape"
          style={{
            top: "24%",
            left: "48%",
            width: "200px",
            height: "250px",
            background: `radial-gradient(rgba(${bgClr},0.9), rgba(${bgClr},0.5))`,
            boxShadow: `0 0 20px rgba(${bgClr},0.5)`,
          }}
        ></div>
      </div>
      <div className="mainContainer">
        {/* Top Nav Section */}
        <div className="TopSection">
          <div className="logoSpace"> TAG - AI assistant </div>
          <input
            type="text"
            className="ChatLabelBox"
            defaultValue="Untitled0"
          />
          <div className="settingsOption"> Settings </div>
        </div>
        {/* Mid Chat Section */}
        <div className="chatWrapper">
          {conversations.map((conversation, index) => {
            return (
              <div
                className="chatPosition"
                key={index}
                style={conversation.user ? { justifyContent: "flex-end" } : {}}
              >
                <div
                  className="chatContainer"
                  style={
                    conversation.user
                      ? {
                          justifyContent: "flex-end",
                          backgroundColor: "rgb(155 148 148 / 43%)",
                        }
                      : {}
                  }
                >
                  <div className="chatMsgContainer">{conversation.msg}</div>
                  <div className="chatMsgTime">{conversation.time}</div>
                </div>
              </div>
            );
          })}

          {/* Conditionally render the loading indicator */}
          {generating && (
            <div className="chatPosition">
              <div className="chatContainer">
                <div className="chatMsgContainer">Generating...</div>
              </div>
            </div>
          )}
        </div>

        {/* Bottom Input Box */}
        <div className="bottomSection">
          <input
            type="text"
            className="PromptInput"
            placeholder="Type here /"
            value={prompt}
            onKeyDown={(e) => {
              enterClicked(e.key);
            }}
            onChange={(e) => {
              setPrompt(e.target.value);
            }}
          />
          <div
            className="sendBtn"
            onClick={() => {
              sendMsg();
            }}
          >
            {" "}
            Send{" "}
          </div>
        </div>
      </div>
    </div>
  );
}
