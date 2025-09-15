class QuizBrain:

    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=str(input(f"Q.{self.question_number}: {current_question.text} (True/"
                           f"False)?: ")).capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer==correct_answer:
            print(f"You got it right!\nThe correct answer was: {correct_answer}")
            self.score+=1
            print(f"Your current score is: {self.score}/{len(self.question_list)}")
        else:
            print(f"You got it wrong!\nThe correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{len(self.question_list)}")
        print("\n")
    def final_score(self):
        return self.score

