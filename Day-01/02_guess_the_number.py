# Guess the number game

secret_number = 9
try:
    number_guessed_by_user = int(input("Enter a number between 1 to 10: "))
    if not 1 <= number_guessed_by_user <= 10:
        print("Please enter a number between 1 and 10.")
        number_guessed_by_user = int(input("Enter a number between 1 to 10: "))
except ValueError:
    print("Hey! That is not a number. Please enter digits only!")
    number_guessed_by_user = int(input("Enter a number between 1 to 10: "))
if number_guessed_by_user == secret_number:
    print("Correct! You guessed it!")
else:
    print("Wrong guess.")