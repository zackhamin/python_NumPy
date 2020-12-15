
import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
arrTwo = np.array(my_mat)

arrange = np.arange(0,20,2)
#// the last number is how much you want to count up by.



countingNumbers = np.linspace(0,50,10)
# works from the first number to the second with jumps of the last.


print(my_list)
print(arr)
print(my_mat)
print(arrTwo)
print(arrange)
print(countingNumbers)
