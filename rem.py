
start=0;
end=0;
count=0;
pattern1="^/\*.*\*$"
pattern2="^\*.*\*\/$"
l=[]
import re
with open(r"C:\Users\home\Desktop\py\log.txt", "wt") as fout:
    with open(r"C:\Users\home\Desktop\py\abc.txt", "rt") as fin:
        for line in fin:
            l.append(line)
            count=count+1
            if re.search(pattern1,line):
                start = count


            elif re.search(pattern2,line):
                print(end)
                end = count

        del l[start-1:end]

        for e in l:
            fout.write(e)






