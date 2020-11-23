
while True:
    begin=int(input("請輸入起始值:"))
    endl=int(input("請輸入結束值:"))
    total=0
    count=0
    
    if begin<=0 or endl <=0 or begin>endl:
            print('wrong input,try it again')
            continue
    else:
        for nums in range(begin, endl+1):
            if nums%7==0 or nums%11 ==0:
                print("{:<4d}".format(nums),end='')
                total+=nums
                count+=1
                if count%10==0:
                    print()
        
    print()
    print("總數共有",count,'個')
    print("數字總合為",total)
    break
