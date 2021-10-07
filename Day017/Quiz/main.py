from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    new_question = Question(q["text"], q["answer"])
    question_bank.append(new_question)

game_on = True
quiz_brain = QuizBrain(question_bank)
num_of_questions = len(question_bank)
while game_on:
    if quiz_brain.next_question():
        if quiz_brain.question_number >= num_of_questions:
            print("You won! Out of questions!")
            game_on = False
    else:
        print("You guessed wrong.")
        print(f"The correct answer was: {quiz_brain.correct_answer}.")
        print(f"Final score: {quiz_brain.score}/{quiz_brain.question_number + 1}.")
        game_on = False
