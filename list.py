####Lists -> Ordered sequence of values ex - odd = [1,3,5]
##List can also contain mix of different kinds of variables
##List elemests can be accessed using square brackets. Indexing starts from 0.
##Lists are mutable(means we can change elemets of list after they have been created)(Lists are "mutable", meaning they can be modified "in place".)
##list[0]->1st elemet
##list[-1]-> last element.
##First 3 elements list[0:3] or list[:3]
##elemts from 3rd to last list[2:](start from index 2 till the end)
##negative indexing means starting from last element. -1->last, -2->second last

##A function attached to an object is called a method.

##List methods

sample = [1,2,3,4,5]
print("sample before append",sample)

##list.append(value) will add the object at the end

sample.append(6)

print("sample after append-")
sample

###list.pop removes and returns the last element of a list:
sample.pop()

###We can get its index using the list.index method.

sample.index(3)

###inn operator can be used to check if a element exists inside the list


