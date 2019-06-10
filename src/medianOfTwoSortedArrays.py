import math
#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#You may assume nums1 and nums2 cannot be both empty.

class Solution:
    def findMedianSortedArrays(nums1, nums2) -> float:
        index1 = 0
        index2 = 0
        complete_list = list()
        while index1 < len(nums1) and index2 < len(nums2):
            if int(nums1[index1]) < int(nums2[index2]):
                complete_list.append(nums1[index1])
                index1 += 1
            elif int(nums2[index2]) < int(nums1[index1]):
                complete_list.append(nums2[index2])
                index2 += 1
            else:
                complete_list.append(nums1[index1])
                complete_list.append(nums2[index2])
                index1 += 1
                index2 += 1
        if index1 < len(nums1):
            while index1 < len(nums1):
                complete_list.append(nums1[index1])
                index1 += 1
        if index2 < len(nums2):
            while index2 < len(nums2):
                complete_list.append(nums2[index2])
                index2 += 1
        median = 0
        if len(complete_list) % 2 == 0:
            num1 = complete_list[int(len(complete_list)/2)]
            num2 = complete_list[(int(len(complete_list)/2) - 1)]
            median = (num1 + num2)/2
        else:
            median = complete_list[math.floor(len(complete_list)/2)]
        print("Median is " , median)
        return median

firstList = list()
firstList.append(1)
firstList.append(2)
firstList.append(3)
firstList.append(4)
firstList.append(10)
secondList = list()
secondList.append(1)
secondList.append(6)
secondList.append(7)
secondList.append(8)
secondList.append(9)
secondList.append(100)
secondList.append(110)

print(Solution.findMedianSortedArrays(firstList, secondList))