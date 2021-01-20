#UI (User Interface)
import modules

def input_number(text_value):
    while True:
        input_value=input(text_value)
        if input_value.isdigit():
            return int(input_value)
        print("Invalid input,input not a number!")

def divisable_numbers():
    print("Enter two numbers to find common divisable numbers up to 1000.")
    number1=input_number("Input the first nubmer:")
    number2=input_number("Input the second nubmer:")
    print(modules.generate_divisible_numbers(number1,number2))

divisable_numbers()
modules.guessing_number()

