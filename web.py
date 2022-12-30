import streamlit as st
import todo_functions

todos = todo_functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    todo_functions.write_todos(todos)

todos = todo_functions.get_todos()

st.title("My Todo App :)")
st.subheader("This app is made to increase your productivity!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todo_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", 
              on_change=add_todo, key='new_todo')