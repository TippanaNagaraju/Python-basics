# passwhile

i=1
while i<=5:
    if i==3:
        pass
    else:
        print("Processing:",i)
    i+=1

    """
    iteration 1 : i=1; i<=5 --> 1<=5 --> True --> i==3 --> 1==3 --> false -->processing --> 1+=1=1+1=2 i=2
    iteration 2 : i=2; i<=5 --> 2<=5 --> True --> i==3 --> 2==3 --> false -->processing --> 1+=1=2+1=3 i=3
    iteration 3 : i=3; i<=5 --> 3<=5 --> True --> i==3 --> 3==3 --> True -->i+=1=i=3+1=4 
    iteration 4 : i=4; i<=5 --> 4<=5 --> True --> i==3 --> 4==3 --> false -->processing --> 1+=1=4+1=5 i=5
    




    """