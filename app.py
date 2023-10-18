import streamlit as st

# Initialize state for issues and todos
issues = []
todos = []

# Page selection
page = st.sidebar.selectbox("Select a Page", ["Open Issues", "To-Do's"])

if page == "Open Issues":
    st.title("Open Issues")
    
    # Add an issue
    issue = st.text_input("Add an Issue:")
    if st.button("Add Issue"):
        if issue:
            issues.append(issue)
            st.text(f"Added Issue: {issue}")
    
    # Display open issues
    st.subheader("Issues:")
    for i, issue in enumerate(issues):
        if st.checkbox(f"{i + 1}. {issue}", key=f"issue_{i}"):
            issues.remove(issue)

elif page == "To-Do's":
    st.title("To-Do's")
    
    # Add a to-do
    todo = st.text_input("Add a To-Do:")
    if st.button("Add To-Do"):
        if todo:
            todos.append(todo)
            st.text(f"Added To-Do: {todo}")

    # Display to-do list
    st.subheader("To-Do List:")
    for i, todo in enumerate(todos):
        if st.checkbox(f"{i + 1}. {todo}", key=f"todo_{i}"):
            todos.remove(todo)

# Display the app
