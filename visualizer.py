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
        players = input("ENTER NUMBER OF PLAYERS:")
        return True, players

def starting_table(playerList):
    print(f"╭╼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╾╮\n"
          f"╽                                                        ╽\n"
          f"┃                                                        ┃\n"
          f"┃                                                        ┃\n"
          f"┃                                                        ┃\n"
          f"┃                                                        ┃\n"
          f"┃                                                        ┃\n"
          f"┃                                                        ┃\n"
          f"╿                       {playerList[0]}                       ╿\n"
          f"╰╼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╾╯")