@echo off

if "%1" == "bj" (
    ::backjoon폴더가 없으면 일단 생성한다.
    if not exist ".\backjoon\" md ".\backjoon"
    ::backjoon/ 첫번째인수명/ 으로 해당 문제의 폴더를 생성한다.
    if not exist ".\backjoon\%2" (
        md ".\backjoon\%2"
    ) else (
        echo "already solved problem"
        GOTO:EOF
    )
    ::변수할당시 = 사이에 공백이 있으면 안된다.
    Set CURRENT_FOLDER=backjoon
) else if "%1" == "pg" (
    :: else는 닫는괄호와 같은 위치여야한다.
    :: programmers폴더가 없으면 일단 생성한다.
    if not exist ".\programmers\" md ".\programmers"
    ::programmers/ 첫번째인수명/ 으로 해당 문제의 폴더를 생성한다.
    if not exist ".\programmers\%2" (
        md ".\programmers\%2"
    ) else (
        echo "already solved problem"
        GOTO:EOF
    )
    Set CURRENT_FOLDER=programmers
)  else if "%1" == "lc" (
    ::leetcode폴더가 없으면 일단 생성한다.
    if not exist ".\leetcode\" md ".\leetcode"
    ::leetcode/ 첫번째인수명/ 으로 해당 문제의 폴더를 생성한다.
    if not exist ".\leetcode\%2" (
        md ".\leetcode\%2"
    ) else (
        echo "already solved problem"
        GOTO:EOF
    )
    Set CURRENT_FOLDER=leetcode
)  else if "%1" == "others" (
    ::others폴더가 없으면 일단 생성한다.
    if not exist ".\others\" md ".\others"
    ::others/ 첫번째인수명/ 으로 해당 문제의 폴더를 생성한다.
    if not exist ".\others\%2" (
        md ".\others\%2"
    ) else (
        echo "already solved problem"
        GOTO:EOF
    )
    Set CURRENT_FOLDER=others
) else if "%1" == "cpt" (
   ::concept폴더가 없으면 일단 생성한다.
   if not exist ".\concept\" md ".\concept"
   ::concept/ 첫번째인수명/ 으로 해당 문제의 폴더를 생성한다.
   if not exist ".\concept\%2" (
       md ".\concept\%2"
   ) else (
       echo "already solved problem"
       GOTO:EOF
   )
   Set CURRENT_FOLDER=concept
)  else (
    echo "Must First arguments contains bj, pg, lc, cpt"
    GOTO:EOF
)

::Solution.py -> .\backjoon\첫번째인수명\첫번째인수명.py으로 복사한다
if "%3" == "" copy %cd%\Solution.py .\%CURRENT_FOLDER%\%2\%2.py
::               만약, 2번째 인수가 존재한다면-> .\backjoon\첫번째인수명(2번째인수명).py으로 복사한다.
if not "%3" == "" copy %cd%\Solution.py .\%CURRENT_FOLDER%\%2\%2(%3).py
:: input, output.txt를 .\backjoon\첫번째인수명 폴더로 복사한다.
copy %cd%\input.txt .\%CURRENT_FOLDER%\%2\input.txt
copy %cd%\output.txt .\%CURRENT_FOLDER%\%2\output.txt


::기존 Solution.py 초기문장 적어 초기화
echo import sys > .\Solution.py
echo. >> .\Solution.py
echo input = sys.stdin.readline >> .\Solution.py
echo. >> .\Solution.py
echo. >> .\Solution.py
echo def solution(): >> .\Solution.py
echo     pass >> .\Solution.py
echo. >> .\Solution.py
echo. >> .\Solution.py
echo if __name__ == '__main__': >> .\Solution.py
echo     solution() >> .\Solution.py

:: 기존 input, output.txt를 빈 파일로 생성
type NUL > .\input.txt
type NUL > .\output.txt
