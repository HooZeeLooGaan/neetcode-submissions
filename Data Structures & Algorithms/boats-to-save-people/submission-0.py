class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        no = 0
        left, right = 0, len(people) - 1
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1

            elif people[left] > people[right]:
                left += 1

            else:
                right -= 1
            
            no += 1 

        return no