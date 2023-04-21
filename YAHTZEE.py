import random

def Reroll(dice):
    reroll = list(map(int, input('Which dice do you want to reroll').split()))
    
    for i in range(len(reroll)):
        reroll[i] = reroll[i] - 1

    for index in reroll:
        dice[index] = random.randint(1, 6)

def Same_kind(dice):
    freq = {}
    for i in dice:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def Check_full_house(dice):
    freq = Same_kind(dice)
    for key, value in freq.items():
        if value == 3:
            for key, value in freq.items():
                if value == 2:
                    return True
    return False

def Check_small_straight(dice):
    rolls = dice
    rolls = set(rolls)
    rolls = list(rolls)
    rolls.sort
    if len(rolls) > 3:
        for i in range(len(rolls)):
            if i < len(rolls) - 1 and (rolls[i]+ 1 != rolls[i + 1]):
                return False
        return True
    return False

def Check_large_straight(dice):
	rolls = dice
	rolls = set(dice)
	rolls = list(rolls)
	rolls.sort
	if len(rolls) > 4:
		for i in range(len(rolls)):
			if i < len(rolls) - 1 and (rolls[i]+ 1 != rolls[i + 1]):
				return False
		return True
	return False

score_list = []
lower_score = []
upper_score = []
chance = c = 0
'''flag = f = 0    
score = 0
'''
''' box -> 7-Three of a kind, 8-Four of a kind, 9-Full house, 10-Small straight, 11-Large straight, 12-Yatzee, 13-Chance '''
for i in range(13):
    flag = f = 0
    chance = want_reroll = 0
    score = 0
    dice = []
    for d in range(5):
        dice.append(random.randint(1,6))

    print("you rolled: ",dice)
    reroll = 1
    while reroll < 4:
        if Check_full_house(dice) and (9 not in score_list):
            print("Full house! Please type 'Yes' if you want to take it")
            if input() == "Yes":
                flag = 1
                chance = want_reroll = 1
                lower_score.append(25)
                score_list.append(9)
            
        freq = Same_kind(dice)
        for key, value in freq.items():
            if value == 4 and (8 not in score_list):
                print("Four of a kind! Please type 'Yes' if you want to take it")
                if input() == "Yes":
                    chance = want_reroll = 1
                    lower_score.append(sum(dice))
                    score_list.append(8)
               
            if value == 3 and (7 not in score_list):
                if flag == 0:
                    print("Three of a kind! Please type 'Yes' if you want to take it")
                    if input() == "Yes":
                        chance = want_reroll = 1
                        lower_score.append(sum(dice))
                        score_list.append(7)
    
            if value == 5 and (12 not in score_list):
                print("YAHTZEE! Please type 'Yes' if you want to take it")
                if input() == "Yes":
                    chance = want_reroll = 1
                    lower_score.append(50)
                    score_list.append(12)
                
        if Check_large_straight(dice) and (11 not in score_list):
            print("Large Straight! Please type 'Yes' if you want to take it")
            if input() == "Yes":
                f = 1
                chance = want_reroll = 1
                lower_score.append(40)
                score_list.append(11)

        if Check_small_straight(dice) and (10 not in score_list):
            if f == 0:
                print("small Straight! Please type 'Yes' if you want to take it")
                if input() == "Yes":
                    chance = want_reroll = 1
                    lower_score.append(30)
                    score_list.append(10)
        
        if chance == 0 and c == 0:
            print('''If you want to take a 'Chance' type "Yes"''')
            if input() == "Yes" and (13 not in score_list):
                chance = want_reroll = c = 1
                lower_score.append(sum(dice))
                score_list.append(13)

        if reroll < 3 and want_reroll == 0:
            print("If you want to reroll please type 'Yes'")
            if input() == "Yes":
                Reroll(dice)
            #reroll += 1
                print(reroll)
                print("you rolled: ",dice)    
            else:
                break
        reroll += 1
    if chance == 0:
        print("If you want to take a number type 'Yes'")
        if input() == "Yes":
            score = 0
            scoring_number = int(input("What number do you select"))
            score_list.append(scoring_number)
            for d in dice:
                if d == scoring_number:
                    score += d
            upper_score.append(score)
        
    print("Completed round", i + 1)
    print("\n")


if sum(upper_score) >= 63:
    upper_score.append(35)
'''
print(upper_score)
print(lower_score)
'''
u_s = sum(upper_score)
l_s = sum(lower_score)
'''
print(u_s)
print(l_s)
'''
Total_score = u_s + l_s
print(Total_score)

