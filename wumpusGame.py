#-*- coding:utf-8 -*-
from random import choice
cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

for i in cave_numbers:
    for j in range(3):
        passge_to = choice(cave_numbers)
        caves[i].append(passge_to)
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

		