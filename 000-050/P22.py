"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each 
name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score 
of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
with open('p022_names.txt', 'r') as names_file:
    names = names_file.readline()

names = names.replace('"','')
names_list = names.split(',')
ordered_list = []
for i in range(len(names_list)):
    min_name = min(names_list)
    names_list.remove(min_name)
    ordered_list.append(min_name)

print(ordered_list[0])

score = 0
for index, name in enumerate(ordered_list):
    name_chars = [ord(char) - ord('A') + 1 for char in name]
    score += sum(name_chars) * (index + 1)

print(score)