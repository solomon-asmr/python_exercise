programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
student_scores={
    "Harry": 90,
    "Ron": 78,
    "hermione": 95,
    "Draco": 75,
    "Neville": 60
}
student_grades={}
def scores_to_grades():
    for name in student_scores:
        if 91<=student_scores[name] <=100:
            student_grades[name]="Outstanding"
        elif 81<=student_scores[name]<=90:
            student_grades[name]="Exceeds Expectations"
        elif 71<=student_scores[name]<=80:
            student_grades[name]="Acceptable"
        elif student_scores[name]<=70:
            student_grades[name]="Fail"
    print(student_grades)
scores_to_grades()