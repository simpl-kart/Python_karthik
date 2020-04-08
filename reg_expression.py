import re

#########There are many types of regular expresssions and few are mentioned below
print(re.sub('ab','*', 'abdecl;aoadbab'))     ######finds the ab pair in the string and replace it with *
print(re.sub('[ab]','*', 'abdecl;aoadbab'))   ######finds out whereever a or b is available in teh given string and replaces it with *
print(re.sub('[abc][123]','*', 'abc1243a3')) ####    combination fo a and 1or2or3 or b and 1or2or3 and c and 1or2or3 replace it with *
print(re.sub('A..B','*', 'A2323B A@@B A#B'))   #A and then any two character and B then replace with *
print(re.sub('AB+','*', 'AB ABBBBBBBBBBBC ABCA')) ## replace A and N number of Bs
print(re.sub('AB{3,6}', '*', 'ABBB ABBBBBBBBBC  ABBBBBBC')) #A and B should be between 3 to 6 times.
print(re.sub('^ab','*','abcijoijoiqejwr b;fdlsas; bab;wefr'))  ##which starts with ab
print(re.sub('AB{3,6}', '*', 'ABBB ABBBBBBBBBC  ABBBBBBC')) #A and B should be between 3 to 6 times.
print(re.sub('ab$','*','abcijoijoiqejwrab')) ###end of the string has ab
print(re.sub('^ab','*','abcijoijoiqejwrab')) ###starting of the string has ab


############search and match functions

print(re.search('ab', 'Here is an absolute string'))  ### Search looks for patterns anywhere in the string
print(re.match('He', 'Here is an absolute string'))  ####### Match found at the starting of the string
