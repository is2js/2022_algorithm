import sys
import re

input = sys.stdin.readline

if __name__ == '__main__':
    new_id = input().strip()

    new_id = new_id.lower()

    new_id = re.sub('[^0-9a-z-_.]', '', new_id)

    new_id = re.sub('[.]+', '.', new_id)

    new_id = new_id.strip('.')

    new_id = (not len(new_id) and 'a') or new_id

    new_id = new_id[:15]\
        .strip('.')

    while len(new_id) <= 2:
        new_id += new_id[-1]

    print(new_id)
pass
