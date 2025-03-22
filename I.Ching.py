import allFunctions
import os
import textwrap

class IChing:
    def __init__(self):
        self.hexagrams = self.load_hexagrams()
        
    def load_hexagrams(self):
        """Load all 64 hexagrams with their names and basic meanings"""
        hexagram_data = {
            1: {"name": "Qián (The Creative)", "meaning": "Action: Initiate. Embodies the active principle in the universe and represents initiating action. An opportunity for expansion and authentic empowerment emerges which requires assertiveness and persistence."},
            2: {"name": "K'un (The Receptive)", "meaning": "Action: Reflect. Calls for a period of patience and reflection. Where you may have been reactive in the past, it is time to learn how to be more responsive."},
            3: {"name": "Chun (Difficult Beginnings)", "meaning": "Action: Persevere. New endeavors face obstacles, refining sincerity and vision. Push through challenges to manifest your dream."},
            64: {"name": "Wei Chi (Before Completion)", "meaning": "Before completion. The end is in sight but not yet achieved. Final efforts required for success."}
        }
        
        # Hexagram 1
        hexagram_data[1]["full_interpretation"] = """
ián (The Creative) embodies the active principle and initiating action, symbolized by the Dragon, a benevolent, powerful figure in China.

This hexagram highlights creativity, urging you to tap your inner vision. Dormant empowerment or assertiveness can lead to giving power away, fueling the ego’s fear and self-gratification.

Suppressed energy feeds the Shadow in dreams, a source of authentic power we project onto others until reclaimed.

An opportunity for expansion and authentic empowerment emerges which requires assertiveness and persistence. If you currently feel held back or victimized, remove the shackles because they are merely self limiting beliefs.

Initiative is required to succeed, although it is important to move in sync with the time and respond with openness. The Creative is duplicated, and in the hidden influence position and underscores the idea of initiating something.

The Receptive as the underlying cause or opposite condition shows that a period of reflection and retreat must give way to active expression. A new burst of inspiration has gestated and you can now bring it life.

There is great potential waiting for you to tap it. Take a chance and go for it!
        """
        
        # Hexagram 1 lines
        hexagram_data[1]["lines"] = {
            1: "Hidden Dragon = do not act. The timing is inappropriate for action. Have patience so your plan can develop further, avoiding negative repercussions.",
            2: "Dragon in the Field = get helpers. Develop your talent and explore networking ideas. Establish a plan of action and incorporate the feedback and/or skills of others.",
            3: "All day all night = powerful but does not threaten. The power to succeed is rising although tread carefully, knowing that new ideas can bring about opposition.",
            4: "Dragon leaping over pond = attempting to fly but safe. Your plan of action is ready for implementation and yet you may need to play it safe.",
            5: "Dragon flying in sky = realizing ambition. Due to connections and confidence, all lights are green and your success is assured.",
            6: "Haughty Dragon = acts without support, cause to repent. Success needs no aggression and pomp. Remove doubt and insecurity to ensure completion in your efforts."
        }
        
        # Hexagram 1 changes
        hexagram_data[1]["changes"] = {
            1: 44,
            2: 13,
            3: 10,
            4: 9,
            5: 14,
            6: 43
        }
        
        # Hexagram 2
        hexagram_data[2]["full_interpretation"] = """
K'un (The Receptive) calls for patience and reflection, urging you to shift from reaction to responsiveness. Reaction defends the past; responsiveness opens you to the present.

This hexagram, composed of all Yin lines, embodies a fertile field ready for gestation. It's time to turn inward, like winter preparing for spring, and cultivate your inner world.

The Creative as the underlying cause suggests a shift from action to stillness. Growth requires both outward effort and inner renewal, each influencing the other.

Be a witness to life, removing judgment to see how it speaks to you. Yielding and serving others can reveal your greater capabilities.

The Receptive holds the energy of attraction. Plant your intention, stay patient, and let circumstances guide you. Strength lies in stillness—observe, don't react.
        """
        
        # Hexagram 2 lines
        hexagram_data[2]["lines"] = {
            1: "Treading on hoarfrost, surely turns to ice = each step solidifies your decision. It is important to follow your inner drummer but realize that some decisions cannot be undone. Once you take this step, there may be no going back. You may have to go against another's wishes to take the path you feel is right for you. However, you may Return to face the consequences of your impulsiveness. Observe cycles in nature because if it looks like winter is coming, it probably is. You may have to contend with another's coldness in response to your actions.",
            2: "Straight through the unfamiliar = speak your heart, it is not a disadvantage. Everything unfolds naturally because it feels right and others recognize the value in following your initiative. Your open and honest invitation comes from the heart and is straight to the point. Any illusions or misconceptions are clarified. The situation has elements that you haven't dealt with before but being truthful can help gain allegiance to your cause. Move forward like a soldier of the heart, unafraid of what you encounter.",
            3: "Keeping the story to yourself = relying on another's completion of matters. Acting humbly and working hard allows you to complete the job. You may need to work quietly for the benefit of another without seeking credit. Or, you may need to allow another to complete something prior to moving forward. Eventually success is ensured because you put quality work and integrity above your need for recognition. Authenticity can only develop through interdependency not dependency.",
            4: "Enclosing in a sack = no improvement because one remains closed. Awareness may be too narrow or being fearful, you miss out on the joy of discovery. You may be hesitant about entering a situation where you will gain benefit. There is no reason not to trust events and invitations. Your own attitude and outlook are diminishing the opportunity for joy and fulfillment. Open to the mystery of life without the need to classify the outcome.",
            5: "A yellow lower garment = modest and ordinary so all goes well. Dreams and meditation allow you to tap into a higher sense of awareness. It may seem that ego is here to discover spirit, but witnessing life as spirit is just a shift in perception, an awakening that will connect you to the here and now. Ego understands time as limitation but spirit has a timeless and unbiased outlook. Union suggests two manifestations of one thing, like matter and energy, although nothing is separate. When in doubt about your nature, remember who you were as a child. What is unchanging about you? Be that. Find a way to give it expression to your field of dreams.",
            6: "Dragons fight in the field, their blood is old = fighting for a long time in an incapacitating situation. The difference between having a response and having a reaction is the ability to listen and not defend your beliefs. Sometimes people defend each other's differences rather than identify their similarities. The opportunity for renewal in the situation requires a blending of opposite qualities into a higher order. The symbol of 3 in dreams is how an either/or outlook blends to allow for all possibilities. If you want to discover the other person's value, learn to listen to them. However, there is a limit to what can be done in this situation because the negativity has festered for some time."
        }
        
        # Hexagram 2 changes
        hexagram_data[2]["changes"] = {
            1: 24,
            2: 7,
            3: 15,
            4: 16,
            5: 8,
            6: 23
        }
        
        # Hexagram 3
        hexagram_data[3]["full_interpretation"] = """
Chun (Difficult Beginnings) reflects a seedling pushing through soil and rocks to grow. New endeavors face obstacles that refine your sincerity and vision.

Born from the Creative and Receptive, Chun embodies opposing energies birthing something new. It's a challenging yet destined start, like a commitment turning attraction into effort.

Obstacles are evolution's friction—don't blame them, embrace them. Tao sharpens deficiencies into skills, with interdependency key to success.

The hidden influence, Split Apart, breaks old thinking, while the Cauldron refines your capabilities. Persevere through uncertainty to manifest your dream.

See challenges as teachers, not barriers. A rock stabilizes a seedling; adversity strengthens you. Fear projects barriers—release it to find power.

There are no true adversaries, only opportunities. Trust your inner direction, push forward fearlessly, and let difficulties shape your path to greatness.
        """
        
        # Hexagram 3 lines
        hexagram_data[3]["lines"] = {
            1: "Insurmountable obstacle, conserve and build strength = seek advice. An obstacle appears that seems insurmountable like stone, but there is someone who is able to help you. Your path is correct and you are offered support by a reliable person who won't let you down. In this line we learn the value of relationships.",
            2: "The wagon and horses are separated. It is not a robbery, but a wooing = commitment makes anything possible. Limitations are the breeding ground for nature's strengths. A period of waiting has to occur to test your resolve and allow you to discover a sense of commitment. Rather than change course, stay with what you have built. The power of commitment is like gravity and is unaffected by obstacles or time. If you know you want it then make a commitment to 'woo' it. In this line we see how the excited energy of opposing forces feels like a robbery, but has 'joining together' as its purpose.",
            3: "Hunting deer without knowing the way = resist acting without foresight or experience. Although a special opportunity has appeared, it is not wise to pursue it blindly because of the danger it presents. You do not have the experience or knowledge to make it work in your favor. Going forward leads to endings and humiliation. Complete a course of study or seek advice prior to moving forward.",
            4: "The wagon and horses are separated, you are cut off from something essential = striving for union. While following another, you may have become trapped. They may have followed you and feel trapped. The attraction is strong, but gaining union requires that you demonstrate your sincerity. Look at the situation more closely to understand what you are offering another and their intentions in accepting. Pursue the path that leads to fulfillment. Don't accept less than complete satisfaction. What you think you 'need' externally is actually found within.",
            5: "Difficulties that fertilize = move forward delicately. While you may have left the situation, returning is acceptable and is well received. The realization that comes from making a mistake actually improves the situation. The obstacle allowed you to connect with sincerity. It is still important to tread delicately.",
            6: "The wagon and horses are separated, an impasse is reached = brings great sadness and frustration in bloody tears. While a door appears to close or an impasse emerges, know that opportunity for greater fulfillment is still possible. Perhaps the first approach to the situation was just too hard or unworkable. Increase is a message about taking your game to a different level through a win/win solution. Crying won't get you anywhere. Don't allow failure to keep you from pursuing new opportunities or new approaches."
        }
        
        # Hexagram 3 changes
        hexagram_data[3]["changes"] = {
            1: 8,
            2: 60,
            3: 63,
            4: 17,
            5: 24,
            6: 42
        }
        
        return hexagram_data

    def create_hexagram(self):
        """Create a hexagram by throwing coins six times"""
        tosses = []
        coin_results = []
        
        for i in range(6):
            coin_result = allFunctions.throwThreeCoins()  # Use function from allFunctions.py
            coin_results.append(coin_result)
            sum_value = allFunctions.sumResults(coin_result)  # Use function from allFunctions.py
            line_type = allFunctions.classifyToss(sum_value)  # Use function from allFunctions.py
            
            # Create a dictionary for the line based on the classification
            line_dict = self.create_line_dict(line_type)
            tosses.append(line_dict)
        
        return tosses, coin_results
    
    def create_line_dict(self, line_type):
        """Convert line type string to a dictionary with all required properties"""
        if line_type == "changing_yin":
            return {"value": "changing_yin", "binary": 0, "changing": True, "display": "---   --- (changing to solid)"}
        elif line_type == "static_yang":
            return {"value": "static_yang", "binary": 1, "changing": False, "display": "---------"}
        elif line_type == "static_yin":
            return {"value": "static_yin", "binary": 0, "changing": False, "display": "---   ---"}
        elif line_type == "changing_yang":
            return {"value": "changing_yang", "binary": 1, "changing": True, "display": "--------- (changing to broken)"}

    def get_hexagram_number(self, tosses):
        """Convert the hexagram lines to a number (1-64)"""
        binary_code = ""
        for line in tosses:
            binary_code = str(line["binary"]) + binary_code  # Bottom line first
        
        hexagram_number = int(binary_code, 2) + 1
        return hexagram_number

    def get_derived_hexagram(self, tosses):
        """Create the derived hexagram by changing any changing lines"""
        derived_tosses = []
        has_changes = False
        
        for line in tosses:
            if line["changing"]:
                has_changes = True
                # Flip the line
                if line["value"] == "changing_yin":  # Broken line changing to solid
                    derived_tosses.append({
                        "value": "static_yang", 
                        "binary": 1, 
                        "changing": False, 
                        "display": "---------"
                    })
                else:  # Solid line changing to broken
                    derived_tosses.append({
                        "value": "static_yin", 
                        "binary": 0, 
                        "changing": False, 
                        "display": "---   ---"
                    })
            else:
                # Keep the line the same
                derived_tosses.append(line)
        
        if has_changes:
            return derived_tosses
        else:
            return None

    def display_hexagram(self, tosses, title):
        """Display the hexagram visually"""
        print(f"\n{title}:")
        for i, line in enumerate(reversed(tosses)):  # Display from top to bottom
            line_num = 6 - i  # Line number (6 at top, 1 at bottom)
            print(f"{line_num}: {line['display']}")

    def detect_changing_lines(self, tosses):
        """Detect which lines are changing"""
        changing_lines = []
        for i, line in enumerate(tosses):
            if line["changing"]:
                changing_lines.append(i + 1)  # Line positions are 1-based
        
        return changing_lines

    def interpret_hexagram(self, hexagram_number, changing_lines=None):
        """Provide an interpretation of the hexagram"""
        if hexagram_number in self.hexagrams:
            hexagram = self.hexagrams[hexagram_number]
            interpretation = f"\nHexagram {hexagram_number}: {hexagram['name']}\n"
            interpretation += "-" * 60 + "\n"
            interpretation += textwrap.fill(hexagram['meaning'], width=80) + "\n"
            
            # Add full interpretation if available
            if "full_interpretation" in hexagram:
                interpretation += "\nFULL INTERPRETATION:\n" + "-" * 60 + "\n"
                interpretation += textwrap.fill(hexagram['full_interpretation'], width=80) + "\n"
            
            # Add changing line interpretations if available
            if changing_lines and "lines" in hexagram:
                interpretation += "\nCHANGING LINES:\n" + "-" * 60 + "\n"
                for line in changing_lines:
                    if line in hexagram["lines"]:
                        interpretation += f"Line {line}: {hexagram['lines'][line]}\n"
            
            return interpretation
        else:
            return f"\nHexagram {hexagram_number} interpretation not found in database."

    def run(self):
        """Run the I Ching oracle"""
        self.clear_screen()
        print("THE I CHING ORACLE - DISCOVER WHAT THE FUTURE HOLDS FOR YOU")
        print("-" * 60)
        print("Choose an option to begin:")
        print("\ta) EXPLANATION: What is the I Ching?")
        print("\tb) ORACLE: See what the future holds for me.")
        
        option = input(">>> ").lower().strip()
        
        while option not in ['a', 'b']:
            print("ERROR: The selected option is not valid.")
            print("Choose an option to begin:")
            print("\ta) EXPLANATION: What is the I Ching?")
            print("\tb) ORACLE: See what the future holds for me.")
            option = input(">>> ").lower().strip()
        
        if option == 'a':
            self.show_explanation()
            input("\nPress Enter to continue to the oracle...")
            self.clear_screen()
            self.perform_reading()
        else:
            self.clear_screen()
            self.perform_reading()

    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_explanation(self):
        """Show an explanation of the I Ching"""
        explanation = """
The I Ching oracle, also known as the Book of Changes, is a classic Chinese text used for divination and spiritual guidance.

It consists of a system of 64 hexagrams, each formed by combinations of six lines (solid or broken) that represent different states of change and dynamics in life. It is consulted by tossing coins or yarrow stalks to build a hexagram, which is interpreted through the book, offering wisdom on how to face a situation or make decisions.

The I Ching emphasizes harmony with the laws of natural change and adaptability. Rather than predicting the future, it guides in the present with philosophical and ethical teachings.

The solid lines (—) represent yang energy: active, masculine, creative.
The broken lines (– –) represent yin energy: receptive, feminine, nurturing.

Each line can be either stable or changing. Changing lines indicate a transformation occurring, and create a second hexagram that shows where the situation is heading.

When using the three-coin method:
- 3 heads (3+3+3=9): Changing yang (solid becoming broken)
- 2 heads, 1 tail (3+3+2=8): Stable yin (broken)
- 1 head, 2 tails (3+2+2=7): Stable yang (solid)
- 3 tails (2+2+2=6): Changing yin (broken becoming solid)

The philosophy behind the I Ching is based on the concept that everything is in flux, and understanding these patterns of change can help us navigate life more harmoniously.
        """
        print(textwrap.fill(explanation, width=80))

    def perform_reading(self):
        """Perform an I Ching reading"""
        print("ORACLE: Before casting the I Ching, focus on your question or situation.")
        input("When you are ready, press Enter to continue...")
        
        print("\nFocusing on your question, take a deep breath...")
        input("Press Enter to cast the I Ching...")
        
        print("\nPROCEEDING TO READ YOUR ORACLE...")
        tosses, coin_results = self.create_hexagram()
        
        # Display the coin results for transparency
        print("\nCOIN RESULTS:")
        for i, coins in enumerate(coin_results):
            total = sum(coins)
            print(f"Line {i+1}: {coins} = {total} -> {tosses[i]['value']}")
        
        # Get the hexagram number
        hexagram_number = self.get_hexagram_number(tosses)
        
        # Display the hexagram
        self.display_hexagram(tosses, "YOUR HEXAGRAM")
        
        # Check for changing lines
        changing_lines = self.detect_changing_lines(tosses)
        if changing_lines:
            print(f"\nChanging lines at positions: {', '.join(map(str, changing_lines))}")
            
            # Create the derived hexagram
            derived_tosses = self.get_derived_hexagram(tosses)
            
            # Display the derived hexagram
            self.display_hexagram(derived_tosses, "YOUR DERIVED HEXAGRAM (after changes)")
            
            # Get the derived hexagram number
            derived_number = self.get_hexagram_number(derived_tosses)
            
            print(f"\nYour hexagram is {hexagram_number}, changing to {derived_number}")
            
            # Interpret both hexagrams
            print(self.interpret_hexagram(hexagram_number, changing_lines))
            print(f"\nAFTER TRANSFORMATION - Your situation is moving toward:")
            print(self.interpret_hexagram(derived_number))
        else:
            print(f"\nYour hexagram is {hexagram_number} (no changing lines)")
            print(self.interpret_hexagram(hexagram_number))
        
        print("\nRemember that the I Ching is a tool for reflection, not a deterministic prediction.")
        print("Consider how these symbols and their meanings might apply to your current situation.")

if __name__ == "__main__":
    oracle = IChing()
    oracle.run()
