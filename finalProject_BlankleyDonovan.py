# Final Project
# 5-12-2026
# Donovan Blankley
# This is a UFC moshpit/Free For All game between 5 of my favorite UFC fighters in the 155lbs division

import random
import time

#Fighter list with attributes. Each player's attributes adds up t 300
fighters = {
    "Conor": {"stamina": 80, "striking": 140, "grappling": 80},
    "Khabib": {"stamina": 110, "striking": 60, "grappling": 130},
    "Ilia": {"stamina": 90, "striking": 105, "grappling": 105},
    "Charles": {"stamina": 110, "striking": 90, "grappling": 100},
    "Arman": {"stamina": 100, "striking": 100, "grappling": 100}
}

# -------------------------------
# DISPLAY FUNCTIONS
# -------------------------------

def display_fighters():
    """Display all available fighters."""
    print("\n===== AVAILABLE FIGHTERS =====")

    for fighter in fighters:
        if not is_eliminated(fighter):
            print(f"- {fighter}")

    print()


def display_stats():
    """Display stats for all fighters."""
    print("\n========== FIGHTER STATS ==========")

    for fighter, stats in fighters.items():
        status = "ELIMINATED" if is_eliminated(fighter) else "ACTIVE"

        print(f"\n{fighter} ({status})")
        print(f"Stamina:   {stats['stamina']}")
        print(f"Striking:  {stats['striking']}")
        print(f"Grappling: {stats['grappling']}")

    print("\n===================================")


# -------------------------------
# ATTACK FUNCTIONS
# -------------------------------

def strike_attack(attacker, defender):
    """
    Strike attack:
    - Reduce defender striking by 10
    - Reduce attacker stamina by 5
    """

    print(f"\n{attacker} throws a STRIKE at {defender}!")

    fighters[defender]["striking"] -= 10
    fighters[attacker]["stamina"] -= 5

    time.sleep(1)

    print(f"{defender}'s striking reduced by 10!")
    print(f"{attacker}'s stamina reduced by 5!")


def grapple_attack(attacker, defender):
    """
    Grappling attack:
    - Reduce defender grappling by 25
    - Reduce attacker stamina by 15
    """

    print(f"\n{attacker} attempts a GRAPPLE on {defender}!")

    fighters[defender]["grappling"] -= 25
    fighters[attacker]["stamina"] -= 15

    time.sleep(1)

    print(f"{defender}'s grappling reduced by 25!")
    print(f"{attacker}'s stamina reduced by 15!")


# -------------------------------
# ELIMINATION FUNCTIONS
# -------------------------------

def is_eliminated(fighter):
    """
    A fighter is eliminated if any stat is 0 or below.
    """

    stats = fighters[fighter]

    if (
        stats["stamina"] <= 0 or
        stats["striking"] <= 0 or
        stats["grappling"] <= 0
    ):
        return True

    return False


# -------------------------------
# AI FUNCTION
# -------------------------------

def opponent_ai(attacker, defender):
    """
    Randomly chooses strike or grapple attack.
    """

    if is_eliminated(attacker) or is_eliminated(defender):
        return

    print(f"\n{attacker} is preparing a counterattack...")
    time.sleep(1)

    attack_choice = random.randint(1, 2)

    if attack_choice == 1:
        strike_attack(attacker, defender)
    else:
        grapple_attack(attacker, defender)


# -------------------------------
# PLAYER INPUT FUNCTIONS
# -------------------------------

def choose_fighter(prompt):
    """Allow user to choose an active fighter."""

    while True:
        fighter = input(prompt)

        if fighter not in fighters:
            print("Invalid fighter name.")
        elif is_eliminated(fighter):
            print("That fighter has been eliminated.")
        else:
            return fighter


def choose_attack():
    """Allow player to choose attack type."""

    while True:
        print("\nChoose attack:")
        print("1. Strike Attack")
        print("2. Grapple Attack")

        choice = input("Enter choice: ")

        if choice == "1":
            return "strike"
        elif choice == "2":
            return "grapple"
        else:
            print("Invalid choice.")

def display_fight_stats(fighter1, fighter2):

    print("\n========== CURRENT FIGHT STATS ==========")

    print(f"\n{fighter1}")
    print(f"Stamina:   {fighters[fighter1]['stamina']}")
    print(f"Striking:  {fighters[fighter1]['striking']}")
    print(f"Grappling: {fighters[fighter1]['grappling']}")

    print(f"\n{fighter2}")
    print(f"Stamina:   {fighters[fighter2]['stamina']}")
    print(f"Striking:  {fighters[fighter2]['striking']}")
    print(f"Grappling: {fighters[fighter2]['grappling']}")

    print("\n=========================================")


# -------------------------------
# MAIN GAME FUNCTION
# -------------------------------

def main():

    print("===================================")
    print("        UFC 1v1 FIGHT GAME")
    print("===================================")

    display_fighters()

    # Choose fighters
    player = choose_fighter("Choose your fighter: ")

    while True:
        opponent = choose_fighter("Choose opponent fighter: ")

        if opponent != player:
            break
        else:
            print("Choose a different fighter.")

    round_number = 1

    while True:

        print(f"\n========== ROUND {round_number} ==========")

        display_stats()

        # Player chooses attack
        attack = choose_attack()

        # Player attacks
        if attack == "strike":
            strike_attack(player, opponent)
        else:
            grapple_attack(player, opponent)

        # Check if opponent lost
        if is_eliminated(opponent):
            print(f"\n🏆 {player} WINS THE FIGHT!")
            break

        time.sleep(1)

        # Opponent counterattacks
        opponent_ai(opponent, player)

        display_fight_stats(player, opponent)

        # Check if player lost
        if is_eliminated(player):
            print(f"\n💀 {player} HAS BEEN DEFEATED!")
            print(f"🏆 {opponent} WINS THE FIGHT!")
            break

        round_number += 1

        # Continue?
        choice = input("\nContinue? (yes/no): ").lower()

        if choice != "yes":
            print("\nGame ended.")
            break


# PROGRAM ENTRY POINT

if __name__ == "__main__":
    main()


