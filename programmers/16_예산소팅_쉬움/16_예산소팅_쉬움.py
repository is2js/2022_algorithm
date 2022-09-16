import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 예산 소팅: https://daekyojeong.github.io/posts/Algorithm4/
    # 각 부서에 필요한 돈이 d에 있다. 가장 많은 부서에 지원하려면?
    # -> 예산이 적은 팀부터 순서대로 지원해준다
    d = list(map(int, input().split()))
    budget = int(input().strip())
    d.sort()


    count = 0
    for department_budge in d:
        if budget >= department_budge:
            budget -= department_budge
            count += 1
        else:
            break
    print(count)
