def Merge(nums1,nums2):
    i=j=0
    sorted = []
    while i<len(nums1) and j< len(nums2):
        if nums1[i]>nums2[j]:
            sorted.append(nums2[j])
            j+=1
        else:
            sorted.append(nums1[i])
            i+=1
    while i< len(nums1):
        sorted.append(nums1[i])
        i+=1
    while j< len(nums2):
        sorted.append(nums2[j])
        j+=1
    return sorted
  
nums1 = list(map(int,input("ENter the nums1 in sorted : ").split()))
nums2 = list(map(int,input("ENter the nums2 in sorted : ").split()))
print(Merge(nums1,nums2))