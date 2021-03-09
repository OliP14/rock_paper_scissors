# Ask for R, P, S
# user enters choice - try and implement button options
# computer chooses random choice
# try and implement psychology "tricks"/trends in rps for the computer
# keep track of score
# add different levels of difficulty? - You could use the computer keeping track of moves to add difficulty

import time
import random

# Global Variables
shoot_options = ["rock", "paper", "scissors"]
computer_choice = ""
shoot = ""
tie = False
again = True


def play():
    global again
    while again == True:
        countdown()
        computer_shoot()
        check_winner()
        play_again()


def countdown():
    global shoot

    print("Rock")
    time.sleep(0.6)
    print("Paper")
    time.sleep(0.6)
    print("Scissors")
    time.sleep(0.6)
    shoot = input("Shoot: ")
    spell_check()

def computer_shoot():
    global computer_choice
    computer_choice = random.choice(shoot_options)
    print("The computer chose: " + computer_choice)
    return computer_choice

def check_winner():
    global tie
    check_tie()
    if not tie:
        check_rock_win()
        check_paper_win()
        check_scissor_win()
        if check_rock_win() or check_paper_win() or check_scissor_win():
            print("You win!")
        else:
            print("You lost :(")
    return

# Checks to see if the user won with rock
def check_rock_win():
    if shoot == shoot_options[0] and computer_choice == shoot_options[1]:
        return False
    elif shoot == shoot_options[0] and computer_choice == shoot_options[2]:
        return True
    return

# Checks to see if the user won with paper
def check_paper_win():
    if shoot == shoot_options[1] and computer_choice == shoot_options[2]:
        return False
    elif shoot == shoot_options[1] and computer_choice == shoot_options[0]:
        return True
    return

# Checks to see if the user won with scissors
def check_scissor_win():
    if shoot == shoot_options[2] and computer_choice == shoot_options[0]:
        return False
    elif shoot == shoot_options[2] and computer_choice == shoot_options[1]:
        return True
    return

def check_tie():
    global tie
    if shoot == computer_choice:
        tie = True
        print("Draw")
    return

def spell_check():
    global shoot
    while shoot not in shoot_options:
        shoot = input("That is an invalid input. Please shoot again: ")

def play_again():
    global again
    answer = input("Would you like to play again? (y/n): ")
    if answer == "y":
        again = True
    else:
        again = False

play()