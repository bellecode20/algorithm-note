# 관련 문제: boj 마법사상어와토네이도
# --------------------------------

# 반시계 회전
for _ in range(d):
    new_sand = []
    for sr, sc, p in rotated_sand:
        nsr, nsc = -sc, sr  # 90도 반시계 회전
        new_sand.append([nsr, nsc, p])
    rotated_sand = new_sand

# 시계 회전
N = len(A)
B = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        B[c][N-1-r] = A[r][c]

# --------------------------------

# 반복문 사용 틀린 코드
# 모든 원소들을 d번 회전해야 하는데, 지금은 sand의 d번째까지만 회전하고 있음
def get_rotate_sand(d):
    rotated_sand = deepcopy(sand)

    # 방향으로 회전
    for i in range(d):
        sr, sc, p = rotated_sand[i]
        nsr, nsc = -sc, sr
        rotated_sand[i] = [nsr, nsc, p]
    

    return rotated_sand

#수정한 코드
def get_rotate_sand(d):
    rotated_sand = [x[:] for x in sand]
    rotated_alpha = alpha[:]

    # 방향 d만큼 90도 반시계 회전 🔥
    for _ in range(d):
        new_sand = []
        for sr, sc, p in rotated_sand:
            nsr, nsc = -sc, sr  
            new_sand.append([nsr, nsc, p])
        rotated_sand = new_sand

        ar, ac = rotated_alpha
        rotated_alpha = [-ac, ar]

    return rotated_sand, rotated_alpha
