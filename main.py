import constants
import random

difficult = ''


def select_requirements(my_input):
    my_options = {}
    if my_input == 'E':
        my_options = constants.EASY_OPTION

    if my_input == 'M':
        my_options = constants.MEDIUM_OPTION

    if my_input == 'H':
        my_options = constants.HARD_OPTION

    return my_options


def random_list(my_qty, my_min, my_max):
    return random.sample(range(my_min, my_max), my_qty)


def select_question_no():
    return random.randint(1, 4)


print("=" * constants.HEADER_LENGTH)
print("Welcome to the Number List Test Programme".center(constants.HEADER_LENGTH))
print("=" * constants.HEADER_LENGTH)

while True:
    difficult = input("Select difficulty: \n[E]asy\n[M]edium\n[H]ard\n")
    if difficult.capitalize() == 'E' or difficult.capitalize() == 'M' or difficult.capitalize() == 'H':
        break
    else:
        print("Invalid choice.")

requirements = select_requirements(difficult.capitalize())
score = correct_answers = 0
i = 0

while i < requirements.get("question"):
    print("Question", (i + 1))
    question = select_question_no()

    # ask relevant question
    if question == 1:
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the smallest number of this?", my_list)
        answer = int(input(""))

        if answer == min(my_list):
            print("Correct!")
            score = score + 1
            correct_answers = correct_answers + 1
        else:
            print("Your answer is incorrect\nCorrect answer is:", min(my_list))
    elif question == 2:
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is biggest number of this list?", my_list)
        answer = int(input(""))

        if answer == max(my_list):
            print("Correct!")
            score = score + 1
            correct_answers = correct_answers + 1
        else:
            print("Your answer is incorrect\nCorrect answer is:", max(my_list))
    elif question == 3:
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the sum of the number of this list?", my_list)
        answer = int(input(""))

        if answer == sum(my_list):
            print("Correct!")
            score = score + 1
            correct_answers = correct_answers + 1
        else:
            print("Your answer is incorrect\nCorrect answer is:", sum(my_list))
    else:
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the average of the number in the list?", my_list)
        answer = int(input(""))

        if answer == (sum(my_list) / len(my_list)):
            print("Correct!")
            score = score + 1
            correct_answers = correct_answers + 1
        else:
            print("Your answer is in correct\nCorrect answer is:", (sum(my_list) / len(my_list)))
    i = i + 1

print(" " * constants.HEADER_LENGTH)
print(correct_answers)
print("Test Completed!\nYou Scored ", str(correct_answers) + "/" + str(requirements.get("qty")), round(((correct_answers / requirements.get("qty")) * 100)), "100%")
# print(random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max")))
