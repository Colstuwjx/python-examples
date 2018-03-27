# coding=utf-8

a = [1, 3, 4, 5, 9, 13]
b = [2, 3, 3, 4, 5, 6, 23, 34]


def merge_sort(a, b):
    i = 0
    j = 0
    pivot = 0  # 0 or 1, means pivot for a or b
    c = []

    while i <= len(a) - 1 and j <= len(b) - 1:
        # 如果小，那么继续遍历当前数组，直到有一方终了
        if pivot == 0:
            if a[i] <= b[j]:
                pivot = 0
                c.append(a[i])

                if i == len(a) - 1:
                    c = c + b[j:]
                    break
                else:
                    i = i + 1
            else:
                pivot = 1
                continue
        else:
            if b[j] <= a[i]:
                pivot = 1
                c.append(b[j])

                if j == len(b) - 1:
                    c = c + a[i:]
                    break
                else:
                    j = j + 1
            else:
                pivot = 0
                continue

    return c

print merge_sort(a, b)
