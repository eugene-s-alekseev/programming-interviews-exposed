import random


def binary_search(lst, el):
    def search(start, end):
        if end - start == 0:
            return start if lst[start] == el else None
        else:
            mid = start + (end - start) // 2
            if el == lst[mid]:
                return mid
            elif el < lst[mid]:
                return search(start, mid)
            else:
                return search(mid+1, end)

    return search(0, len(lst) - 1)


def main():
    lst = [random.randint(1, 30) for _ in range(10)]
    lst = sorted(lst)
    print(lst)
    print(binary_search(lst, 4))
    print(binary_search(lst, 15))
    print(binary_search(lst, 10))


if __name__ == "__main__":
    main()