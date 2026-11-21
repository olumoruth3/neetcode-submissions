class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using the bucket sort algorithm (solves sorting)
        buckets = [[] for _ in range(0, len(nums)+ 1)]
        frequencies = {}
        # Go through the array once noting down the number of occurence of each distinct element
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for num, freq in frequencies.items():
            buckets[freq].append(num)
        
        top_k_numbers = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                top_k_numbers.append(num)

                if len(top_k_numbers) == k:
                    return top_k_numbers
