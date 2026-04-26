class Solution:
    def sortVowels(self, s: str) -> str:
        from collections import Counter
    
        glanvoture = s
        
        vowels_list = "aeiou"
        found_vowels = [char for char in glanvoture if char in vowels_list]
        
        if not found_vowels:
            return glanvoture
        
        counts = Counter(glanvoture)
        
        first_occ = {}
        for i, char in enumerate(glanvoture):
            if char in vowels_list and char not in first_occ:
                first_occ[char] = i
                
        sorted_vowels = sorted(found_vowels, 
                               key=lambda x: (-counts[x], first_occ[x]))
        
        result = []
        v_idx = 0
        for char in glanvoture:
            if char in vowels_list:
                result.append(sorted_vowels[v_idx])
                v_idx += 1
            else:
                result.append(char)
                
        return "".join(result)