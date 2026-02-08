class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        for idx in range(len(nums2)):
            freq[nums2[idx]] = idx
        stack = []
        greater = [-1] * len(nums2)
        for idx in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[idx]:
                    stack.pop()
            if stack:
                greater[idx] = stack[-1]
            else:
                greater[idx] = -1
            stack.append(nums2[idx])
        for idx in range(len(nums1)):
            i = freq[nums1[idx]]
            nums1[idx] = greater[i]
        return nums1