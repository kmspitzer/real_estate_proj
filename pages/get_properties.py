from utilities.db_utils import *
import streamlit as st

# utility function to pull property data as foreign key
def get_properties():

    # pull existing players from database
    props = db_get_table('properties')

    # create a column with first and last name concatenated
    props['prop_address'] = props['address_line_1'] + ', ' + props['address_line_2'] + ', ' + props['city'] + ', ' + props['state'] + ', ' + props['zip']

    # create a list of concatenated names
    property_address = props['prop_address'].tolist()

    # create a player_mapping dictionary, player id: player_name
    prop_mapping = pd.Series(props['property_id'].values, index=props['prop_address']).to_dict()

    return property_address, prop_mapping

st.write(db_get_table("properties"))