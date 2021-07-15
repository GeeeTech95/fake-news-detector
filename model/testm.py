import time 
import sys
array = [1,3,5,7,9,11,15]
match = []
n = 0
start = time.time()
for x in array :
    for y in array :
        for z in array :
            n += 1
            if x + y + z ==  int(sys.argv[1]):
                match.append('{},{},{}'.format(x,y,z))
                
end = time.time()
print(match)
print() 
print("{} different combinations were tried  in {} seconds".format(n,end-start) )