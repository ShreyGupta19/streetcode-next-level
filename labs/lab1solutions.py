def squareIfOdd(num):
	if num % 2 != 0:
		return num**2
	else:
		return num

def tictactoe():
	for i in range(5):
		if i % 2 == 0:
			print("  |  |  ")
		else:
			print("--------")

def tictactoe_forpros():
	print('\n'.join((["  |  |  ", "--------"] * 3)[:-1]))

def hourglass(n):
	for i in range(n):
		print(" " * i + "*" * (2 * (n - i)))
	# TODO: Finish this solution

def rotate2(string):
	return string[2:] + string[:2]

import datetime

def how_old(bday):
	bday_list = bday.split("/")
	day = int(bday_list[1])
	month = int(bday_list[0])
	year = int(bday_list[2])
	today = datetime.date.today()
	years_old = today.year - year
	if month > today.month:
		years_old -= 1
	elif month == today.month and day > today.day:
		years_old -= 1
	return years_old 

def how_old_forpros(bday):
	month, day, year = [int(xx) for xx in bday.split("/")]
	today = datetime.date.today()
	years_old = today.year - years
	if month > today.month or (month == today.month and day > today.day):
		years_old -= 1
	return years_old

def in_range_1to10(n, outside_mode):
	if not outside_mode and 1 <= n <= 10:
		return True
	elif outside_mode and (n < 1 or n > 10):
		return True
	else:
		return False

def in_range_1to10_forpros(n, outside_mode):
	return outside_mode != (1 <= n <= 10)

def in_range(start, end, n, outside_mode):
	if not outside_mode and start <= n <= end:
		return True
	elif outside_mode and (n < start or n > end):
		return True
	else:
		return False

def in_range_forpros(start, end, n, outside_mode):
	return outside_mode != (start <= n <= end)

def max_diff(nums):
	max_num = -float('inf')
	min_num = float('inf')
	for num in nums:
		if num > max_num:
			max_num = num
		if num < min_num:
			min_num = num
	return max_num - min_num

def max_diff_shorter(nums):
	return max(nums) - min(nums)

def shuffle(arr):
	return arr[0:len(arr):2] + arr[1:len(arr):2]

def shuffle_forpros(arr):
	return arr[::2] + arr[1::2]

def numToRoman(num):
	translation = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
	return translation[num - 1]

def max_ascending(arr):
	max_len = 1
	curr_len = 0
	for i in range(1, len(arr)):
		if arr[i] > arr[i-1]:
			curr_len += 1
		elif curr_len > 0:
			if max_len < curr_len:
				max_len = curr_len
			curr_len = 0

def numberToWords(num):
	place_vals = ["", "thousand", "million", "billion", "trillion", "quadrillion"]
	name = []
	curr_place_val = 0
	while num > 0:
		last_three_digits = num % 1000
		if last_three_digits != 0:
			name.append(numberToWordsHundreds(num % 1000) + " " + place_vals[curr_place_val])
		num = num // 1000
		curr_place_val += 1
	name = reversed(name)
	return ' '.join(name)


def numberToWordsHundreds(num):
	ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	digits = list(reversed([int(digit) for digit in str(num)]))
	num_digits = len(digits)
	name = []
	if num_digits == 1: return ones[digits[0]]
	if num_digits >= 3:
		name.append(ones[digits[2]] + " hundred")
	if num_digits >= 2:
		last_two_digits = digits[1] * 10 + digits[0]
		if last_two_digits == 0:
			return ' '.join(name)
		if 10 <= last_two_digits < 20:
			name.append(teens[digits[0]])
		else:
			name.append(tens[digits[1]])
			if digits[0] != 0:
				name.append(ones[digits[0]])
	return ' '.join(name)