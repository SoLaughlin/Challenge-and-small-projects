"""
Takes a roman numeral as its argument and returns the corresponding decimal integer.
"""
def solution(string):
    roman_numeral_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    string_list = list(string)
    sub_strings = []
    string_values = []
    numerical_value = 0

    def find_sub_strings(input):
        common_value = 1

        for counter, each_char in enumerate(string_list):
            # ensures for loop doesn't index out of range of list
            if counter + 1 == len(string_list):
                # checks if last character is not unique
                if each_char == input[counter - 1]:
                    sub_strings.append(each_char * common_value)
                else:
                    sub_strings.append(each_char)
            elif each_char == string_list[counter + 1]:
                common_value += 1
            elif each_char != string_list[counter + 1]:
                sub_strings.append(each_char * common_value)
                common_value = 1 # resets this value

    find_sub_strings(string)

    for each_item in sub_strings:
        length = len(each_item)
        value = roman_numeral_values.get(each_item[0]) * length
        string_values.append(value)

    for count, each_value in enumerate(string_values):
        # ensures for loop doesn't index out of range of list
        if count + 1 == len(string_values):
            numerical_value += each_value
        elif each_value > string_values[count + 1]:
            numerical_value += each_value
        elif each_value < string_values[count + 1]:
            numerical_value -= each_value

    return numerical_value
