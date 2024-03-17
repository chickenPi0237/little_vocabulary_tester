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
        
        #select vocabulary from specific category
        if cat == 0:
            for i in range(len(self.cat_list)):
                self.test_list.extend(self.data_dct[self.cat_list[i]])  
        elif cat > 5 or cat < 0:
            print('錯誤輸入，重新選擇')
            return False
        else:
            self.test_list = self.data_dct[self.cat_list[cat-1]]

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
                if self.test_list[i]['group'] != group:
                    self.test_list.remove(self.test_list[i])
                    i-=1
                i+=1

        #start chose voc
        if num > len(self.test_list):
            print('--題目數大於可用單字數，已使用最大單字數--')
            num = len(self.test_list)
        self.test_list = random.sample(self.test_list, k = num)

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
        for item in mis_list:
            print("Question：{} Accent：{} CN：{} Ans(O):{} Ans(X):{}".format(item['voc'], item['accent'], item['t_cn'], item['ans'], item['mis_ans']))            
                

    def insert_voc(self):
        quit_flag = False
        print('start enter vocabulary. (q)uit')
        set_cat = self.check_input_int(input("選擇詞性(1)~(5)： "))-1
        set_lv = self.check_input_int(input("是否預設難度(0)否(1)~(5)： "))
        set_group = self.check_input_int(input("是否預設群組(0)否(輸入群組號)： "))
        while(1):
            for key in self.input_dict:
                if key == "level" and set_lv != 0:
                    self.input_dict[key] = set_lv
                    continue
                if key == "group" and set_group != 0:
                    self.input_dict[key] = set_group
                    continue
                if key == "level" or key == "group":
                    input_ = int(input("{}: ".format(key)))
                else:
                    input_ = input("{}: ".format(key))
                if input_ == 'q':
                    quit_flag = True
                    break
                self.input_dict[key] = input_
            if quit_flag:
                break
            # careful the difference of self.input_dict and self.input_dict.copy()
            # because of reference issue, use copy to avoid "overwriting" problem
            self.data_dct[self.cat_list[set_cat]].append(self.input_dict.copy())
            

        self.save_data_dct()

    def save_data_dct(self):
        try:
            output_json_file = open('.\\voc_data.json', 'w', encoding='UTF-8')
            json.dump(self.data_dct, output_json_file, indent=4, ensure_ascii=False)
            output_json_file.close()
        except FileNotFoundError :
            print(FileNotFoundError)


    def view_voc(self):
        set_cat =  self.check_input_int(input('選擇詞性類別： '))-1
        view_list = self.data_dct[self.cat_list[set_cat]]
        for item in view_list:
            #print("Vocabulary：{voc:20s}Hiragana/Spelling：{ans:<12s} Accent：{accent:<10s} CN：{t_cn:<10s} Group:{group:<5d} Levels:{level:<5d}".format(**item))
            print("Vocabulary：{voc:8s}Hiragana/Spelling：{ans:8s} Accent：{accent:3s} CN：{t_cn:<8s} Group:{group:<5d} Levels:{level:<5d}".format(**item))






if __name__ == "__main__":
    print("this is vocabulary.py")