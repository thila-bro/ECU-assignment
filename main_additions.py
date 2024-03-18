# Student name: Thilan Maduranga Bentharage
# Student ID: 10656631
# main_additions.py for Assignment 1

import random
import time

# constant values for the system
HEADER_LENGTH = 75

# system requirement constants
EASY_OPTION = {"question": 2, "qty": 3, "min": 1, "max": 5}
MEDIUM_OPTION = {"question": 4, "qty": 5, "min": 3, "max": 12}
HARD_OPTION = {"question": 6, "qty": 8, "min": 10, "max": 25}


# showing question and answers to user
def show_question_answer(challenging=False):
    # get random number for question selection
    question = select_question_no()

    # if challenging question updated the max min values
    if challenging:
        requirements["min"] = requirements["min"] * 2
        requirements["max"] = requirements["max"] * 2

    # when question no 1 comes
    if question == 1:
        # generating list and display list for this iteration
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the smallest number of this?", my_list)
        # question started time
        start_time = time.time()
        answered_time = 0

        # requesting a valid input from user
        while True:
            try:
                answer = int(input(""))  # getting user input
                answered_time = round(time.time() - start_time, 1)
            except ValueError:
                # show error message to user
                print("Please enter a valid input")
                # continue when wrong input is given
                continue
            else:
                # break when valid input is given
                break

        # when user answer is correct
        if answer == min(my_list):
            print("Correct! You answered in", answered_time, "seconds")
            return True
        else:
            # otherwise shows the answer
            print("Your answer is incorrect\nCorrect answer is:", min(my_list))
            return False
    # when question no 2 comes
    elif question == 2:
        # generating list and display list for this iteration
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is biggest number of this list?", my_list)
        # question started time
        start_time = time.time()
        answered_time = 0

        # requesting a valid input from user
        while True:
            try:
                answer = int(input(""))  # getting user input
                answered_time = round(time.time() - start_time, 1)
            except ValueError:
                # show error message to user
                print("Please enter a valid input")
                # continue when wrong input is given
                continue
            else:
                # break when valid input is given
                break

        # when user answer is correct
        if answer == max(my_list):
            print("Correct! You answered in", answered_time, "seconds")
            return True
        else:
            # otherwise shows the answer
            print("Your answer is incorrect\nCorrect answer is:", max(my_list))
            return False
    # when question no 3 comes
    elif question == 3:
        # generating list and display list for this iteration
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the sum of the number of this list?", my_list)
        # question started time
        start_time = time.time()
        answered_time = 0

        # requesting a valid input from user
        while True:
            try:
                answer = int(input(""))  # getting user input
                answered_time = round(time.time() - start_time, 1)
            except ValueError:
                # show error message to user
                print("Please enter a valid input")
                # continue when wrong input is given
                continue
            else:
                # break when valid input is given
                break

        # when user answer is correct
        if answer == sum(my_list):
            print("Correct! You answered in", answered_time, "seconds")
            return True
        else:
            # otherwise shows the answer
            print("Your answer is incorrect\nCorrect answer is:", sum(my_list))
            return False
    # additional question
    elif question == 4:
        # generating list and display list for this iteration
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the difference between the smallest and biggest numbers in this list?", my_list)
        # question started time
        start_time = time.time()
        answered_time = 0

        # requesting a valid input from user
        while True:
            try:
                answer = int(input(""))  # getting user input
                answered_time = round(time.time() - start_time, 1)
            except ValueError:
                # show error message to user
                print("Please enter a valid input")
                # continue when wrong input is given
                continue
            else:
                # break when valid input is given
                break

        # when user answer is correct
        if answer == max(my_list) - min(my_list):
            print("Correct! You answered in", answered_time, "seconds")
            return True
        else:
            # otherwise shows the answer
            print("Your answer is incorrect\nCorrect answer is:", max(my_list) - min(my_list))
            return False
    elif question == 5:
        # generating list and display list for this iteration
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        # store automatically selected number
        selected_number = random.choice(my_list)
        print("How many", str(selected_number) + "s are there in this list?", my_list)
        # question started time
        start_time = time.time()
        answered_time = 0

        # requesting a valid input from user
        while True:
            try:
                answer = int(input(""))  # getting user input
                answered_time = round(time.time() - start_time, 1)
            except ValueError:
                # show error message to user
                print("Please enter a valid input")
                # continue when wrong input is given
                continue
            else:
                # break when valid input is given
                break

        # when user answer is correct
        if answer == my_list.count(selected_number):
            print("Correct! You answered in", answered_time, "seconds")
            return True
        else:
            # otherwise shows the answer
            print("Your answer is incorrect\nCorrect answer is:", my_list.count(selected_number))
            return False
    # when something else comes
    else:
        # generating list and display list for this iteration
        my_list = random_list(requirements.get("qty"), requirements.get("min"), requirements.get("max"))
        print("What is the average of the number in the list?", my_list)
        # question started time
        start_time = time.time()
        answered_time = 0

        # requesting a valid input from user
        while True:
            try:
                answer = float(input(""))  # getting user input
                answered_time = round(time.time() - start_time, 1)
            except ValueError:
                # show error message to user
                print("Please enter a valid input")
                # continue when wrong input is given
                continue
            else:
                # break when valid input is given
                break

        # when user answer is correct
        if answer == round(sum(my_list) / len(my_list), 2):
            print("Correct! You answered in", answered_time, "seconds")
            return True
        else:
            # otherwise shows the answer
            print("Your answer is incorrect\nCorrect answer is:", round(sum(my_list) / len(my_list), 2))
            return False


# selecting features according to user input
def select_requirements(my_input):
    my_options = {}
    if my_input == 'E':
        my_options = EASY_OPTION

    if my_input == 'M':
        my_options = MEDIUM_OPTION

    if my_input == 'H':
        my_options = HARD_OPTION

    return my_options


# generating random array as required
def random_list(my_qty, my_min, my_max):
    return random.sample(range(my_min, my_max), my_qty)


# generating random number for questing selection
def select_question_no():
    return random.randint(1, 6)


# actual programme starting point
print("=" * HEADER_LENGTH)
print("Welcome to the Number List Test Programme".center(HEADER_LENGTH))
print("=" * HEADER_LENGTH)

# globally access user selection
difficult = ''

# requesting a valid input from the user
while True:
    user_input = input("Select difficulty: \n[E]asy\n[M]edium\n[H]ard\n")
    # allow case-sensitive inputs
    if user_input.capitalize() == 'E' or user_input.capitalize() == 'M' or user_input.capitalize() == 'H' or user_input.upper() == 'EASY' or user_input.upper() == 'MEDIUM' or user_input.upper() == 'HARD':
        difficult = user_input[0].capitalize()
        break
    else:
        print("Invalid choice.")

# selecting the directory according to the user selection
requirements = select_requirements(difficult)
score = correct_answers = 0  # storing correct answers and the correct answer count
i = 0  # counting loop count

# looping until requirement satisfied (question times cycles in selected directory)
while i < requirements.get("question"):
    print("Question", (i + 1))

    # calling and calculating correct answer and score
    if show_question_answer():
        score = score + 1
        correct_answers = correct_answers + 1

    i = i + 1

# challenging question
print("\nChallenge question!")
show_question_answer(True)

# showing final result as requested
print(" " * HEADER_LENGTH)
print("Test Completed!\nYou Scored ", str(correct_answers) + "/" + str(requirements.get("question")),
      "(" + str(round(((correct_answers / requirements.get("question")) * 100))) + "%)")
