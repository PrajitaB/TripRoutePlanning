def getWays(n, c):
    # Write your code here
    dp=[0]*(n+1)
    dp[0]=1
    sorted(c)
    j = 0
    for i in range(len(c)):
        for j in range(n+1):
            if c[i]>j:
                continue
            else:
                dp[j]+=dp[j-c[i]]
                print(f"j={j}, dp={dp}")
            
    return dp[n]

n = 3
c = [8,3,1,2]
print(getWays(n, c))