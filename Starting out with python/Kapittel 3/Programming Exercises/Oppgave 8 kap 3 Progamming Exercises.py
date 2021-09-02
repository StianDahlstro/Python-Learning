# Kap 3 Progamming Exercises
# Oppgave 8 - Hot Dog Cookout Calculator

# Assume that hotdogs come in packages of 10,
# and hot dog buns come in packages of 8.
# Write a program that calculates the number of
# packages of hot dogs and the number of packages 
# of hot dog buns needed for a cookout, with the
# minimum amount of leftovers.
# The program should ask the user for the number of
# people attending the cookout and the number of hot dogs
# each person will be given.
# The program should display the following:
# The minimum number of packages of dogs required
# The minimum number of packages of buns required
# The number of dogs left
# The number of buns left

dogs_in_package = 10
buns_in_package = 8

cookout_participants = int(input('How many people will attend the cookout? '))
dogs_per = int(input('How many dogs will be served to each attendee? '))
dogs_total = cookout_participants * dogs_per

packs_dogs_total = dogs_total // dogs_in_package
dogs_left_over = dogs_total % dogs_in_package
packs_buns_total = dogs_total // buns_in_package
buns_left_over = dogs_total % buns_in_package

print('The total number of dogs served during the cookout is: ', dogs_total)

if dogs_left_over > 0:
   print('The number of packs of hotdogs needed is: ', packs_dogs_total + 1)
   print('The number of dogs left after the cookout is: ', dogs_in_package - dogs_left_over)
else:
   print('The number of packs of hotdogs needed is: ', packs_dogs_total)
   print('There are no dogs left after the cookout.')

if buns_left_over > 0:
    print('The number of packs of buns needed is: ', packs_buns_total + 1)
    print('The number of buns left after the cookout is: ', buns_in_package - buns_left_over)
else:
    print('The number of packs of buns needed is: ', packs_buns_total)
    print('There are no buns left after the cookout.')