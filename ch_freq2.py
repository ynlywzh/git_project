import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from PIL import ImageFont

font_path = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
font = ImageFont.truetype(font_path, size=14)








with open('Harry.txt','r',encoding='utf8')as f:
    txt = f.read()

words = jieba.lcut(txt)
for ch in '，。？！“”：；（）、\n \u3000':
    if ch in words:
        for i in range(words.count(ch)):
            words.remove(ch)
txt = ''
count = Counter()
for word in words :
    if(len(word)>=2):
        count[word] = count.get(word,0)+1
        txt = txt +' '+word

items = list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{0:^4}\t{1:^3}'.format(word,count))

wc = WordCloud(background_color='white',max_words=200,width=800,height=600,relative_scaling=1,max_font_size=80,random_state=40,font_path=font)
wc.generate(txt)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

