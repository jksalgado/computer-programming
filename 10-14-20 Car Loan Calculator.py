#Car Loan Payment Calculator
#Jasmin Salgado
#CP1
#10/14/20

#inputs:
print("This program will help you determine the monthly cost\n of a newly purchased car")
#sticker price
stickerPrice = int(input('Enter the sticker price: $ '))
#trade in value
tradeIn = int(input('Enter your trade in price of you car if not trading in enter 0: $ '))
#tax rate
taxRate = float(input('Enter your local tax rate as a decimal: $ '))
#dealer fees
dealerFees = int(input('Enter any dealer fees: $ '))
#rebates/incentative
rebates = int(input('Enter the amount of rebates or incentatives you will be receiving\n if none enter 0: $ '))


#calculations
subtotal = stickerPrice - tradeIn
tax = taxRate * subtotal
subtotal = subtotal + tax
subtotal += dealerFees
subtotal -= rebates

print(f"Your ar will cost ${subtotal}, now let's do the financing")

#down payment
downPayment = int(input('Enter your down payment: $ '))
#length of loan
lengthOfLoan = int(input('Enter months of how long you would like the loan to be: '))
#interest rate
interestRate = float(input('Enter the interest rate as a decimal: '))

#calculations
financed = subtotal - downPayment
print(f'You will be financing ${financed} over {lengthOfLoan} months')

#calculate financed amount
monthlyRate = interestRate / 12
payment = subtotal * ((monthlyRate*((1 + monthlyRate)**lengthOfLoan))/(((1 + monthlyRate)**lengthOfLoan)-1))

#output monthly payment value
print(f'Your {subtotal} car will be paid in {lengthOfLoan} monthly payments of ${payment} ')


input('Press enter to quit')
