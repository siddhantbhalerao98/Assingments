#Python program to reverse a string.


def ReverseString(A):
    reverse=A[::-1]
    return reverse
A=input('Enter the string-')

print('Reversed String=',ReverseString(A))