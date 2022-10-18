import random

MAX_LINES=3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2 ,
	"B" : 4 ,
	"C" : 6 ,
	"D"	: 8	
}


symbol_value = {
    "A" : 5 ,
	"B" : 4 ,
	"C" : 3 ,
	"D"	: 2	
}

def check_winnings(columns, lines,bet,values):
	winnings = 0
	winning_lines = []
	winning_lines
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_check = column[line]
			if symbol != symbol_check:
				break
		else:
			winnings = winnings + values[symbol] * bet
			winning_lines.append(line + 1)
			
	return winnings, winning_lines


def get_spin(rows,cols,symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)
	
	columns = []
	for _ in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)
			
		columns.append(column)
			
	return columns	




			
def print_spin(columns):
	for row in range(len(columns[0])):
		for i, column in enumerate(columns):
			if i != len(columns) - 1:
				print(column[row], end= " | ")
			else :
				print(column[row], end="")
				
		print()



	

def deposit():
	while True:
		amount = input("how much do you want to deposit : $")
		if amount.isdigit():
			amount=int(amount)
			if amount > 0:
				break
			else:
				print("amount must be greater than 0")
		else:
			print("please enter a number")
			
	return amount






def get_number_of_lines():
	while True:
		lines = input("enter the number of lines to bet (1-" + str(MAX_LINES) + ")? ")
		if lines.isdigit():
			lines=int(lines)
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print("Enter a valid number of lines")
		else:
			print("please enter a number")  
			
	return lines	





	

def get_bet():
	while True:
		amount = input("what do you want to bet on each line ? : $")
		if amount.isdigit():
			amount=int(amount)
			if MIN_BET <= amount <= MAX_BET:
				break
			else:
				print("amount must be between " + str(MIN_BET )+ "-" + str(MAX_BET) + ".")
		else:
			print("please enter a number")	
			
	return amount		




	
def main():
	balance = deposit()
	lines = get_number_of_lines()
	while True :
		bet = get_bet()
		total_bet = bet * lines
		
		if total_bet > balance :
			print("balance not enough")
		else:
			break
		
	print("you are betting " + str(bet) + " on " + str(lines) + " lines. total bet is equal to:" + str(total_bet) + ".\n")
	
	
	print(balance,lines)
	
	slots = get_spin(ROWS, COLS, symbol_count)
	print_spin(slots)
	winnings,winning_lines = check_winnings(slots, lines, bet, symbol_value )
	print("\nyou won " + str(winnings) + ".")
	
	
main()
	
