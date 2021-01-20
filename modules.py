# Functions
def generate_divisible_numbers(number1, number2,limit = 1001):
    number_list = []
    for counter in range(1, limit):
        if counter % number1 == 0 and counter % number2 == 0:
            number_list.append(counter)
    average = 0
    for item in number_list:
        average += item
    average = average/len(number_list)
    return {"number_list": number_list, "average": average}


def guessing_number(limit_upper = 100, limit_lower = 1):
    attempts = 0
    from random import randint
    rand_number = randint(limit_lower, limit_upper + 1)
    while True:
        try_input = input(f"Guess a number betwenne {limit_lower} to {limit_upper} :")
        if not try_input.isdigit():
            print("Input is not valid a number!")
            continue
        else:
            try_input = int(try_input)
        if try_input>limit_upper or try_input<limit_lower:
            print(f"Input ({try_input}) is outside of scope ({limit_lower} to {limit_upper}) ")
            continue
        else:
            attempts+=1
        if try_input == rand_number:
            print(f"WOOHOO!!! Your guess of {try_input} was correct. Congratualtions!, Attempts={attempts}")
            break
        else:
            if rand_number > try_input:
                hint = "larger"
            else:
                hint = "smaller"
            print(f"Your guess was incorrect , the nubmer your looking for is {hint}.")
