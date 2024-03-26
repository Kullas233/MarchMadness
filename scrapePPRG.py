import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Regex Cheat sheet : https://www.dataquest.io/blog/regex-cheatsheet/
# Regex python tester : https://pythex.org/
# re doc : https://docs.python.org/3/library/re.html

teams = []
with open("PPRG.txt", "r") as txt_file:
   lines = txt_file.readlines()
reg = r'<td class="text-left nowrap" data-sort="[A-z\s\.&\-\(\)\;]*">' #the group of char a to c
string = ""
for line in lines:
    string+=line
    #   print(line)
regs = re.findall(reg,string)
for reg in regs:
    teams.append(reg[40:-2])
# if re.match(reg, line): #Check if regex is correct
#     print(line)
    
    
reg = r'<td class="text-right" data-sort="\d*\.*\d*">' #the group of char a to c
poss = []
regs = re.findall(reg,string)
count = 0
for reg in regs:
    if count % 6 == 0:
        poss.append(reg[34:-2])
    count+=1


print(fuzz.ratio("Liverpool Football Club", "Liverpool FC"))


for x in range(len(poss)):
    print(poss[x])