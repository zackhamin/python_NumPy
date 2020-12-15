# print("Hey, what is your name?")
# # myName = input()
# print("Nice to meet you,")

# print(True is not False)

# spam = ["cat","Bat","Rat","Elephant"]

# print(spam[1:3])



# def convert_string(numbers):
#     numbers_list = []
#     number_list = numbers
   

#     print(number_list)


# convert_string('1,2,3')


def number_divisble(number):
    if number % 15 == 0:
        print("Yeah, man", number)
    elif number % 3 == 0:
        print("Solid work", number)
    elif number % 5 == 0:
        print("Getting there" , number)
    else:
         print(number)
number_divisble(30)