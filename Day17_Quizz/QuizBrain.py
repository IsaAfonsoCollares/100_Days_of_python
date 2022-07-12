class QuizBrain :
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list


    def next_question(self):
        current_question = self.question_list(self.question_number)
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        return current_question, answer

    def check_answer(self, answer):
        if next_question()[0] == answer