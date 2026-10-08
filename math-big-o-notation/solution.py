def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        
        if arr[i] == target:
            return (True, comparisons)

    return (False, comparisons)


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    l = 0
    r = len(sorted_arr) - 1
    comparisons = 0

    while l <= r:
        mid = (l + r) // 2
        comparisons += 1
        
        if sorted_arr[mid] == target:
            return (True, comparisons)

        elif sorted_arr[mid] < target:
            l = mid + 1

        else:
            r = mid - 1

    return (False, comparisons)
