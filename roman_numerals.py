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
  pass

def roman_true_numbers(roman):
  pass

def compute_array(array):
  pass

if __name__ == "__main__":
  # assert roman_to_arabic('MCMXII') == 1912
  # assert roman_to_arabic('MM') == 2000
  # assert roman_to_arabic('MDCCLXXVI') == 1776

  assert roman_true_numbers('MCMXII') == [1000, 100, 1000, 10, 1, 1]
  assert roman_true_numbers('MM') == [1000, 1000]
  assert roman_true_numbers('MDCCLXXVI') == [1000, 500, 100, 100, 50, 10, 10, 5, 1]

  # assert compute_array([1000, 100, 1000, 10, 1, 1]) == 1912
  # assert compute_array([1000, 1000]) == 2000
  # assert compute_array([1000, 500, 100, 100, 50, 10, 10, 5, 1]) == 1776
  