# import pytest for using utilities
from pytest import approx

# import the code to be tested
from gradeConverter import gradeAverage, convertNumberToGrade, getMessage

# write a smoke test
def test_smoke():
  assert True == True

# test conversion of grades averages
def test_gradeAverage():
	assert gradeAverage(0,0,0) == 0
	assert gradeAverage(60,80,90) == 81
	assert gradeAverage(50,60,80) == 68

# test convert number to grade
def test_convertNumberToGrade():
	assert convertNumberToGrade(90) == "A" 
	assert convertNumberToGrade(84) == "B"
	assert convertNumberToGrade(78) == "C"
	assert convertNumberToGrade(69) == "D"
	assert convertNumberToGrade(31) == "F"

# test get message
def test_getMessage():
	assert getMessage(97,"A") == "The student's grade average is 97. They will recieve a A in the class."
	assert getMessage(85,"B") == "The student's grade average is 85. They will recieve a B in the class."
	assert getMessage(71,"C") == "The student's grade average is 71. They will recieve a C in the class."
	assert getMessage(62,"D") == "The student's grade average is 62. They will recieve a D in the class."
	assert getMessage(15,"F") == "The student's grade average is 15. They will recieve a F in the class."
