class QuizBrain:
    def __init__(self, q_questions):
        self.question_number = 0
        self.num_of_questions = len(q_questions)
        self.question_list = q_questions
        self.score = 0
        self.correct_answer = ""

    def next_question(self):
        next_q = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {next_q.text}. (True/False)?: ")
        if answer.title() == next_q.answer:
            self.score += 1
            self.correct_answer = next_q.answer
            print("You got it right!")
            print(f"The correct answer was: {self.correct_answer}")
            print(f"Your current score is : {self.score}/{self.question_number+1}.")
            self.question_number += 1
            return True
        else:
            return False

