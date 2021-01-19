# functions

def generate_numbers(num1 ,num2):
    number_list=[]
    limit=1000
    for counter in range(limit):
        if counter%num1==0 and counter%num2==0:
            number_list.append(counter)
    average=0
    for item in number_list:
        average+=item
    return { "number_list":number_list , "average":average}

def guessing_number():
    limit_upper=100
    limit_lower=1
    from random import randint
    rand_number=randint(limit_lower,limit_upper)
    while True:
        try_input=input(f"Guess a number betwenne {limit_lower} to {limit_upper} :")
        if not try_input.isnumeric():
            print("Input is not numeric!")
            continue
        else:
            try_input=int(try_input)
        if try_input==rand_number:
            print(f"WOOHOO you guess of {try_input} was correct. Congratualtions!")
            break
        else:
            if rand_number>try_input:
                hint="larger"
            else:
                hint="smaller"
            print(f"Your Guess was incorrect , the nubmer your looking for is {hint}.")
