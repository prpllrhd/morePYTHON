#!/usr/bin/env python
def get_numeric_value_from_keyboard():
    '''Get a value from keyboard, if the value is not a valid number, raise a "ValueError" exception'''
    input_value = input("Please, enter an integer: ")
    if not input_value.isdigit():
        raise ValueError("The value inserted is not a number")
    return input_value

while True:
    try:
        numeric_value = get_numeric_value_from_keyboard()
        print("You have inserted the value " + str(numeric_value))
        break
    except ValueError as ex:
        print("Something strange happened...")
        raise
