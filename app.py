import streamlit as st
from pathlib import Path
import base64
import os
import pandas as pd
from streamlit import session_state
import subprocess

def home_page():
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image.png"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    # Title and Welcome Message
    st.title("Welcome to :blue[Kick-Start-Up!]")
    st.markdown("<p style='color: lightblue; font-size: 30px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Connecting Social Impact Projects with Potential Investors""</p>",
    unsafe_allow_html=True)

    # Description
    st.markdown(
    "<p style='color: white; font-size: 15px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>"
    "Kick-Start-Up is a platform dedicated to fostering sustainability and driving positive change. "
    "We bridge the gap between social impact projects and investors who are passionate about making a difference. "
    "Whether you're an investor looking to support impactful initiatives or an ideator seeking funding to bring your vision to life, "
    "Kick-Start-Up is your platform for sustainable change."
    "</p>",
    unsafe_allow_html=True  
    )

    # Buttons for Login
    # Buttons for Login with increased size
    col1, col2 = st.columns([2,2])
    ideatorlogin=col1.button("Login as Ideator")
    if ideatorlogin: 
        st.session_state['page'] = 'ideatorlogin'
    investorlogin=col2.button("Login as Investor")
    if investorlogin:
        subprocess.Popen(["streamlit", "run", "app2.py"])
    # Custom CSS to increase button size
    st.markdown(
        """
        <style>
        div[data-testid="stButton"] > button {
            width: 200px; /* Adjust button width as needed */
            height: 50px; /* Adjust button height as needed */
            font-size: 30px; /* Adjust font size as needed */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def authenticate_user(username, password):
    df = pd.read_csv('ideators.csv')
    #hashed_password = hash_password(password)
    if ((df['username'] == username) & (df['password'] == password)).any():
        return True
    else:
        return False

def ideatorlogin():
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image3.png"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)  

    st.title("LOGIN AS :blue[IDEATOR]")
    username = st.text_input("USER NAME")
    session_state["username"] = username
    password = st.text_input("PASSWORD",type="password")
    login= st.button("LOG IN")
    if login:
        if authenticate_user(username, password):
            st.session_state['page'] = 'ideate'
        else:
            st.error("Invalid username or password.")
    st.write("<div style='text-align: center;'><p style='font-size: 24px;'>New  user ? Dont have  an  account</p> </div>", unsafe_allow_html=True)
    col1,col2,col3=st.columns([2,2,1])
    ideatorsignup=col2.button("SIGN UP AS IDEATOR")
    if ideatorsignup:
        st.session_state['page'] = 'ideatorsignup'

def ideatorsignup():
    if st.button("Back to Login"):
        st.session_state['page'] = 'ideatorlogin'
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image3.png"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    st.title("Sign Up as Ideator")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Create Account"):
         add_ideator(new_username, new_password)
         st.session_state['page'] = 'home'

# Function to add a new user to CSV
def add_ideator(username, password):
    df = pd.DataFrame({'username': [username], 'password': [password]})
    df.to_csv('ideators.csv', mode='a', index=False)

def authenticate_investor(username, password):
    df = pd.read_csv('investors.csv')
    if ((df['username'] == username) & (df['password'] == password)).any():
        return True
    else:
        return False
    

def ideate():
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image4.png"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    st.title("Ideate ")
    if "username" in session_state:
        username = session_state["username"]
    st.write(f"<span style='font-size: 24px; font-family: \"Comic Sans MS\", cursive, sans-serif'>Welcome, {username}!</span>", unsafe_allow_html=True)
    st.markdown("<p style='color: lightblue; font-size: 20px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Do you've your idea and working model ready?""</p>",
    unsafe_allow_html=True)
    but1 = st.button("Share a New Idea")
    if but1:
        username = st.session_state['username']
        subprocess.Popen(["streamlit", "run", "ideation.py", "--username", username])
    st.markdown("<p style='color: lightblue; font-size: 20px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Have an idea but don't know how to build a prototype? </br> We've got your back, build prototype with the help of our AI""</p>",
    unsafe_allow_html=True)
    but2=st.button("Develop a prototype")
    if but2:
        st.session_state['page'] = 'prototype'
    st.markdown("<p style='color: lightblue; font-size: 20px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Improve your idea with the help of AI-powered bot""</p>",
    unsafe_allow_html=True)
    but3=st.button("Improve your existing idea")
    if but3:
        subprocess.Popen(["streamlit", "run", "chatai.py"])
    st.markdown("<p style='color: lightblue; font-size: 20px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Check the status of your submitted idea.""</p>",
    unsafe_allow_html=True)
    but3=st.button("Check Status.")
    if but3:
        st.session_state['page'] = 'checkstatus'
    st.markdown("<p style='color: lightblue; font-size: 20px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Chat with investors.""</p>",
    unsafe_allow_html=True)
    but4=st.button("Chat with investors")
    if but4:
        st.session_state['page'] = 'chat'

def prototype():
    if st.button("Back"):
        st.session_state['page'] = 'ideate'
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image4.png"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    st.title("Build a Prototype")
    st.markdown("<p style='color: lightblue; font-size: 30px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Build prototype using our AI powered bot!""</p>",
    unsafe_allow_html=True)
    but1=st.button("Build Prototype")
    if but1:
        subprocess.Popen(["streamlit", "run", "chatbot.py"])
    st.markdown("<p style='color: lightblue; font-size: 30px; font-family: \"Comic Sans MS\", cursive, sans-serif; max-width: fit-content;'>""Test your prototype""</p>",
    unsafe_allow_html=True)
    but2=st.button("Test prototype")
    if but2:
        subprocess.Popen(["streamlit", "run", "interpretor.py"])

import pandas as pd
import streamlit as st

def checkstatus():
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image4.png"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    back=st.button("Back")
    if back:
        st.session_state['page']= 'ideate'
    st.title("Status of your submitted idea:")
    username = session_state["username"]
    df = pd.read_csv('ideators.csv')
    # Filter the row corresponding to the given username
    user_row = df[df['username'] == username]
    # Retrieve the idea for the user
    idea = user_row['idea'].iloc[0] if not user_row.empty else "No idea found"
    st.write(f"Your idea: {idea}")
    # Filter reviews for the given username
    user_reviews = user_row['reviews'].tolist() if not user_row.empty else []
    # Display reviews
    st.write("Reviews:")
    for review in user_reviews:
        st.write(review)
    # Calculate average score
    average_score = user_row['scores'].mean() if not user_row.empty else None
    st.write(f"Average score for {username}: {average_score:.2f}" if average_score is not None else "No scores found")

def chat():
    back=st.button("Back")
    if back:
        st.session_state['page'] = 'ideate'
    st.title("Chat with investors")

    # Retrieve the username of the ideator
    username = st.session_state["username"]

    # Read chats.csv to check if the username is present in the 'to' column
    df_chats = pd.read_csv('chats.csv')

    # Check if username is present in 'to' column
    if username in df_chats['to'].unique():
        st.write("You have received messages from investors.")
        
        # Get unique names from 'from' column
        investor_names = df_chats[df_chats['to'] == username]['from'].unique()

        # Display buttons for each investor
        for investor_name in investor_names:
            if st.button(investor_name):
                # Update session_state with investor's name
                st.session_state["investorname"] = investor_name
                # Navigate to chat page with the selected investor
                st.session_state["page"] ="chatinvestors"
    else:
        st.write("You didn't receive any messages from investors.")

import streamlit as st
import pandas as pd
from datetime import datetime

def chat_with_investors():
    back=st.button("Back")
    if back:
        st.session_state['page'] = 'chat'
    # Retrieve ideator and investor names from session state
    ideator_name = st.session_state['username']
    investor_name = st.session_state['investorname']
    st.title(f"Chat with {investor_name}")

    # Read chats.csv to get chats between ideator and investor
    df_chats = pd.read_csv('chats.csv')

    # Filter chats between ideator and investor
    filtered_chats = df_chats[(df_chats['from'] == ideator_name) & (df_chats['to'] == investor_name) |
                              (df_chats['from'] == investor_name) & (df_chats['to'] == ideator_name)]

    # Sort chats by timestamp
    filtered_chats = filtered_chats.sort_values(by='timestamp')

    # Container for chat messages
    chat_container = st.container()

    # Display chats
    for _, row in filtered_chats.iterrows():
        if row['from'] == ideator_name:
            with chat_container:
                st.markdown(f'<div style="text-align: right; background-color: black; padding: 10px; border-radius: 10px;">{row["chat"]}</div>', unsafe_allow_html=True)
        else:
            with chat_container:
                st.markdown(f'<div style="background-color: blue; padding: 10px; border-radius: 10px;">{row["chat"]}</div>', unsafe_allow_html=True)

    # Textbox for new chat
    new_chat = st.text_input("Your message:")
    send_button = st.button("Send")

    if send_button and new_chat.strip():
        # Get the current timestamp
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append new chat to DataFrame
        new_row = pd.DataFrame({'from': [ideator_name], 'to': [investor_name], 'chat': [new_chat], 'timestamp': [current_timestamp]})
        df_chats = pd.concat([df_chats, new_row], ignore_index=True)

        # Save updated chats
        df_chats.to_csv('chats.csv', index=False)

        # Clear the text input
        new_chat = ''

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == 'home':
        home_page()
    elif st.session_state['page'] == 'ideatorlogin':
        ideatorlogin()
    elif st.session_state['page'] == 'ideatorsignup':
        ideatorsignup()
    elif st.session_state['page'] == 'ideate':
        ideate()
    elif st.session_state['page'] == 'prototype':
        prototype()
    elif st.session_state['page'] == 'checkstatus':
        checkstatus()
    elif st.session_state['page'] == 'chat':
        chat()
    elif st.session_state['page'] == 'chatinvestors':
        chat_with_investors()


if __name__== "__main__":
    main()
