file1=open("fil1.txt","r")
file2=open("fil2.txt","w")
data=file1.readlines()
count=0
for i in data:
    count+=1
    if(count%2!=0):
       file2.write(i)
        
