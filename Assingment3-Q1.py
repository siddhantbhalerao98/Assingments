#  Python function to sum all the numbers in a list.
 
 
def Sum_fn(List1):
    sum=0
    for i in List1:
        sum = sum+i
    return sum    

List1=[8, 2, 3, 0, 7]

print('output:-',Sum_fn(List1))