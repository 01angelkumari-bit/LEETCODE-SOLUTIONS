class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        max_fruit=0
        left=0
        for right in range(len(fruits)):
            fruit=fruits[right]
            count[fruit]=count.get(fruit,0)+1

            while len(count)>2:
                count[fruits[left]]-=1
                if(count[fruits[left]]==0):
                    del count[fruits[left]]
                left+=1

            max_fruit=max(max_fruit,right-left+1)
        return max_fruit
        