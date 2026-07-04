class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(companies) for companies in favoriteCompanies]
        n = len(sets)
        result = []

        for i in range(n):
            is_subset_of_someone = False
            for j in range(n):
                if i == j:
                    continue
                if len(sets[i]) < len(sets[j]) and sets[i].issubset(sets[j]):
                    is_subset_of_someone = True
                    break
            if not is_subset_of_someone:
                result.append(i)

        return result

                
                
