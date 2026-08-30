for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print("")
    """ 
     iteration 1: i=0 --> range(i+1) -->range(0+1) --> range(1) --> j=0 -->print(*) -->end=" "(space)-->print-->new line
     
    iteration 2: i=1 -->rnage(i+1) -->range(1+1)-->range(2)-->j=0,1
                                                          -->j=0 -->print(*) -->end=" "(space)
                                                          -->j=1 -->print(*) -->end=" "(space)-->print -->new line
    iteration 3: i=2 -->range(i+1) -->range(2+1) -->range(3) -->j=0,1,2
                                                             -->j=0 -->print(*) -->end=" "(space)
                                                             -->j=1 --print(*) -->end=" "(space)
                                                             -->j=2 --print(*) -->end=" "(space)
    iteration 4: i:3 -->range(i+1 -->range(3+1) -->range(4) -->print(*) -->end" "(space) -->print -->new line
                                                            -->j=0,1,2,3
                                                            -->j=0 -->print(*)-->end=" "(space)
                                                            -->j=1 -->print(*)-->end=" "(space)
                                                            -->j=2 -->print(*)-->end=" "(space)
                                                            -->j=3 -->print(*)-->end=" "(space)
    iteration 5: i:4 -->range(i+1 -->range(4+1) -->range(5) -->print(*) -->end" "(space) -->print -->new line
                                                                -->j=0,1,2,3,4
                                                                -->j=0 -->print(*)-->end=" "(space)
                                                                -->j=1 -->print(*)-->end=" "(space)
                                                                -->j=2 -->print(*)-->end=" "(space)
                                                                -->j=3 -->print(*)-->end=" "(space)  
                                                                -->J=4 -->print(*) -->end" "(space) -->print -->new line"""