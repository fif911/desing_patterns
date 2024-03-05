from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if n == 0:
#             return
#         n1_i = 0
#         n2_i = 0
#         # print(f"\nnums1: {nums1}, m: {m}, nums2: {nums2}, n: {n}")
#         i = 0
#         while True:
#             if n1_i > m - 1 or n2_i > n - 1:
#                 # print(f"i >= m - 1 i: {i}, m: {m}")
#                 break
#             # if n2_i > n - 1:
#             #     print(f"i >= n - 1 i: {i}, n: {n}")
#             #     break
#             current_max_1 = nums1[n1_i]
#             current_max_2 = nums2[n2_i]
#
#             # print(f"current_max_1: {current_max_1}, current_max_2: {current_max_2}")
#             if current_max_1 >= current_max_2:
#                 # put current 2 before current 1
#                 # move the rest of the nums1 to the right
#                 nums1[i + 1:] = nums1[i:-1]
#                 nums1[i] = current_max_2
#                 n2_i += 1
#                 n1_i += 1
#                 m += 1
#             else:
#                 # nothing to change, just proceed to get the new current max
#                 n1_i += 1
#
#             i += 1
#         # after M just copy the rest to the nums1
#         # print(f"COPY nums1: {nums1}, m: {m}, nums2: {nums2}, n: {n}")
#         # print(f"range(n2_i, n): {list(range(n2_i, n))}")
#         # for cc in range(n2_i, n):
#         for cc in range(0, n - n2_i):
#             nums1[m + cc] = nums2[n2_i + cc]

# Optimised
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize three pointers.
        p1 = m - 1  # End of the actual elements in nums1
        p2 = n - 1  # End of nums2
        i = m + n - 1  # End of the combined array

        # Iterate while there are elements in nums2
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1


class TestSolution:
    # def setup(self):
    #     self.sol = Solution()

    def test_case1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_case4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_case5(self):
        nums1 = [4, 0, 0, 0, 0, 0]
        m = 1
        nums2 = [1, 2, 3, 5, 6]
        n = 5
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_case6(self):
        nums1 = [1, 2, 3, 5, 6, 0]
        m = 5
        nums2 = [4]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_case2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1]

    def test_case3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1]
