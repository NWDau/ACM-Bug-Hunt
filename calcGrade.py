### Grade Calculator

#functions
def grade (avg):
  if (avg < 60): letter = 'F'
  elif (avg < 70): letter = 'D'
  elif (avg < 80): letter = 'C'
  elif (avg < 90): letter = 'B'
  else: letter = 'A'
  return letter

def calcAvg (exam1, exam2, exam3, exam4):
  avg = (exam1 + exam2 + exam3 + exam4)/4
  return avg

#MAIN
##input
exams = [0]*4
for i in range(4):
  exams[i] = float(input("Enter exam score: "))
##calc average score & grade
avg = calcAvg(exams[0], exams[1], exams[2], exams[3])
print("Average:", avg, "\nGrade:", grade(avg))
