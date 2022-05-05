import csv
import math
import requests 
import pandas as pd 
from pyquery import PyQuery as pq


def readfile(filename):
    text =''
    with open(filename,'r',encoding ='utf8') as f:
        text = f.read()
    return text

def parse_rawtext(raw_text):
    if raw_text!='':
        page =pq(raw_text,parser ='html')
        search_content = page('#search')
        lst = search_content('a').items()
        res =[]
        for i in lst:
            temp = i.attr('href')
            if temp!=None and 'google'not in temp:
                res.append(temp)
        #print(res)
        return res       
    else:
        return None


#def visit_page(page_url):


if __name__ == "__main__":
    url = []
    for i in range(1,11):
        text =readfile('{}.html'.format(str(i)))
        url.extend(parse_rawtext(text))
    print(url)
    with open('w.txt','w',encoding= 'utf-8') as f:
        for item in url:
            f.write(str(item))
            f.write('\n')
    