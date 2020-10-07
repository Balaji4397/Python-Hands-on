import random as r
r.seed(20)
print(r.random())
print(r.randrange(3,9))
print(r.randint(3,9))
a=[1,2,3,4,5]
r.shuffle(a)
print(a)
print(r.uniform(2,6))
import requests
#a=requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
#print(a.text)
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {"a": 'b'}
x = requests.post(url, data = myobj)
#print the response text (the content of the requested file):
print(x.text)


