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
