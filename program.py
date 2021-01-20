import modules

def input_number(text_value,errortext="Invalid input,input not a valid number!"):
    while True:
        input_value = input(text_value)
        if input_value.isdigit():
            return int(input_value)
        print(errortext)
        
def input_not_zero(text_value):
    while True:
        number=input_number(text_value)
        if number!=0:
            return number
        print("Input can not be zero!")

def divisable_numbers():
    print("Enter two numbers to find common divisable numbers up to 1000.")
    number1 = input_not_zero("Input the first nubmer:")
    number2 = input_not_zero("Input the second nubmer:")
    print(modules.generate_divisible_numbers(number1, number2))

def menu():
    while True:
        print("1. Generate Divisable Numbers\n2. Guessing Game\n3. Exit")
        choice = input_number("Input choice:","Invalid option! Try again.")
        if choice == 1:
            divisable_numbers()
        elif choice == 2:
            modules.guessing_number()
        elif choice == 3:
            print("Exiting Menu.")
            return
        else:
            print("Invalid option! Try again.")

menu()