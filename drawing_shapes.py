# You're provided with a base shape class and square class which extends it. The goal is to create ASCII art Square

class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):
		print(self.printChar * (i + 1))

t = Triangle()
t.print()

t = Square()
print()
t.print()