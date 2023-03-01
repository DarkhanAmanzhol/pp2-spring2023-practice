# You have some kind of text. You should be able to find the first sentence by regex till the dot(.) sign and print it to the terminal.

# Input -> string - One or more occurences 

import re
from text_paypal import text_paypal
    
def search_input():
    user_string = input("Please write the keyword which we should search: ")
    has_starts_symbol = input("It looks for sentences where it starts with user input: ")
    has_ends_symbol = input("It looks for sentences where it ends with user input: ")
    has_digits = input("It contains a number in it? ")


    texts = [x.strip() for x in re.split('\.', text_paypal)]

    # 3 options
    if has_starts_symbol.lower() == 'true':
        user_string = '^' + user_string

    if has_ends_symbol.lower() == 'true':
        user_string = user_string+ '$'

    match_digits = True
    if has_digits.lower() == 'false':
        match_digits = False


    for text in texts:
        matched_input = re.search(user_string, text)
        # checks each text if it matched with digit's containings 
        if matched_input and (match_digits == bool(re.search('\d', text))): 
            print(matched_input.string) # text