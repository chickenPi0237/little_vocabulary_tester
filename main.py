import os
import json
from vocabulary import vocabulary

"""
名詞 noun
形容詞 adj
形容動詞 adjn (Adjectival noun)
動詞 verb
副詞 adverb

accent
[0] 平板
[1] 頭高
[2] 中高(標示小於字數)
[3] 尾高(標示與字數相同)
"""
"""
data_dct = {
    "noun" :[],
    "adj" :[{"voc":"暑い","ans":"あつい","accent":"2","t_cn":"熱的","group":1,"level":5},
        {"voc":"寒い","ans":"さむい","accent":"2","t_cn":"冷的","group":1,"level":5}
    ],
    "adjn" :[],
    "verb" :[],
    "adverb" :[]
}
input_list = []
input_dict = {"voc":" ","ans":" ","accent":" ","t_cn":" ","group":" ","level":" "}
"""

if __name__ == "__main__":
    voc = vocabulary()

    while(1):
        print("單字小教室")
        chose = input("請選擇功能：(1)測驗(2)新增單字(q)離開")
        if chose == '1':
            #setting test
            voc.setting_test()
        elif chose == '2':
            voc.insert_voc()
        elif chose == 'q':
            print('結束程式')
            break

'''
for i in input_dict.keys():
    if i == "group":
        input_dict[i] = 1
    elif i == "level":
        input_dict[i] = 5
    else:
        input_dict[i] = input(f"{i}: ")
print(input_dict)
input_list.append(input_dict)

data_dct['noun'] = input_list

output_json_file = open('.\\voc_data.json', 'w', encoding='UTF-8')
json.dump(data_dct, output_json_file, indent=4, ensure_ascii=False)
output_json_file.close()

empty_dct = {}

input_json_file = open('.\\voc_data.json', 'r', encoding='UTF-8')
empty_dct = json.load(input_json_file)

print(empty_dct)
print(type(empty_dct))
input_json_file.close()
'''