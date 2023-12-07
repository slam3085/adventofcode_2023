from collections import Counter
from functools import cmp_to_key


all_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_hand_type(hand):
	counts = Counter(hand)
	max_v = max(counts.values())
	sorted_values = list(sorted(counts.values()))
	if len(counts.keys()) <= 2:
		if max_v == 5:
			return 7 # "Five of a kind"
		elif max_v == 4:
			return 6 # "Four of a kind"
		elif max_v == 3:
			return 5 # "Full house"
	elif len(counts.keys()) == 3:
		if max_v == 3:
			return 4 # "Three of a kind"
		elif sorted_values[0] == 1 and sorted_values[1] == 2 and sorted_values[2] == 2:
			return 3 # "Two pair"
	elif len(counts.keys()) == 4:
		if max_v == 2:
			return 2 # "One pair"
	elif len(counts.keys()) == 5:
		return 1 # "High card"


def get_hand_type_joker(hand):
	if hand == "JJJJJ":
		return 7 # "Five of a kind"
	counts = Counter(hand.replace("J", ''))
	most_common = counts.most_common(1)[0][0]
	return get_hand_type(hand.replace("J", most_common))
	

def get_card_strength(card):
	_map = {all_cards[i]: len(all_cards) + 1 - i for i in range(len(all_cards))}
	return _map[card]


def compare_hands(hand1, hand2):
	hand1_type = get_hand_type(hand1[0])
	hand2_type = get_hand_type(hand2[0])
	if hand1_type < hand2_type:
		return -1
	elif hand1_type > hand2_type:
		return 1
	else:
		for c1, c2 in zip(hand1[0], hand2[0]):
			c1_strength = get_card_strength(c1)
			c2_strength = get_card_strength(c2)
			if c1_strength < c2_strength:
				return -1
			elif c1_strength > c2_strength:
				return 1
	return None


def compare_hands_joker(hand1, hand2):
	hand1_type = get_hand_type_joker(hand1[0])
	hand2_type = get_hand_type_joker(hand2[0])
	if hand1_type < hand2_type:
		return -1
	elif hand1_type > hand2_type:
		return 1
	else:
		for c1, c2 in zip(hand1[0], hand2[0]):
			c1_strength = get_card_strength(c1)
			c2_strength = get_card_strength(c2)
			if c1_strength < c2_strength:
				return -1
			elif c1_strength > c2_strength:
				return 1
	return None


def p1(filename):
	hands_bids = []
	with open(filename) as f:
		for line in f:
			hand, bid = line.strip().split(" ")
			hands_bids.append([hand, int(bid)])
	hands_bids.sort(key=cmp_to_key(compare_hands))
	res = 0
	for i, hand in enumerate(hands_bids):
		res += (i + 1) * hand[1]
	return res


def p2(filename):
	hands_bids = []
	with open(filename) as f:
		for line in f:
			hand, bid = line.strip().split(" ")
			hands_bids.append([hand, int(bid)])
	hands_bids.sort(key=cmp_to_key(compare_hands_joker))
	res = 0
	for i, hand in enumerate(hands_bids):
		res += (i + 1) * hand[1]
	return res


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")