from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank= []

for question in question_data :
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)
# print(question_bank)
quiz=QuizBrain(question_bank)
for question in question_bank :
    quiz.next_question()