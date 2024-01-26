import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["todolist"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.write("An app to track your day")


for index, todo in enumerate(todos):
    # st.checkbox(todo, key=todo)
    # print(todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a todo",
              on_change=add_todo, key="todolist")
