# score = 0
correct_answer = []
incorrect_answer = []

incorrect_num = []
correct_num = []

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
question4 = "4. Do Spindas have a unique pattern of spots?"
question5 = "5. Is Fairy type weak against Dark type?"
question6 = "6. At what age can you start your Pokemon journey?"
question7 = "7. Why does Mimikyu wear a Pikachu costume?"
question8 = "8. What does a male Ralts need to evolve into a Gallade?"
question9 = "9. Can Legendaries have a gender?"
question10 = "10. Can Dugtrio learn Sucker punch?"

def questions():

    """Question1"""
    print(question1)
    print("a. Truck b. House c. Grass d. Tower")
    print("Enter a, b, c or d as a response")
    answer = 'a'
    result = input()

    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("The correct answer is a, Truck!")
        incorrect_num.append(1)

    else:
        correct_num.append(1)

    """Question2"""
    print(question2)
    answer = 'rhydon'
    result = input("Enter a Pokemon name: ".lower())

    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Incorrect. The correct answer is: Rhydon!")
        incorrect_num.append(2)
    else:
        correct_num.append(2)


    """Question3"""
    print(question3)
    print("a. Adamant orb b. Razor Claw c. King's Rock d. Razor Fang")
    print("Enter a, b, c or d as a response")
    answer = 'b'
    result = input()

    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("The correct answer was b, Razor Claw!")
        incorrect_num.append(3)
    else:
        correct_num.append(3)

    """Question4"""
    print(question4)
    answer = 't'
    result = input("Enter t for true or f for false: ".lower())
    if result != answer:
        print("Nope, the correct answer was: True!")
        incorrect_num.append(4)
    else:
        correct_num.append(4)

    answers(result, answer, correct_answer, incorrect_answer)


    """Question5"""
    print(question5)
    answer = 'f'
    result = input("Enter t for true or f for false: ".lower())

    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Correct answer is: False!")
        incorrect_num.append(5)

    else:
        correct_num.append(5)

    """Question6"""
    print(question6)
    print("Enter a numeric response")
    result = int(input())
    answer = 10


    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Correct answer is 10!")
        incorrect_num.append(6)
    else:
        correct_num.append(6)


    """Question7"""
    print(question7)
    print("a. Because Mimikyu is Pikachu b. It's Pikachu's evolution c. Because it wants to be Pikachu d. Because Mimikyu is lonely")
    answer = 'd'
    result = input()

    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Correct answer is d, because Mimikyu is lonely!")
        incorrect_num.append(7)
    else:
        correct_num.append(7)


    """Question8"""
    print(question8)
    print("a. King's Rock b. Dragon Scale c. Moon Stone d. Dawn Stone")
    answer = 'd'
    result = input()

    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Correct answer is d, Dawn Stone")
        incorrect_num.append(8)
    else:
        correct_num.append(8)


    """Question9"""
    print(question9)
    answer = 'f'
    result = input("Enter t for true or f for false: ".lower())



    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Correct answer is: False!")
        incorrect_num.append(9)
    else:
        correct_num.append(9)


    """Question10"""
    print(question10)
    answer = 't'
    result = input("Enter t for true or f for false: ".lower())


    answers(result, answer, correct_answer, incorrect_answer)
    if result != answer:
        print("Correct answer is: True!")
        incorrect_num.append(10)
    else:
        correct_num.append(10)



def answers(result, answer, correct_answer, incorrect_answer):
    """Prints 1 if answer is correct, prints 0 if incorrect. Appends a 1 to the correct_answer list"""
    # i = 0
    if result == answer:
        print("1") #Returning 1? ask Jess
        # score += 1
        correct_answer.append(1)

        # for i in range(i):
        #     if len(correct_answer) > 0:
        #         correct_answer.append()
        #     i+=1


    elif result != answer:
        print("0")
        incorrect_answer.append(1)


def results():
    a = sum(correct_answer)
    b = sum(incorrect_answer)

    print("Thanks for playing the Pokemon Quiz! Here are your scores: ")
    print("Total of correct answers:")
    print(a)
    print("Total of incorrect answers:")
    print(b)
    print("Questions you got correct:")
    print(correct_num)
    print("Questions you got incorrect:")
    print(incorrect_num)

    print("Your total score is:")
    print(a)

    if a == 10:
        print("Great! You're a complete Pokemon master!")
    elif a < 6:
        print("You're getting there, just gain a bit more of Pokemon knowledge!")
    elif a < 3:
        print("You'll get there eventually, don't give up!")


questions()
results()
