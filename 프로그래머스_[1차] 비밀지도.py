def solution(n, arr1, arr2):
    answer = [] * n
    for i in range(n):
        answer.append(format(arr1[i] | arr2[i], 'b').zfill(n).replace("1", "#").replace("0", " "))
    return answer


# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17681