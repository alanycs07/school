

fruits = ('apple', 'banana', 'cherry', 'date')  # creating a tuple named fruits


numbers = (1, 2, 3, 4, 5)   # creating a tuple named numbers


empty = ()  # creating an empty tuple



# Printing the first and last elements of the fruits tuple
print(fruits[0])  
print(fruits[3])  

# Printing the second and fourth elements of the numbers tuple
print(numbers[1])  
print(numbers[3])  

# using negative indexing to print the last element of the fruits tuple
print(fruits[-1])  


# concatenating fruits and numbers tuples
concatenated_tuple = fruits + numbers
print(concatenated_tuple) 

# repeating the numbers tuple three times
repeated_tuple = numbers * 3
print(repeated_tuple)  



# creating a tuple named colors
colors = ('red', 'blue', 'green', 'blue', 'yellow')

# how many times blue is counted
print(colors.count('blue'))  

# index of green
print(colors.index('green')) 



# trying to change the first element (this will raise an error)
# fruits[0] = 'avocado'   UNCOMMENT THIS TO RUN IT 



def get_student_info():
    #returns a tuple containing a student's name, age, and grade.
    name = "Alan"
    age = 17
    grade = "D"
    return (name, age, grade)

# calling the function and printing the returned tuple
print(get_student_info())  



# creating a nested tuple
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'))

# Accessing and printing the second element of the first tuple
print(nested_tuple[0][1])  

# Accessing and printing the third element of the second tuple
print(nested_tuple[1][2])  