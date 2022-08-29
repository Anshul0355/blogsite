#List Comprehension:

lst=[i for i in range(10)]
print(lst)

#Using List Comprehension
l2=[i*i for i in range(1,11)]
print (l2) #Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Using for loop
l1=[]
for i in range(1,11):
    a=i*i
    l1.append(a)
print (l1)     #Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#List comprehension vs filter.
lst1=filter(lambda x: x%2==0 , range(10))
print(lst1)

#Using map() function
l1=map(lambda x:x*x,range(1,11))
#Returns an iterator(map object)
print (l1)#Output:<map object at 0x00C0EC10>
print (list(l1))#Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#  Nested loops in List Comprehension.
# List comprehension can contain one or more for clause.


l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[num2 for num1 in l1 for num2 in num1]
print (l2) #Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]


# Multiple if condition in List Comprehension.
# List comprehension can contain zero or more if clause.

l1=[1,2,3,4,5,6,7,8,9,10,11,12]
l2=[n for n in l1 if n%2==0 if n%3==0]
print (l2)#Output:[6, 12]