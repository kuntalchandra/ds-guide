"""
test branch prediction
"""
import random

arr = list(range(1000000))
filter_condition = arr[len(arr) // 2]
random_arr = list(arr)
random.shuffle(random_arr)


def test_some_func() -> int:
    total = 0
    for cnt in arr:
        total += cnt
    return total


def test_some_func_condition() -> int:
    total = 0
    for cnt in arr:
        if cnt >= filter_condition:
            total += cnt
    return total


def test_some_func_random() -> int:
    total = 0
    for cnt in random_arr:
        if cnt >= filter_condition:
            total += cnt
    return total


def recursion(n: int) -> None:
    if n <= 1:
        return
    else:
        n -= 1
    recursion(n)
    print(n)


if __name__ == "__main__":
    recursion(7)
