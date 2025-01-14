import turtle

def draw_branch(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth > 0:
        # Draw the current branch
        turtle.forward(branch_length)
        
        # Draw the right branch
        turtle.right(right_angle)
        draw_branch(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        
        # Backtrack
        turtle.left(right_angle)
        
        # Draw the left branch
        turtle.left(left_angle)
        draw_branch(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        
        # Backtrack
        turtle.right(left_angle)
        
        # Return to the original position
        turtle.backward(branch_length)

def main():
    # Set up the turtle
    turtle.speed(0)  # Fastest drawing speed
    turtle.left(90)  # Point the turtle upwards
    turtle.up()
    turtle.backward(100)  # Move the turtle down
    turtle.down()
    turtle.color("green")

    # Define parameters
    left_angle = 30  # Left branch angle
    right_angle = 30  # Right branch angle
    starting_length = 100  # Starting branch length
    recursion_depth = 5  # Recursion depth
    reduction_factor = 0.7  # Branch length reduction factor

    # Draw the tree with specified parameters
    draw_branch(starting_length, left_angle, right_angle, recursion_depth, reduction_factor)

    # Finish up
    turtle.done()

if __name__ == "__main__":
    main()
    
    