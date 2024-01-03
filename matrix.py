def Check (txt):
    a = [['a', 'b', 'c', 'd', 'e'],
         ['l', 'm', 'n', 'o', 'f'],
         ['k', 'p', 'q', 'r', 'g'],
         ['j', 's', 't', 'u', 'h'],
         ['i', 'v', 'w', 'x', 'y']]
    
    result = None
    counter = 0
    amount =len(txt)
    
    for k in range (amount) :
        around = " " 
        
        given = txt[k]
        nxt = txt[k+1] if k + 1 < amount else txt[k - 1]
        
        for i1 in range(len(a)):
            for p in range(len(a[0])):
                if a[i1][p] == given:
                    row, col = i1, p
        
        for i in range(len(a)):
            for p in range(len(a[0])):
                if(i,p) == (row,col):
                    pass
                elif (i,p) in [(row - 1, col - 1), (row - 1,col),(row - 1,col + 1),
                               (row, col - 1), (row, col + 1),
                            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]:
                    around+=a[i][p]
                else:
                    pass
                    
        if nxt in around:
            counter += 1         
                      
    result = counter == amount     
    
    if result:
        print("True",end="       ")
    else:
        print("False",end="       ")   
        
data = ["pqruxw", "kpuxy", "abcdefgrq", "mnorhy", "abmnptrod", "lmrqtw", "abcdefghyxurqpsvi", "tplmno"]
print(data)
for h in range(8):
    Check(data[h])
                               
    