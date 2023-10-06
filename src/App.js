import { useState } from 'react';
import './index.css';
import { useDispatch, useSelector } from 'react-redux';
import { adding, updating } from './redux/Counter';

function App() {
  const { count } = useSelector((state) => state.task)
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>values: { count }</h1>
      <button onClick={() => {dispatch(adding())}} >adding</button>
      <button onClick={() => {dispatch(updating(6))}}>updating</button>
      <button onClick={() => {dispatch(updating())}}>removing</button>
    </div>
  );
}

export default App;
