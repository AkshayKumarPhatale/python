text="('$CMB','$MAO','$XYZ','$ABC')"
index=0
flag=False
endposition=0
startposition=0
l=[]
for element in range(0,len(text)):
    if text[element]=="$":
        flag=True
        startposition=element
    elif flag:
        if text[element] ==";" or text[element]=="\'" or text[element]=="." or text[element]==")":
            endposition=element
            l.append(text[startposition+1:endposition])
            flag=False

for item in l:
    print(item)