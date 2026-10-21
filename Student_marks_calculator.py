students = {
    "Nikita": 92,
    "Aarav": 35,
    "Riya": 40,
    "Sam": 67,
    "Priya": 28,
    "Kabir": 76
}
total_marks=0
average_marks=0
for name in students:
    marks=students[name]
    total_marks+=marks
    average_marks=total_marks/len(students)

print("Total:",total_marks)
print("Average:",average_marks)

highest=0
lowest=0
for marks in students:
  if students[marks]>highest:
    highest=students[marks] 
  elif students[marks]<lowest:
     lowest=students[marks]

print(highest)
print(lowest)
     
    