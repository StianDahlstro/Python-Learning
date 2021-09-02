# Programming Exercises kap 5
# Oppgave 5 - Property Tax

# A country collects property taxes on the assessment value
# of property, which is 60 percent of the property's actual value.
# For example, if an acre of land is valued at $10,000, its 
# assessment value is $6,000.
# The property tax is then 72 cents for each $100 of the assessment value.
# The tax for an acre assessed at $6,000 will be $43.20. 
# Write a program that asks the user for the actual value of a piece of
# property and displays the assessment value and property tax.

def main():
# Using return values in the functions called by the main function to 
# keep more data in the main function. I do this to mainly prevent the 
# called functions to call another function, making a long "one-way road"
    taxable_value = assessment_value()
    tax_total = property_tax(taxable_value)
    tax_format = format(tax_total, ',.2f')
    print('Total property tax for this property is $', tax_format, sep='')

def assessment_value():
    aquired_value = float(input("Enter the property's actual value: $"))
    return aquired_value * 0.6

def property_tax(taxable_value):
    return taxable_value * 72 / 10000

main()