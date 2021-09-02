# Kapittel 2 Algorithm Workbench & Programming Exercises

# Algorithm Workbench
# Oppgave 1
height = input("What is your height in centimeters? ")
print(f"Your height is {height}cm")

# Oppgave 2
color = input("What is your favorite color? ")
print(f"Your favorite color is {color}!")

# Oppgave 3 --> 3 = var4 er ikke en gyldig variabel

# Oppgave 4
w = 5
x = 4
y = 8
z = 2
result_a = x + y
result_b = z * 2
result_c = int(y / x)
result_d = y - z
result_e = int(w // z)

print("result_a = ", result_a)
print("result_b = ", result_b)
print("result_c = ", result_c)
print("result_d = ", result_d)
print("result_e = ", result_e)

# Oppgave 5
total = 10 + 14
print(total)

# Oppgave 6
total_cost = 1000
down_payment = 100
payment_due = total_cost - down_payment
print(f"Your payment due is ${payment_due}")

# Oppgave 7
subtotal = 70
tax = 0.15
total = subtotal * (1 + tax)
print(f"The total price is ${total}")

# Oppgave 8
a = 5
b = 2
c = 3
result = a + b * c
print(result)

# Oppgave 9
a = 20
b = 40
c = 30
(x, y, z) = (a, b, c)
print(x, y, z)

# Oppgave 10
sales = 12345.6789
print("The total amount of sales with comma separators and rounded to 2 decimal points is", format(sales, ",.2f"))

# Oppgave 11
number = 1234567.456
print("""To display the float number "1234567,456" as "1,234,567.5",""", \
    "we will need to format the number with commas as separators and", \
    """with a single decimal point using the "format(1234567.456, ",.1f")" function,""", \
    "which will return the value", format(number, ",.1f"))

# Oppgave 12
print("George", "John", "Paul", "Ringo", sep="@")
print("George", "John", "Paul", "Ringo", sep="")
print("George", "John", "Paul", "Ringo", sep=" ")
print("George", "John", "Paul", "Ringo", sep="-")


# Programming Exercises
# Oppgave 1
print("My name is Stian")
print("I live in Langelandvegen 14, 7540 Klæbu, Trøndelag, Norway")
print("My phone number is 94 83 93 11")
print("My college major is in business administration")

# Oppgave 2
projected_revenue = int(input("What is the projected revenue for the company? "))
expected_profit_margin = format(0.23, ".0%")
print(f"The expected profit margin is {expected_profit_margin}")
projected_profit = projected_revenue * 0.23
print(f"The projected profit of the company is ${int(projected_profit)}")

# Oppgave 3
users_land_sq_feet = int(input("How many square feet of land do you want to convert into acres? "))
sq_feet_in_acres = 43560
convert_sq_feet_to_acres = users_land_sq_feet / sq_feet_in_acres
print(convert_sq_feet_to_acres)

# Oppgave 4
item_1 = float(input("What is the price of the first item? "))
item_2 = float(input("What is the price of the second item? "))
item_3 = float(input("What is the price of the third item? "))
item_4 = float(input("What is the price of the fourth item? "))
item_5 = float(input("What is the price of the fifth item? "))

sub_total_unformatted = item_1 + item_2 + item_3 + item_4 + item_5
sub_total = format(sub_total_unformatted, ",.2f")
tax_unformatted = sub_total_unformatted * 0.07
tax_formatted = format(tax_unformatted, ",.2f")
total_unformatted = sub_total_unformatted + tax_unformatted
total = format(total_unformatted, ",.2f")
print(f"The subtotal is {sub_total}, the 7% sales tax amounts to {tax_formatted}", \
    f"and the total price to pay is {total}")

# Oppgave 5
# Distance = Speed x Time, Speed = 70mph
print(f"The distance travelled in 6 hours is {70 * 6} miles")
print(f"The distance travelled in 10 hours is {70 * 10} miles")
print(f"The distance travelled in 15 hours is {70 * 15} miles")

# Oppgave 6
purchase_total = float(input("What is the amount of the purchase excluded taxes? "))
purchase_total_formatted = format(purchase_total, ",.2f")
state_tax_unformatted = purchase_total * 0.05
state_tax_formatted = format(state_tax_unformatted, ",.2f")
country_tax_unformatted = purchase_total * 0.025
country_tax_formatted = format(country_tax_unformatted, ",.2f")
total_price_formatted = format(purchase_total + state_tax_unformatted + country_tax_unformatted, ",.2f")
print(f"The total price to pay is {total_price_formatted}, whereas the state sales tax amounts for", \
    f"{state_tax_formatted} of the price and the country sales tax amounts for {country_tax_formatted} of the price")
    
# Oppgave 7 --> MPG = Miles driven / Gallons of gas used
miles = float(input("How many miles did you drive? "))
gas_used = float(input("How many gallons of gas was used for the trip? "))
mpg = format(miles / gas_used, ",.2f")
print(f"The miles per gallon ratio on the trip was {mpg}")

# Oppgave 8
food_cost = float(input("Enter the price for the food: "))
tax = 0.07
tip = 0.18
tax_cost = food_cost * tax
tip_cost = food_cost * tip
total_price = food_cost + tax_cost + tip_cost
print("The tax amounts to", format(tax_cost, ",.2f"))
print("The tip amounts to", format(tip_cost, ",.2f"))
print("The total cost amounts to", format(total_price, ",.2f"))

# Oppgave 9
degrees_C = float(input("How many degrees celsius do you want displayed in farenheit? "))
degrees_F = 9 / 5 * degrees_C + 32
print(f"{degrees_C} degrees Celsius is the equivalent of {degrees_F} degrees Farenheit")

# Oppgave 10
sugar_per_cookie = 1.5 / 48
butter_per_cookie = 1 / 48
flour_per_cookie = 2.75 / 48
desired_amount_cookies = int(input("How many cookies do you want to cook? "))
sugar_desired = sugar_per_cookie * desired_amount_cookies
butter_desired = butter_per_cookie * desired_amount_cookies
flour_desired = flour_per_cookie * desired_amount_cookies

print(f"The required ingredients for {desired_amount_cookies} cookies are:")
print(format(sugar_desired, ".2f"), "cups of sugar")
print(format(butter_desired, ".2f"), "cups of butter")
print(format(flour_desired, ".2f"), "cups of flour")

# Oppgave 11
males = int(input("How many males are in the class? "))
females = int(input("How many females are in the class? "))
total_classmates = males + females
males_share = males / total_classmates
females_share = females / total_classmates
males_percentage = format(males_share, ".2%")
females_percentage = format(females_share, ".2%")

print("The total percentge of genders in the class consisting of", total_classmates, "people are:")
print(males_percentage, "males and", females_percentage, "females")

# Oppgave 12
shares_bought = int(input("How many shares of the company did you buy? "))
price_per_share_buy = float(input("What was the average purchase price of the shares bought? "))
cost_all_shares = shares_bought * price_per_share_buy
commission_purchase = cost_all_shares * 0.03
shares_sold = int(input("How many shares of the company did you sell? "))
price_per_share_sell = float(input("What was the average price of the shares sold? "))
total_sell_price = shares_sold * price_per_share_sell
commission_sale = total_sell_price * 0.03
profit = - (cost_all_shares + commission_purchase) + (total_sell_price - commission_sale)
print("The total purchase including commission paid to the broker was", format(cost_all_shares + commission_purchase, ",.2f"), "$")
print("The total sale including commission paid to the broker was", format(total_sell_price - commission_sale, ",.2f"), "$")
print("The total profit from the investment / trade is", format(profit, ",.2f"), "$")