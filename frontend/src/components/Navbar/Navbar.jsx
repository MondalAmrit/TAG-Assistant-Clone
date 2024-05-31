import { useState } from "react";
import "./navbar.css";
import { Link } from "react-router-dom";

const Navbar = () => {
  const [isEditClicked, setIsEditClicked] = useState(false);
  const [topic, setTopic] = useState("Chat Topic");

  const handleTopic = () => {
    setIsEditClicked(true);
  };

  const handleOutsideClick = (e) => {
    setTopic(e.target.value);
    setIsEditClicked(false);
  };

  const handleEnter = (e) => {
    if (e.key === "Enter") {
      setTopic(e.target.value);
      setIsEditClicked(false);
    }
  };

  return (
    <header className="nav-header">
      <div>
        <Link to="/">
          <h2>TAG by GPT</h2>
        </Link>
      </div>
      <div className="convo">
        {isEditClicked ? (
          <input
            onBlur={handleOutsideClick}
            onKeyDown={handleEnter}
            type="text"
            defaultValue={topic}
            maxLength="30"
            autoFocus
          />
        ) : (
          <h2>{topic}</h2>
        )}
        <span onClick={handleTopic} className="material-symbols-outlined">
          edit
        </span>
      </div>
      <div>
        <span className="material-symbols-outlined">settings</span>
      </div>
    </header>
  );
};

export default Navbar;
