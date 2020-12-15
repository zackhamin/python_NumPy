
import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
arrTwo = np.array(my_mat)

arrange = np.arange(0,20,2)
#// the last number is how much you want to count up by.



counting_numbers = np.linspace(0,50,10)
# works from the first number to the second with counts by the number of the last.


one_digit_arrays = np.ones(6)
# print 1 six times.

one_digit_double_arrays = np.ones((4,4))
#Double array of 1s 4x4

identity_matrix = np.eye(4)
# identity matrix is a matrix useful with linear algebra, two dimensional, diagnal of ones. 


random_array = np.random.rand(5)
#random numbers from 0 to 1

random_array_tuple = np.random.rand(5,5)
#random numbers from 0 to 1 in a multidemnsional array

random_array_int = np.random.randint(1,100,10)
#random numbers from 0 to 100, last number is how many numbers you want.


new_array = np.arange(25)

ranrarr = np.random.randint(0,50,10)

reshaped_array = new_array.reshape(5,5)
#changes the shape of an array. 


max = ranrarr.max()
#max value of an array

min = ranrarr.min()
#min value of an array


max_position = ranrarr.argmax()
#position of the highest number in the array

min_position = ranrarr.argmin()
#position of the lowest number in the array


print(my_list)
print(arr)
print(my_mat)
print(arrTwo)
print(arrange)
print(counting_numbers)
print(one_digit_arrays)
print(one_digit_double_arrays)
print(identity_matrix)
print(random_array)
print(random_array_tuple)
print(random_array_int)
print("--------------------------")
print(new_array)
print(ranrarr)
print(reshaped_array)
print("--------------------------")
print(max)
print(max_position)
print(min)
print(min_position)
print(ranrarr.shape)
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("----------ARRAY INDEXING----------------")

array_indexed = np.arange(0,11)
print(array_indexed[9])
print(array_indexed[1:4])

array_indexed[0:5] = 100
print(array_indexed)
#Changes the first 5 numbers to 100

two_dimen_array = np.array([[5,10,15], [20, 25, 30],[35,40,45],[50,55,60]])
print(two_dimen_array)
print(two_dimen_array[0,0])
print(two_dimen_array[0])
print(two_dimen_array[1,2])


print(two_dimen_array[:2,1:])
# to access the top right of the 2d Array you can use the above. It grabs everything up to row 2 and column 1 onwards
print(two_dimen_array[2:,1:])

conditional_selections = np.arange(1,11)
bool_array = conditional_selections > 5
print(bool_array)
print(conditional_selections[bool_array])
print(conditional_selections[conditional_selections>5])