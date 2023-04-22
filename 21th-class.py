from array import *
arr = array('i',[10,20,30])
print(type(arr))

#append
list=[1,2,3,4,5]
list.append(6)
print(list)

#clear
list.clear()
print(list)

#.copy
x=list.copy()
print(x)

#count
list1=[1,2,3,4,5,'g','d']
print(list1)
print(list1.count('g'))
print(list1.count('2'))

#pop
print(list1.pop())
list1.pop()
print(list1)

#reverse
list1.reverse()
print(list1)

#soerting list in reverse order
list2=[5,2,1,8,9,4]
print(list2)
list2.sort(reverse=True)
print(list2)

#remove
list3=[1,3,2,4,2,5,6]
list3.remove(2)
print(list3)
#list3.sort(reverse=True)
#print(list3)

#insert
list4=[1,2,3,4,5]
list4.insert(5,6)
print(list4)

#extend
list4.extend("a")
print(list4)


#exceptions
#zero division error
#print(1/0)

#arr=[1,2,3]
#print(arr[5])#IndexError

try:
    x=23/0
    print(x)
except:
    print("exception occured")#exception occured

try:
    x=23/10
    print(x)
except:
    print("exception occured")#2.3

try:
    print(1/0)
except IndexError:
    print("index error occured")
except RuntimeError:
    print("run time error occured")
except ZeroDivisionError:
    print("zero division error occured")


try:
    print(1/10)
except IndexError:
    print("index error occured")
except RuntimeError:
    print("run time error occured")
except ImportError:
    print("import error")
else:
    print("control is inside else")#executed after try if there is no exception in try

try:
    print(1/0)
except ZeroDivisionError as err:
    print(err)#division by zero
finally:
    print("finally will always get executed")

#raise an exception intentionally
arr=[1,2,3,4,5]
try:
    if len(arr)>=4:
        raise ValueError("length of the array greater or equal to 4")
    else:
        print("everything is fine")
except ValueError as err:
    print(err)

#how to define a custom exception
class CustomException(Exception):
    "This is a custom exception"
    pass
  
  
try:
    x=20
    if(x==20):
        raise CustomException
    else:
        print("x is not 20")
except CustomException as err:
    print("exception occured")





