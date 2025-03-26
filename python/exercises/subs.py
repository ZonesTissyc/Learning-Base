fo = open('rosalind_subs.txt','r')
lines = fo.readlines()
str1 = lines[:-1]
str2 = lines[:-1]
len_1 = len(str1)
len_2 = len(str2)
for i in range(len_1):
    if(len_1-i+1<len_2):
        break
    if(str1[i]==str2[0]):
        if(str1[i:i+len_2]==str2):
            print(i+1,end=" ")
    