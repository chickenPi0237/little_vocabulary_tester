import json
import random

class vocabulary:
    def __init__(self):
        try:
            input_json_file = open('.\\voc_data.json', 'r', encoding='UTF-8')
            self.data_dct = json.load(input_json_file)
            input_json_file.close()
        except FileNotFoundError:
            self.data_dct = {
                "noun" :[],
                "adj" :[],
                "adjn" :[],
                "verb" :[],
                "adverb" :[]
            }

        
        self.input_dict = {"voc":" ","ans":" ","accent":" ","t_cn":" ","group":" ","level":" "}
        self.cat_list = ["noun", "adj", "adjn", "verb", "adverb"]
        self.test_list = []
    
    def setting_test(self):
        cat = input('選擇類別：(1)名詞(2)形容詞(3)形容動詞(4)動詞(5)副詞 ')
        lv = input('輸入難度(N)：(1)~(5) ')
        gp = input('輸入小組分類(0不選擇)： ')
        test_num = input('輸入題目數量： ')
        cat = self.check_input_int(cat)
        lv = self.check_input_int(lv)
        gp = self.check_input_int(gp)
        test_num = self.check_input_int(test_num)
        self.test(cat, lv, test_num, gp)

    def check_input_int(self, vtc, set_default=0):
        if vtc == "":
            vtc = set_default
        return int(vtc)

    def test(self, cat, lv, num, group=0):
        print(cat, lv, num, group)
        
        #select vocabulary from specific category
        if cat == 0:
            for i in range(len(self.cat_list)):
                self.test_list.extend(self.data_dct[self.cat_list[i]])  
        elif cat > 5 or cat < 0:
            print('錯誤輸入，重新選擇')
            return False
        else:
            self.test_list = self.data_dct[self.cat_list[cat-1]]
        print(self.test_list)

        #select vocabulary from specific level
        if lv > 5 or lv < 0:
            print('錯誤輸入，重新選擇')
            return False
        elif lv <=5 and lv >= 1:
            i = 0
            while(i < len(self.test_list)):
                if self.test_list[i]['level'] != lv:
                    self.test_list.remove(self.test_list[i])
                    i-=1
                i+=1
            
        #select vocabulary from specific group
        if group < 0:
            print('錯誤輸入，重新選擇')
            return False
        elif group > 0:
            i = 0
            while(i < len(self.test_list)):
                if self.test_list[i]['group'] != gp:
                    self.test_list.remove(self.test_list[i])
                    i-=1
                i+=1

        print(self.test_list)
        #start chose voc
        if num > len(self.test_list):
            print('--題目數大於可用單字數，已使用最大單字數--')
            num = len(self.test_list)
        self.test_list = random.sample(self.test_list, k = num)
        print(self.test_list)
        #start testing
        #initial some stats
        mistakes = 0
        mis_list = []
        for item in self.test_list:
            qst = "Question：{} Accent：{} CN：{} Ans: ".format(item['voc'], item['accent'], item['t_cn'])
            ans = input(qst)
            if ans != item['ans']:
                mistakes += 1
                item['mis_ans'] = ans
                mis_list.append(item)
                print('X')
            else:
                print('O')
        print("correct % :{:.2f}".format( (1-(mistakes/len(self.test_list)))*100 ))
        self.show_wrong_answers(mis_list)
        
        
    def show_wrong_answers(self, mis_list):
        print('wrong answers')
        for item in mis_list:
            print("Question：{} Accent：{} CN：{} Ans(O):{} Ans(X):{}".format(item['voc'], item['accent'], item['t_cn'], item['ans'], item['mis_ans']))            
                

    def insert_voc(self):
        print('insert')
    def view_voc(self):
        print('view')







if __name__ == "__main__":
    print("this is vocabulary.py")