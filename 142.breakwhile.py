i=1
while i<=10:
    if i==3:
        break
    print(i)
    i+=1
    """
    iteration 1 : i=1; i<=10 --> i==3 --> 1==3 -->False --> 1 --> i+=1 --> i+=1+1=1 --> i=2
    iteration 2 : i=2; i<=10 --> i==3 --> 2==3 --> False --> 2 --> i+=1 --> i+=2+1=3 --> i=3
    iteration 3 : i=3; i<=10 --> i==3 --> 3==3 --> jumps out of the loop
    
    """