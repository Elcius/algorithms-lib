def lcs(str1, str2, A, B):
    if A == 0 or B == 0:
       return 0
    elif str1[A-1] == str2[B-1]:
       return 1 + lcs(str1, str2, A-1, B-1)
    else:
       return max(lcs(str1, str2, A, B-1), lcs(str1, str2, A-1, B))

def call_lcs(str1, str2, A, B):
    answer = lcs(str1, str2, A, B)
    print("The longest common subsequence is: " + str(answer))