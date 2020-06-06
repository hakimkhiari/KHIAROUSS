
Secret_word = "Lioon324"
guess = ""
out_of_guess = False
guess_score = 0
limit_of_guess = 3

while secret_word != guess:
    if guess_score <= limit_of_guess and not(out_of_guess):
        print(input("Enter your username : ")
              guess_score += 1
    else:
         out_of_guess = True
    if out_of_guess == True:
        print("This username is Your password is invalid. Please try again.")

colo

