class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        largest=max(len(i) for i in words)
        dic=defaultdict(list)
        order="$"+order
        
        for _ in range(len(words)):
            words[_]+=("$"*(largest-len(words[_])))
            
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j in dic:
                    if words[i][j]!=dic[j][len(dic[j])-1]:
                        if order.index(words[i][j])<order.index(dic[j][len(dic[j])-1]):
                            
                            return False
                        else:
                            dic.clear()
                            for a in range(len(words[i])):
                                dic[a].append(words[i][a])
                            break
                    
                    dic[j].append(words[i][j])
                else:
                    dic[j].append(words[i][j])
        return True