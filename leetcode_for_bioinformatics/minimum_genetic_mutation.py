# solution using bfs

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = [[startGene, 0]]
        while queue:
            # pop(0) for FIFO, using pop() results in stack like behaviour
            word, length = queue.pop(0)
            if word == endGene:
                return length
            for i in range(len(word)):
                for c in 'ACTG':
                    next_word = word[:i] + c + word[i+1:] 
                    if next_word in bank:
                        bank.remove(next_word)
                        queue.append([next_word, length + 1])

        return -1
    
# look into edit distance algorithm

class Solution_dfs:
    def dfs(self, current, end, mutations, remaining_bank):
        if current == end:
            return mutations
        if len(remaining_bank) == 0:
            return -1
        mutations_list = []
        for gene in remaining_bank:
            gene_separated = sum([gene[i] != current[i] for i in range(len(gene))])
            if gene_separated == 1:
                new_mut = self.dfs(gene, end, mutations+1, [i for i in remaining_bank if i != gene])
                if new_mut != -1:
                    mutations_list.append(new_mut)
        return min(mutations_list) if len(mutations_list) != 0 else -1
    
    def minMutation(self, start, end, bank):
        mutations = self.dfs(start, end, 0, bank)
        return mutations
