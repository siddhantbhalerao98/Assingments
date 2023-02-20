# Python function that accepts a string and calculate the number of upper case letters and lower case letters


def Count(A):
     
        count_upper=0
        count_lower=0
        
        for i in A:
            if i.isupper():
                count_upper+=1
            elif i.islower():
                count_lower+=1
            else:
                pass
        return (count_upper, count_lower)    
        
A=input("Enter the String:-")


print('The no. of uppercase characters and lower case characters in given string are',Count(A),'respectively.') 


    