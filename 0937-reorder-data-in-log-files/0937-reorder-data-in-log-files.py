class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        nums = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                nums.append(log)
            else:
                answer.append(log)
        answer.sort(key = lambda x: [x.split(" ")[1:],x.split(" ")[0]])
        return answer + nums
        