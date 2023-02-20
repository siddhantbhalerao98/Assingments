
# Python program to print a dictionary whose keys should be the alphabet from a-z and the value corresponding ASCII values

A=dict()
for i in range (97,123,1):
    A.setdefault(chr(i),ord(chr(i)))
    
print(A)    