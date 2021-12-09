class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list1 = []
        for i in range(1,n+1):
            list1.append(i)
        for i in range(0,len(list1)):
            if((list1[i]%5==0) and (list1[i]%3==0) ):
                list1[i] = "FizzBuzz"
            elif (list1[i]%3==0):
                list1[i] = "Fizz"
            elif(list1[i]%5==0):
                list1[i] = "Buzz"
            
       
        return [str(i) for i in list1]