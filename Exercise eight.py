#QUESTION 8-2
fruit="banana"
print(fruit.count("a"))

#QUESTION 8-3
def is_palindrome(word):
    return word[::-1]
print(is_palindrome("reer"))

#QUESTION 8-4
def any_lowercase1(s):
 for c in s:
  if c.islower():
   return True
 else:
   return False
def any_lowercase2(s):
 for c in s:
   
  if 'c'.islower():
   return 'True'
 else:
  return 'False'
def any_lowercase3(s):
 for c in s:
  flag = c.islower()
  return flag
def any_lowercase4(s):
 flag = False
 for c in s:
  flag = flag or c.islower()
  return flag
def any_lowercase5(s):
 for c in s:
  if not c.islower():
   return False
 return True

print(any_lowercase1("samawade"))
print(any_lowercase2("nabsiile"))
print(any_lowercase3("DABANGAALE"))
print(any_lowercase4("iskukaris"))
print(any_lowercase5("KAARJEBIS"))

#QUESTION 8-5
def rotating_word(string1 , string2):
 dif1 = ord(string1[0:1])-ord(string2[0:1])
 dif2 = ord(string1[1:2])-ord(string2[1:2])
 dif3 = ord(string1[2:3])-ord(string2[2:3])
 dif4 = ord(string1[3:4])-ord(string2[3:4])
 dif5 = ord(string1[4:5])-ord(string2[4:5])
 if dif1 or dif2 or dif3 or dif4 or dif5 is True:
  print(string2)
print(rotating_word('nerbo', 'nervo'))  