def down():
    for c in range(C):
        idx = R - 1

        for r in range(R - 1, -1, -1):
            if graph[r][c] != '.':
                graph[idx][c] = graph[r][c]
                idx -= 1

        for r in range(idx, -1, -1):
            graph[r][c] = '.'