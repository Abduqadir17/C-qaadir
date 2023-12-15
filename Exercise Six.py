#QUESTION 6-1
def b(z):
    prod= a(z,z)
    print(z, prod)
    return prod
def a(x,y):
    x=x+1
    return x*y
def c(x,y,z):
    total = x+y+z
    square = b(total)**2
    return square
x=1
y=x+1
print(c(x,y+3,x+y))

#QUESTION 6-2
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
result=ackermann(3,4)  
print(result)  

#QUESTION 6-3
def is_palindrome(s):
    return  s==s[::-1]
print(is_palindrome("ilatali"))    

#QUESTION 6-4
def is_power(a, b):
    if a/b:
        return True
    else:
        return False
result =is_power(9,3)   
print(result)

#QUESTION 6-5
def gcd(a, b):
    while b:
        a, b = b%a, a % b
    return a

result = gcd(48, 20)
print(result) 

