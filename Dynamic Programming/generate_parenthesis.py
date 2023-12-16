# 22. Generate Parentheses
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

def pa(n):
    if n == 0:
        return []
    
    dp = [[] for _ in range(n+1)]
    dp[0] = [""]
    
    for i in range(1, n+1):
        print("i",i)
        for j in range(i):
            print("j=",j)
            left = dp[j]
            right = dp[i-j-1]
            print ("left=",left)
            print ("right=",right)
            
            for l in left:
                print("l=",l)
                for r in right:
                    print("r=",r)
                    dp[i].append("(" + l + ")" + r)
                    print ("dp[i]=",dp[i])
                    print("\n")
    return dp

n = 5
result = pa(n)
print(result)
