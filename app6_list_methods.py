# List Methods

list1 = [1, 2, 3, 4, 5]
list2 = ['bananas', 'apples', 'oranges']


list3 = list1.copy() # Creates a copy of the list given.
# appends an item to a list, even if you append a list the whole list will be considered in one index.
list3.append(list2)

print(list3)

list1.extend(list2) # adds individual objects at the end of the list.

print(list1)

list4 = ['bananas', 'apples', 'oranges']
list4.insert(2, 'cherry') # Helps us insert at a particular position.
print(list4)

list4.remove('cherry')
# list4.clear() -> empty the list.

a = list4.index('apples')
b = list4.count('mango') # Tells how many times an objects is in the list.
print(a, b)


list5 = [3, 2, 4, 5, 1]

list5.sort()
print(list5)

list5.reverse()
list5.pop() # removes any index if you put it, otherwise last index.