# Eg:
# I/P: "Welcome to this code"
# O/P: "code this to Welcome"

# Python code for the above approach

def reverse_words(s):
	left = 0
	i = 0
	s = list(s)
	n = len(s)
	
	while(s[i] == ' '):
		i = i+1
		
	left = i
	
	while(i < n):
		if(i+1 == n or s[i] == ' '):
			j = i-1
			if i+1 == n:
				j = j+1
			
			while left < j:
				s[left], s[j] = s[j], s[left]
				left = left+1
				j = j-1
			
			left = i + 1
		
		if(i > left and s[left] == ' '):
			left = i
		
		i = i+1
		
	s = ''.join(s)
	
	s = s[::-1]
	
	return s