from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions=[]
for qu in question_data:
    text=qu["text"]
    answer=qu["answer"]
    quest=Question(text, answer)
    questions.append(quest)

quize=QuizBrain(questions)
total_questions=0
while quize.still_has_questions():
    quize.next_question()
    total_questions+=1

print("you have finished the quiz")
print(f"Your final score was {quize.final_score()}/{total_questions}")
# result=0
#
# for q in questions:
#     ans=str(input(f"{q.text} (True/False) ")).capitalize()
#     if ans==q.answer:
#         result+=1
#         print("perfect!!")
#     else:
#         print("wrong")
# print(f"you got {result}/{len(questions)}")