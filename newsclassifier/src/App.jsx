import { useRef, useState } from "react";
import "./App.css";
import bg from "../assets/bg.png";
function App() {
  const inputRef = useRef(null);
  const [isSending, setisSending] = useState(false);
  const [resultclass, setResultClass] = useState(null);
  const classes = {
    "cultural and artistic": "فرهنگی و هنری",
    economic: "اقتصادی",
    environment: "محیط زیست",
    miscellaneous: "متفرقه",
    political: "سیاسی",
    social: "اجتماعی",
    sports: "ورزشی",
    technological: "فناوری",
    tourism: "جهان و گردشگری",
  };
  const handleClick = async () => {
    const text = inputRef.current.value;
    setisSending(true);
    try {
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
      console.error("zarp", result);
      result.json().then((data) => {
        setisSending(false);
        setResultClass(classes[data]);
      });
    } catch {
      setisSending(false);
    }
  };

  return (
    <div className="main">
      {/* <div className="left-container"></div> */}
      <div className="middle-container">
        <textarea
          className="scroll-container"
          ref={inputRef}
          type="text"
          placeholder="متن خبر را وارد کنید"
        />
        <button onClick={handleClick}>ارسال</button>
        {resultclass && (
          <h3>
            دسته بندی : <span>{resultclass}</span>
          </h3>
        )}
        {isSending && (
          <div className="waiting">
            <div className="loader"></div>
          </div>
        )}
      </div>
      {/* <div className="right-container"></div> */}
    </div>
  );
}

export default App;
