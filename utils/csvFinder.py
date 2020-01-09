import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import operator


class csvFinder():
    def __init__(self , csvPath ):
        self.csvPath = csvPath 
        self.csvdata = self.read_data()
        self.blank = "-"
    
    def set_blank_char(self,char):
        #กรณีต้องการเปลี่ยน "ไม่ระบุ"
        self.blank = char
        
    
    
    def find_row(self,val,limit=3):
        
        
        found_data = []
        num_found = 0
        
        default_scoring = 95

        while not found_data:
            num = 0
            for each_dict in self.csvdata:
                
                # if num_found > 0:
                #     break
                
                for key,value in each_dict.items():
                    
                    if val.strip() == value.strip():
                        print("found data at key:" + str(key) )
                        print("found data at row:" + str(num+2) )
                        data = {"row" : num , "true_row" : num+2 , "col_name" : key , "search_type" : "pure" , "score" :1000 }
                        found_data.append(data)
                        num_found += 1
                        # break
                    
                    else :

                        match = self.match_value(val.strip(),value.strip(),score=default_scoring)
                        if match :
                            print("found data at key:" + str(key) )
                            print("found data at row:" + str(num+2) )
                            data = {"row" : num , "true_row" : num+2 , "col_name" : key , "search_type" : match[1] , "score" :match[2] }
                            found_data.append(data)
                            # num_found += 1
                        
                num += 1

            if found_data:

                for i in found_data:
                    index = i["row"]

                    clean_data = {}

                    for key,val in self.csvdata[index].items():
                        if val.strip() == "":
                            continue
                        
                        elif val.strip() == self.blank:
                            clean_data[key] = "ไม่ได้ระบุไว้"

                        else :
                            clean_data[key] = val.strip()

                    i["result"] = clean_data

                found_data.sort(key=operator.itemgetter('score'), reverse=True)
                return found_data[0:limit]

            else :
                default_scoring -= 5
                continue
    
    
    def find_value(self,val,col_to_find,limit=3):
        
        cols = [i for i in self.csvdata[0].keys()]  
        score = process.extractOne(col_to_find,cols)
        col_to_find = score[0]
        
        found_data = []
        num_found = 0
        
        default_scoring = 95

        while not found_data:
            num = 0
            for each_dict in self.csvdata:
                
                if num_found > 0:
                    break
                
                for key,value in each_dict.items():
                    
                    if val.strip() == value.strip():
                        print("found data at key:" + str(key) )
                        print("found data at row:" + str(num+2) )
                        data = {"row" : num , "true_row" : num+2 , "col_name" : key , "col_to_find" : col_to_find , "search_type" : "pure" , "score" :1000 }
                        found_data.append(data)
                        num_found += 1
                        break
                    
                    elif val.strip() in value.strip() and len(val.strip()) >= 5:
                        print("found data at key:" + str(key) )
                        print("found data at row:" + str(num+2) )
                        data = {"row" : num , "true_row" : num+2 , "col_name" : key , "col_to_find" : col_to_find , "search_type" : "partial" , "score" :120 }
                        found_data.append(data)
                    
                    else :

                        match = self.match_value(val.strip(),value.strip(),score=default_scoring)
                        if match :
                            print("found data at key:" + str(key) )
                            print("found data at row:" + str(num+2) )
                            data = {"row" : num , "true_row" : num+2 , "col_name" : key , "col_to_find" : col_to_find , "search_type" : match[1] , "score" :match[2] }
                            found_data.append(data)
                            # num_found += 1
                        
                num += 1

            if found_data:

                for i in found_data:
                    index = i["row"]
                    i["result"] = self.csvdata[index][col_to_find]
                    if i["result"].strip() == "":
                        i["result"] = "ไม่ระบุ"

                found_data.sort(key=operator.itemgetter('score'), reverse=True)
                return found_data[0:limit]

            else :
                default_scoring -= 5
                continue
    
    
    
    
    def read_data(self):
        with open(self.csvPath,encoding = "utf-8") as file:
            csvdata = csv.DictReader(file, delimiter=',')
            csvdata = [i for i in csvdata]
            file.close()
            return csvdata

    
    def match_value(self,val,val_to_match,score):
        
        if fuzz.ratio(val,val_to_match) >= score :
            res = [True , "fuzz_ratio" ,fuzz.ratio(val,val_to_match)]
            return res
        elif fuzz.partial_ratio(val,val_to_match) >= score :
            res = [True , "fuzz_partial_ratio" ,fuzz.partial_ratio(val,val_to_match)-70]
            return res
        # elif fuzz.token_sort_ratio(val,val_to_match) >= 90 :
        #     res = [True , "fuzz_token_sort_ratio" ,fuzz.token_sort_ratio(val,val_to_match)]
        #     return res
        return False
    


# if __name__ == '__main__':
    
    # CSV = csvFinder(csvPath="test_csv02.csv")
    
    # ค้นหา ข้อมูล ของคำที่ใส่เข้าไป
    # res = CSV.find_row(val="ครอบสันโค้ง" , limit=5)
        
    # a = res2[0]["result"] #findrow
    # print(a)
    
    # ค้นหา คำนี้ ที่ คอลัมน์ อื่น 
    # ค้นหา รายการนี้ .. มีค่าแรงเท่าไหร่
    # res2 = CSV.find_value(val="เค้าบอกให้มาถาม รวมค่างานกลุ่มที่ 2 อ่าครับ", col_to_find="ค่าวัสดุจำนวนเงิน" , limit=50)
    # print(res)
    # for i in res2:
    #     if i["search_type"] == "fuzz_ratio":
    #         print(i)