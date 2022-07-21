from question_model import QuizQuestion
from data import question_data
from QuizBrain import QuizBrain
questions = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = QuizQuestion(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz!\nYour final score is {quiz.score}/{quiz.question_number}")
