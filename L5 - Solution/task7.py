import re
from text import text

unwanted_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "()", "(", ")", "-", "_", "+", "=", "'", "|",
                       "/", ":", ">", "<", ".", ",", "�s", "?", "`", "~", "]" ,"["]
for index in range(len(text)):
    for character in unwanted_characters:
        if character in text[index]:
            text[index] = text[index].replace(f"{character}", " ").lower()

def delete_whitespaces(x):
    #Начало вашего кода
    result = re.sub(r'\s+',' ', x).rstrip()
    return result

correct_text = list(map(delete_whitespaces, text))
print(correct_text)