"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

#correct

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule):

        #flatten entries
        schedule_ = []
        for emp_schedule in schedule:
            
            [schedule_.append([emp_schedule[k].start,emp_schedule[k].end]) for k in range(len(emp_schedule))]



        #sort it based on starting time

        schedule_.sort()
        print(schedule_)      
        #merging overlapping intervals

        def get_merged(schedule_):
            merged_intervals =[]
            for emp_schedule in schedule_:
                if not merged_intervals or merged_intervals[-1][1] < emp_schedule[0]:

                    merged_intervals.append(emp_schedule)

                else:

                    merged_intervals[-1][1] = max(merged_intervals[-1][1],emp_schedule[1])
            



            print("new sch", merged_intervals)
            return merged_intervals

        merged_intervals = get_merged(schedule_)

        #find time between these intervals
        free_intervals = []
        for i in range(1,len(merged_intervals)):

            if merged_intervals[i-1][1] != merged_intervals[i][0]:

                free_intervals.append(Interval(start = merged_intervals[i-1][1],end = merged_intervals[i][0])) 

        return free_intervals



#Brute Force

class Solution:
    def employeeFreeTime(self, schedule):

        #flatten entries
        schedule_ = []
        for emp_schedule in schedule:
            
            [schedule_.append([emp_schedule[k].start,emp_schedule[k].end]) for k in range(len(emp_schedule))]



        #sort it based on starting time

        schedule_.sort()
        print(schedule_)      
        #merging overlapping intervals

        def get_merged(schedule_):
            merged_intervals =[]
            
            for k in range(len(schedule_)):
                for i in range(1,len(schedule_)):
                    print(i)

                    if schedule_[i][0] < schedule_[i-1][1]:  #if current start time is less than previoys end time mergeinterval

                        schedule_[i-1][1] = max(schedule_[i-1][1],schedule_[i][1])

                        print(schedule_.pop(i))
                        print(schedule_)
                        break
                    


            print("new sch", schedule_)
            return schedule_

        merged_intervals = get_merged(schedule_)

        #find time between these intervals
        free_intervals = []
        for i in range(1,len(merged_intervals)):

            if merged_intervals[i-1][1] != merged_intervals[i][0]:

                free_intervals.append(Interval(start = merged_intervals[i-1][1],end = merged_intervals[i][0])) 

        return free_intervals


            




        









 