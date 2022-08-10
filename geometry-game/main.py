from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fall_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        # Go to certain coordinate
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.x)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)  # move 100 pixel
        canvas.left(90)  # turn 90 degrees left
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        turtle.done()


gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))
print(gui_rectangle.area())

my_turtle = turtle.Turtle()
gui_rectangle.draw(canvas=my_turtle)

# Create rectangle object
# rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
# print("Rectangle Coordinates: point1.x: ", rectangle.point1.x,
#       ', point1.y: ', rectangle.point1.y,
#       ', point2.x: ', rectangle.point2.x,
#       ', point2.y: ', rectangle.point2.y)
#
# # Get point and area from user
# user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
# user_area = float(input("Guess rectangle area: "))
# print('user_point => ', user_point)
# # Print out the game result
# print("Your point was inside rectangle: ", user_point.fall_in_rectangle(rectangle))
# print("Your area was off by: ", rectangle.area() - user_area)
