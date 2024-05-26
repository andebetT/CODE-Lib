def intToRoman(num):
    mapping = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}

    roman = ''
    for value, symbol in mapping.items():
        while num >= value:
            roman += symbol
            num -= value

    return roman
print(intToRoman(4))


def convert_integers_to_romans(nums):
    mapping = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}
    roman_numerals_list = []

    for num in nums:
        roman_numeral = ""
        for key, value in mapping.items():
            while num >= key:
                roman_numeral += mapping[key]
                num -= key
        roman_numerals_list.append(roman_numeral)

    return roman_numerals_list
print(convert_integers_to_romans([1, 4, 179]))
