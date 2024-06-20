from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

def calculate_required_monsters(total_cards):
    possible_combinations = []
    for fusion_level in range(1, total_cards):
        remaining = total_cards - fusion_level
        rank = remaining // 2
        if remaining % 2 == 0 and rank > 0 and fusion_level + rank <= 12:
            possible_combinations.append((fusion_level, rank, rank))
            if len(possible_combinations) >= 10:
                return possible_combinations
    return possible_combinations

def find_matching_return_monsters(opponent_monster_level_rank, possible_combinations):
    matching_combinations = []
    for fusion_level, rank1, rank2 in possible_combinations:
        if fusion_level + rank1 == opponent_monster_level_rank:
            matching_combinations.append((fusion_level, rank1, rank2))
            if len(matching_combinations) >= 10:
                return matching_combinations
    return matching_combinations

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    cards_on_play = int(request.form['cards_on_play'])
    opponent_monster_level_rank = int(request.form['opponent_monster_level_rank'])

    total_cards = cards_on_play
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
