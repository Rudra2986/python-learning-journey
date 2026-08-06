class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        alice = 0
        bob = 0
        first = 0
        last = len(piles) - 1

        for i in range(len(piles)):

            if piles[first] >= piles[last]:
                maxno = piles[first]
                first += 1
            else:
                maxno = piles[last]
                last -= 1

            if i%2 == 0:
                alice += maxno
            else:
                bob += maxno

        if alice > bob:
            return True
        else:
            return False

