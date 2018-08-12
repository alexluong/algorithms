from collections import defaultdict
import data

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        indices = defaultdict(list)
        for i in range(0, len(S)):
            indices[S[i]].append(i)

        numMatching = 0
        for word in words:
            record = { k:0 for k in indices.keys() }
            legal = True
            index = -1

            for c in word:
                if c not in indices or record[c] == len(indices[c]) or index > indices[c][-1]:
                    legal = False
                    break

                for i in range(record[c], len(indices[c])):
                    if index > indices[c][i]:
                        continue
                    else:
                        index = indices[c][i]
                        record[c] = i+1
                        break

            if legal:
                numMatching += 1

        return numMatching

print(Solution().numMatchingSubseq(data.S, data.words))