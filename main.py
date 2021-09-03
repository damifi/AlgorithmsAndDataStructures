
#Comprehenstion
#Syntax: newlist = [expression for item in iterable if condition == True]

#list containing car names
cars = ["Honda", "VW", "Polo", "Mercedes", "Toyota", "Porsche", "Dacia"]

#new list with car names with more than 5 characters
 
newListA = [item for item in cars if len(item) >= 5]
print(newListA)


#*args and **kwargs: variable parameter amount
#1) *args is used to pass a variable number of non keyword arguments(including zero arguments)

#function to multiply a variable amount of numbers
def myMult(*args): 
    result = 1
    for i in args: 
        result = result * i
    return result

print("First call of myMult: " + str(myMult(2,2)))
print("Second call of myMult: " + str(myMult(2,2,5,10)))

#2) **kwargs 

#lambda functions
#syntax: lambda arguments : expression

#lambda function to multiply values:
lFuncA = lambda a, b : a*b
print(lFuncA(5,10))

# dunder methods
# __init__ , __str__ , __len__ etc are dunder methods to override starndart function of python (overload function)

# concurrency
#asyncio and Threading run on a single core. multiprocessing runs on different cores.
#Threading can be interupted by the operating system at any time, even in a statement as x= x+1
#In asyncio the tasks must cooperate by announcing when they can be paused

#important keyword: with
# with is used when working with unmanaged resources like file streams, making it so the resource is cleaned up after the code is finished with it




#for I/O bound slowness: try asyncio first, then threading
#for CPU-bound slowness: try mutliprocessing

