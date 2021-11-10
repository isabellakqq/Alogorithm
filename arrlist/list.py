data = [ [1487799425, 14, 1], 
        [1487800378, 10, 1],
        [1487801478, 18, 1],
        [1487901013, 1,  0],
        [1487901211, 37,  1],
        [1487901211, 7,  0] ]
def find_busiest_time(data):
    if len(data) == 1:
        return data[i][0]
    res = None
    max_one = float('-inf')
    cur_left = 0
    for i in range(len(data)):
        people = data[i][1]
        e = data[i][2]
        if e:
            cur_left += people
        else:
            cur_left -= people
        if i + 1 < len(data) and data[i][0] == data[i+1][0]:
            continue
        if max_one < cur_left:
            max_one = cur_left
            res = data[i][0]
    return res

print(find_busiest_time(data))