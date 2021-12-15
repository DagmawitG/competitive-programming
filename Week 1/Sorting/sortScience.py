class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1= s.split()
        list2 = [0]*len(list1)

        for i in list1:
            x = (int(i[-1])) - 1
            list2[x] = i[:-1]
        return ' '.join(list2)
            
            
        