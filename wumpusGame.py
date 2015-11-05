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
print "你能看到", len(cave_numbers),"号房间"
print "你需要输入你将想要下一个房间的数字"
while True:
    print "你在房间里了号码是:", player_location
    if (player_location == wumpus_location - 1 or player_location == wumpus_location + 1):
        print "我闻到了wumpus的气味!"
    if (player_location == wumpus_friend_location -1 or player_location == wumpus_friend_location + 1):
        print "我嗅到了另外一个wumpus的味道!臭豆腐的味道啊~"
        print "下个你要移动的房间号是多少"
    player_input = raw_input(">")
    if (not player_input.isdigit() or int(player_input) not in  cave_numbers):
        print player_input, "不在这个房间"
    else:
        player_location = int(player_input)
    if player_location == wumpus_location:
        print "哈呀呀呀!你被萌萌哒Wumpus次掉了"
        break
    if player_location == wumpus_friend_location:
        print "Ha~你被臭豆腐味的wumpus次掉了~"
        break

		