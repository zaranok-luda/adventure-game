
import time
import random

templates = ['troll', 'dragon', 'pirate', 'gorgon', 'wicked fairie']

hero = ""

sword = False

is_cave_visited = False


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and, yellow wildflowers.")
    print_pause(f"Rumor has it that a {hero} is somewhere around here, and "
                "has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def choice():
    print("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    knock_the_door_or_go_to_cave()


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 == response:
            return response
        elif option2 == response:
            return response


def hero_attacks():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {hero}.")
    print_pause(f"Eep! This is the {hero}'s house!")
    print_pause(f"The {hero} attacks you!")


def knock_the_door_or_go_to_cave():
    response = valid_input("(Please enter 1 or 2.)", "1", "2")
    global is_cave_visited
    if response == "1":
        hero_attacks()
        response_choice_again()
    elif response == "2" and not is_cave_visited:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        global sword
        sword = True
        is_cave_visited = True
        choice()
    elif response == "2" and is_cave_visited:
        cave_second_visit()


def cave_second_visit():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff. "
                "It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    choice()


def response_choice_again():
    response = valid_input("Would you like to (1) fight or (2) run away?",
                           "1", "2")

    if response == "1":
        if sword:
            fight()
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {hero}.")
            print_pause("You have been defeated!")
            play_again()
    elif response == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        choice()


def play_again():
    response = valid_input("Would you like to play again? (y/n)", "y", "n")

    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")


def fight():
    if sword:
        print_pause(f"As the {hero} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"But the {hero} takes one look at your shiny new toy "
                    "and runs away!")
        print_pause(f"You have rid the town of the {hero}. "
                    "You are victorious!")
        play_again()
    else:
        hero_attacks()
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")


def play_game():
    global is_cave_visited
    global sword
    global hero
    sword = False
    is_cave_visited = False
    hero = random.choice(templates)
    intro()
    choice()


play_game()
