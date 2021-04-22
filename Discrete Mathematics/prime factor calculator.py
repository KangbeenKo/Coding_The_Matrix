def get_prime_factor(num): 
    from collections import defaultdict 
    dic=defaultdict(int) 
    d=2 
    
    while d<=num: 
        if num%d==0: 
            dic[d]+=1 
            num=num/d 
        else: 
            d+=1 
        
    return dic 

print(get_prime_factor(98765432100123456789).items())