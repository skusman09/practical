# Map words to properties using python dictionaries

pos={} 
pos
pos['colorless'] = 'ADJ' 
pos
pos['ideas'] = 'N'
pos['sleep'] = 'v' 
pos['furiously'] = 'ADV' 
pos
pos['ideas']
pos['colorless']
list(pos)
sorted(pos)
[w for w in pos if w.endswith('s')]
for word in sorted(pos):
    print(word + ":", pos[word])
pos.keys()
pos.items()
pos['sleep'] = ['N', 'V'] 
pos.items()
pos = {'colorless':'ADJ', 'ideas':'N', 'sleep':'V', 'furiously': 'ADV'} 
pos
