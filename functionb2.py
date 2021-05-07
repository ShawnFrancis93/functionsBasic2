#1
def  countDown(num):
    tempList = [] #create a list
    for i in range(num, -1, -1): #using num
        tempList.append(i) #append i into the new list
    return tempList #return the list and end function
print(countDown(5))

#2
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([100,64]))

#3
def first_plus_length(list):
    return len(list) + list[0]
print(first_plus_length([20,2,3,7,8]))

#4
def values_greater_than_second(list):
    if len(list)<2: #if list provided is has more than 2 objects
        return False #function should return false if there aren't enough letters
    secList = []# should be greater than = list[1]
    for i in list:
        if i>list[1]: #if the value is greater than the value in list position 1
            secList.append(i) #push into new list
    print(len(secList)) #the length of second list 
    return secList #return the list, end function
print(values_greater_than_second([8,5,3,3,10,50,6,4])) #should print 4
print(values_greater_than_second([0,4,3,2,4,1])) # no number is greater than 4
print(values_greater_than_second([9])) #return false
print(values_greater_than_second([0])) #return false

#5
def length_and_value(size,value): #function has two parameters 
    valueList = [] #a list is created
    for i in range(size): #Create a for loop using size as the first argument, should go up to whatever number.
        valueList.append(value) #push a given argument (as the value,) into the new list
    return valueList #return the list
print(length_and_value(7,100))
print(length_and_value(10,8))