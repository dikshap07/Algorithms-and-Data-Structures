def plusOne(digits):

    #base case: if last digit is not 9

    if digits[-1] != 9:

        digits[-1]+= 1

        return digits

    

    if digits[-1] == 9:

        # digits[-1] = 0

        if len(digits) == 1:

            digits.append(1)
            digits[-1] = 0
            digits[-2] = 1
        
        else:

            
        
            digits = plusOne(digits[:-1])

            digits.append(0)

        return digits
        


print(plusOne([4,3,2,5,6]))

print(plusOne([9,8,7,6,5,4,3,2,1,0]))

# print(plusOne([[4,3,2,1]]))
