# Kapittel 3 Programming Exercises
# Kap 11 - Book Club Points

# Serendipity Booksellers has a book club that awards points
# to its customers based on the number of books purchased
# each month. The points are awarded as follows:
# If a customer purchases 0 books, they earns 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.

# Write a program that asks the user to enter the number 
# of books that they purchased this month, and generate an 
# answer that displays how many points they got.

books_purchased = int(input('How many books have you purchased this month? '))

if books_purchased == 0 or books_purchased == 1:
    print('You have earned 0 points this month.')
elif books_purchased == 2 or books_purchased == 3:
    print('You have earned 5 points this month.')
elif books_purchased == 4 or books_purchased == 5:
    print('You have earned 15 points this month.')
elif books_purchased == 6 or books_purchased == 7:
    print('You have earned 30 points this month.')
elif books_purchased >= 8:
    print('You have earned 60 points this month.')
else:
    print('Error. Invalid number of books.')