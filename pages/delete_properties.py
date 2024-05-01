import streamlit as st
from menu import property_menu
from utilities.db_utils import *


# display property sidebar and center title
property_menu()
st.title("Real Estate Managment System")

# button to reset the view and select another agent
if st.button('Refresh Properties'):
    st.session_state['property_data'] = None
    st.session_state['delete_property'] = False

# retrieve display data for properties and clear nulls
prop_df = db_get_properties_display()
prop_df = prop_df.fillna('')

# write properties table
st.write(prop_df.to_html(index=False), unsafe_allow_html=True)

# display form
with st.form("delete_prop_form"):
    st.write("## Delete Property")

    # accept record id input
    record_id = st.text_input("Property ID", max_chars=50).strip()

    # form submission button
    submitted = st.form_submit_button("Delete Property")

    if submitted:
        # submit button clicked -- initialize validated flag
        validated = True

        # perform any edits on property id
        if not record_id.isdigit():
            st.error("Property ID must be numeric.")
            validated = False

        if validated:
            # call the function to delete the record from the database
            success = delete_property({'property_id': record_id})
            if success:
                st.success(f"Property deleted.")
            else:
                st.error("Record ID does not exist.")