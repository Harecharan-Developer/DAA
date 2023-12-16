class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        answer=0
        for substring in words:
            main_word_length=len(s)
            substr_len=len(substring)

            dp=[[0 for col in range(main_word_length+1) ] for row in range(substr_len+1)]
            for row in range(1,substr_len+1):
                for col in range(1,main_word_length+1):
                
                    if row<=col :
                        dp[row][col]=dp[row-1][col]
                    elif substring[row-1]==s[col-1]:
                        dp[row][col]=dp[row-1][col-1]+1
                    else:
                        dp[row][col]=dp[row][col-1]
            print(dp)
            if dp[-1][-1] == substr_len:
                answer+=1
            answer+=0
        return answer
        