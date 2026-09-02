class Solution:
    def isPalindrome(self, s: str) -> bool:

        pointA = 0
        pointB = len(s) - 1

        while pointA < pointB:

            while pointA < pointB and not s[pointA].isalnum():
                pointA +=1
            while pointB > pointA and not s[pointB].isalnum():
                pointB -=1
            if s[pointA].lower() !=   s[pointB].lower():
                return False
            pointA, pointB = pointA+1, pointB-1

        return True    

            


        