class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for i in strs:
            nums = [0] * 26
            for j in i:
                num = ord("a") - ord(j)
                nums[num] += 1
            hashmap[tuple(nums)].append(i)
        return [i for i in hashmap.values()]
