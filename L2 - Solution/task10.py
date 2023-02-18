word = input().lower()

number_of_letters = {}

for letter in word:
    if letter in number_of_letters:
        number_of_letters[letter] += 1
    else:
        number_of_letters[letter] = 1

for letter, count in number_of_letters.items():
    print(letter, count)