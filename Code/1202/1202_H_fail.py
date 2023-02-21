## 실패 ##
import sys
sys.stdin = open('input.txt', 'r')
#####
# import heapq
# from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
item = []
for _ in range(n):
    item.append(list(map(int, input().split())) + [0])
item = sorted(item, key = lambda X:(-X[1], X[0]))
bag = []

for _ in range(k):
    bag.append([int(input()), 0])
bag.sort()

print(item)
print(bag)

bag_idx = 0
item_idx = 0
while bag_idx < len(bag) and item_idx < len(item):
    if bag[bag_idx][0] >= item[item_idx][0] and not item[item_idx][2]:
        bag[bag_idx][1] = item[item_idx][1]
        bag_idx += 1
        item[item_idx][2] = 1
        item_idx = 0
    else:
        item_idx += 1
        if item_idx == len(item) and bag_idx < len(bag):
            bag_idx += 1
            item_idx = 0

print(item)
print(bag)

Sum = 0
for i in bag:
    Sum += i[1]
print(Sum)

'''
2 1
5 10
100 100
11
###
[[100, 100, 0], [5, 10, 0]]
[[11, 0]]
[[100, 100, 0], [5, 10, 1]]
[[11, 10]]
10

#####

3 2
1 65
5 23
2 99
10
2
###
[[2, 99, 0], [1, 65, 0], [5, 23, 0]]
[[2, 0], [10, 0]]
[[2, 99, 1], [1, 65, 1], [5, 23, 0]]
[[2, 99], [10, 65]]
164

#####

9 5
4 5
4 9
4 10
8 55
14 20
9 15
8 55
8 5
11 54
10
5
4
15
20
###
[[8, 55, 0], [8, 55, 0], [11, 54, 0], [14, 20, 0], [9, 15, 0], [4, 10, 0], [4, 9, 0], [4, 5, 0], [8, 5, 0]]
[[4, 0], [5, 0], [10, 0], [15, 0], [20, 0]]
[[8, 55, 1], [8, 55, 1], [11, 54, 1], [14, 20, 0], [9, 15, 0], [4, 10, 1], [4, 9, 1], [4, 5, 0], [8, 5, 0]]
[[4, 10], [5, 9], [10, 55], [15, 55], [20, 54]]
183

#####

4 4
1 100
2 200
13 300
10 500
10
10
10
14
###
[[10, 500, 0], [13, 300, 0], [2, 200, 0], [1, 100, 0]]
[[10, 0], [10, 0], [10, 0], [14, 0]]
[[10, 500, 1], [13, 300, 1], [2, 200, 1], [1, 100, 1]]
[[10, 500], [10, 200], [10, 100], [14, 300]]
1100
'''