
dl=[]
l=[]
flag=False
with open(r"C:\Users\home\Desktop\py\CLINCAL_TRIMED_APID9617_MERGE.sh", "rt") as fin:
    for line in fin:
        dl.append(line)
for text in dl:
    for element in range(0, len(text)):
        if text[element] == "$":
            flag = True
            startposition = element
        elif flag:
            if text[element] == ";" or text[element] == "\'" or text[element] == "." or text[element] == ")":
                endposition = element
                l.append(text[startposition + 1:endposition])
                flag = False
for item in l:
    print(item)

