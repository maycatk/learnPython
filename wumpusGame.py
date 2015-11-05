#-*- coding:utf-8 -*-
from random import choice
cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

unvisited_caves = range(0,20)
visited_caves = [0]
unvisited_caves.remove(0) #准备工作

while unvisited_caves !=[]:
    i = choice(visited_caves)
    if len(caves[i]) >= 3:
        continue   #随机选择一个已连接的洞穴

    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i) #将其连接到一个未连接的洞穴

    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave) #将洞穴标记为已连接

    for number in cave_numbers:
        print number, ":", caves[number]
    print '-----------'   #报告进度

for i in cave_numbers:
    while len(caves[i]) < 3:
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)  #添加其他通道

    for i in cave_numbers:
        print number,":",caves[number]
    print '------------'    #报告进度        
    
for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
print caves

wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)
print "欢迎来到打打小怪兽游戏"
print "你能看到", len(cave_numbers),"号洞穴"
print "你需要输入你将想要下一个洞穴的数字"
while True:
    print "你在洞穴里了号码是:", player_location
    print "在这，你能看到的洞穴", caves[player_location]
    if wumpus_location in caves[player_location]:
         print "我嗅到了一个wumpus的味道"
    
    print "下次要去哪个？"
    player_input = raw_input(">")
    if(not player_input.isdigit() or int(player_input) not in caves[player_location]):
        print player_input + "?"
        print "不是这个方向啦~·"
        continue             
    else:
        player_location = int(player_input)
    if player_location == wumpus_location:
        print "哈呀呀呀!你被萌萌哒Wumpus次掉了"
        break
    if player_location == wumpus_friend_location:
        print "Ha~你被臭豆腐味的wumpus次掉了~"
        break

		