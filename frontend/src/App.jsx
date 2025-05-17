import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const runThisCode = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "task1": "fulltime job",
          "task2": "gym",
          "task3": "meal prep",
          "task4": "clean bathroom",
          "task5": "walk dog"
        })
      });
      const data = await response.json();
      console.log('Data:', data);
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }

  return (
    <>
      <div className="text-3xl font-bold">
        <h1>Hello world!n</h1>
        <button onClick={runThisCode}>run this code</button>
      </div>
    </>
  )
}

export default App
