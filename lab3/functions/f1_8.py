def spy_game(nums):
    zzs= [0, 0, 7]
    i = 0  
    for num in nums:
        if num==zzs[i]:
            i+=1 
        if i==len(zzs):  
            print("True")
            return
    print("False")

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 