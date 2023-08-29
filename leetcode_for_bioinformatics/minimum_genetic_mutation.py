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