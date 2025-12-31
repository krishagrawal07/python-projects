def calc_grade(avg):
        if avg>=90:
                return "A+"
        elif avg>=80:
                return "A"
        elif avg>=70:
                return "B"


print("Welcome")
name = input("Enter your name")
roll = input("Enter your roll number")
classs = input("Enter your class")

subjects = ["Physics","Chemistry","Maths","English"]
marks =[]
for subject in subjects:
          while True:
                  try:
                          mark = float(input(f"Enter your marks for {subject} out of 100:"))
                          if 0<marks<=100:
                                  marks.append(mark)
                                  break
                          else:
                                  print("Marks should be between 0 and 100 ")
                  except ValueError:
                              print("Please enter a valid number")  
total = sum(marks)
avg = total/len(subjects)
grade = calc_grade(avg)

print("\n Student report card generated")
print("-"*30)
print(f"Name  : {name}")
print(f"rollno  : {roll}")
print(f"class  : {classs}")
print("-"*30)
for i in range(len(subjects)):
        print(f"{subjects[i]:10} : {marks[i]}/100")

print("-"*30)

print(f"total  : {total}/100")
print(f"average  : {avg}")
print(f"grde  : {grade}")




