n = int(input())
for i in range(n):
    n, m =map(int, input().split())
    m_fac, n_fac, m_n_fac = 1, 1, 1
    for i in range(m):
        m_fac *= (i+1)
    for i in range(n):
        n_fac *= (i+1)
    for i in range(m-n):
        m_n_fac *= (i+1)
    print(m_fac // (n_fac*m_n_fac))