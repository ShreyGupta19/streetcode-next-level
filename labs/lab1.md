#Lab 1: Python and Programming Fundamentals

Welcome to the first lab! We're going to have a lab every Wednesday starting this week. These labs are a chance for you to really drill down into the core concepts we discuss. Here's how labs are set up:

1. **Rapidfire Questions**: Quick comprehension questions to make sure you get the basics. These typically involve predicting what a code snippet will output, and can be easily verified using Python's interactive interpreter!
2. **Warmup Coding**: Some short, typically straightforward practice problems that require 5-10 lines of good Python to solve.
3. **Mini Project**: An interesting problem that can take anywhere from 15-50 lines of code to solve. These problems tend to be more complex and sophisticated, and it can help to take a few minutes to think and design an optimal solution before coding!

We also have some advanced sections made for those of you who want a little extra challenge or are interested in interviewing for tech companies soon!

Also, don't worry if the labs have some material you haven't seen yet! The labs are meant to challenge you and force you to search online and use your resources well! Remember, if you want to test some code, use the interactive interpreter, and if you want to find Python functions, use the Python docs and StackOverflow.

**And most importantly**: the labs are huge! You're NOT meant to finish the whole thing during class. The idea is to leave you with some stuff you can also do over the weekend!

#Rapidfire Questions
What will the Python 3.5 Interactive Interpreter return for the following? (First try guessing yourself, then pop it into the interpreter!)

1. `1 + 2`
2. `1 / 3`
3. `1 // 3`
4. `2**3`
5. `float("inf")`
6. `float(1) // 3`
7. `int(1 / 3)`
8. `'Hello' == "Hello"`
9. `'Hello' != "hello"`
10. `2 == 2 && true`
11. `2 == 2 and True`
12. `!False`
13. `not False`
14. `"Hello World!"[0:5]`
15. `"Hello World!"[0:5] != "Hello World!"[:5]`
16. `"Hello World!"[6:] != "Hello World!"[-6:]`
17. `[2, 3, 4] == [2, 3, 4]`
18. `[2, 3, 4] == [2, 4, 3]`
19. `[2, 3, 4] == (2, 3, 4)`
20. `{"a": 1, "b": 2} == {"b": 2, 'a': 1}`

Bob wants to write a function that will take a number and return its square ONLY if the number is odd. If the number is even, the function simply returns the number. Bob writes the following code, but it doesn't even run! Correct the code so it works properly. There are 6 errors to correct.

	function squareIfOdd(int num):
	if !(num % 2 == 0):
		return num^2
		else:
			return num
			
#Warmup
Some questions adapted from Stanford's CS41 Materials (cs41.stanford.edu) and from codingbat.com.

1. *Tic Tac Toe*: Write a function that uses `print()` to create a Tic Tac Toe board:
	
		  |  |
		--------
		  |  |
		--------
		  |  |  

2. *Hourglass*: Write a function that prints an hourglass shape of a given size `n` (i.e. the base of the hourglass has `2 * n` stars).
	
	For example, the following is an hourglass of size 3 :
	
		******
		 ****
		  **
		 ****
		******
	
	And the following is an hourglass of size 5:
	
		**********
		 ********
		  ******
		   ****
		    **
		   ****
		  ******
		 ********
		**********

3. *Rotate 2*: Write a function that takes a string and returns a version of the string "rotated to the left by 2" (i.e. the first two characters are moved to the end). If the string doesn't have enough characters to rotate by 2 characters, return `None`.

		rotate2('Hello') --> 'lloHe'
		rotate2('java') --> 'vaja'
		rotate2('Hi') --> 'Hi'
		rotate2('a') --> None

4. *How Old am I?*: Write a function that takes a birthday in the format `"MM/DD/YYYY"` and returns the age of the person in number of days (rounded down). You might find the [`str.split`](https://docs.python.org/3.5/library/stdtypes.html#str.split) function useful. Also, to get today's date, you can use the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects) module. Remember to import the module properly!

	Hint: Remember about leap years!

		how_old('11/12/2000') --> 5925
		
5. *In Range 1 to 10*: Write a function that takes two arguments: a number `n` and a boolean `outside_mode`. THe function returns `True` if `n` is in the range 1 to 10, inclusive, and `False` otherwise. However, if the argument `outside_mode` is `True`, return `True` if `n` is *outside* the range 1 to 10, inclusive, and `False` otherwise.

		in_range_1to10(5, False) --> True
		in_range_1to10(11, False) --> False
		in_range_1to10(-1, False) --> False
		in_range_1to10(5, True) --> False
		in_range_1to10(11, True) --> True
		
6. *Maximum Difference*: Given a list of integers, find the maximum difference between any two numbers in the list. In other words, find the difference between the minimum and maximum elements of the list.

		max_diff([10, 2, 1, 12]) --> 11
		max_diff([10, 10]) --> 0
		max_diff([10, -10, 2]) --> 20
		
7. *Array Shuffle*: Write a function that shuffles a list by taking every element with an even index and places them together at the beginning of the array. For example:

		shuffle([1, 2, 3, 4, 5, 6]) --> [1, 3, 5, 2, 4, 6]
		shuffle([10, 4, 1, 8, 2]) --> [10, 1, 2, 4, 8]
		shuffle([1]) --> [1]

8. *Number to Roman*: Write a function that takes any integer from 1 to 10 and converts it to roman numeral form. *Note*: It's easy enough to just write ten if statements for this, but you can do better! Try using a list -- you can get your solution down to around 2 lines this way!

		numToRoman(4) --> "IV"
		numToRoman(10) --> "X"
		numToRoman(3) --> "III"
		
9. **CHALLENGE!** *In Range General*: Write a function that is similar to the one you wrote for "In Range 1 to 10", but works on any range. Your function should accept four arguments: the start of the range, the end of the range, the number to check, and the `outside_mode` flag. If there is an invalid range defined, return `None`.

		in_range(2, 10, 3, False) --> True		in_range(2, 10, 3, True) --> False
		in_range(10, 2, 3, True) --> None
		
10. **CHALLENGE!** *Maximum Ascending Sublist*: Write a function that takes an list of integers and returns the size of the largest ascending sublist. An ascending sublist is one where each element is greater than the previous one. For example, for the list `[1, 5, 9, 9, 8, 7]`, `[1, 5, 9]` is an ascending sublist, but `[9, 9]` (not strictly greater), `[9, 8, 7]` (descending), and `[1, 5, 8]` (not consecutive) are not. 

		max_ascending([5, 10, 15, 20]) --> 4
		max_ascending([1, 3, 2, 4, 5, 6, 1]) --> 3
		max_ascending([4, 3, 2, 1]) --> 1

#Mini-Project
Write a function that can take a number from 0 to 999 and convert it to its English form. For example:

| Number (Input) | Word (Output) |
| -------------- | ------------- |
| 0 | zero |
| 19 | nineteen |
| 72 | seventy-two |
| 102 | one hundred two |
| 185 | one hundred eighty-five |
| 999 | nine hundred ninety-nine |

This project will test your ability to think about problems and break them down into simpler, more manageable parts. It will also test how clever you are with writing your code! While it is possible to write lots of code filled with if statements to get the job done, it's far from the best way. A complete working solution for this problem can be written in just 15 lines of Python! While it is not expected that your code will be as short, try to keep it as short as possible!

##Tips

1. Don't jump right into coding. Think about how you want to approach this problem, then flag down one of us and tell us what you're thinking!
2. Start small: at first, try to just handle the numbers 0-9. Then 0-99. Then tackle 0-999! You'll notice that the problem will get easier if you approach it as various smaller and easier problems.
3. Think about what you need: you need a way of extracting digits from the number one by one and a way to name each digit (e.g. `1 -> "one"`). 
4. We'll give you a testing script that you can use to see if your implementation works. Beware, we will test various edge cases too, so make sure your function is robust!

##Extensions
If you finish this, here's a few challenging extensions!

1. Write a version of your number translator that works for numbers from 1 - 1,000,000.
2. Write a version of your number translator that works for numbers from 1 - 10^15.

#Advanced Material
TBD.