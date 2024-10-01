num = int(input("Enter a number:" ))
count = 0

for i in range(2,num,1):
	if num%i==0:
		count = count + 1
	
if count>=1:
	print("not prime")
else:
	print("prime")	
		
