import distance

def edit_distance(s1, s2):
    return distance.levenshtein(s1, s2)

s1 = 'string'
s2 = 'setting'
print(edit_distance(s1, s2))

