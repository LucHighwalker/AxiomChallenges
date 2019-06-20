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
    roman = roman.upper()  # Makes sure all letters are uppercase
    array = []

    for letter in roman:
        try:
            # Appends the true value of the roman letter.
            array.append(roman_dict[letter])
        except KeyError:
            return []  # If not a valid roman number, return empty array.

    return array


def compute_array(array):
    """Adds numbers in reverse, if a number is less than the previous number,
    that number should be subtracted instead of added to the total."""
    array = array[::-1]  # Reverse array, could be optimized by walking through the array backwards via indexes.
    # The last number added from the array. Starts at 0 because roman numerals are all greater than 0.
    previous = 0
    total = 0  # The end result to be returned

    for number in array:
        if number < previous:  # If the number is less than the previous number, subtract number from total
            total -= number
        else:  # Otherwise, add number to total and set previous to that number.
            total += number
            previous = number

    return total


def test():
    assert roman_true_numbers('MCMXII') == [1000, 100, 1000, 10, 1, 1]
    assert roman_true_numbers('MM') == [1000, 1000]
    assert roman_true_numbers('MDCCLXXVI') == [1000, 500, 100, 100, 50, 10, 10, 5, 1]

    assert compute_array([1000, 100, 1000, 10, 1, 1]) == 1912
    assert compute_array([1000, 1000]) == 2000
    assert compute_array([1000, 500, 100, 100, 50, 10, 10, 5, 1]) == 1776
    
    assert roman_to_arabic('MCMXII') == 1912
    assert roman_to_arabic('MM') == 2000
    assert roman_to_arabic('MDCCLXXVI') == 1776


if __name__ == "__main__":
    running = True

    while running:
        roman = input('\nEnter a roman numeral (q to quit): ')
        if roman == 'q' or roman == 'Q':
            running = False
        elif roman == 't' or roman == 'T':
            test()
            print('Everything seems to be in order.\n')
        else:
            result = roman_to_arabic(roman)
            if result == 0:
                print('Invalid roman numeral.\n')
            else:
                print('Arabic conversion: {}\n'.format(result))
