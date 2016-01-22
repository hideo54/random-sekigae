#coding: utf-8
import json
import random

def main():
    # Read json data:
    f = open('data.json', 'r')
    jsonData = json.load(f)
    f.close()
    normal = jsonData['normal']
    considered = jsonData['considered']
    front_seat = [3, 9, 8, 10, 2, 4, 16, 15, 17, 14, 18, 7, 11, 1, 5]
    used_front_seat = front_seat[:len(considered)]

    # Shuffle the array:
    random.shuffle(normal)
    random.shuffle(considered)

    # Output:
    result = []
    count = 0
    for i in range(55):
        if i in used_front_seat:
            result.append(considered[count])
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
