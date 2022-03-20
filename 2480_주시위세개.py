a, b, c = map(int, input().split())

if a == b == c:
    print(f"{10000+a*1000}")
elif a == b or c == a:     # 5, 7 라인은 2번 규칙 
    print(f"{1000+a*100}")
elif b == c:
    print(f"{1000+c*100}")
elif a != b or a != c or b != c:
    print(max(a, b, c) * 100)

