# Functions
def generate_divisible_numbers(number1, number2,limit = 1000):
    number_list = []
    average = 0
    for counter in range(1, limit + 1):
        if counter % number1 == 0 and counter % number2 == 0:
            number_list.append(counter)
            average+=counter
    average = average/len(number_list)
    return {"number_list": number_list, "average": average}

def guessing_number(limit_upper = 100, limit_lower = 1):
    attempts = 0
    from random import randint
    rand_number = randint(limit_lower, limit_upper + 1)
    while True:
        try:
            try_input = int(input(f"Guess a number betwenne {limit_lower} to {limit_upper} :"))
        except ValueError:
            print("Input is not valid a number!")
            continue
        try_input = int(try_input)
        if try_input>limit_upper or try_input<limit_lower:
            print(f"Input ({try_input}) is outside of the scope ({limit_lower} to {limit_upper}).")
            continue
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
