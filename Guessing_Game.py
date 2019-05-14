
word = "Animal"
guess_word = ""
limit = 5
guess_count = 0
limit_crossed = False

while guess_word != word and not(limit_crossed):
    if guess_count < limit:
        guess_word = input("Give your guess in an animal: ")
        guess_count += 1
    else:
        limit_crossed = True

if limit_crossed == True:
    print("You Lose")
else:
    print("You win")

