import re
import requests 
# Create phone numbers regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)######注意的是三引号里有个()，此时它是groups[0]

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(requests.get('https://www.globearts.org.uk/contact-3').text)

matches = []
#添加电话号码到序列matches中
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])#join属于序列list类型的方法，序列groups中1,3,5用-连接起来。
    if groups[8] != '':#判断是否有分机号，假如有的话,此时phoneNum后面需要加上' x' + groups[8]，否则不管
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
#添加邮箱地址到序列matches中	
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

