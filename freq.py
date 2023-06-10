import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_words(txt):
   # words = re.split('[\s,:."!*] ',txt)
    for char in '?{}!,."()*<>+-=\'://#[]':
        txt = txt.replace(char,' ')
    words = txt.split()    
    return words


def sort_top(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0)+1
    res = list(counts.items())
    res.sort(key=lambda x:x[1],reverse=True)
    return res


if __name__=="__main__":
    with open("HarryPotter.txt",'r')as f:
        txt = f.read()
    txt = txt.lower()
    words = get_words(txt)
   # print(words)
    c = 0
    for w in words:
        if w == 'hello':
            c += 1
   # print(c)
    results = sort_top(words)
    for i in range(10):
        print(results[i])

    wc = WordCloud(background_color='white',max_words=100)
    wc.generate(txt)
    plt.imshow(wc)
    plt.show()
