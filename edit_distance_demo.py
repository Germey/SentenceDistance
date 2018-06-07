import distance

def edit_distance(s1, s2):
    return distance.levenshtein(s1, s2)

strings = [
    '你在干什么',
    '你在干啥子',
    '你在做什么',
    '你好啊',
    '我喜欢吃香蕉'
]

target = '你在干啥'

results = list(filter(lambda x: edit_distance(x, target) <= 2, strings))
print(results)
