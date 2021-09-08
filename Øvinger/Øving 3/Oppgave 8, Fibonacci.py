# Oppgave 8
# Fibonacci

# A) & B) & C)
k = int(input('Enter how many fibonacci iterations you want to run: '))
iteration_number = 0
sum = 0
fib_list = []
for i in range(k):
    if i == 0:
        iteration_number = 0
        fib_list.append(iteration_number)
    elif i == 1:
        iteration_number = 1
        sum += 1
        fib_list.append(iteration_number)
    else:
        iteration_number = fib_list[i - 1] + fib_list[i - 2]
        sum += iteration_number
        fib_list.append(iteration_number)

print(f'The last fibonacci number in the given sequence is {iteration_number}.')
print(f'The sum of all the fibonacci numbers in the series is {sum}.')
print(fib_list)