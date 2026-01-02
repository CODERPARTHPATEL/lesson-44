#creaat new file
new_file = open('new file.txt','w')

#check if file exists
import os
print('check if my fil exists or not....')
if os.path.exists('my_file.txt'):
    os.remove("my_file.txt")
else:
    print('the file does not exist')
#creat new if it don't
my_file = open('my_file.txt','w')
my_file.write('hi i am penguin and i am 1yr old')
my_file.close()
#delete file named codingal
os.remove('Codingal (1).txt')

#delete folder
os.rmdir('Folder')