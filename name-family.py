class Student:
	courseMarks={}
	name=""
	family = ""
	def __init__(self, name, family):
		self.courseMarks={}
		self.name=name
		self.family=family

	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark
		return "Mark added!"

	def average(self):
		total = 0
		for course, mark in self.courseMarks.items():
			total += mark
		total=total/len(self.courseMarks)
		return total



if __name__=="__main__":
	
	student = Student("Ana", "Marcu")
	print("Student Ana Marcu created")
	student.addCourseMark("Math", 100)
	print("Math mark 100")
	student.addCourseMark("English", 80)
	print("English mark 80")
	average = student.average()
	print("Marks average: " + str(average))


#def do_stuff_with_number(n, list1):
	
#	print(list[n])
#list1 = [1, 2, 3, 7, 2, 4]
#for  i in range(10):
#	try:
#		do_stuff_with_number(i, list1)
##		print(0)
		
	
#inside main:
#import doctest
#doctest.testmod()

#inside class:
#def addition(self, x, y):
#"""
#testing:
#>>> c = MyClass()
#>>> print(c.addition(3, 4))
#7
#"""
#return x+y
