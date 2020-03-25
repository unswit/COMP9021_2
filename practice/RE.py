import re
# get the first word
xx = "ggx is very intresting"
r1= re.findall(r"^\w+",xx)
print(r1)
# get the first charactor
xx = "gag,sdfaf,gagfsf"
r2 = re.findall(r"^\w",xx)
print(r2)

# split sentence into each words
print((re.split(r'\s','We are splitting the words')))

# remove 's' in a sentence
print((re.split(r's',"We are splitting words")))

# find the words start with 'g'
list = ["grudfaf aet","guru99 give","guru Selenium"]
for i in list:
    z=re.match("(g\w+)\W(a\w+)",i)
    if z:
     print(z.groups())

patterns =['software testing','guru99']
text = 'software testing is fun?'

for pattern in patterns:
    print('Looking for "%s" in "%s" - >' % (pattern,text), end=' ' )
    if re.search(pattern, text):
        print('found a match')
    else:
        print('no match')
abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.,com'
emails = re.findall(r'[\w\.-]')

