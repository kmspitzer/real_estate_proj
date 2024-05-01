import streamlit as st

def apply_custom_css():

    st.markdown("""
    <style>
    /* Adjust the main content area */
    .streamlit-container {
        margin-left: 0px;  /* Reduce left margin to shift content left */
        padding-left: 0px; /* Reduce padding to shift content left */
    }

    /* Adjust the sidebar width and spacing if necessary */
    .streamlit-sidebar {
        width: 250px; /* Set the width of the sidebar */
        margin-left: 0px;
        padding-left: 0px;
    }

    /* Ensure DataFrames do not wrap text unnecessarily */
    .dataframe th, .dataframe td {
        white-space: nowrap;
        text-align: left;
        padding: 8px 16px;
    }

    /* Enable horizontal scrolling for DataFrames if they are too wide */
    .dataframe-container {
        overflow-x: auto;
    }
    </style>

    <style>
    /* Additional styling for DataFrame to ensure it doesn't break layout */
    div.dataframe-container {
        overflow-x: auto; /* Enable horizontal scrolling */
    }
    </style>
    
    """, unsafe_allow_html=True)