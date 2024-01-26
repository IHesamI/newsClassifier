import { useRef } from "react";
import './App.css';
function App() {
  const inputRef = useRef(null);
  const handleClick = async () => {
    const text = inputRef.current.value;
    const result = await fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text,
        title: "hello from front",
      }),
    });
    console.error(result);
  };

  return (
    <div
    className="container">
      <textarea ref={inputRef} type="text" />
      <button onClick={handleClick}>send</button>
    </div>
  );
}

export default App;
