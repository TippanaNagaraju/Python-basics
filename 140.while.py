
while i<=3:
    j=1
    while j<=2:
            print(i,j)
            j+=1
    i+=1
"""
iteration 1: i=1; i<=3 True-->j=1--> j<=2 --> 1<=2 --> true --> print(i,j) --> 1 1 --> j+=1 --> j=j+1=1+1=2 --> j=2
                        i=1; j=2 --> j<=2 --> 2<=2 --> true --> print(i,j) --> 1 2 --> j+=1 --> j=j+1=2+1=3 --> j=3 --> j<=2 --> 3<=2--->false
                        i+=1; i=i+1 --> i=1+1 --> i=2
    
    """