# [# Introduction to Functions (Precalculus - College Algebra 2)](https://youtu.be/FkUEsP9efFg)
**Domain** => range of inputs {1,2,3,... N}
**Range** => range of outputs {1,2,3,... N}
1:1 function must always map a single consistent value to a single consistent value
1:N function must map a single value to one or move values

**Independent Variables** => X values
**Dependent Variables** => Y value
the goal is the notation y = f(x) 
	- dep var `y` is a function of ind. var `x`
**How to determine if algebraic formula is a function**
	- function should return a single value given an input
	- plugging in values for X is not a sufficient way to test. X values like 0 and 1 may make it seem like it's a function when it is not
	- **IS FUNCTION** check if the formula is solved for y (example `y = mx + b`)
	- **IS FUNCTION** `y = √3-2x`
	- **IS NOT FUNCTION** `y = ±√3-2x` because ± indicates a choice between values or a pos/neg value, yields 2 outputs for every input
	- if you simplify the function and y is raised to an even number, it is not a function because it will result in a `±` in front of the square root
		- eg: `3x^2 + 3y^2 = 1`
		- ![[Pasted image 20230805132150.png]]![[Pasted image 20230805132443.png]]
	- if the formula is not, solve for y first (`2x - 4y = 8`  => `-4y = -2x + 8` => `y = -1/2x - 2`)
		- when simplifying a function, the goal is to zero out values
# [How to Evaluate Functions (Precalculus - College Algebra 3)](https://youtu.be/p1sGAHulT8w)
## function notation
- ![[Pasted image 20230806193114.png]]
- `y = -7x + 5` is the same as `f(x) = -7x + 5`
- `f(x) = ...` is preferred because
	- it's descriptive and names the equation and identifies the independent variable `x`
	- instructs you to look at a specific function and a specific variable passed to that funciton
	- if you have the function defined you can simplify the expression to f(2) = 9
	- shows you the input and the output the ordered pair is (2,-9)
- `h(x) = -2x^2 + x -1`
## function evaluation
- the variable is the only replacable thing change your variables with blank spaces 
	- ![[Pasted image 20230806193051.png]]
	- `h(x) = -2x^2+x-1` can be thought of as `h(-1) = -2(__)^2+(__)-1` > `h(-1) = -2(-1)^2+(-1)-1`
		- parens keeping sign and operation
		- remember order of operations
		- don't attempt to solve in your head, it's easy to forget signs and order of operations
		- simplify the function as normal
	- ![[Pasted image 20230806193425.png]]
	- ![[Pasted image 20230807203913.png]]
	- `h(x+1) = -2( )^2 + ( ) -1`
		- `h(x+1) = -2(x+1)^2 + (x+1) - 1`
			- `h(x+1) = -2((x+1) * (x+1)) + (x+1) - 1`
				- `h(x+1) = -2((x * x) + (x * 1) + (1 * x) + (1 * 1) * (x+1)) + (x+1) - 1`
					- `h(x+1) = -2(x^2+2x+1) + (x+1) - 1`
						- `h(x+1) = -2(x^2) + -2(2x) + -2(1) + (x+1) - 1`
							- `h(x+1) = -2x^2 - 4x - 2 + x + 1 - 1`
								- `h(x+1) = -2x^2 - 3x - 2`
## Difference Quotient
- Difference, meaning subtraction, quotient meaning division
- ![[Pasted image 20230809212133.png]]
	- when solving, `- f(x)` will change your `-/+` signs
- ![[Pasted image 20230809212523.png]]
	- in this example you're effective getting of rate of change between two inputs
	- subtract 1 function output value from another, then dividing by change of `x` and `x + h`
	- the formula above gives the slope of a line or rise-over-run (y2-y1)/x
- 
- going to evaluate the equation: **the main goal is to cancel out the `h`**
	- solve `f(x+h)` then `f(x)` then combine outcomes into numerator
- ![[Pasted image 20230809214229.png]]
- ![[Pasted image 20230809213349.png]]
- ![[Pasted image 20230809213420.png]]
- ![[Pasted image 20230809213901.png]]
- ![[Pasted image 20230809213957.png]]
	- notice `+ 1` becomes `- 1` because we're distributing the minus operator
- ![[Pasted image 20230809214058.png]]
	- as `h` approaches a limit `0`. this value becomes closer to just `2x`
	- this allows you to find the slope of on any part of a  curve
- ![[Pasted image 20230809215300.png]]
	- this means the slope at the specific (x,y) point (2,5) in the curve `x = 2` is 4 when `f(x) = x^2 + 1`
		- `4` comes from the `x^2` or `2^2`. The leftover `+ 1` indicates the "run" of the slop
- `f(x+h)`
![[Pasted image 20230807210523.png]]
![[Pasted image 20230807210612.png]]
## Even/Odd Functions
- even if you plug in `-x` and gives you the same value as `x` then you have an even function
	- if you plug in `-x` and outcomes gives you the opposite sign for every value, then it's odd
## Domain Issues
- the goal is to see if the numbers plugged into the function provide real and defined numbers
- having the square root of 0 is fine. The inverse is 0 
- ![[Pasted image 20230807210709.png]]
	- **1 is a problem because you can't have the negative square root**
	- 1 is only a problem because the result gives you a negative number (radicant)
- **1 issue is numbers that give you negative numbers inside of square roots (not cube roots)**
- ![[Pasted image 20230807212806.png]]
- ![[Pasted image 20230807212604.png]]![[Pasted image 20230807212624.png]]
	- **this is a problem because `0` can't be a denominator, this is an undefined number**
	- `5` is not in the domain of this function
- ![[Pasted image 20230809211812.png]]
	- `-` in front of function means to just put a neg sign in front of function — `-` does not affect the variable's value, just the function outcome
# [Finding the Domain of Functions (Precalculus - College Algebra 4)](https://www.youtube.com/@ProfessorLeonard)
- Domain is the set of inputs for a function that give a real number output
	- these are instructions on what value the function has to have for the function to work
	- Domain of Square Root describes the allowed values
	- Domain of a Denominator describes values that are not allowed
	- a **real number** is a number that can be used to measure a continuous one-dimensional quantity such as a distance, duration or temperature.
- ![[Pasted image 20230810203235.png]]
	- a negative number inside a square root is an imaginary number
- ![[Pasted image 20230810203820.png]] 
- ![[Pasted image 20230810205645.png]]
- the domain is `x <= 5/4` 
	- represents the interval of numbers that will give you a real number
	- can be written as `{x <= 5/4}`
	- **Set Builder Notation** `D:{x|x <= 5/4}`
		- "domain is x such that x is ..."
	- Interval Notation `(-∞,5/4]`
- ![[Pasted image 20230810210523.png]]
- ![[Pasted image 20230810211342.png]]
	- the domain cannot include any of the values at the bottom
- ![[Pasted image 20230810210740.png]]
	- if t were 4 or -4, the domain would hit a vertical asymptote
- ![[Pasted image 20230813213048.png]]
	- if your function doesn't have a Log, Square Root or Denominator, then the domain is all real numbers for every polynomial
- ![[Pasted image 20230813213107.png]]
	- when you have fractions and square roots, deal with both issues separately — think about what conditions must be met for both
	- ![[Pasted image 20230813213425.png]]
		- don't switch the inequality unless you divide by a negative
	- ![[Pasted image 20230813213628.png]]
		- don't need `x != 4` since it's redundant information
	- ![[Pasted image 20230813214046.png]]
	- ![[Pasted image 20230813214209.png]]
		- denom can't be `0` so remove the `=` part of equality
# [Operations of Functions (Precalculus - College Algebra 5)](https://youtu.be/7N_-G4usp6Q)
- add, subtract, multiply, divide functions
- **you never cancel original domain restrictions**
- 1st Step - Find the domain of each invidual function
- ![[Pasted image 20230815210429.png]]
	- all numbers still work except for 2/3
	- either one of the domains will be in the domain of the resulting function
- ![[Pasted image 20230815210845.png]]
	- denoms should always be factored
- ![[Pasted image 20230815210941.png]]
- ![[Pasted image 20230815211526.png]]
	- keep common denoms as factors then move to exponent
	- need to leave as exponent denom because fn will give as asymtote where when `x=2/3`
- ![[Pasted image 20230815212941.png]]
	- when dividing domains:
		- **must** always start with the original domain restriction `x != 2/3` and the problem may reveal addition restrictions
![[Pasted image 20230815213605.png]]
	- these domain restrictions will follow us, but we might add more
![[Pasted image 20230815213812.png]]
	- start by adding the original domains, worst case, you add more restrictions to the domain
- ![[Pasted image 20230815214214.png]]
# [Using the Vertical Line Test (Precalculus - College Algebra 6)](https://youtu.be/7j6kh8Z2H90)
