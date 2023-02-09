import sys
sys.stdin = open("input.txt", "r")

arr = list(map(lambda x : x.rstrip(), sys.stdin.readlines()))
l = len(arr)
arr_s = list(set(arr))
arr_s.sort()

trie = {}
for word in arr:
    cur = trie
    for s in word:
        if s not in cur:
            cur[s] = {}
        cur = cur[s]
    if 'v' in cur:
        cur['v'] += 1
    else:
        cur['v'] = 1

for word in arr_s:
    cur = trie
    for s in word:
        cur = cur[s]
    print(f"%s %.4f"%(word,cur['v']*100/l))
