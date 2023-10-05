import re
f=open("dry_lab.md",'r')
g=open("dry_lab_formatted.md",'w')
buff=f.read()
tag_pattern = r'\[(\d+ liked)]'
print(buff)
stuff=re.sub('Edited','',buff)
g.write(stuff)
g.close()