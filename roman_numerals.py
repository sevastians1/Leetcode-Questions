def to_roman(num):
    lis=[]
    if num==0:
        return "MUST BE GREATER THEN 0"
    num = [*str(num)]
    # print(num, len(num))
    sv=0
    mv=0
    bv=0
    while num !=[]:
        if len(num)>3:
            sv="M"; mv="BIG V"; bv="BIG X"
        elif len(num)==3:
            sv="C";mv="D";bv="M"
        elif len(num)==2:
            sv="X";mv="L";bv="C"
        else:
            sv="I";mv="V";bv="X"
        # print(sv, mv, bv)
        if int(num[0]) ==1:
            lis.append(sv)
        elif int(num[0])==2:
            lis.append(sv+sv)
        elif int(num[0])==3:
            lis.append(sv+sv+sv)   
        elif int(num[0])==4:    
            lis.append(sv+mv)
        elif int(num[0])==5:    
            lis.append(mv)
        elif int(num[0])==6:    
            lis.append(mv+sv)
        elif int(num[0])==7:    
            lis.append(mv+sv+sv)
        elif int(num[0])==8:    
            lis.append(mv+sv+sv+sv)
        elif int(num[0])==9:    
            lis.append(sv+bv)
        num.pop(0)
    return "".join(lis)
