class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        
        top_counter = 0
        while top_counter < (len(s)-1):
            # print(s[top_counter])
            sub_tracker = {}
            sub_tracker[s[top_counter]] = 1
            sub_length = 1
            sub_counter = top_counter + 1
            while (sub_counter < len(s)) and (s[sub_counter] not in sub_tracker):
                sub_tracker[s[sub_counter]] = 1
                sub_length += 1
                sub_counter += 1
                # print(f"Subtrack: {sub_tracker}")

            if sub_length > max_length:
                max_length = sub_length

            top_counter += 1
            
        return max_length
