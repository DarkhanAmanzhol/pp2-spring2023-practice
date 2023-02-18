# Dictioanry, set
quiz = {
    "1. Which is the currency of Kazakhstan ? ": {"Tenge", "KZT"},
    "2. Name one of the past/present presidents of Kazakhstan: ": {"Nazarbayev", "Tokayev"},
    "3. What year Kazakhstan proclaim independence? ": "1991"
} # Initialization of variable 'quiz'

counter = 0 # Your points! Starts from 0
for question, correct_answers in quiz.items(): # Dictionary has 'key' and 'value'. 
    # When used .items() > {"question": "answers"} => [("question", "answers")].
    user_answer = input(question)
    if user_answer in correct_answers: # Checks is there any right answers in correct_answers list
        counter += 1

result_perc = (counter / len(quiz)) * 100 # Final results with calculations

if result_perc > 70:
    print(f"Congrats, you won with {result_perc:.2f}% correctness") # :.2f => ':.' - used for float numbers, to get last numbers in 
    # this case. ':.2f' says, we need to take last 2 digits after '.' decimal. You can change it into ':.3f' => gets last 3 digits.
    # Example: ':.2f' > 85.6723 => 85.67 or 85 => 85.00 and so on.

else:
    print(f"You lost! You got only {result_perc:.2f}% correctness")