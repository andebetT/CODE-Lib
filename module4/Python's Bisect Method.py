import bisect
l=[1,2,3,5]
print(bisect.bisect_right(l,3))
print(bisect.bisect_left(l,2))
#bisect left is used for finding the index of the given target in sorted array if the target is reapeted in the array it will reteurn the left most inedx of the target
#bisect right is used to find the index after the given target in the right direction