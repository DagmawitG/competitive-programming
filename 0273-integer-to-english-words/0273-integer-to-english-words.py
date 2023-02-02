class Solution:
    def numberToWords(self, num: int) -> str:
        to_19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def words(n):
            if n < 20:
                return to_19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to_19[n//100-1]] + ['Hundred'] + words(n%100)
            for (th, st) in ((10**12, 'Trillion'), (10**9, 'Billion'), (10**6, 'Million'), (10**3, 'Thousand'), (10**2, 'Hundred')):
                if n < th:
                    continue
                return words(n//th) + [st] + words(n%th)
        
        if num == 0:
            return 'Zero'
        return ' '.join(words(num))
        