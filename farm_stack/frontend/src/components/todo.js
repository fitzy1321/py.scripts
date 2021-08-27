import axios from "axios";
import React from "react";

import { todoUrl } from '../common'

export default function TodoItem(props) {
  const deleteTodoHandler = (title) => {
    console.log(title)
    axios.delete(`${todoUrl}/${title}`).then(res => console.log(res.data))
  }

  return (
    <div>
      <p>
        <span style={{fontWeight: 'bold, underline'}}>{props.todo.title} : </span> {props.todo.description}
        <button onClick={() => deleteTodoHandler(props.todo.title)} className="btn btn-outline-danger my2 mx-2" style={{'borderRadius': '50px', }}>X</button>
        <hr></hr>
      </p>
    </div>
  )
}
