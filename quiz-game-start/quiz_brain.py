class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("No, That's a wrong answer")
        print(f"The correct Answer is {correctAnswer}")
        print(f"Your current score {self.score}/{self.question_number}")
        print("\n")