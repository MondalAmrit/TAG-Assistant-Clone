import "./App.css";
import { Routes, Route } from "react-router-dom";
import Chat from "./pages/Chat/Chat";
import Home from "./pages/Home/Home";
import SimpleChat from "./pages/Testing/SimpleChat";

const App = () => {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/testing" element={<SimpleChat />} />
      </Routes>
    </div>
  );
};

export default App;
