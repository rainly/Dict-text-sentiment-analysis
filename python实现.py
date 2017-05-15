# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:04:08 2017
wordcloud required C++ 14.0
running on python 3.5
@author: wangmin
"""

import jieba
import collections
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt 
# 读入评论数据，正负情感词典并合并
evaluation = []
stopwords = []
pos = []
neg = []
mydict = []

infile = open("evaluation.csv", 'r')
for line in infile:
    data = line.rstrip().split(',')
    evaluation.append(data[1])
del evaluation[0]
    
infile = open("negative.csv", 'r')
for line in infile:
    data = line.rstrip().split(',')
    neg.append(data[1])
infile = open("positive.csv", 'r')
for line in infile:
    data = line.rstrip().split(',')
    pos.append(data[1])

mydict = pos + neg
   
file = open("stopwords.csv", 'r')
for s in file:
    data = s.rstrip().split(',')
    stopwords.append(data[1])
 
# 对每条评论分词,并保存分词结果
eva = []
for i in range(len(evaluation)):
    seg_list = jieba.cut(evaluation[i], cut_all=False)
    seg_list = list(seg_list)
    eva.append(seg_list)
        
# 删除一个字的词
new_eva = eva
tmp = []
t = 0
for j in range(3321):
    for k in range(len(eva[j])):
        if len(eva[j][k]) >= 2:
            tmp.append(eva[j][k])
    new_eva[t] = tmp
    tmp = []
    t=t+1
  
# 删除停止词(对分析没有意义的词)
#for word in stopwords:
          
# 自定义情感类型得分函数
def GetScore(list):
    neg_s = 0
    pos_s = 0
    for w in list:
        if (w in neg) == True:
            neg_s = neg_s + 1
        elif (w in pos) == True:
            pos_s = pos_s + 1
    if (neg_s-pos_s) > 0:
        score = 'NEGATIVE'
        return score
    elif (neg_s-pos_s) < 0:
        score = 'POSITIVE'
        return score
    else:
        score = 'NEUTRAL'
        return score
        
# 计算每条评论的正负得分
Score = []
for l in range(len(new_eva)):
    Score.append(GetScore(new_eva[l]))
    
'''   
def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]
            
NEG=find_all_index(Score,'NEGATIVE')
POS=find_all_index(Score,'POSITIVE')
NEU=find_all_index(Score,'NEUTRAL')       

print(len(NEG))
print(len(POS))
print(len(NEU)) 
'''

    
# 统计词频
wf = {}
for p in range(len(new_eva)):
    for word in new_eva[p]:
        if word not in wf:
            wf[word]=0
        wf[word]+=1

def Sort_by_count(d):
    d = collections.OrderedDict(sorted(d.items(),key = lambda t: -t[1]))
    return d

wf = Sort_by_count(wf)    
top_key = []
top_word = []
for key in wf.items():
    top_key.append(key)


top_word = top_key[1:51]   
print(top_key[0:49])
#for key,values in wf.items():
#    print(key + "%d" % values)



# 绘制词云
word_space_split = 'a'
for i in range(3322):
     new_eva[i] = " ".join(new_eva[i])
     word_space_split += new_eva[i]
 
word_space_split = word_space_split.replace('word','')
     
 
  
abel_mask = np.array(Image.open('C:/Users/wangmin/Pictures/aaa/abc.png'))
   
  
wc = WordCloud(font_path='C:\Windows\Fonts\STSONG.TTF',#设置字体
                background_color="black", #背景颜色   
                scale=5,
                margin=1, 
                stopwords = stopwords, #设置停用词
                max_words=50,# 词云显示的最大词数  
                max_font_size=150, #字体最大值  
                random_state=30,)   # 设置有多少种随机生成状态，即有多少种配色方案

wc.generate(word_space_split)
    
#image_colors = ImageColorGenerator(abel_mask)    

# 以下代码显示图片  
plt.imshow(wc)  
plt.axis("off")  
plt.show()  





   


    
    
    
    
    
    
    
    
    
    


