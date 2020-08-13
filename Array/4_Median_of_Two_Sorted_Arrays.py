class Solution:
        def findMedianSortedArrays(self, A, B):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """

            # n>=m
            m, n = len(A), len(B)
            if n < m:
                A, B, m, n = B, A, n, m

            imin, imax, halfLen = 0, m, (m + n + 1) / 2
            while (imin <= imax):
                i = int((imin + imax) / 2)
                j = int(halfLen) - i
                if i > 0 and A[i - 1] > B[j]:
                    imax = i - 1
                elif i < m and A[i] < B[j - 1]:
                    imin = i + 1
                else:
                    # i is perfect
                    if i == 0:
                        maxLeft = B[j - 1]
                    elif j == 0:
                        maxLeft = A[i - 1]
                    else:
                        maxLeft = max(A[i - 1], B[j - 1])

                    if (m + n) % 2 == 1:
                        return maxLeft
                    else:
                        if i == m:
                            minRight = B[j]
                        elif j == n:
                            minRight = A[i]
                        else:
                            minRight = min(A[i], B[j])
                    return (maxLeft + minRight) / 2


if __name__ == '__main__':
    A = [1, 3]
    B = [2]
    mm = Solution()
    result = mm.findMedianSortedArrays(A, B)
    print(result)