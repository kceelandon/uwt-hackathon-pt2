import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [tasks, setTasks] = useState([]);
  const addTask = (task) => {
    setTasks(prevTasks => [...prevTasks, task])
  }

  const taskDescription = useState();
  const [showNewTask, setShowNewTask] = useState(false);

  const handleTask = () => {
    setShowNewTask(false);
  }

  const newTask = () => {
    setShowNewTask(true);
  }
  return (
    <>
      <div className="min-h-screen w-full bg-gray-50 text-gray-900 p-4">
        <form className="grid grid-cols-1 gap-4 w-full rounded-sm border-2 border-indigo-600 p-4 text-cyan-600">
          <div className="flex flex-col">
            <label htmlFor="task" className="text-lg mb-1">Task</label>
            <textarea id="task" type="text" className="border-2 border-indigo-600 rounded px-2 py-1" />
          </div>
          <div className='grid grid-cols-2 gap-2'>
          <button className='bg-cyan-500 rounded-sm h-12 text-gray-50' onClick={() => handleTask()}>Save</button>
          <button className='rounded-sm border-2 border-cyan-500' onClick={() => handleTask()}>Cancel</button>
          </div>
        </form>
        {
          showNewTask &&
          <button onClick={() => addTask("New Task")} className='w-full p-2 mt-2 bg-indigo-600 rounded-sm text-gray-50 active:bg-gray-50 active:border-2 active:border-indigo-600 active:text-indigo-600'>New Task</button>
        }
        <ul>
          <h2 className='text-xl bold text-cyan-500'>To Do List</h2>
          {tasks.map((t, index) => (
            <li key={index}>{t}</li>
          ))}
        </ul>
        <div>
          <h2 className='text-xl bold text-cyan-500'>Organized To Do List</h2>
        </div>
      </div>
    </>
  )
}

export default App
