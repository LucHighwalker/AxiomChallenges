roman_dict = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}

def roman_to_arabic(roman):
  """Takes in a roman numeral, calls function to convert to 
  array of true numbers, then calls and returns another function
  which computes the resulting array."""
  true_numbers = roman_true_numbers(roman)
  return compute_array(true_numbers)

def roman_true_numbers(roman):
  """Converts roman numeral to an array of true number conversions"""
  roman = roman.upper() # Makes sure all letters are uppercase
  array = []

  for letter in roman:
    try:
      array.append(roman_dict[letter]) # Appends the true value of the roman letter.
    except KeyError:
      return [] # If not a valid roman number, return empty array.
      
  return array

def compute_array(array):
  """Adds numbers in reverse, if a number is less than the previous number,
  that number should be subtracted instead of added to the total."""
  array = array[::-1] # Reverse array, could be optimized by walking through the array backwards via indexes.
  previous = 0 # The last number added from the array. Starts at 0 because roman numerals are all greater than 0.
  total = 0 # The end result to be returned

  for number in array:
    if number < previous: # If the number is less than the previous number, subtract number from total
      total -= number
    else: # Otherwise, add number to total and set previous to that number.
      total += number
      previous = number
  
  return total

if __name__ == "__main__":
  assert roman_to_arabic('MCMXII') == 1912
  assert roman_to_arabic('MM') == 2000
  assert roman_to_arabic('MDCCLXXVI') == 1776

  assert roman_true_numbers('MCMXII') == [1000, 100, 1000, 10, 1, 1]
  assert roman_true_numbers('MM') == [1000, 1000]
  assert roman_true_numbers('MDCCLXXVI') == [1000, 500, 100, 100, 50, 10, 10, 5, 1]

  assert compute_array([1000, 100, 1000, 10, 1, 1]) == 1912
  assert compute_array([1000, 1000]) == 2000
  assert compute_array([1000, 500, 100, 100, 50, 10, 10, 5, 1]) == 1776
  