import './App.css';
import { useState } from "react";
  
export default function App() {
  const [text, setText] = useState("");
  const [result, showResult] = useState(null);

  const handleSubmit = async () => {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    console.log("Sentiment:", data.label);
    console.log("Confidence:", data.confidence*100, "%");
    showResult(data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p className="Title">
          Sentiment Analysis
        </p>
        <textarea className="textInput" name="textInput" value={text} onChange={(e) => setText(e.target.value)} placeholder="Please Spill Your Thoughts Here..."></textarea>
        <button type = "button" className='Analyze' onClick={handleSubmit}>Analyze Thought</button>   
        {result && (
          <div>
            <p>Sentiment: {result.label}</p>
            <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
          </div>
        )}
      </header>
    </div>
  );
}