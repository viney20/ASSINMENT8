#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class circle:
    r = int(input("Enter radius"))
    def getArea(self):
        print("Area of circe", 3.14 * self.r * self.r)
    def getCircumference(self):
        print("Circumference of circe", 2 * 3.14 * self.r)
x = circle()
x.getArea()
x.getCircumference()
#Create a Student class and initialize it with name and roll number
class student:
    def __init__(self):
        self.name = input("Enter name")
        self.rollno = int(input("Enter roll no"))

    def setAge(self):
        self.age = int(input("Enter age"))

    def setMarks(self):
        self.marks = int(input("Enter marks"))

    def display(self):
        print("name =", self.name, " rollno =", self.rollno, " age =", self.age, " marks =", self.marks)


x = student()
x.setAge()
x.setMarks()
x.display()


#Q.3 Create a Temprature class and create two methods
class temperature:
    def convertFarenheit(self, c):
        print("farenheit = ", c * 1.8 + 32)

    def convertCelsius(self, f):
        print("celsius = ", (f - 32) / 1.8)


c = float(input("enter celcius value"))
t = temperature()
t.convertFarenheit(c)
f = float(input("enter farenheit value"))
t.convertCelsius(f)

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
class MovieDetails:
    def __init__(self):
        self.name = input("Enter aritist_name")
        self.year = int(input("Enter Year of release"))
        self.rating = int(input("Enter Ratings"))

    def display(self):
        print("Artist name =", self.name, " Year of release=", self.year," Rating =", self.rating )
x=MovieDetails()
x.display()
    

#Q.5 Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def animal_attribute(self):
        print("animal")
class Tiger(Animal):
    def tiger(self):
        print("tiger")

a = Animal()
t = Tiger()
t.animal_attribute()



#Q.6- What will be the output of following code.
"""
ANS:-> #geting error because interprator wants '(' this  in line no 14&15  AFTER  solving error output is
'A', 'B'
'A', 'B'




"""
#Q.7 Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
class shape:
    def __init__(self):
        self.length=int(input("enter length"))
        self.breath=int(input("enter breadth"))
    def area(self):
        if self.length==self.breath:
            area = self.length * self.breath
            print("square area= ", area)
        else:
            area = self.length * self.breath
            print("rectangle area= ", area)
        
class square(shape):
    def __init__(self):
        super().__init__()
   
class rectangle(shape):
    def __init__(self):
        super().__init__()
sq = square()
sq.area()
re = rectangle()
re.area()


