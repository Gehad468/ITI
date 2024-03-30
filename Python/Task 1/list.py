num=int(input("Please enter number"))
tbls=[]
for i in range(1,num+1):
    tbl=[]
    for j in range(1,i+1):
        tbl.append(j*i);
    tbls.append(tbl)

print(tbls)
