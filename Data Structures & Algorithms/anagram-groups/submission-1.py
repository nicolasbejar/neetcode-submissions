class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(List[str])

        for s in strs:
            key = "".join(sorted(s))
            if key not in ans:
                ans[key] = [s]
            else:
                lista = ans[key]
                lista.append(s)
                ans[key] = lista

        return list(ans.values())