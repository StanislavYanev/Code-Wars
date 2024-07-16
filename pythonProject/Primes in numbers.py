def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1

    factor_strings = []
    for p, e in factors.items():
        if e > 1:
            factor_strings.append(f"({p}**{e})")
        else:
            factor_strings.append(f"({p})")

    return "".join(factor_strings)

print(prime_factors(7775460))
print(prime_factors(7919))

