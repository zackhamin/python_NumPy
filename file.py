

# x = 1
# y = 2.254

# name = "Ishaq"
# age = 32

# #String
# print("My name is {} and I am {} years old".format(name,age))

# string = "abcdeghijkl"

# print(string[2])
# print(string[0:])

# # Lists / Arrays
# my_list = ["a","b","c","d"]
# print(my_list)

# my_list.append("e")
# print(my_list)
# print(my_list[0:3])

# # Keys

# key = {'key1':"Some information", 'key2':12334}
# print(key['key1'])
# print(key['key2'],key['key1'])


# print(1 > 2)

# # If statement
# if 1>2:
#     print("Got it")
# elif 1<2:
#     print("Middle")
# else:
#     print("Not got it")


# #For statement
# for letter in my_list:
#     print(letter)

# for letter in my_list:
#     print("Hello")

# i = 1

# while i < 5:
#     print("i is {}".format(i))
#     i = i+1

# for letter in range(0,3):
#     print("Hello")

# for number in range(0,22):
#     print(number)


# x = [1,2,3,4]
# out = []

# for num in x:
#     out.append(num ** 2)
# print(out)

# #List comprehension

# out = [num ** 2 for num in x]
# print(out)

# def my_func(param1):
#     print(param1)
# my_func(1234567890)

# def my_name(name):
#     print("Hey "+name)
# my_name("Ishaq")

# def square_num(num):
#     return num **2
# output = square_num(12)
# print(output)

# #map() and lambda expressions

# def times2(var): return var*2
# print(times2(5))

# #Map(below) can take the function and run it for every item in the array.

# sequence = [1,2,3,4,5]
# outlist = list(map(times2,sequence))
# print(outlist)

# #Lambda is an anonymous functions

# # lambda var: var *2

# lmb_output = list(map(lambda num: num*2, sequence))
# print(lmb_output)

# #filter

# flt_output = list(filter(lambda num: num%2 == 0 , sequence))
# print(flt_output)


# #methods

# name_string = "Hello my name is Zack"
# print(name_string.lower())
# print(name_string.upper())
# print(name_string.split())

# lst = [1,2,3,4,5]
# lst.pop()
# new_lst = lst.pop()
# print(new_lst)
# print(lst)

# def convert_to_int(list):
#     string_numbers = list
#     string_numbers.split()
#     print(string_numbers)

# convert_to_int("123")

# seven = 7
# four = 4

# print(seven ** four)

# test_string = "Hi there sam!"

# print(test_string.split())

# planet = "Earth"
# diameter = 12742

# print("The diameter of {} is {} kilometers".format(planet,diameter))

# #Grab the word hello in the list
# nested_list = [1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7]
# nested_output = nested_list[3][1][2]
# print(nested_output)

# # Return the email domain name after the @
# def grab_email(email):
#     email_split =  email.split("@")[-1]
#     print(email_split)
# grab_email("zack@domain.com")

# def findDog(st):
#      contains =  "dog" in st.lower().split()
#      print(contains)
# findDog("Does this text contain the word dog")


# sequence_test = ["soup","dog","salad","cat","great"]
# sqnc_contains = list(filter(lambda word: word[0] == "s",sequence_test))
# print(sqnc_contains)

def speedingTicket(speed, is_birthday):

    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if(speeding < 60):
        print("No ticket")
    elif(speeding >= 61 and speeding <= 80):
        print("Small ticket")
    else:
        print("Big ticket")


speedingTicket(64, False)