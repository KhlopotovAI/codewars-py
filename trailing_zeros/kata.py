def zeros(n):
    z = 0
    q = n

    while q:
        q //= 5
        z += q

    return z
