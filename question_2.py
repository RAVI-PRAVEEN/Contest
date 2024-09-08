def wordBreak(n, s, dictionary):

    word_set = set(dictionary)
    dp = [False] * (len(s) + 1)

    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return 1 if dp[len(s)] else 0

n = int(input())
s = input()
dictionary = input().split()

result = wordBreak(n, s, dictionary)
print(result)
