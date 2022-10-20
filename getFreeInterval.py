
#Brute Force - O(N)

def getFreeInterval(schedule):



    free_intervals = {}
    emp_free = []
    for i,employee_schedule in enumerate(schedule):
        print(f"i {i} employee_schedule {employee_schedule}")
        
        print("len ", len(employee_schedule))

        if len(employee_schedule) == 1:

            emp_free.append([float('-inf'),schedule[i][0].start])
            emp_free.append([schedule[i][0].end,float('inf')])
            

        for k in range(0,len(employee_schedule)-1):
            # print("k",k)

            # print(f"employee_schedule[{k}].start, {schedule[i][k].start}" )
            # print(f"employee_schedule[{k}].end, {schedule[i][k].end}" )


            if k == 0:

                emp_free.append([float('-inf'),schedule[i][k].start])


            
    
            emp_free.append([schedule[i][k].end,schedule[i][k+1].start])

            if k == len(employee_schedule) -2 :  #last interval

                emp_free.append([schedule[i][k+1].end,float('inf')])
            #     print("emp_freee end" , emp_free)
                
            # print("emp_freee all" , emp_free)

        
    emp_free.sort()
    print(emp_free)
