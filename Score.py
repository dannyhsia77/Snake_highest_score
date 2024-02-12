score = 0
score =score + 6
time = 1

posi =[6]
tool36 =[]
lenth =[6]

for m in range(3):
    tool36.clear()
    for j in range(6**time):
        if j%2 == 0:
            tool36.append(3)
        else:
            tool36.append(6)
    

    for n in range(6**(time-1)):
        for i in range(6):
            posi.append(posi[n]+3*(i+1))
    for o in range(6**(time-1)):
        del posi[o]
    


    for k in range(6**time):
        posi.append(posi[k]+tool36[k])
    

    for l in range(6**time):
        del posi[l]
    

    
    print('----------------')

    
    for p in range(6**(time-1)):
        for q in range(6):
            lenth.append(tool36[q]+lenth[p])
    for r in range(6**(time-1)):
        del lenth[0]
        
    print(lenth)

    for s in range(len(lenth)):
        if lenth[s] < 189:
            pass
        else:
            pass
            
    


    time = time + 1
