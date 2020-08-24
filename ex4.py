def most_frequent(string):
    d = dict()
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
o = most_frequent('Mississippi')
print (o)
sort_o = sorted(o.items(), key=lambda x: x[1], reverse=True)
for i in sort_o:
     print(i[0], i[1])
#sorted_o =  ['i'=4,'s'=4,'p'=2,'M'=1]
