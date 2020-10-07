file=open('sample.txt','w')#creating new file with write command
file.write("Hi everyone, How are you ")
file.write("I am a cricket player ")
file.close()#it will close the writing operation in the file
file1=open('sample.txt','r')#reading the created file
print (file1.read())
#print (file1.read(5))#to print the first 5 character
file2=open('sample.txt','a')#appending new strings to the file
file2.write("I am a opening batsman")
file2.close()
with open('sample.txt') as f:
    print(f.read())
#with open('sample.txt','w') as f:
#    f.write(" I have played state level tournaments")
with open('sample.txt') as f:
    data=f.readlines()
    print(data)
    for x in data:
        word=x.split()
        print(word)
with open('first.txt',) as t:
    print(t.read())
with open('first.txt','w') as t:
    t.write("Hi,Hello ")
with open('first.txt','a') as t:
    t.write("Bye Bye")