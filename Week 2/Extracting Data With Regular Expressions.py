'''
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
'''
import re

fname = ('regex_sum_42.txt')
#fname = ('regex_sum_1683143.txt')
handle = open(fname)
sum=0
count = 0
for line in handle:
	f = re.findall('[0-9]+',line)
	for num in f:
		if num >= [0]:			
			count += 1
			sum += int(num)
		
print('There are ',count,'values with the sum = ', sum)
