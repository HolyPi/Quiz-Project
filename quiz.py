score = 0
correct_answer = []
incorrect_answer = []
# Truck
# Rhydon
# Razor Claw
# true
# true
# 10
# Because it wants to be like Pikachu
# Dawn stone
# false
# true

print("Welcome to a Pokemon quiz, this will generally be about the Pokemon games. Try your best!")

question1 = "1. What did people think Mew was hiding under in Pokemon red?"
question2 = "2. What was the first Pokemon ever created?"
question3 = "3. What does Sneasel need to hold in order to evolve?"
question4 = "4. Does Spinda have unique pattern of spots?"
question5 = "5. Is Fairy weak against Steel?"
question6 = "6. At what age can you start your Pokemon journey?"
question7 = "7. Why does Mimikyu wear a Pikachu costume?"
question8 = "8. What does a male Ralts need to evolve into a Gallade?"
question9 = "9. Can Legendaries have a gender?"
question10 = "10. Can Dugtrio learn Sucker punch?"

def questions():
    print(question1)
    print("Enter a, b, c or d as a response")
    print("a. Truck b. House c. Grass d. Tower")
    answer = 'a'
    result = input()

    answers(result, answer, correct_answer, incorrect_answer)


    print(question2)
    answer = 'rhydon'
    result = input("Enter a Pokemon name:".lower())
    
    answers(result, answer, correct_answer, incorrect_answer)

def question3():
    print(question3)
    answer = ''



def answers(result, answer, correct_answer, incorrect_answer):
    i = 0
    if result == answer:
        print("Nice! That's correct.")
        score =+ 1

        for i in range(i):
            if len(correct_answer) > 0:
                correct_answer.append()
            i+=1




    elif result != answer:
        print("Uh oh! Not correct.")
        incorrect_answer.append(1)


def results():
    print("You have gotten " + str(correct_answer) + " correct" )
    print("You have gotten " + str(incorrect_answer) + " incorrect")




questions()
results()
