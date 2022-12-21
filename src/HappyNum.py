
def isHappy(n: int):

    #inside fucn
    def sum_sq(n):
        num =str(n)
        sq = 0
        for i in num:
            sq+=int(i)**2
        # print(sq)
        return sq

    og = n
    hash = []

    while len(str(n)) >= 1:

        n = sum_sq(n)
        

        if n == 1:
            break

        if n in hash:  #if endless loop has started
            break
            
        
        hash.append(n)
    
    return n==1


print(isHappy(2))