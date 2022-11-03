import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 오픈채팅방: https://school.programmers.co.kr/learn/courses/30/lessons/42888
    record = []
    for _ in range(5):
        record.append(input().strip())

    uid_nickname = {}
    history = []

    for data in record:
        data = data.split()
        cmd = data[0]
        uid = data[1]
        if cmd == 'Enter':
            history.append(['Enter', uid])
            uid_nickname[uid] = data[2]
        elif cmd == 'Leave':
            history.append(['Leave', uid])
            ...
        else:  # Change
            uid_nickname.update({uid: data[2]})
    # print(history)
    # print(uid_nickname)

    result = []
    for cmd, uid in history:
        if cmd == 'Enter':
            result.append(f"{uid_nickname[uid]}님이 들어왔습니다.")
        else:
            result.append(f"{uid_nickname[uid]}님이 나갔습니다.")

    print(result)
