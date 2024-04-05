import re

def standardize_phone_number(phone_number):
    # Extract digits from the phone number using a regular expression
    digits = re.sub(r'\D', '', phone_number)
    
    # Format the digits into the desired format if the length is correct
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        raise ValueError("Invalid phone number format")