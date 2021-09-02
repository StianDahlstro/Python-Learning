# Kap 3, Programming Exercises
# Oppgave 2 - Areas of Rectangles

# The area of a rectangle is the rectangle's
# length times its width. Write a program that
# asks for the length and width of two rectangles.
# The program should tell the user which rectangle
# has the grater area, or if the areas are the same.

length_rectangle_1 = float(input('What is the length of the first rectangle? '))
width_rectangle_1 = float(input('What is the width of the first rectangle? '))

length_rectangle_2 = float(input('What is the length of the second rectangle? '))
width_rectangle_2 = float(input('What is the width of the second rectangle? '))

area_rectangle_1 = length_rectangle_1 * width_rectangle_1
area_rectangle_2 = length_rectangle_2 * width_rectangle_2

if area_rectangle_1 > area_rectangle_2:
    print('Rectangle 1 has a greater area than rectangle 2.')
elif area_rectangle_1 < area_rectangle_2:
    print('Rectangle 2 has a greater area than rectangle 1.')
else:
    print('Both rectangles have the same area.')