# Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


def last(i):
    return i[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)
  
a= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("Sorted List:",sort(a))