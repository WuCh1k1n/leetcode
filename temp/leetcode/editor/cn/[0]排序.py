import heapq
import random
from typing import List


class Solution(object):
    def selection_sort(self, numbers):
        """
        选择排序
        """
        n = len(numbers)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    def insertion_sort(self, numbers):
        """
        插入排序
        """
        n = len(numbers)
        for i in range(n):
            curr = numbers[i]
            prev_index = i - 1
            while prev_index >= 0 and numbers[prev_index] > curr:
                numbers[prev_index + 1] = numbers[prev_index]
                prev_index -= 1
            numbers[prev_index + 1] = curr

    def bubble_sort(self, numbers):
        """
        冒泡排序
        """
        n = len(numbers)
        for i in range(n - 1, -1, -1):
            for j in range(0, i):
                if numbers[j + 1] < numbers[j]:
                    numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]

    def randomized_quicksort(self, nums, l, r):
        """
        随机快速排序
        """
        def randomized_partition(nums, l, r):
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            counter = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[counter] = nums[counter], nums[i]
                    counter += 1
            nums[counter], nums[r] = nums[r], nums[counter]
            return counter

        if l >= r:
            return
        mid = randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def merge_sort(self, numbers: List[int], left: int, right: int):
        """
        归并排序
        """
        def merge(numbers: List[int], left: int, mid: int, right: int):
            temp = [0] * (right - left + 1)
            i, j, k = left, mid + 1, 0
            while i <= mid and j <= right:
                if numbers[i] <= numbers[j]:
                    temp[k] = numbers[i]
                    i += 1
                else:
                    temp[k] = numbers[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = numbers[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = numbers[j]
                j += 1
                k += 1
            for p in range(len(temp)):
                numbers[left + p] = temp[p]
        if right <= left: return
        mid = (left + right) // 2
        self.merge_sort(numbers, left, mid)
        self.merge_sort(numbers, mid + 1, right)
        merge(numbers, left, mid, right)

    def heap_sort(self, numbers):
        """
        堆排序
        """
        # heapq.heapify(numbers)
        h = []
        for i in range(len(numbers)):
            heapq.heappush(h, numbers[i])
        for i in range(len(numbers)):
            numbers[i] = heapq.heappop(h)

    def counting_sort(self, numbers, min_value, max_value):
        """
        计数排序
        """
        bucket = [0] * (max_value - min_value + 1)
        for num in numbers:
            bucket[num - min_value] += 1
        i = 0
        for j in range(len(bucket)):
            while bucket[j]:
                numbers[i] = j + min_value
                i += 1
                bucket[j] -= 1
        return numbers


if __name__ == '__main__':
    # test = [1, 8, 7, 2, 3, 9, 4, 5]
    test = [1, 2, 1, 3, 1, 3, 2, 1]
    n = len(test)
    Solution().merge_sort(test, 0, n - 1)
    print(test)
