# Find() Method
#The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
article = 'abbcddddeec'

orderOfA = article.find('a')
orderOfD = article.find('d')
print(orderOfA, orderOfD)

def checkWhetherC(object):
    for character in object:    # Each time Check single character in the article.
        if character.find('c') >= 0:
            print("C occur!")

checkWhetherC(article)



# Search() Method & Regular Expression
# re.search() return an address, and it also could be used as boolean!
import re

article = 'I love you!'
print(re.search('v', article))

def searchParticularO():
    for character in article:
        if re.search('o', character):
            print('Find!')
        else:
            print('-')

searchParticularO()

phrase = ['Regular: expression', 'Regular activity', 'Rectangular exposure', 'Resolute: abbreviation', 'Rudex']
def checkparticularWord(word):
    for i in range(0, len(phrase)):
        if re.search(word, phrase[i]):
            print("Discover", word, "in phrase no.", str(i+1))
    print("\n")

checkparticularWord('Reg')
checkparticularWord('exp')
checkparticularWord('a*.i')     # * means any word (zero times is okay) in regular expression.
checkparticularWord('R*.:')     # . means the word for any time in regular expression.
checkparticularWord('R\S+x')    # In regular expression, \S means no white space character, and + means one or more times.



# Regular Expression & Greedy Matching
# re.findall() could be used to extract the words!
import re

article = 'IPod was created in 1995, while iPhones were discovered in 2005!'
resultOfYear = re.findall('[0-9]+', article)    # [] means a limit interval
resultOfProduct = re.findall('[iI]P\S+', article)
print(resultOfYear)
print(resultOfProduct)

resultOfGreedy = re.findall('[iI].+n\s', article)   # In regular expression, \s means white space character.
resultOfNonGreedy = re.findall('was.+?in', article)     # Add ? before the end word to prevent the problem of greedy matching.
print(resultOfGreedy)
print(resultOfNonGreedy)
print('\n')

mail = 'If you have some question regarding to Avenger:End Game, please send your mail to abc@google.com. Hoped to see you at 9:10 tomorrow.'
mailBox = re.findall('\S+@\S+', mail)
timePoint = re.findall('at (\S+:\S+)', mail)    # () determine the interval of the data we want to extract.
print(mailBox)
print(timePoint)
print('\n')

#split the text with split() method.
seperated = mail.split()    # split() method could be used to split the text with the word inside the ().
print(seperated)
frontName = seperated[14].split('@')
print(frontName[0] + '@yahoo.com')
frontName = re.findall('(\S+)@', mail)
print(frontName[0] + '@yahoo.com')
print('\n')

# escape the character
comment = 'The data are 0.875, 0.625, 0.5, and 0.375. The rest of the data cost $ 10.05, but you...'
figures = re.findall('[0-9.]+', comment)
print(figures)
price = re.findall('\$ [0-9.]+', comment)   # $ represent other meanings in regular expression, we could add \ so that this $ means the real dollar sign.
print(price)

# Regular expression is harder for human to understand, remember to add some comment beside the code.
# Some important characters of regular expression: https://www.py4e.com/lectures/Py4Inf-11-Regex-Guide.pdf
