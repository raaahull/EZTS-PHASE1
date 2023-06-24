#list1 = [10,20,30]
#list2 = [30,10,40]
#list3=[]
##print([(x,y) for x in [10,20,30] for y in [30,10,40]if x!=y])
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns that start with '*'
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    # Fill in the table row by row
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] in {s[i-1], '?'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
    
    return dp[m][n]
