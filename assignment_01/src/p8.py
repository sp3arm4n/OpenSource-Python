def population_average(dic):
    s = 0
    c = 0
    for x in dic:
        s += int(dic[x])
    return int(s/len(dic))