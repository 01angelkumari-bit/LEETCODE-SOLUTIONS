class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        max_fruit=0
        left=0
        for right in range(len(fruits)):
            fruit=fruits[right]  #key of dictionary
            count[fruit]=count.get(fruit,0)+1   #value to key

            while len(count)>2:    #total fruit type means key is more than 2
                count[fruits[left]]-=1 #count of lefftmost is decrement by 1
                if(count[fruits[left]]==0):   #if count of leftmost is 0
                    del count[fruits[left]]   #that means no fruit exit of that type so delete leftmost fruit
                left+=1   #increment by 1 by left pointer that is expanding sliding window

            max_fruit=max(max_fruit,right-left+1)   #retuning each iteration with max fruit type
        return max_fruit
        