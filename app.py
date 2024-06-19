from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_required_monsters(total_cards):
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    hand_cards = int(request.form['hand_cards'])
    field_cards = int(request.form['field_cards'])
    opponent_monster_level_rank = int(request.form['opponent_monster_level_rank'])

    total_cards = hand_cards + field_cards
    possible_combinations = calculate_required_monsters(total_cards)
    matching_combinations = find_matching_return_monsters(opponent_monster_level_rank, possible_combinations)

    if matching_combinations:
        return jsonify({
            "message": "Effect can be activated!",
            "combinations": matching_combinations
        })
    else:
        return jsonify({
            "message": "No valid combination of Fusion and Xyz Monsters found to activate the effect."
        })

if __name__ == '__main__':
    app.run(debug=True)
