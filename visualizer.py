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