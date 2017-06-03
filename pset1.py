# part A
# assume s is a set of lower-string characters
# write program that enumerates vowels in the string 's'

s = str(input('Enter a string: '))
# initialize list of vowels and empty vectors
vowels = ['a','e','i','o','u']
numVowels = 0
# loop thru char's asking if each is in vowels, if so + 1
for char in s:
    if char in vowels != False:
        numVowels = numVowels + 1
# print result
print('Number of Vowels:', numVowels)


# part B
# still working with s
# enumerate the instances of 'bob' in the string s

s = str(input('Enter a string: '))
# initialize empty vectors
numBobs = 0
bobTest = str('')
# loop thru 1 to length s, if b is found, ask if it is beginning of 'bob', if so +1
for i in range(0,len(s)):
    if s[i] == 'b':
        bobTest = s[i:(i+3)]
    else:
        bobTest = ''
    if bobTest == 'bob':
        numBobs = numBobs + 1
# print result
print('Number of times bob occurs is:', numBobs)

# part C
# first set up nest list matching letter with index
L = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0,26,1):
    L.append([alphabet[i],(i+1)])
# now index over numbers and if greater than print letter and add to empty string
# which we'll save until end and then print that
print(L)
