# ------
# part A
# ------
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

# -------
# part B
# -------
# still working with s
# enumerate the instances of 'bob' in the string s

s = str(input('Enter a string: '))
# initialize empty vectors
numBobs = 0
bobTest = str('')
# loop thru 1 to length s, if b is found, ask if it is beginning of 'bob', if so +1
for i in range(0,len(s)-1):
    if s[i] == 'b':
        bobTest = s[i:(i+3)]
    else:
        bobTest = ''
    if bobTest == 'bob':
        numBobs = numBobs + 1
# print result
print('Number of times bob occurs is:', numBobs)

# -------
# part C
# -------
s = str(input('Enter string: '))
longestString = ''
breaks = []
subStrings = []
subBreaks = []
starts =[0]
stops = []

# ask what the index points of the letters that are NOT in alpha order
for i in range(0, len(s)-1):
    if s[i] > s[(i+1)]:
        breaks.append(i)
    # if none then the whole string is longest, there are no substrings
    else:
        longestString = s
# now we create two lists: one for the beginning and the other for the end of each substring
for i in breaks:
    starts.append(i + 1)
    stops.append(i + 1)
stops.append(len(s))

# now we create a list of the substrings
for i in range(0,len(starts)):
    subStrings.append(s[(starts[i]):(stops[i])])
# sort that list by the item's lengths
subStrings.sort(key = len)

# loop to ask if each object in substring list is shorter than the one to the right
# again, subsetting by the breaks in the length values
for i in range(0,len(subStrings)-1):
    if len(subStrings[i]) < len(subStrings[(i+1)]):
        subBreaks.append(i)
# if there are no breaks, substring list is only one item, the longest string
if len(subBreaks) == 0:
    longestString = subStrings[0]
# if not, we want the string to the left of the block with the longest length
else:
    longestString = subStrings[(int(subBreaks[-1] + 1))]
# and finally, our print output
print('Longest substring in alphabetical order is: ', longestString)
