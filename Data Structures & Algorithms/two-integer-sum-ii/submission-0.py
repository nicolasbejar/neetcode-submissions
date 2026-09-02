class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1:
            return False

        pointA = 0 
        pointB = len(numbers) -1

        while pointA < pointB:

            if (numbers[pointA] + numbers[pointB]) == target:
                return [pointA+1, pointB+1]
            
            elif(numbers[pointA] + numbers[pointB] > target):
                pointB -= 1
            
            else:
                pointA+=1

        return []