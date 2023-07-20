file=open('hello.txt','r+')
file2=open('hello2.txt',"r+")
count=1
for i in file:
    if count%2!=0:
        file2.writelines(i)
    count+=1
data=file2.readlines()
print(data)
