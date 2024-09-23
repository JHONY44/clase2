import streamlit as st

# Initialization of users
users = []

# Function to add a user
def add_user(name):
    if name:  # Check if the name is not empty
        users.append(name)
        st.success(f"User {name} added.")
    else:
        st.error("Name cannot be empty.")

# Function to show users
def show_users():
    if users:  # Check if there are any users to display
        st.write("Users:")
        for user in users:
            st.write(user)
    else:
        st.write("No users added yet.")

# Streamlit app layout
st.title("User Management App")
option = st.selectbox("Choose an option:", ["Add User", "Show Users"])

if option == "Add User":
    name = st.text_input("Enter user name:")
    if st.button("Add"):
        add_user(name)
elif option == "Show Users":
    show_users()