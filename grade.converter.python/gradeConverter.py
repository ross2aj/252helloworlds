def gradeAverage(quiz, test, final):
	return quiz * 0.2 + test * 0.3 + final * 0.5

def convertNumberToGrade(n):
	if n >= 90: return "A"
	if n >= 80: return "B"
	if n >= 70: return "C"
	if n >= 60: return "D"
	return "F"

def getMessage(avg, grade):
	return "The student's grade average is {}. They will recieve a {} in the class.".format(avg, grade)

avg = gradeAverage(98,77,84)
g = convertNumberToGrade(avg)
print(getMessage(avg, g))
