def calculate_required_monsters(total_cards):
    # This function calculates possible Fusion and Xyz Monster levels/ranks that can be used
    possible_combinations = []
    for fusion_level in range(1, total_cards):
        remaining = total_cards - fusion_level
        for rank1 in range(1, remaining):
            rank2 = remaining - rank1
            if rank1 > 0 and rank2 > 0:
                possible_combinations.append((fusion_level, rank1, rank2))
                if len(possible_combinations) >= 10:
                    return possible_combinations
    return possible_combinations

def find_matching_return_monsters(opponent_monster_level_rank, possible_combinations):
    matching_combinations = []
    for fusion_level, rank1, rank2 in possible_combinations:
        if (fusion_level + rank1 == opponent_monster_level_rank or 
            fusion_level + rank2 == opponent_monster_level_rank):
            matching_combinations.append((fusion_level, rank1, rank2))
            if len(matching_combinations) >= 10:
                return matching_combinations
    return matching_combinations

# Get inputs from the user
hand_cards = int(input("Enter the number of cards in your hand: "))
field_cards = int(input("Enter the number of cards on the field (both players): "))
opponent_monster_level_rank = int(input("Enter the level or rank of the opponent's face-up monster: "))

total_cards = hand_cards + field_cards

# Calculate required monsters to banish all cards
possible_combinations = calculate_required_monsters(total_cards)

# Check if there is a combination that allows the effect to be activated
matching_combinations = find_matching_return_monsters(opponent_monster_level_rank, possible_combinations)

if matching_combinations:
    print("Effect can be activated!")
    print(f"To banish all your opponent's cards, use one of the following combinations of monsters:")
    for idx, (fusion_level, rank1, rank2) in enumerate(matching_combinations, start=1):
        print(f"Combination {idx}: Fusion Monster (Level {fusion_level}), Xyz Monsters (Rank {rank1} and Rank {rank2})")
else:
    print("No valid combination of Fusion and Xyz Monsters found to activate the effect.")
