N = int(input())
"""

Nがめちゃくちゃでかい時はTLE

for i in range(1,N+ 1):
    if i*(i+1) > 2*(N+1):
        print(N-i+2)
        exit()
"""
