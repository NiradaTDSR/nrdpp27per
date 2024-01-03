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
    
    
# a = [['a', 'b', 'c', 'd', 'e'], ...]: กำหนดตัวแปร a เป็น array 2 มิติ 5x5 ที่มีอักษรต่างๆเรียงตัวเป็นตาราง 5x5.

# result = None: กำหนดตัวแปร result เป็น None ในตอนแรก.

# counter = 0: กำหนดตัวแปร counter เป็น 0 ในตอนแรก.

# amount = len(txt): หาความยาวของข้อความ txt และกำหนดให้ amount เป็นค่านี้.

# for k in range(amount):: วนลูปตามจำนวนตัวอักษรใน txt.

# around = " ": กำหนด around เป็นช่องว่าง.

# given = txt[k]: นำตัวอักษรที่ k ใน txt มาเก็บไว้ในตัวแปร given.

# nxt = txt[k+1] if k + 1 < amount else txt[k - 1]: นำตัวอักษรถัดไป (ถ้ามี) มาเก็บไว้ในตัวแปร nxt หรือนำตัวอักษรก่อนหน้า (ถ้าไม่มี) ถ้า k + 1 น้อยกว่า amount.

# for i1 in range(len(a)): ...: วนลูปเพื่อหาตำแหน่ง (row, col) ของตัวอักษรที่กำลังพิจารณาใน a.

# for i in range(len(a)): ...: วนลูปเพื่อสร้างรายการ around ที่ประกอบไปด้วยตัวอักษรที่อยู่รอบๆ ตัวอักษรที่กำลังพิจารณา.

# if nxt in around: counter += 1: ถ้าตัวอักษรถัดไปอยู่ใน around ให้เพิ่มค่าของ counter 1.

# result = counter == amount: กำหนดค่า result ว่าจะได้ True หาก counter เท่ากับ amount, มิฉะนั้นค่า result จะเป็น False.

# if result: print("True",end=" ") else: print("False",end=" "): พิมพ์ "True" หรือ "False" และกำหนดให้จบด้วยช่องว่าง 7 ตัว.

# for h in range(8): Check(data[h]): วนลูปเรียกใช้ฟังก์ชัน Check สำหรับทุกข้อความในลิสต์ data ทั้ง 8 รายการ.
                               
    