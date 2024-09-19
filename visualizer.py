from card_deck import *

def welcome():
    print("     #==============================================#\n"
          "     ║                  POKER-BOT                   ║\n"
          "     ║                 \033[94m ¯¯\033[92m¯¯\033[90m¯\033[91m¯¯\033[93m¯¯ \033[0m                  ║\n"
          "     ║       taking the risk out of gambling        ║\n"
          "     #==============================================#\n")
    start = ""
    while start not in ["Y", "y", "N", "n"]:
        start = input("                    START GAME? (Y/N)")
    if start in ["Y","y"]:
        players = input("ENTER NUMBER OF PLAYERS 2-6:")
        return True, int(players)

def starting_table(playerList):
    playerCards = {1: "        ", 2: "        ", 3: "        ", 4: "        ", 5: "        "}
    playerLabel = {1: "", 2: "", 3: "", 4: "", 5: ""}
    for i, player in enumerate(playerList):
        print()
        playerCards[i] = "|XX||XX|"
        playerLabel[i] = f"    P{i}    "

    print(f"   {playerLabel[1]} {playerLabel[2]} {playerLabel[3]} {playerLabel[4]} {playerLabel[5]}\n"
          f"╭╼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╾╮\n"
          f"╽   {playerCards[1]}   {playerCards[2]}   {playerCards[3]}   {playerCards[4]}   {playerCards[5]}   ╽\n"
          f"┃                                                          ┃\n"
          f"┃                                                          ┃\n"
          f"┃                                                          ┃\n"
          f"┃                                                          ┃\n"
          f"┃                                                          ┃\n"
          f"┃                                                          ┃\n"
          f"╿                        {playerList[0]}                        ╿\n"
          f"╰╼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╾╯")


def requestHand(deck: Deck):
    print("ENTER HAND, FORMAT: SUIT|RANK\n"
          "Example: Clubs|Q for Queen of Clubs")
    card1Valid, card2Valid = False, False
    Final1, Final2 = None, None
    while not card1Valid:
        try:
            card1 = input("Card 1: ")
            suit, rank = card1.split("|")
            if rank != "10":
                rank = " " + rank
            Final1 = Card(suit, rank)
            card1Valid = Final1 in deck.getDeck()
        except:
            print("Invalid Card")

    while not card2Valid:
        try:
            card2 = input("Card 2: ")
            suit, rank = card2.split("|")
            if rank != "10":
                rank = " " + rank
            Final2 = Card(suit, rank)
            card2Valid = Final2 in deck.getDeck() and Final1 != Final2
        except:
            print("Invalid Card")
        else:
            print("Invalid Card")

    return Final1, Final2