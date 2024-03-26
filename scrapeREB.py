import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Regex Cheat sheet : https://www.dataquest.io/blog/regex-cheatsheet/
# Regex python tester : https://pythex.org/
# re doc : https://docs.python.org/3/library/re.html

teams = []
with open("rebounds.txt", "r") as txt_file:
   lines = txt_file.readlines()
reg = r'<td><.*"><.*class="school">[A-z\s\.&\-\(\)\;\']*</a>' #the group of char a to c
string = ""
for line in lines:
    string+=line
    #   print(line)
regs = re.findall(reg,string)
for reg in regs:
    teams.append(reg[reg.index('"school"')+9:-4])


reg = r'<td>.*</td>' #the group of char a to c
rebs = []
regs = re.findall(reg,string)
count = 0
for reg in regs:
    if(count % 8 == 4 or count % 8 == 6):
        rebs.append(reg[4:-5])
    count+=1

print(rebs)