import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a turtle
t.pensize(5)
t.color("green")
t.fillcolor("lightgreen")
t.begin_fill()
t.circle(50)
t.end_fill()

# Add eyes
t.penup()
t.goto(-15, 60)
t.pendown()
t.color("black")
t.dot(10)

t.penup()
t.goto(15, 60)
t.pendown()
t.color("black")
t.dot(10)

# Add text
t.penup()
t.goto(-30, 30)
t.pendown()
t.color("black")
t.write("Turtle", font=("Arial", 12, "bold"))

# Hide the turtle
t.hideturtle()

# Close the turtle graphics window on click
turtle.exitonclick()
