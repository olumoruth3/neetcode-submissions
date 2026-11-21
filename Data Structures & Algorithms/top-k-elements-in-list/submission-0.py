class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Go thorugh the array once counting the occurence of each didtinct value encountered
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        top_k_pairs = sorted(frequencies.items(), key = lambda item: item[1], reverse = True)[:k]
        top_k_numbers = [num for num, _ in top_k_pairs]

        return top_k_numbers