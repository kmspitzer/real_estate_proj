def validate_property(data):

    # check each field separately
    if not data['address_line_1']:
        return 'Address Line 1 is required.'

    if not data['city']:
        return 'City is required.'

    if not data['state']:
        return 'State is required.'

    # ensure zip is 5-digit
    if len(data['zip']) != 5 or not data['zip'].isdigit():
        return 'A valid ZIP code is required.'

    # handle original_listing_price as a special case because it can be None
    if data['original_listing_price'] == "":
        data['original_listing_price'] = None
    else:
        try:
            # remove commas for database
            data['original_listing_price'] = int(data['original_listing_price'].replace(",", "").strip())
        except ValueError:
            return "Please enter a valid number for the Original Listing Price."

    # handle sold price as a special case because it can be None
    if data['sold_price'] == "":
        data['sold_price'] = None
    else:
        try:
            # remove commas for database
            data['sold_price'] = int(data['sold_price'].replace(",", "").strip())
        except ValueError:
            return "Please enter a valid number for Sold Price."

    if not data['type']:
        return 'Property Type is required.'

    # if populated, characteristics must be numeric --
    # otherwise, set to None for db
    if  data['sqft'] == '':
        data['sqft'] = None
    elif not data['sqft'].isdigit():
        return 'Square Feet must be numeric.'

    if data['bedrooms'] == '':
        data['bedrooms'] = None
    elif not data['bedrooms'].isdigit():
        return 'Number of Bedrooms must be numeric.'

    if data['bathrooms'] == '':
        data['bathrooms'] = None
    elif not data['bathrooms'].isdigit():
        return 'Number of Bathrooms must be numeric.'

    # year built is required
    if len(data['year_built']) != 4 or not data['year_built'].isdigit():
        return 'Year Built must be 4 digits.'

    if not data['agent_name']:
        return 'Agent Name is required.'

    return None