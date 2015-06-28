import pdb
f = open("dataforlesk.txt")
lines = f.readlines()
f.close()
sentence = set([x.lower() for x in "Time flies like an a arrow".split(" ")])
#word = ["fly", "flies", "flew"]
#word = ["time"]
#word =["like", "likes", "liked"]
word = ["arrow"]
for idx, line in enumerate(lines):
    count = 0
    overlapped = []
    for x in line.strip().split(" "):
        x =''.join( [ w  for w in x.lower() if w.isalpha()])
        if x not in word and x in sentence:    
            overlapped.append(x)
            count += 1
    print "\#%d %s \\\\" %(idx+1,  line.strip())
    print "Overlapped words: %s\\\\" %(' '.join(overlapped) if overlapped else "None")
    print "Overlapped number: %d\\\\" %count
    

