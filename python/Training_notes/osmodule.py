'''import os
print(os.name)
print(os.getcwd())
try:
    filename="first1.txt"
    text=open(filename,'r')
    print(text.read())
    text.close()
except Exception as e:#os error function, exception handling
    print("Error reading "+ filename)
    print(e)
finally:
    filename = "first.txt"
    text = open(filename, 'r')
    print(text.read())
    text.close()
#os.rename('file_name.txt','first.txt')#changing the name of the file
#text1=os.popen('first.txt','r')#popen is similar to open but output will not print it will open the file
#print(text1.read())
#os.close(text1)'''
'''import os
print(os.getcwd())
#os.mkdir("folder1")
#os.rename('folder1','newfolder')
#os.chdir('newfolder')
#print(os.getcwd())
#os.rmdir('newfolder')
print(os.listdir())'''
'''import os
os.mkdir('sample_folder')
default_path=os.getcwd()
os.chdir('sample_folder')
path=os.getcwd()
print(path)
a=1
for x in range(10):
    text=open('sample_%s.txt'% a,'w')
    a+=1
print(os.listdir())
b=1
for x in range(5):
    text1=open('sample_%s.txt'% b,'w')
    text1.write("Content to be written in sample_%s file"% b)
    b+=2
    text1.close()
a=1
print('File contain data:')
dataless=[]
for x in range(10):
    path = os.getcwd()+'\sample_%s.txt'% a
    size=os.path.getsize(path)
    if size>0:
        print('sample_%s.txt'% a)
    else:
        dataless.append('sample_%s.txt'% a)
    a+=1
print('File without data:')
for x in dataless:
    print(x)
#print(os.getcwd())
a=input()
print(os.path.exists(a))'''
'''import os
import sys
print(sys.argv)
folder=sys.argv[1]
if not os.path.exists(folder):
    os.mkdir(folder)
default_path = os.getcwd()
os.chdir(folder)
path = os.getcwd()
print(path)
a =[1,3,5,6,8]
for x in range(10):
    file_name='sample_%s.txt' % x
    if not os.path.exists(file_name):
        print("File Name:" + file_name)
        if x not in a:
            text = open(file_name, 'w+')
            text.write("Content to be written in sample_%s file" % x)
            text.close()
        else:
            text = open(file_name, 'w+')
            text.close()
print(os.listdir())
print("Completed Generating Data")
os.chdir(default_path)
file_path=os.path.join(default_path,folder)
data_files = [x for x in os.listdir(file_path) if os.path.getsize(os.path.join(file_path,x)) > 0]
no_data_files = [x for x in os.listdir(file_path) if os.path.getsize(os.path.join(file_path,x)) == 0]
print(data_files)
print(no_data_files)'''
import sys
if "C:\\Users\\balaji.a.arunachalam" not in sys.path:
    sys.path.append("C:\\Users\\balaji.a.arunachalam")
print(sys.path)










