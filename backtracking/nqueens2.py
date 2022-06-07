def is_available(candidate, current_col):
    # 수직체크와 대각선 체크 수행
    # 수직체크와 대각선 체크가 통과되면
    # dfs함수내 로직에 따라 current_col current_candidate에 들어간다.
    current_low = len(candidate)
    # 3번째 행을 처리하고 있는경우
    # candidate에는 2번째 행까지의 정보가 들어있을것. 즉, len(candidate) == 2
    # 3번째 행이면 0,1,2에 따라 2이므로
    # current_low == 2 이다.
    for queen_row in range(current_low):  # 현재 열이 0이라면 이 반복문 수행x
        if (
            candidate[queen_row] == current_col
            or abs(candidate[queen_row] - current_col) == current_low - queen_row
        ):
            # candidate[queen_row] : 퀸의 열 위치
            return False
    return True


def dfs(N, current_row, current_candidate, final_result):
    if current_row == N:
        # 종료조건. 현재 행이 마지막 행인 경우
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):  # 0 , 1, 2, 3, 4
        # N*N의 체스판임. 한 행마다 그 행의 모든 열을 다 체크
        if is_available(current_candidate, candidate_col):  # 체크하는 메서드 호출.
            print(
                "current_row [%d] candidate_col [%d] : " % (current_row, candidate_col)
            )
            current_candidate.append(candidate_col)
            print(
                "     current_row + 1 [%d] candidate_col [%d] : "
                % (current_row + 1, candidate_col)
            )
            dfs(N, current_row + 1, current_candidate, final_result)  # 다음열 탐색
            v = current_candidate.pop()
            # 더이상 진행할 곳이 없는 경우
            # 종료조건에 따라 콜스택에 들어가있는 dfs함수들이 종료되기시작
            # 종료와 함께 해당 열(candidate_col)은 current_candidate에서 제외된다.


def solve_n_queens(N):
    final_result = []
    dfs(N, 0, [], final_result)
    return final_result


print(solve_n_queens(4))
