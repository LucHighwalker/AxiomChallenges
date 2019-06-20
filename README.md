# Axiom Coding Challenges

## 1:
Given a string representing a Roman numeral, write a function to compute the Arabic numerical equivalent. For example `roman_to_arabic("MDCCLXXVI")` should return `1776`.

## Solution:
Converting the letters into their true values was easy using a simple dictionary. The challenge came trying to add those numbers together. I've decided to reverse the array of numbers and keep track of the previously added number. For each number, if it is larger than the previously added value, then it adds it to the sum. But if it is smaller, it will subtract it instead. This ensures that left sided roman numerals get subtracted properly without any complex looking ahead.


## 2:
Write a generic function to compute various scenarios for the following optimization problem: A farmer owns X acres of land. She profits P1 dollars per acre of corn and P2 dollars per acre of oats. Her team has Y hours of labor available. The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre. How many acres of each can be planted to maximize profits?
Test the function for the following cases:
a) X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
b) X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
c) X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2

## Solution:
I struggled a bit with this one. It's one of those math problems you see a ton in high school/college, but for the life of me, could not remember how to solve it. Getting tripped up on and failing to remembering the formula, I decided to simply brute force it. Creating a while loop which simply calculates all possibilities of splitting up the land. Honestly not too proud of this one, as I'm sure there is a more efficient way of calculating this, than running all possibilites.


## 3: 
Given the differential equation f'(x) = x^x, write a function that uses Euler's method to approximate the value of f(x1) given an initial condition (x0, f(x0)) and the value of x1.