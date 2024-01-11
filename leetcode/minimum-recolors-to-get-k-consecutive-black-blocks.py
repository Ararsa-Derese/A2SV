class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
            mini=k
            if len(blocks)==k:
                return blocks.count('W')
            for i in range(len(blocks)-k+1):
                if blocks[i:i+k].count('W')<mini:
                    mini=blocks[i:i+k].count('W')
            return mini
            