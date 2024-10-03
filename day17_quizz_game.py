import os
import time
import base64
from day17_question_model import Question
from day17_data import TriviaData
from day17_quiz_brain import QuizBrain

def clear_screen():
    """Function to clean the screen"""
    return os.system("cls") if os.name == "nt" else os.system("clear")

if __name__ == "__main__":
    trivia_data = TriviaData.ask_difficulty()
    question_data = trivia_data.fetch_questions()

    question_bank = []
    for data in question_data:
        decoded_question = base64.b64decode(data["question"]).decode("utf-8")
        decoded_answer = base64.b64decode(data["correct_answer"]).decode("utf-8")
        question_bank.append(Question(decoded_question,decoded_answer))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        clear_screen()
        quiz.next_question()
        time.sleep(1.5)

    print("You've completed the quiz.")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")