# 검은 블록일때는 멈추기

def gravity():
    for c in range(N):          # 열 기준
        pointer = N - 1         # 블록이 떨어질 위치
        
        for r in range(N-1, -1, -1):   # 아래 → 위
            if board[r][c] == -1:      # 검은 블록
                pointer = r - 1
                
            elif board[r][c] >= 0:     # 일반 블록 / 무지개
                board[pointer][c] = board[r][c]
                
                if pointer != r:
                    board[r][c] = -2   # 빈칸
                
                pointer -= 1
