import React from "react";
import TodoItem from "./todo";

export default function TodoView(props) {
  return (
    <div>
      <ul>
        {props.todoList.map(todo => <TodoItem todo={todo} />)}
      </ul>
    </div>
  )
}
