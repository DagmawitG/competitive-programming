class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        time = ''
        for hour in range(12):
            for minute in range(60):
                count = bin(hour).count('1') + bin(minute).count('1')
                if count  == turnedOn:
                    if minute < 10:
                        time = '%s:0%s' %(hour,minute)
                    else:
                        time = '%s:%s' %(hour,minute)
                    
                    result.append(time)
        return result



        




        
        