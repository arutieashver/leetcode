class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        i = 0
        j = 1
        difference = 0 
        tot_duration = 0

        while j < len(timeSeries):
            difference = timeSeries[j] - timeSeries[i]
            if difference >= duration:
                tot_duration += duration
            elif difference < duration:
                tot_duration += difference
            i += 1
            j += 1  

        return tot_duration + duration

