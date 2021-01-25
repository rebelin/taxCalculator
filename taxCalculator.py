# Rebecca Lin
# 4/24/17

def numInput(answer): # Asks the user for an integer gross income, returns the gross income when it is an integer
	""" Asks the user for an integer, makes sure the input is an integer, returns an integer. """
	x = False
	while x == False: 
		try: # This checks if the input is what's needed for the program (an integer)
			answer = int(answer)
			x = True
		except ValueError: # If the user doesn't enter an integer, the program will ask again
			answer = input("Sorry, that's not an integer number. Try again: ")
			
	return answer
		
def adjustedIncome(num): 
	""" Takes the integer gross income, subtracts standard deductions, and returns the adjusted income. """
	
	if num >= 9500:
		adjustedIncome = num - 9500 # Single exempt is $3700; standard deduction is $5800
	else:
		adjustedIncome = 0 # If gross income is less than 9500, the deductions make the adjusted income 0
	
	return adjustedIncome
	
# incomes less than $9500 are tax free
def tax(num, taxplan):	
	""" Takes the integer adjusted income and calculates the owed taxes for the specified taxplan. """
	
	tax = 0		
	for amount, percent in taxplan:
		if num > amount: 
			num -= amount
			amount *= percent
			tax += amount	
		else: # When num < amount, the remaining amount of money (num) is taxed, not the whole tax rate range (amount)
			num *= percent  
			tax += num
			num = 0 # This stops the for loop from adding additional tax
	return round(tax, 2)

def percent(tax, gross): # Tax rate is the total tax divided by the gross income
	""" Takes and divides the total tax by the gross income to return the tax rate. """
	
	rate = round(tax / gross, 2) * 100
	return int(rate)

def net(income, tax): # Net income is the gross income minus the total tax
	""" Takes and subtracts the tax from the adjusted income to return the net income. """
	
	net = income - tax
	return net

def results(year, tax, percent, net):
	""" Takes four numbers and returns the results with corresponding numbers. """
	return "Results for the {} plan\nTakes owed: ${}\nPercent of gross: {}%\nNet income: {}\n".format(year, tax, percent, net) 

#----------- Main Program ---------------
print("Welcome to the tax calculator.")
grossIncome = numInput(input("How much gross income did you earn last year (rounded to nearest dollar)? $"))

adjustedIncome = adjustedIncome(grossIncome)		

# 2000 Tax Plan 
# list of the differences between tax rates of the 2000 tax plan
taxplan00 = [(2650, 0), (25199, .15), (32049, .28), (74299, .31), (155749, .36), (289951, .396)] 
tax00 = tax(adjustedIncome, taxplan00)

print(results(2000, tax00, percent(tax00, grossIncome), net(grossIncome, tax00)))


# 2008 Tax Plan
# list of the differences between tax rates of the 2008 tax plan
taxplan08 = [(8025, .1), (24524, .15), (46299, .25), (85699, .28), (193149, .33), (357701, .35)]
tax08 = tax(adjustedIncome, taxplan08)

print(results(2008, tax08, percent(tax08, grossIncome), net(grossIncome, tax08)))


# 2014 Tax Plan
# list of the differences between tax rates of the 2014 tax plan
taxplan14 = [(8700, .1), (26649, .15), (50299, .25), (92999, .28), (209699, .33), (388351, .35)]
tax14 = tax(adjustedIncome, taxplan14)

print(results(2014, tax14, percent(tax14, grossIncome), net(grossIncome, tax14)))

