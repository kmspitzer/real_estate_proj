import re


def validate_client(data):

    # check each field separately
    if not data['first_name']:
         return 'First Name is required.'

    if not data['last_name']:
        return 'Last Name is required.'

     # handle budget as a special case because it can be None
    if data['budget'] == "":
        data['budget'] = None
    else:
        try:
            # remove commas for database
            data['budget'] = int(data['budget'].replace(",", "").strip())
        except ValueError:
            return "Please enter a valid number for Budget."

    if not data['address_line_1']:
        return 'Address Line 1 is required.'

    if not data['city']:
        return 'City is required.'

    if not data['state']:
        return 'State is required.'

    # ensure zip is 5-digit
    if len(data['zip']) != 5 or not data['zip'].isdigit():
        return 'A valid ZIP code is required.'

    # as long as we get 10 digits
    if len(re.sub(r'\D', '', data['phone'])) != 10:
        return 'Enter valid Phone.'

    if not data['status']:
        return 'Status is required.'

    if not data['agent_name']:
        return 'Agent Name is required.'

    return None
