# coding=utf-8

'''
    一场战局的一方一共有5个位置(A,B,C,D,E)供5个人选择，每个人可以有两个倾向的位置，
    当池子里有N个人时，求最大有效组合（即匹配出最多的战局组合）

    input: [(a1, A, B), (a2, C, D), (a3, E, A), (a4, E, D), (a5, B, A)] ...
    output: (a1, a5, a2, a4, a3)（不是唯一解！）

    数学：TODO

    <程序>
    已知：匹配的最大可能有效组合个数M = N / tupple_num
    已知：要使得本次有解，至少需要保证 Union(all tupples) = (A, B, C, D, E)
    最大有效组合F(N) = Max{A(5M, N)} (其中M = N/tupple_num，定义Max为求取组合的最多个数)

    穷举：这是一个排列组合问题，有A(5M, N)个搭配，某些是解不出来的方程式，我们只需要列出所有的全排列方案
    然后取出对应的元素值，只要能满足A-E的，就可以提取出来

    换个思路O(n)：
    A: (a1, a3, a5)
    B: (a1, a5)
    C: (a2)
    D: (a2, a4)
    E: (a3, a4)

    a1,
         a2,
       a1,
           a2,
    a3,
              a3,
           a4,
              a4,
    a5,
       a5

    TODO:
    当三元组变成了四元组呢：(a1, A, B, Score)?

    <参考>
    全排列算法：http://www.cnblogs.com/ayqy/p/3853545.html
'''

import copy


def lol_permutation(players, results, k, N):
    print "Calculating %s..." % results

    if k >= N:
        print "☆☆ {} ☆☆".format(results)
    else:
        # due to Python make results arg as pointer
        # we need to copy it as a new object.
        copied_results = copy.deepcopy(results)

        i = 0
        # <=1 means we have two choices.
        while i <= 1:
            position = players[k][i+1]

            # N/5 * 5 = max_team_members
            while position < (N/5 * 5):
                if players[k][0] not in copied_results and \
                  copied_results[position] == "":
                    # set ak in results.
                    copied_results[position] = players[k][0]
                    lol_permutation(players, copied_results, k+1, N)

                    # swap it!
                    copied_results[position] = ""

                position += 5

            i += 1


def main():
    A, B, C, D, E = 0, 1, 2, 3, 4
    players = [
        ("a1", A, B),
        ("a2", C, D),
        ("a3", E, A),
        ("a4", E, D),
        ("a5", B, A),
    ]
    N = len(players)
    tupple_num = 5
    max_team_members = N/tupple_num * tupple_num
    results = ['' for n in xrange(max_team_members)]

    lol_permutation(players, results, 0, N)


if __name__ == '__main__':
    main()
