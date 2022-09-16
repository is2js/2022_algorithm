import string
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
## 진법 변환

############ N진법 -> 10진수
## [1] 타진수 숫자 -> 10진수 by [ >> 0 or print]
# (1) >> 0 우쉬프트해보면 바로 알려준다.
x = 0x011 >> 0
print(x)
# (2) print()시 10진수로 변환되어 출력된다.
print(0x011)

## [2] 타진수 문자열 -> 10진수 [ int(, bas= )]
# (1) int( , base =)
y = '011'
print(int(y, base=16))
# (2) [::-1]로 뒤집은 이후 -> enumerate
result = 0
for index, value in enumerate(y[::-1]):
    result += 2**(index) * int(value)
print(result)


############ 10진수 -> N진수 문자열 문제
# (1) 10 -> 2진수 문자열 : 우shift 하며 1자리 체크
# (2) 10 -> K진법 문자열 : 몫이0될때까지 나눈 나머지들 챙기기 with 나머지 -> 1개 문자열 매핑 seq사용
# (3) 10 -> 8, 16진수 문자열 :
#     (3-1) 10에서 가는 것은 다 내장함수 bin()[2:] / oct()[2:] / hex()[2:
#     (3-2)10 -> 2진수 변환후 -> 구간처리(pair)로 3개씩 8 or 4개씩 묶어 16진수로 변환 (시간초과)
# ex> https://raw.githubusercontent.com/is3js/screenshots/main/image-20211024160308802.png
## 10진수 -> 2진수(문자열) by 우shift
# (1) bit연산을 갖다되면 2진수 숫자로 자동변환되며 -> 1의자리 on/off체크 & '0' or '1'을 누적 후 -> 우shift업뎃
x = 4
result = ''
while x:
    result += '1' if x & (1 << 0) else '0'
    x = x >> 1
result = result[::-1] # 역순으로 처리되기 때문에, 뒤집어서 출력한다.

print(result) # 100

## (2) bin()을 이용한 2진수문자열로 변환
# -> 시작문자열이 딸린 문자열을 반환한다.
print(bin(4)) # 0b100

## 10진수 -> N진수(문자열) by 몫이 0이되기전까지, 나누어서 나머지 챙기기
# (1) 10이하의 진법으로 변경할 때
x = 4
base = 2
result = ''
# 몫으로 없데이트하며, 다음 몫x가 0이 아닐때까지
# -> 몫 -> x -> 0이 된 순간 멈춘다. 몫 0이 나올때까진 연산을 한다.
# => 수학에서는 몫0이 되기전까지 나누어서, 마지막 몫 + 나머지들을 연결↺
# => 반복문에서는 몫이 0이 된 이후 while조건에 걸려 멈춤 -> 몫 0 + 전부 나머지로 들어간 상태
while x:
    # (1) 나눌때마다 나머지를 챙겨둔다.
    share, remainder = divmod(x, base)
    result += str(remainder)
    x = share
print(result[::-1])

# (2) 10진수 이상의 진법으로 변경할 때 => 16진수 문자열에서 10부터는 1글자를 넘어서므로 문자열로 다루기 까다롭다
# => 나머지를 챙겨놓는 순간에 str()변환을 어차피 하므로
#    [N진수 -> 0~N-1개의 문자열 몇개 안됨 -> 나머지로 나오는 숫자에 암묵적 매핑]
#    + [10이상의 숫자를 대문자알파벳]으로 매핑한다.
# => 1글자 문자열 매핑배열은, 굳이 list()로 안만들어도, 문자열자체로도
#    암묵적index로 매핑된 seq이다.
print(string.digits)  # 0123456789
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# => 10이상의 숫자 or 매번 문자열로 변환해야할 숫자들을 위해 => 1글자 문자열 매핑 seq(seq문자열)
map_numbers = string.digits + string.ascii_uppercase
x, base = 31, 16
result = ''
while x:
    share, remainder = divmod(x, base)
    result += map_numbers[remainder] # 나머지들(숫자)는 -> 문자열로 챙겨놓는다. N진법은 문자열로 변환하여 반환한다.
    x = share
print(result[::-1]) # 1F -> 1*16 + 15


## 2진수 <-> 8진수, 16진수
# (1) 2진수 -> 8진수 를 2진수 -내장int-> 10진수 -> 내장oct()-> 8진수로 변경
# (1-1) oct(2진수문자열 -> 10진수)를  활용해서 10진수를 8진수로 변경
이진수 = '11001100'
print(oct(int(이진수, base=2))[2:])

# (1-2) 2진수를 3개씩 끊어서 10진수로 풀어내면, 8진수가 된다.
x = '110011100'
# => 8bit라서 3개씩 안끊어진다.
# => 앞에 1개를 더 맞춰야한다.
# 9//3 -> 3  8//3 -> 2
# => 안나누어떨어지면, (1)앞에 0을 붙여 배수로 맞추던지,
#    (2) section_index를 +1해줘야한다.
# 구간별 길이 3 -> 구간의 갯수
# section_len = len(x) // 3  # 안나누어떨어지면 + 1해줘야한다.
if len(x) % 3 != 0:
    # section_len += 1
    # 안나누어떨어지면 rjust를 왼쪽을 0으로 채우되, 그 갯수를 배수중 바로 1개 큰 것으로 맞춘다.
    # -> rjust는 inplace가 아니라 return이다.
    target_len = (len(x) // 3 + 1) * 3
    print(target_len)
    x = x.rjust(target_len, '0')


# 뒤집더라도, 연산하는 3개씩 잘랐을 때 뒤집어서 연산한다..

result = ''
for section_index in range(len(x) // 3):
    parts = x[section_index * 3 + 0: section_index * 3 + 3]
    print(parts)
    # 110 -> 이 2진수를 10진수로 풀면 8진수가 된다?
    sum = 0
    for i, value in enumerate(parts[::-1]):
        sum += (2**(i) * int(value))
    result += str(sum)

print(result)

## 8진수 -> 2진수 -> 1개씩 3자리의 2진수로 만들면 된다.
# (1) 10진수용 내장함수를 이용하면 8진수 -> 10진수 -> 2진수
팔진수 = '314'
print(bin(int(팔진수, base=8))[2:])
# (2) 1개씩 끊어서  10진수를 2진수로 변환하면 된다.
result = ''
for num in 팔진수:
    이진수3개 = bin(int(num, base=8))[2:]
    # 3자리씩 채운다.
    이진수3개 = 이진수3개.rjust(3, '0')
    result += 이진수3개
print(result.lstrip('0'))











