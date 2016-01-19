#coding: utf-8
import json
import random

# Read json data:
f = open('data.json', 'r')
jsonData = json.load(f)
f.close()
#members
normal = jsonData['normal']
concerned = jsonData['concerned']
front_seat = [3,8,9,10]

def main():
    random.shuffle(normal)
    random.shuffle(concerned)
    result = []
    count = 0
    for i in range(55):
        if i in front_seat:
            result.append(concerned[count])
            count += 1
        else:
            result.append(normal[i-count])
    result_str = ''
    for i in range(55):
        u_str = result[i]
        if len(u_str) == 1:
            result_str += '|  ' + u_str + '  '
        elif len(u_str) == 2:
            result_str += '| ' + u_str + ' '
        elif len(u_str) == 3:
            result_str += '|' + u_str
        if i % 7 == 5:
            result_str += '|\n'
    print result_str

if __name__ == '__main__':
    main()
