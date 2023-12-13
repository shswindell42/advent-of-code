from dataclasses import dataclass
from functools import cmp_to_key


face_value = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4, 
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 11,
    "K": 12,
    "A": 13
}

@dataclass
class Hand:
    cards: str
    bid: int

    # calculate the value of the hand
    def value(self) -> int:
        value = self._hand_value(self.cards)

        other_cards = set(self.cards) - {'J'}
        for o in other_cards:
            alt_hand = self.cards.replace("J", o)
            value = max(value, self._hand_value(alt_hand))

        return value
        
    def _hand_value(self, cards) -> int:
        agg = {}
        for c in cards:
            agg[c] = agg.get(c, 0) + 1

        highest_multiple = max(agg.values())
        distribution = sorted(agg.values())
        if highest_multiple == 5:
            value = 6 # five of a kind
        elif highest_multiple == 4:
            value = 5 # four of a kind
        elif distribution == [2, 3]:
            value = 4 # full house
        elif highest_multiple == 3:
            value = 3 # three of a kind
        elif distribution == [1, 2, 2]:
            value = 2 # two pair
        elif distribution == [1, 1, 1, 2]:
            value = 1 # one pair
        else:
            value = 0 # high card

        return value

# compares two hands
# return 1 if left > right
# 0 if left = right
# -1 if left < right
def compare_hands(left: Hand, right: Hand) -> int:
    left_value = left.value()
    right_value = right.value()

    if left_value > right_value:
        result = 1
    elif left_value < right_value:
        result = -1
    else:
        # compare cards in order
        for l, r in zip(left.cards, right.cards):
            if face_value[l] > face_value[r]:
                result = 1
                break
            elif face_value[l] < face_value[r]:
                result = -1
                break
            else:
                result = 0
    
    return result

hands: list[Hand] = []
with open("./day7.txt", "r") as fp:
    for line in fp.readlines():
        data = line.split(" ")
        hands.append(Hand(data[0], int(data[1].strip())))

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

#calculate winnings
winnings = 0
for i, h in enumerate(sorted_hands):
    winnings += (i + 1) * h.bid
    print(f"{h.cards} {h.bid} {winnings}")

print(winnings)