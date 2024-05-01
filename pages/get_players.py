from utilities.db_utils import *

# utility function to pull player data as foreign key
def get_players(tbl, id_col, new_col):

    # pull existing players from database
    players = db_get_table(tbl)

    if players is None:
        raise ValueError("Failed to retrieve agent/client data")

    # create a column with first and last name concatenated
    players[new_col] = players['first_name'] + ' ' + players['last_name']

    # create a list of concatenated names
    player_names = players[new_col].tolist()

    # create a player_mapping dictionary, player id: player_name
    player_mapping = pd.Series(players[id_col].values, index=players[new_col]).to_dict()

    return player_names, player_mapping