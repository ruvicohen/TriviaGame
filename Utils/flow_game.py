from random import random

from toolz import first

from Repository.answer_repository import find_answer_by_question_id
from Repository.question_repository import find_all_questions
from Repository.user_repository import find_user_by_id


def flow_trivia_game():
    while True:
        print("\nTrivia game:")
        print("1. login")
        print("2. sign-up to game trivia")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            user = login()
            if user:
                playing(user)
        elif choice == '2':
            user = sign_up()
            if user:
                playing(user)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


def login():
    user_id = input("write your ID")
    user = find_user_by_id(user_id)
    if user:
        return user
    return

def sign_up():
    first_name = input("write your first name")
    last_name = input("write your last name")
    email = input("write ")

def playing(user):
    while True:
        print("1. get question")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            display_question()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def display_question():
    list_questions = find_all_questions()
    random_index = random.randint(0, len(list_questions) - 1)
    question = list_questions[random_index]
    answers = find_answer_by_question_id(question.id)
    print(question.question_text)
    for index, answer in enumerate(answers):
        print(f"{index}: {answer.incorrect_answer}")
    print(f"{len(answers)}: {question.correct_answer}")
    user_answer = input("write num of answer")
    if user_answer == len(answers):
        print("you write")
    else:
        print("wrong")

