"""
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE
    to match.
()  Enclose a group of REs
\d  Matches any decimal digit; equivalent to the set [0-9].
\D  The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
\s  Matches any whitespace character; equivalent to [ \t\n\r\f\v].
\S  The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
\w  Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
\W  Matches the complement of \w.
\b  Matches the empty string, but only at the start or end of a word.
\B  Matches the empty string, but not at the start or end of a word.
\\  Matches a literal backslash.
"""
import re
print(dir(re))
txt = "The rain in Spain heavelly"
x = re.search("^The.*Spain", txt)
print(x)
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x=re.split('\s',txt,1)
print(x)
x=re.match("\w",txt)
print(x)
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
print(match)
match = re.search(r'[\w.-]+@[\w.]+', str)
print(match)
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w.$]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
#for email in emails:    # do something with each found email string
print(emails)
a=re.sub(r'([\w]+)@([\w]+)', r'\1@yahoo', str)
print(a)
