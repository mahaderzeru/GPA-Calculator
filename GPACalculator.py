#GPA Calculator

print("Welcome to the GPA Calculator!") #introduction

name = input("What is your name? ") #prompt user for name

num_of_classes = int(input("How many classes are you taking this semester? ")) #get number of classes

total_credit_hours = 0
total_grade_points = 0

def letter_grade_to_gp(g): #letter grade to grade point conversion method
            if g == 1:
                return 4.0
            elif g == 2:
                return 3.7
            elif g == 3:
                return 3.3
            elif g == 4:
                return 3.0
            elif g == 5:
                return 2.7
            elif g == 6:
                return 2.3
            elif g == 7:
                return 2.0
            elif g == 8:
                return 1.7            
            elif g == 9:
                return 1.3
            elif g == 10:
                return 1.0
            elif g == 11:
                return 0.0
            else: 
                return 0.0
            
for i in range(1, num_of_classes + 1): #for loop to get credit #s of each class
        credit = int(input(f"How many credit hours is class #{i}? "))
        g = int(input("What grade did you receive in this class? (enter a number between 1 and 11) \n1. A  \n2. A- \n3. B+ \n4. B \n5. B- \n6. C+ \n7. C \n8. C- \n9. D+ \n10. D \n11. F \n"))
        total_credit_hours += credit           
        grade_points = letter_grade_to_gp(g) * credit
        total_grade_points += grade_points           


#calculate gpa - (Sum of (Credit Hours * Grade Points)) / Total Credit Hours
gpa = total_grade_points / total_credit_hours

print("Alright",name,", your GPA is",gpa)
print("See ya!" )