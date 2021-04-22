class Hand3:
    def __init__(self, *args, **kw ):
        if len(args) == 1 and isinstance(arg[0], Hand3):
            # clone an existing hand; often a bad idea
            other = args[0]
            self.dealer_card = other.dealer_card
            self.cards = other.cards
        else:
            # Build a fresh, new hand.
            dealer_card, *cards = args
            self.dealer_card = dealer_card
            self.cards = list(cards)


h = Hand( deck.pop(), deck.pop(), deck.pop() )
memento = Hand(h)


# 创建对象的方式
# 对象的初始化
# 使用静态函数作为代理构造函数

class Hand5:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    @staticmethod
    def freeze(other):
        hand = Hand5(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1):
        hand0 = Hand5( other.dealer_card, other.cards[0], card0)
        hand1 = Hand5( other.dealer_card, other.cards[1], card1)
        return hand0,

    def __str__(self):
        return ", ".join(map(str, self.cards))
# 使用一个函数完成了冻结和备忘录模式
d = Deck()
h = Hand5( d.pop(), d.pop(), d.pop() )
s1, s2 = Hand5.split(h, d.pop(), d.pop())


class Player:
    def __init__(self, table, bet_strategy, game_strategy):
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table

    def game(self):
        self.table.place_bet(self.bet_strategy.bet())
        self.hand = self.table.get_hand()
        if self.game_strategy.insurance(self.hand):
            if self.table.insure(self.bet_strategy.bet())





























