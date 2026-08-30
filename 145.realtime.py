# skip lunch break

period=1

while period<=7:
    if period==4:
        period+=1
        continue
    print("period",period)
    period+=1

    """
 perod 1 : period<=7 --> 1<7 --> --> True --> period==4 --> 1==4 --> False --> period 1
 perod 2 : period<=7 --> 2<7 --> --> True --> period==4 --> 2==4 --> False --> period 2
 perod 3 : period<=7 --> 3<7 --> --> True --> period==4 --> 3==4 --> False --> period 3
 perod 4 : period<=4 --> 4<7 --> --> True --> period==4 --> 4==4 --> True skips period 4
 perod 1 : period<=5 --> 5<7 --> --> True --> period==5 --> 1==4 --> False --> period 5
 perod 1 : period<=6 --> 6<7 --> --> True --> period==6 --> 1==4 --> False --> period 6
 perod 1 : period<=7 --> 7<7 --> --> True --> period==7 --> 1==4 --> False --> period 7


    """