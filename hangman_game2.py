import random
import time
select_word = ["java", "python", "django", "javascript", "hypertext"]
word = random.choice(select_word)
length = len(word)
name = input("whwt is your name ")
print("welcomme" + name + "Best of luck")
time.sleep(2)
print("test begins now")
time.sleep(2)

count = 0
display = '*' * length
limit = 6


def hangnan(count, display, word):
    guess = input("this is word" + display + " enter your guess")
    if guess in word:
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    else:
        count += 1
        if count == 0:
            print("wrong input" + str(limit - count) + "guesses reamaining")
            print(
                  "|_________\n"
                  " |    |    \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                 )
        elif count == 1:
            print("wrong input" + str(limit - count) + "guesses reamaining")
            print(
                    "|_________\n"
                    " |   |     \n"
                    " |   O    \n"
                    " |        \n"
                    " |        \n"
                    " |        \n"
                )
        elif count == 2:
            print("wrong input" + str(limit - count) + "guesses reamaining")
            print(
                      "|_________\n"
                      " |   |     \n"
                      " |   O    \n"
                      " |   |     \n"
                      " |        \n"
                      " |        \n"
            )

        elif count == 3:
            print("wrong input" + str(limit - count) + "guesses reamaining")
            print(
                "|_________\n"
                " |   |     \n"
                " |   O    \n"
                " |  /|     \n"
                " |        \n"
                " |        \n"
            )

        elif count == 4:
            print("wrong input" + str(limit - count) + "guesses reamaining")
            print(
                      "|_________\n"
                      " |   |     \n"
                      " |   O    \n"
                      " |  /|\     \n"
                      " |        \n"
                      " |        \n"
            )
        elif count == 5:
            print("wrong input" + str(limit - count) + "guesses reamaining")
            print(
                      "|_________\n"
                      " |   |     \n"
                      " |   O    \n"
                      " |  /|\     \n"
                      " |  /     \n"
                      " |        \n"
            )
        elif count == 6:
            print("wrong input.you hanged")
            print("GANE OVER")
            print(
                      "|_________\n"
                      " |   |    \n"
                      " |   O     \n"
                      " |  /|\    \n"
                      " |  / \    \n"
                      " |         \n"
            )
    if word == "*" * length:
      print("congrats!! you have guessed successfully")
    elif count != limit:
        hangnan(count, display, word)


hangnan(count, display, word)







