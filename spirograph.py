



import turtle
import math
import numpy as np
turtle.exitonclick()



def draw_circle(t, center_x, center_y, radius, color):
    t.penup()
    t.goto(center_x, center_y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.goto(center_x, center_y)
    t.pendown()


def draw_spirograph(big_turtle, small_turtle, R, r, d):
    theta = 0  # Start angle
    update_frequency = 2  # Update the screen every 10 steps; increase this number for faster drawing
    while theta <= 1000 :  # Loop through the angles to draw the spirograph
        # Calculate the position of the spirograph point
        x = (R - r) * math.cos(math.radians(theta)) + d * math.cos(math.radians((R - r) / r * theta))
        y = (R - r) * math.sin(math.radians(theta)) - d * math.sin(math.radians((R - r) / r * theta))

        # Calculate the position of the small circle
        small_circle_x = (R - r) * math.cos(math.radians(theta))
        small_circle_y = (R - r) * math.sin(math.radians(theta))

        # Move the small circle to the new position
        small_turtle.clear()  # Clear the previous small circle
        small_turtle.penup()  # Lift the pen to move without drawing
        small_turtle.goto(small_circle_x, small_circle_y - r)  # Move to the new position
        small_turtle.pendown()  # Put the pen down to start drawing
        small_turtle.fillcolor("")  # Set the fill color to transparent
        small_turtle.circle(r)  # Draw the small circle

        # Draw the spirograph point
        big_turtle.penup()  # Lift the pen to move without drawing
        big_turtle.goto(x, y)  # Move to the spirograph point position
        big_turtle.pendown()  # Put the pen down to draw
        big_turtle.dot(3, "red")  # Draw a dot for the spirograph point

        theta += 1  # Increment the angle

        # Update the screen at the specified frequency
        if theta % update_frequency == 0:
            turtle.update()  # Force the screen to update

def main():
    try:
        # Set up the screen
        screen = turtle.Screen()  # Create a screen object
        screen.bgcolor("white")  # Set the background color to white
        turtle.tracer(0, 0)  # Disable automatic screen updates

        # Set up the turtles
        big_turtle = turtle.Turtle()  # Create a turtle for the large circle and spirograph
        big_turtle.speed(0)  # Set the turtle speed to maximum
        big_turtle.hideturtle()  # Hide the turtle to avoid showing the turtle icon

        small_turtle = turtle.Turtle()  # Create a turtle for the small circle
        small_turtle.speed(0)  # Set the turtle speed to maximum
        small_turtle.hideturtle()  # Hide the turtle to avoid showing the turtle icon

        # Draw the large circle
        draw_circle(big_turtle, 0, 0, 200, "lightblue")  # Draw the large circle at the center

        # Example parameters for the spirograph
        # Example parameters
        R = 200  # Radius of the large circle
        r = 2*R/5  # Radius of the small circle
        d = r   # Distance from the center of the small circle to the drawing point
        # Draw the spirograph
        draw_spirograph(big_turtle, small_turtle, R, r, d)  # Call the function to draw the spirograph

        # Final update
        turtle.update()  # Force the final screen update
        # Finish
        screen.mainloop()


    except turtle.Terminator:
        print("The turtle graphics window was closed prematurely.")  # Handle the window being closed prematurely
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle any unexpected errors

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to execute the script