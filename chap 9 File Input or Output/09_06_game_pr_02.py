def game():
    return 444555

score = game()
with open("highscore.txt") as f:
    highscorestr = int(f.read())

if highscorestr=='':
    with open("hoghscore.txt","w") as f:
        f.write(str(score))

elif int(highscorestr)<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))

# elif int(highscorestr)<score :
#     with open("highscore.txt","w") as f:
#         f.write(str(score))