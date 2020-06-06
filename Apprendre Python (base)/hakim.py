secret_word = "Aid"
guess = ""
out_of_guess = False
limit_of_guess = 3
guess_score = 0

while secret_word != guess and not(out_of_guess):
    if guess_score < limit_of_guess:
        guess = input("Quelle fête qui vient deux fois par année: ")
        guess_score += 1
        if guess_score != limit_of_guess:
           print("Recommence ce n'est pas la bonne réponse ")
    else:
        out_of_guess = True
if out_of_guess:
    print("Tu as atteint le maximum d'essai meilleur chance la prochaine fois")
else:
    print("Tu as gagné pablo")



