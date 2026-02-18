# ------------------------------------EXERCISE----------------------------------
#                                     QUIZ GAME

questions = ("What is the capital of Iran? ",
             "2. What is the biggest ocion in the Earth?",
             "3. Which one is the coolest color?",
             "4. Who invented telephone?")
options = (("A. SHiraz", "B. Esfahan", "C. Tehran", "D. Karaj"),
           ("A. Atlantic Ocean", "B. Pacific Ocean",
            "C. Indian Ocean", "D. Arctic Ocean"),
           ("A. Red", "B. Blue", "C. Yellow", "D. Purple"),
           ("A. Thomas Edison", "B. Joseph Aspdin", "C. Alexander Grahambell", "D. Randi Altschul "))
answers = ("C",
           "B",
           "B",
           "C"
           )

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct !!")
    else:
        print(f"Wrong, the answer is {answers[question_num]}")

    question_num += 1

print("---------------")
print("----RESULTS----")
print("---------------")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / len(questions) * 100))
print(f"Your score is: {score}%")
