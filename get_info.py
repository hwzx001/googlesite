import re
import requests 
from pyquery import PyQuery as pq

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

phoneRegex = re.compile(r'(?:[0-9] ?){6,14}[0-9]$')

def get_email(text):
    match =[]
    for groups in emailRegex.findall(text):
        match.append(groups[0])
    return match

def get_social(text):
    page =pq(text,'html')('a').items()
    res =[]
    for i in page:
        temp = i.attr('href')
        if 'facebook' in temp:
            res.append(temp)
        if 'ins' in temp:
            res.append(temp)
        if 'twitter' in temp:
            res.append(temp)
        if 'whatsapp' or 'what' or'ws' in temp:
            res.append(temp)

def get_phone(text):
    match =[]
    for groups in phoneRegex.findall(text):
        match.append(groups[0])
    return match

if __name__ == "__main__":
    #url = 'https://colourpop.com/'
    lst =[]
    with open(r'uk\art classes studio\w.txt','r',encoding='utf-8') as f:
        lst = f.read().split('\n')
    
    for url in lst:
        raw_html =str(requests.get(url= url).text)
        phone,email = get_phone(raw_html),get_email(raw_html)
        print(phone,email)
     
   



