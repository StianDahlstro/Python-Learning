# Kap 4 Programming Exercises

# Oppgave 2 - Calories Burned
# Running on a particular tredmill you can burn
# 4.2 calories per minute. Write a program that 
# uses a loop to display the number of calories
# burned after 10, 15, 20, 25 and 30 minutes. 

cal_min = 4.2
cal_5 = cal_min * 5
cal_10 = cal_min * 10
total_cal_burned = cal_5

for time in range(10, 31, 5):
    total_cal_burned += cal_5
    print('The amount of caloried burned after', time, 'minutes is', total_cal_burned)
