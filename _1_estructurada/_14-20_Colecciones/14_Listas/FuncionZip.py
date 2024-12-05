if __name__ == '__main__':
    nums1=[1,2,3,4]
    nums2=[5,3,4]
    nums3=[8,9,0,5,7]

    result=0
    for u,v,w in zip(nums1,nums2,nums3):
        print(f"{u} x {v} x {w} = {result}")
        result += u * v * w

    print(result)