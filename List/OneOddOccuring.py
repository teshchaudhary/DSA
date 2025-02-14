def OneOddOccuring(arr):
	num = 0
	
	for element in arr:
		num = num ^ element

	return num

arr = []

print(OneOddOccuring(arr))