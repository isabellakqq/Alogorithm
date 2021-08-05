# cities = ['London', 'Paris', 'Paris', 'Los Angeles', 'New York']
# ind = list(range(5))
# zip_cities = zip(cities, ind)
# sorted_cities = sorted(zip_cities)
# print(list(sorted_cities))
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        modified = list(s)
        for index, source, target in zip(indices, sources, targets):
            print(list(zip(indices, sources, targets)))
            if not s[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index+1, len(source) + index):
                    modified[i] = ""

        return "".join(modified)