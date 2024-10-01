x = int(input("Enter the number"))

while x < 0:
	num = int(input("Please, enter another the number"))
	
	if num > 0 and num%2==0:
		print("Code stopped!")
		print(2*num)
		break;
	else:
		print(num*num)
