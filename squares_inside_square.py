import turtle

def drawSquares(my_turtle, length_of_side, count_squares, distance_apart):

    for n in range(count_squares):
        for _ in range(4):
            my_turtle.forward(length_of_side)
            my_turtle.left(90)

        my_turtle.penup()
        x, y = my_turtle.position()
        my_turtle.goto(x + distance_apart / 2, y + distance_apart / 2)
        my_turtle.pendown()
        length_of_side -= distance_apart

if __name__=='__main__':
  window = turtle.Screen() # Setting up the attributes and thee window
  window.title("Drawing 10 Squares in Python")

  new_turtle = turtle.Turtle()
  new_turtle.penup()
  new_turtle.goto(60, 60)
  new_turtle.pendown()

  drawSquares(new_turtle, 200, 10, 10)
  turtle.done()

