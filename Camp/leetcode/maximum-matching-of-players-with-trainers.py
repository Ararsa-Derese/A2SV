class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i=0
        j=0
        ans=0
        while i<len(players) and j<len(trainers):
            if trainers[j]>=players[i]:
                ans+=1
                j+=1
                i+=1
            else:
                j+=1
        return ans