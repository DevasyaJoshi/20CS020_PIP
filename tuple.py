#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#20CS020 Devasya Joshi
print('Prepard by 20CS020 Devasya Joshi')

#Tuple
    #a. Write a Python program to create a tuple with different data types.
my_tuple = (1, 5.5, "20CS009")
print(my_tuple)

    #b. Write a Python program to create a tuple with numbers and print one item.
tuple1 = (1123, 45.65, 200)
a, b, c = tuple1
print(a)

    #c. Write a Python program to add an item in a tuple.
Tuple = (1, 3, 5, 7)
#Tuples are immutable, so by + operator we create a new tuple with an additional element
Tuple = Tuple + (9,)
print(Tuple)

    #d. Write a Python program to convert a tuple to a string.
my_tuple = ('p', 'y', 't', 'h', 'o', 'n')
s = ''.join(my_tuple)
print(s)

    #e. Write a Python program to find the length of a tuple.
tuple2 = ('p', 'y', 't', 'h', 'o', 'n')
print(len(tuple2))

