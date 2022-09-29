class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        # idea: translate both of them into same dictionary mapping
        
        pattern = list(pattern)
        dict1, dict2 = {}, {}
        count1, count2 = 0, 0
        trans1, trans2 = "", ""
        
        for letter in pattern:
            if letter not in dict1:
                dict1[letter] = count1
                count1 += 1
            trans1 += " " + str(dict1[letter])
    
        string = string.split(" ")
        for w in string:
            if w not in dict2:
                dict2[w] = count2
                count2 += 1
            trans2 += " " + str(dict2[w])
        
        return trans1 == trans2