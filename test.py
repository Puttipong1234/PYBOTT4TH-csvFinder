import re
string = "↵                        ไทยๆtryit1.tar↵ ####///๑๑                       "
text = re.sub('[^\w.]', '', string)
print(type(text)) 
