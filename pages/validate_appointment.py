

def validate_appointment(data):
    # check each field separately
    if not data['tour_date']:
        return 'Tour Date is required.'

    if not data['tour_time']:
        return 'Tour Time is required.'

    if not data['agent_name']:
        return 'Agent Name is required.'

    if not data['client_name']:
        return 'Client Name is required.'

    if not data['property_address']:
        return 'Property is required.'

    # outcome not required, but must be set to None for db
    if data['outcome'] == "":
        data['outcome'] = None

    return None