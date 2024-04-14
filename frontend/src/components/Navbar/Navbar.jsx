import "./navbar.css";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <header className="nav-header">
      <div>
        <Link to="/">
          <h2>TAG by GPT</h2>
        </Link>
      </div>
      <div className="convo">
        <h2>Conversation Name</h2>
      </div>
      <div>
        <span className="material-symbols-outlined">settings</span>
      </div>
    </header>
  );
};

export default Navbar;
