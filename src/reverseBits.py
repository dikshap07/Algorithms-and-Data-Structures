

"""
Reverse the bits of an unsigned 32 bit integer
"""




#Mask and swap solution


def reverseBits(self, n):

    #mask and swap 

    n = (n>>16) | (n<<16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) <<8 )
    n = ((n & 0xf0f0f0f0)>>4) | ((n & 0x0f0f0f0f)<< 4)
    n = ((n & 0xcccccccc)>>2) | ((n & 0x33333333)<<2)
    n = ((n & 0xaaaaaaaa)>>1) | ((n & 0x55555555)<<1)

    return n






#Bit by bit Approach : using bit manipulation : O(1),O(1)


def reverseBits(n):

    res, power = 0,31

    while n:

        res += (n&1) << power   #n&1 gets the right most digit, <<power : shifts the rightmost digit fetched to the left by power no of positions in res
        n = n>>1   #shifting n to right 1 bit i.e discarding the rightmost bit
        power-=1   #reducing power by 1 coz we already filled that position in res

    return res







#My approach: DO NOT USE IN INTERVIEWS

def reverseBits(n):


    num_string = '{0:32b}'.format(n)

    out_string = ''

    for i in range(31,-1,-1):

        out_string+= num_string[i]

    return int(out_string,2)
