"""
Regex Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. = any character, except for a newline
\b the whitespace around words
\. a period

Regex Modifiers:
{1,3} we're expecting 1-3
{1,} we're expecting 1 or more
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ Matching the beginning of a string
| Either or \d{1-3} | \w{1-3}
[] range or "variance" [1-5a-qA-Z]
{x} expecting "x" amount

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form fee
\r return

Don't forget:

. + * ? [ ] $ ^ ( ) { } | \


"""

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString)
# finds all 1 to 3 number digits in exampleString
names = re.findall(r'[A-Z][a-z]*', exampleString)
# finds all uppercase letters followed by lowercase and stops when reaching whitespace
print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)
