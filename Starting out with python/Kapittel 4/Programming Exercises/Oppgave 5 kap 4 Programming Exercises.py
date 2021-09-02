# Kap 4 Programming Exercises

# Oppgave 5 - Average Rainfall
# Write a program that ises nested loops to collect
# data and calculate the average rainfall over a 
# period of years. The program should first ask for
# the number of years. The outer loop will iterate 
# once for each year. The inner loop will iterate 
# twelwe times, once for each month.
# Each iteration of the inner loop will ask the user
# for the inches of rainfall for that month.
# After all the iterations, the program should display
# the number of months, the total inches of rainfall, 
# and the average rainfall per month for the entire period.

another_year = 'y'
total_rain = 0
year = 0
total_months = 0

while another_year == 'y' or another_year == 'Y':
    year += 1
    for month in range(1, 13):
        rain_per_month = float(input(f'How many inches of rainfall was recorded in month {month} in year {year}? '))
        total_rain += rain_per_month
        total_months += 1
    another_year = input('Do you want to record rainfall for another year? Enter Y if yes: ')

rain_average = total_rain / total_months

print('The total inches of rainfall over the period of ', total_months, \
    ' months (', year, ' year(s)) is ', format(total_rain, ',.2f'), ' inches of rain,' \
    ' with the average amount of rain monthly at ', format(rain_average, ',.2f'), ' inches of rain.', sep='')
