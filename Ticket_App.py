import streamlit as st
import pandas as pd
import datetime

# Initialize session state for ticket data
if 'tickets' not in st.session_state:
    st.session_state.tickets = pd.DataFrame(columns=['Ticket ID', 'Title', 'Description', 'Category', 'Priority', 'Assigned To', 'Created Date'])

# Function to add a new ticket
def add_ticket(title, description, category, priority, assigned_to):
    new_ticket = {
        'Ticket ID': len(st.session_state.tickets) + 1,
        'Title': title,
        'Description': description,
        'Category': category,
        'Priority': priority,
        'Assigned To': assigned_to,
        'Created Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.tickets = pd.concat([st.session_state.tickets, pd.DataFrame([new_ticket])], ignore_index=True)
    st.success("Ticket added successfully!")

# Streamlit UI
st.title("Bet-Way-Ticketing System")
st.subheader("Create a New Ticket")
# Sidebar for navigation
st.sidebar.title("Navigation")

# Input fields for ticket details
title = st.text_input("Title")
description = st.text_area("Description")
category = st.selectbox("Category", ["Bug", "Feature Request", "Support", "Other"])
priority = st.selectbox("Priority", ["Low", "Medium", "High"])
assigned_to = st.text_input("Assigned To")

# Button to submit ticket
if st.button("Submit Ticket"):
    if title and description and assigned_to:
        add_ticket(title, description, category, priority, assigned_to)
    else:
        st.error("Please fill in all required fields.")

# Display existing tickets
st.subheader("Existing Tickets")
if not st.session_state.tickets.empty:
    st.dataframe(st.session_state.tickets)
else:
    st.info("No tickets captured yet.")

# Optional: Add a download button for the ticket data
if not st.session_state.tickets.empty:
    csv = st.session_state.tickets.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download Tickets as CSV",
        csv,
        "tickets.csv",
        "text/csv",
        key='download-csv'
    )