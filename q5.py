x = int(input("Enter the number:" ))

if x%4== 0 and (x%100!= 0 or x%400==0):
	print("The entred year is a leap year")

else:
	print("Then entred year is not a leap year")
