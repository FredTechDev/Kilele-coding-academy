
import random
import time
import os


# ==========================================
# 1. GAME SETTINGS
# ==========================================

STARTING_BALANCE = 100
FINISH_LINE = 35
MINIMUM_AGE = 8

HORSES = {
    1: "THUNDER",
    2: "LIGHTNING",
    3: "SHADOW"
}


# ==========================================
# 2. SCREEN MANAGEMENT
# ==========================================

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


def pause(seconds=1):

    time.sleep(seconds)


# ==========================================
# 3. INPUT VALIDATION
# ==========================================

def get_number(prompt, minimum, maximum):

    while True:

        try:

            number = int(input(prompt))

            if minimum <= number <= maximum:

                return number

            else:

                print(
                    "Enter a number between",
                    minimum,
                    "and",
                    maximum
                )

        except ValueError:

            print("Invalid input. Enter a whole number.")


# ==========================================
# 4. WELCOME AND AGE VERIFICATION
# ==========================================

def welcome():

    clear_screen()

    print("=" * 45)
    print("          HORSE RACING CHALLENGE")
    print("=" * 45)

    name = input("Enter your name: ").strip()

    if name == "":

        name = "Racer"

    return name


def check_age():

    age = get_number("Enter your age: ", 1, 120)

    if age < MINIMUM_AGE:

        print("Sorry! You must be at least 8 years old.")

        return False

    elif age <= 12:

        print("Welcome, Young Racer!")

    elif age <= 17:

        print("Welcome, Junior Champion!")

    else:

        print("Welcome, Senior Racer!")

    return True


# ==========================================
# 5. HORSE SELECTION
# ==========================================

def select_horse():

    print("\nAVAILABLE HORSES")

    for number, name in HORSES.items():

        print(number, "-", name)

    choice = get_number(
        "\nChoose your horse (1-3): ",
        1,
        3
    )

    selected_horse = HORSES[choice]

    print("\nYou selected:", selected_horse)

    return selected_horse


# ==========================================
# 6. BETTING SYSTEM
# ==========================================

def place_bet(balance):

    print("\nYOUR CURRENT BALANCE: KSh", balance)

    bet = get_number(
        "Enter your bet amount: KSh ",
        1,
        balance
    )

    print("\nBET CONFIRMED!")

    print("Your bet: KSh", bet)

    print("Your selected horse is:", end=" ")

    return bet


# ==========================================
# 7. HORSE MOVEMENT
# ==========================================

def move_horse(position):

    movement = random.randint(1, 4)

    position = position + movement

    return position


# ==========================================
# 8. DISPLAY RACE TRACK
# ==========================================

def display_race(positions):

    clear_screen()

    print("=" * 55)
    print("                 LIVE HORSE RACE")
    print("=" * 55)

    for horse, position in positions.items():

        distance = min(position, FINISH_LINE)

        track = "." * distance

        print(
            horse.ljust(12),
            "|",
            track,
            "🐎"
        )

    print("-" * 55)

    print("FINISH LINE:", FINISH_LINE)

    print("=" * 55)


# ==========================================
# 9. COUNTDOWN
# ==========================================

def countdown():

    clear_screen()

    print("\nTHE RACE IS ABOUT TO BEGIN!")

    for number in range(3, 0, -1):

        print(number)

        pause(1)

    print("\nGOOOOO!")

    pause(1)


# ==========================================
# 10. RUN THE RACE
# ==========================================

def start_race():

    positions = {
        "THUNDER": 0,
        "LIGHTNING": 0,
        "SHADOW": 0
    }

    winner = None

    countdown()

    while winner is None:

        # Randomise which horse moves first.
        horses = list(positions.keys())

        random.shuffle(horses)

        # Give each horse one movement turn.
        for horse in horses:

            positions[horse] = move_horse(
                positions[horse]
            )

            display_race(positions)

            pause(0.4)

            # First horse to cross the finish line wins.
            if positions[horse] >= FINISH_LINE:

                winner = horse

                break

    print("\n" + "=" * 55)

    print("🏆 THE WINNER IS:", winner, "🏆")

    print("=" * 55)

    pause(2)

    return winner


# ==========================================
# 11. SETTLE THE BET
# ==========================================

def settle_bet(
    player_name,
    selected_horse,
    winner,
    bet,
    balance
):

    print("\n========== RACE RESULTS ==========")

    print("Player:", player_name)

    print("Your horse:", selected_horse)

    print("Winning horse:", winner)

    if selected_horse == winner:

        payout = bet * 2

        balance = balance + payout

        print("\nCONGRATULATIONS!")

        print("Your horse won!")

        print("Your payout: KSh", payout)

    else:

        print("\nBETTER LUCK NEXT TIME!")

        print("Your horse did not win.")

        print("You lost KSh", bet)

    print("\nNEW BALANCE: KSh", balance)

    print("==================================")

    return balance


# ==========================================
# 12. MAIN GAME
# ==========================================

def main():

    player_name = welcome()

    eligible = check_age()

    if not eligible:

        print("Game access denied.")

        return

    balance = STARTING_BALANCE

    race_count = 0

    wins = 0

    print("\nWelcome to the racing arena,", player_name)

    print("Starting game credits: KSh", balance)

    print("\nThese are fictional classroom credits only.")

    pause(2)

    playing = True

    while playing and balance > 0:

        clear_screen()

        print("=" * 45)

        print("NEW RACE")

        print("Current balance: KSh", balance)

        print("=" * 45)

        # Choose a horse.
        selected_horse = select_horse()

        # Place a bet.
        bet = place_bet(balance)

        print(selected_horse)

        # Deduct the bet before the race.
        balance = balance - bet

        print("\nAll horses are preparing...")

        pause(2)

        # Start the actual race.
        winner = start_race()

        race_count = race_count + 1

        # Check whether the player's horse won.
        if selected_horse == winner:

            wins = wins + 1

        # Settle the bet.
        balance = settle_bet(
            player_name,
            selected_horse,
            winner,
            bet,
            balance
        )

        print("\nRACES PLAYED:", race_count)

        print("RACES WON:", wins)

        # Check remaining credits.
        if balance <= 0:

            print("\nYou have run out of game credits.")

            playing = False

        else:

            replay = input(
                "\nWould you like another race? (yes/no): "
            )

            if replay.strip().lower() != "yes":

                playing = False

    # ======================================
    # FINAL RESULTS
    # ======================================

    clear_screen()

    print("=" * 45)

    print("         FINAL GAME RESULTS")

    print("=" * 45)

    print("Player:", player_name)

    print("Races played:", race_count)

    print("Races won:", wins)

    print("Final balance: KSh", balance)

    print("=" * 45)

    print("THANK YOU FOR PLAYING!")


# ==========================================
# 13. START THE GAME
# ==========================================

if __name__ == "__main__":

    main()
