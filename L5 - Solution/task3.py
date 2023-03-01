import re


def is_valid_email(email):
    username_and_domain = email.split('@')
    if len(username_and_domain) != 2:
        return False
    username, domain = username_and_domain

    username_pattern = r'^\w+([\.-]?\w+)*$'
    domain_pattern = r'^\w+([\.-]?\w+)*\.\w{2,3}$'
    print('match: ', re.match(username_pattern, username), '   next match: ', re.match(domain_pattern, domain))
    if re.match(username_pattern, username) and re.match(domain_pattern, domain):
        return True
    else:
        return False


# Test the function with some example email addresses
print(is_valid_email("example@example.com"))  # Output: True
print(is_valid_email("example@example.co.uk"))  # Output: True
print(is_valid_email("example.example.com"))  # Output: False
print(is_valid_email("example@example"))  # Output: False
print(is_valid_email("example@example@.com"))  # Output: False