secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):#Think about how to get out the loop
    if guess_count< guess_limit:
        guess = input("Enter guess:")
        guess_count +=1
        print("out_of_guesses1:",out_of_guesses)
        print("guess1:",guess)
    else:
        print("out_of_guesses2:",out_of_guesses)
        print("guess2:",guess)
        out_of_guesses = True
if out_of_guesses:
   print("out_of_guesses3:", out_of_guesses)
   print("You lose")
else:
   print("out_of_guesses4:",out_of_guesses)
   print("You win")

