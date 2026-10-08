def factorial(n):
    """
    n: a non-negative integer

    Returns:
        n! = n * (n-1) * ... * 1, the product of every integer from 1 to
        n. factorial(0) is 1 (the empty-product convention).
    """
    # TODO: Implement factorial as Prod_{i=1}^{n} i from Theory.
    if n == 0:
        return 1;

    else:
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result
        
        
def n_choose_k(n, k):
    """
    n, k: non-negative integers, 0 <= k <= n

    Returns:
        C(n, k) = n! / (k! * (n - k)!), the number of size-k subsets of
        an n-element set, as an integer.
    """
    # TODO: Implement using factorial, from Theory's formula.
    num = factorial(n)
    den1 = factorial(k)
    den2 = factorial(n - k)

    return num // (den1 * den2)
