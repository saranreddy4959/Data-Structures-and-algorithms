def sqrt(number):

    if (number==0 or number==1):
        return number

    start=0
    end=number

    while(start<=end):
        avg= (start+end)//2

        if(avg*avg==number):
            return avg

        elif(avg*avg< number):
            start=avg+1
            result = avg

        else:
            end=avg-1

    return result


print ("Pass" if  (3 == sqrt(9)) else "Fail")  #Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")  #Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") #Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")  #Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") #Pass





