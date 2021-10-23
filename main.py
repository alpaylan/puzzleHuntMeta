qu_loc_map = {
    1: 6,
    2: 3,
    3: 2,
    4: 9,
    5: 4,
    6: 10,
    7: 5,
    8: 7,
    9: 8,
    10: 1,
    11: 11,
}

loc_que_map = dict(map(lambda x: (x[1], x[0]), qu_loc_map.items()))

# print(loc_que_map)
word_loc_map = {
    1: [4, 7, 10],
    2: [3, 5, 8],
    3: [1, 3, 7, 9],
    4: [4, 5, 6, 7, 8, 9, 11],
    5: [3, 5, 8, 11],
    6: [1, 4, 9],
    7: [3, 6, 11],
    8: [3, 5, 8, 11],
    9: [2, 3, 6, 8, 11],
    10: [1, 3, 7, 9],
    11: [5, 6, 7, 9, 10],
    12: [1, 2, 7, 8, 9],
    13: [6, 8],
    14: [1, 2, 7, 8, 9],
    15: [2, 3, 6, 8, 11],
    16: [4, 5, 6, 7, 8, 9, 11],
}

qu_ans_map = {
    1: 'schadenfreude',
    2: 'jacksonpollock',
    3: 'highcost',
    4: 'spidermonkey',
    5: 'jimhenson',
    6: 'supercomputer',
    7: 'pythagoreantheorem',
    8: 'souredmilk',
    9: 'specificgravity',
    10: 'bakingsheets',
    11: 'waterhyacinth',
}

word_que_map = dict()

for i in range(1, 17):
    word_que_map[i] = []
    for elem in word_loc_map[i]:
        word_que_map[i].append(loc_que_map[elem])
        word_que_map[i].sort()

# print(word_que_map)
for i, v in word_que_map.items():
    print(i)
    print(v)

def get_common_letters(que_list):
    word_list = list(map(lambda x: set(qu_ans_map[x]), que_list))
    # print(word_list)
    commons = word_list[0]
    for word in word_list:
        commons = commons.intersection(word)

    return commons

# for i, v in word_que_map.items():
#     print(i)
#     print(get_common_letters(v))
