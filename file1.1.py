with open('Codingal.txt','w')as file:
    file.write('hi i am penguin and i am  1yr old')
    file.close

    #split file to words
with open('Codingal.txt','r')as file:
    data = file.readlines()
    print('words in the file are...')
    for line in data:
        word = line.split()
        print (word)
file.close()