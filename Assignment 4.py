#1. Write a Python program to calculate the length of a string.
s=input("enter a string")
print(len(s))

#2. Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
import operator
s=input("enter a string : ")
d=dict()
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]]=1
    else:
        d[s[i]]=d[s[i]]+1
d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(dict(d))


#3 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.'
#Sample String : 'thisisniceone'
#Expected Result : 'thne”'
#Sample String : 'ab'
#Expected Result : 'abab'
#Sample String : 'f'
#Expected Result : Empty String''
s=input("Enter the input : ")
if len(s)<= 1:
    print("Empty string")
else:
    print(s[:2]+s[(len(s)-2): ])

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'"""""
s=input("Enter a string")
char=s[0]
s=s.replace(char,'$')
print(char+s[1:])

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

s=input().split(',')
print(s[1][:2]+s[0][2:(len(s[0]))] + ' ' + s[0][:2]+s[1][2:(len(s[1]))])

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'

s=input("enter a string : ")
if len(s)<3:
    print(s)
else:
    if s[len(s)-3:]=='ing':
        print(s+'ly')
    else:
        print(s+'ing')

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

def change(s):
    wnot= s.find('not')
    wpoor=s.find('poor')
    if wnot<wpoor and wnot>1 and wpoor>1:
        return  s.replace(s[wnot:wpoor+4],'good')
    return s
s=input()
print(change(s))

#8. Write a Python function that takes a list of words and returns the length of the longest one.
def maximum(s):
    maxi=s[0]
    for i in s:
        if len(i)>len(maxi):
            maxi=i
    return len(maxi)
s=input("enter a string").split( )
print(maximum(s))


#9.Write a Python program to remove the nth index character from a nonempty string.

s=input("Enter a string")
n=int(input("enter the index number"))
for i in range (len(s)):
    if int(i)==n:
        pass
    else:
        print(s[i],end="")


#10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white
value=input().split(',')
li=[]
print(value)
for i in value:
    if i in li:
        pass
    else:
        li.append(i)
print(sorted(li))

#11. Write a Python function to reverses a string if it's length is a multiple of 4

def reverse(str):
    return  str[::-1]
s=input("enter a string :  ")
if len(s)%4==0:
    print(reverse(s))
else:
    print('Length of the string is not multiple of 4')

#12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def check(c,s):
    if c>=2:
        return(s[::-1])
    else:
        return("The given string does not contain at least 2 uppercase character")
s=input("enter a string")
c=0
for i in range(4):
    if s[i].isupper():
        c=c+1
print(check(c, s)

#13. Write a Python program to check whether a string starts with specified characters.
li=['#','@','$','&']
s=input("enter a string : ")
if s[0] not in li:
    print("does not start with the characters present in the list")
else:
    print("Starts with the characters present in list")

#14. Write a Python program to print the following floating numbers upto 2 decimal places.
#3.1415926
s=3.1415926
print(round(s,2))

#15. Write a Python program to count repeated characters in a stringSample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2
import  operator
s=input("enter a string : ")
d=dict()
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]]=1
    else:
        d[s[i]]=d[s[i]]+1
for k,v in sorted(d.items(),key=operator.itemgetter(1),reverse=True):
    if v >1:
        print(k,v)

#16 Write a Python program to print the index of the character in a string.
s=input("enter a string : ")
for i in range(len(s)):
    print("the character" ,s[i] ,"is at position ", i)

#17 Write a Python program to convert a string in a list.
s=input("enter a string : ").split( )
print(s)

#18. Write a Python program to swap comma and dot in a string.
#Sample string: "32.054,23"
#Expected Output: "32,054.23"
s=input("Enter a string")
s=s.replace(',','a')
s=s.replace('.',',')
s=s.replace('a','.')
print(s)

#19. Write a Python program to find smallest and largest word in a given string.
s=list(input().split( ))
maximum=len(s[0])
for i in s:
    if len(i)>maximum:
        maximum=len(i)
minimum=len(s[0])
for i in s:
    if len(i)<minimum:
        minimum=len(i)
for i in s:
    if len(i)==maximum:
        print("the largest word is",i)
    elif len(i)==minimum:
        print("The swallest word is",i)

#20. Write a Python program to remove all consecutive duplicates of a given string.
def duplicate(s):
    if len(s)==1:
        return s
    elif s[0]==s[1]:
        return duplicate(s[1:])
    else:
        return s[0]+duplicate(s[1:])
s=input("enter a string")
print(duplicate(s))




