import streamlit as st
import pandas as pd

# Load data from CSV files
issues_df = pd.read_csv("issues.csv", header=None, names=["Issue"])
todos_df = pd.read_csv("todos.csv", header=None, names=["ToDo"])

# Initialize state for issues and todos
issues = issues_df["Issue"].tolist()
todos = todos_df["ToDo"].tolist()

# Define a dictionary to store issue discussions
issue_discussions = {}

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
        st.write(f"{i + 1}. {issue}")
        
        # Add a discussion button
        if st.button("Discuss"):
            discussion = st.text_area("Add a comment:")
            if st.button("Add Comment"):
                if i not in issue_discussions:
                    issue_discussions[i] = []
                issue_discussions[i].append(discussion)
                st.text(f"Added Comment: {discussion}")
        
        # Mark Solved button
        if st.button("Mark Solved"):
            issue = "~~" + issue + "~~"
            st.text(f"Marked Issue as Solved: {issue}")

        # Display comments for the issue
        if i in issue_discussions:
            st.subheader("Comments:")
            for j, comment in enumerate(issue_discussions[i]):
                st.write(f"Comment {j + 1}: {comment}")

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
        st.write(f"{i + 1}. {todo}")
        
        # Mark Solved button
        if st.button(f"Mark Solved for To-Do {i + 1}"):
            todos[i] = "~~" + todos[i] + "~~"
            st.text(f"Marked To-Do as Solved: {todos[i]}")

# Save data to CSV files
issues_df = pd.DataFrame({"Issue": issues})
issues_df.to_csv("issues.csv", index=False, header=False)

todos_df = pd.DataFrame({"ToDo": todos})
todos_df.to_csv("todos.csv", index=False, header=False)
