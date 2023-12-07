# %%
import functools

with open("C:/Users/al031880/Desktop/code/AOC/Day-7/input.txt", "r") as f:
    data = f.read().splitlines()


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type_strength = self.get_type_strength(cards)
        self.card_strength = self.get_card_strength(cards)

    def matchJokers(self, cards):
        card_matches = []
        for card in cards:
            card_matches.append(cards.count(card))

        # if max(card_matches) == 1:
        #     return cards

        ind_most_common = card_matches.index(max(card_matches))
        most_common_card = cards[ind_most_common]

        new_cards = []
        for card in cards:
            if card == "J":
                new_cards.append(most_common_card)
            else:
                new_cards.append(card)
        return new_cards

    def checkFiveOfAKind(self, cards):
        strength = 0
        if all(card == cards[0] for card in cards):
            strength = 7
        return strength

    def checkFourOfAKind(self, cards):
        strength = 0
        if any(cards.count(card) == 4 for card in cards):
            strength = 6
        return strength

    def checkFullHouse(self, cards):
        strength = 0
        if any(cards.count(card) == 3 for card in cards) and any(
            cards.count(card) == 2 for card in cards
        ):
            strength = 5
        return strength

    def checkThreeOfAKind(self, cards):
        strength = 0
        if any(cards.count(card) == 3 for card in cards):
            strength = 4
        return strength

    def checkTwoPairs(self, cards):
        cards = cards.copy()
        strength = 0
        pairs = 0
        for card in cards:
            if cards.count(card) == 2:
                cards.remove(card)
                pairs += 1
        if pairs == 2:
            strength = 3
        return strength

    def checkOnePair(self, cards):
        strength = 0
        if any(cards.count(card) == 2 for card in cards):
            strength = 2
        return strength

    def get_type_strength(self, cards):
        type_strength = 0

        cards = self.matchJokers(cards)
        type_strength = self.checkFiveOfAKind(cards)
        if type_strength == 0:
            type_strength = self.checkFourOfAKind(cards)
        if type_strength == 0:
            type_strength = self.checkFullHouse(cards)
        if type_strength == 0:
            type_strength = self.checkThreeOfAKind(cards)
        if type_strength == 0:
            type_strength = self.checkTwoPairs(cards)
        if type_strength == 0:
            type_strength = self.checkOnePair(cards)

        return type_strength

    def get_card_strength(self, card):
        card_strengths = {
            "J": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "Q": 11,
            "K": 12,
            "A": 13,
        }
        strengths = []
        for card in cards:
            strengths.append(card_strengths[card[0]])
        return strengths


all_hands = []
for row in data:
    cards = [*row.split(" ")[0]]
    bid = int(row.split(" ")[1])

    hand = Hand(cards, bid)
    all_hands.append(hand)

cards_by_card_strength = sorted(all_hands, key=lambda x: x.card_strength)
cards_by_type_strength = sorted(cards_by_card_strength, key=lambda x: x.type_strength)
# %%
winnings = 0

for ind, hand in enumerate(cards_by_type_strength):
    rank = ind + 1
    print(hand.cards, hand.type_strength)
    # print(
    #     f"Rank: {rank}",
    #     "|",
    #     f"Strength: {hand.type_strength}",
    #     "|",
    #     hand.card_strength,
    #     hand.bid,
    # )
    winnings = winnings + rank * hand.bid
print(winnings)
# %%
