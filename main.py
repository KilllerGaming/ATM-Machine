money = 0
card = "696969696969/0625/990"
opt = input('Please enter your Card Details : ')

if opt == card:
	opt2 = input('What action to take? Deposit / Withdraw / Balance : ').lower()
	if opt2 == "deposit":
		depamt = int(input('Please enter the amount to be deposited : '))
		money = money + depamt
		print("Now your current balance is Rs. ", money)
	elif opt2 == "withdraw":
		withamt = int(input('Please enter the amount to be withdrawan : '))
		if withamt <= money:
			money = money - withamt
		elif withamt > money:
			print("Dude ur dad ain't Gautum Adani ;-;")
	elif opt2 == "balance":
		print("Your current account balance is Rs. ", money)
elif opt != card:
	print("Incorrect credentials provided!")