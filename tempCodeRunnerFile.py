def prime_num(num):
    for i in range(2,num):
        if(num%2==0):
            return "Number is Not Prime"
            break
    return "It is Prime Number"
prime_num(19)