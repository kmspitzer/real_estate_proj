from utilities.db_utils import *

# utility function to pull agent data as foreign key
def get_agents():

    # pull existing agents from database
    agents = db_get_table('agents')

    # create a column with first and last name concatenated
    agents['agent_name'] = agents['first_name'] + ' ' + agents['last_name']

    # create a list of concatenated names
    agent_names = agents['agent_name'].tolist()

    # create an agent_mapping dictionary, agent_id: agent_name
    agent_mapping = pd.Series(agents['agent_id'].values, index=agents['agent_name']).to_dict()

    return agent_names, agent_mapping