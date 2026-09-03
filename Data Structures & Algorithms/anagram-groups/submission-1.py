class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for w in strs:
            sorted_w = tuple(sorted(w))
            table[sorted_w].append(w)

        return list(table.values())

