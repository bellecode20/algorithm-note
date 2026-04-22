N = int(input())
expression = list(input().strip())
answer = -int(1e9)

def calc(a, op, b):  
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else: 
        return a * b

def dfs(i, result):  
    global answer
    if i >= N:
        answer = max(answer, result)
        return
    
    no_bracket = calc(result, expression[i], expression[i + 1])  
    dfs(i + 2, no_bracket)

    if i + 3 < N:
        yes_bracket = calc(expression[i + 1], expression[i + 2], expression[i + 3])
        dfs(i + 4, calc(result, expression[i], yes_bracket))
    
    
dfs(1, int(expression[0]))  # int로 변환했어야 함
print(answer)


'''
# N == 1일 때 와 같은 경계값에서 주의하기

expression[0]은 문자열이라서, 특히 N == 1일 때 바로 문제가 납니다.

예를 들어 입력이:

1
7

이면 현재 코드는

dfs(1, '7')

로 시작하고, 곧바로 기저조건에서

answer = max(answer, result)

를 하게 되는데,

max(-1000000000, '7')

은 int랑 str 비교라서 에러가 납니다.

최종 수정
dfs(1, int(expression[0]))
'''