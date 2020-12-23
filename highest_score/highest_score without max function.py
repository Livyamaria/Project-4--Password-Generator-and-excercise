""" To find the highest score without using max function"""


student_scores =[]
limit = int(input("Enter limit : "))
for i in range(0, limit):
    elements= int(input("enter the Scores:"))

    student_scores.append(elements)

print(student_scores)
max=0

for i in student_scores:
    if i >max:
       max=i
print(f"Highest score is : {max}")

