# from random import choice
# cave_numbers = range(0,20)
# caves = []
# for i in cave_numbers:
#     caves.append([])
# for i in cave_numbers:
#     passage_to =choice(cave_numbers)
#     caves[i].append(passage_to)
# print caves
# 添加便利函数
def create_tunnel(cave_form, cave_to):
    """Create a tunnel between cave_form and cave_to """
    caves[cave_form].append(cave_to)
    caves[cave_to].append(cave_form) #创建通道以及将洞穴标记为连接

def visit_cave(cave_number): #选择洞穴
    """ Mark a cave a s visited """
    visit_caves.append(cave_number)
    unvisited_caves.remove(cave_number)
def choose_cave(cave_list):
    """Pick a cave from a list,provided that the cave has less than 3 tunnels."""
    cave_number = choice(cave_list)
    while len(cave[cave_number]) >= 3:
        cave_number = choice(cave_list)
       return cave_number    

def print_caves():
	""" Print out the current cave structure """
	for number in cave_numbers:
		print number,":",cave[number]
	print '----------'

