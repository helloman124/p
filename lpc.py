import random
group=["Heatrs","Diamond","Club","Spade"]
deck=['Ace',2,3,4,5,6,7,8,9,10,"King","Queen","Jack"]
cards=[str(r)+" of "+f for f in group for r in deck]
shuffled_cards=random.shuffle(cards)
random_card=random.choice(cards)
random_sample=random.sample(cards,2)
print("Shuffled cards: \n",cards)
print()
print("\nRandom card: ",random_card)
print()
print("\nRandom sample of 2: ",random_sample)
