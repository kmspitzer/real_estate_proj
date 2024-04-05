import re

def validate_zip(zip):
    # Regular expression for a 5-digit ZIP code
    pattern = re.compile(r'^\d{5}$')
    if not pattern.match(zip):
        raise ValueError("Invalid ZIP code format. ZIP code must be exactly 5 digits.")