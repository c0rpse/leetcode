class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # (1,3) (2,4) (3,9)
        # (j-i)*(height[i]+height[j])/2
        left, right = 0, len(height) - 1
        max_area, cur_area = 0, 0
        while left < right:
            cur_area = (right - left) * (height[left] if height[left] < height[right] else height[right])
            if cur_area > max_area:
                max_area = cur_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
