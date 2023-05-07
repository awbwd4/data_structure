def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col)==current_row - queen_row:
            return False
    return True




def dfs(N, current_row, current_candidate, final_result):
        #current_row : 재귀함수가 수행할 행
        # current_candidate : 재귀함수가 수행할 퀸의 위치
    if current_row == N : # 현재 위치한 행의 수가 퀸의 수와 같으면 -> 처리가 다 됐다는 뜻
        print(current_candidate)
        final_result.append(current_candidate[:])
        return
    
    for candidate_col in range(N) : # 체스판의 크기는 N*N이다
        if is_available(current_candidate, candidate_col): # pruning
            current_candidate.append(candidate_col)
            dfs(N, current_row+1, current_candidate, final_result)#현재 행에서 값을 찾았다면 다음 행을 탐색함.
            current_candidate.pop() 
            #다음행에 대한 dfs에서 아무값도 찾지 못한다면, 지금 이 candidate_col은 후보에서 제외한다.


def solve_n_queens(N): # N : 퀸의 수
    final_result = [] # 체스판
    dfs(N, 0, [], final_result)
    return final_result
