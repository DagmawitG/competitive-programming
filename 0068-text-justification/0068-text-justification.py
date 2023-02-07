class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        result = []
        i, j = 0, 0
        currentLen = 0
        while j < len(words):
            if currentLen + len(words[j]) <= maxWidth:
                currentLen += len(words[j]) + 1
                j += 1
            else:
                if i == j - 1:
                    result.append(words[i] + ' ' * (maxWidth - len(words[i])))
                else:
                    number_of_interval = j - i - 1
                    total_length = sum(map(len, words[i:j]))
                    total_space = maxWidth - total_length
                    retStr = (" " * ((total_space // number_of_interval) + 1)).join(words[i:i + 1 + total_space % number_of_interval])
                    retStr = (" " * (total_space // number_of_interval)).join([retStr] + words[i + 1 + total_space % number_of_interval:j])
                    result.append(retStr)
                currentLen = 0
                i = j
        result.append(" ".join(words[i:j]).ljust(maxWidth))
        return result

        