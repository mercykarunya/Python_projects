from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# ques = Question()
question_bank = []
for i in question_data:
    # print(i.get('text'))
    # print(i.get('answer'))
    new_ques = Question(i.get('question'),i.get('correct_answer'))
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You have completed the Quiz")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")