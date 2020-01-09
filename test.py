a = "ราคาต่อหน่วยเหล็กเสริม db 20"

print(a)
stopword = []
def add_stop_word(self,*args):
        #คำที่ไม่มีความหมาย (ขึ้นอยู่กับ spread sheet ของแต่ละคน)
        for x in args:
            stopword.append(x)

add_stop_word("จำนวน","ปริมาณ","ราคา","หน่วย","อยากทราบ","หน่อย","ถาม")
print(stopword)

for word in stopword:
    a = a.replace(word,"")

print(a)