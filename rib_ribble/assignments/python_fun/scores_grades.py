import random

def grading():
    print "Score and Grades"
    for i in range(10):
        random_num = random.randint(60, 100)
        if random_num > 89:
            letter_grade = "A"
        elif random_num > 79:
            letter_grade = "B"
        elif random_num > 69:
            letter_grade = "C"
        else:
            letter_grade = "D"
        print "Score: " + str(random_num) + "; Your grade is: " + letter_grade
    print "End of the Program. Bye!"      

grading() 


