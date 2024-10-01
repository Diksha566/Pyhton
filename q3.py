x = input("Enter your Grade:" )

if x>=90 and x<=100:
	print("Your Grade is A, Excellent!")
	
elif(x<=89 and x>=80):
	print("Your Grade is B, Good!")
	
elif(x<=79 and x>=70):
	print("Your Grade is C, Average!")	
	
elif(x<=60 and x>=69):
	print("Your Grade is D, Needs to improve!")	

else:
	print("Falling")
