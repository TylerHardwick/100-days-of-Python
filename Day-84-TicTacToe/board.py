import random
import time

class Board:

    def __init__(self):
        self.board_list = [[" ", " ", " "],[" "," ", " "],[" ", " ", " "]]
        self.player1 = ""
        self.player2 = ""
        self.player_count = 0
        self.turn_count = 0
        self.play = True
        self.npc = False

# Creates the Board
    def create_board(self):

        for n in range(0,3):
            if n < 2:
                line = "---+---+---"
            else:
                line = ""
            print(f"{self.board_list[n][0]}  | {self.board_list[n][1]} | {self.board_list[n][2]}\n{line}")


# Lets the player chose whether they are X or O
    def chose_player(self):
        counter = str(input("Player 1, would you like to be 'X' or 'O'?: ")).upper()
        if counter == "X":
            self.player1 = "X"
            self.player2 = "O"
        else:
            self.player1 = "O"
            self.player2 = "X"
        print(f"Good choice, Player 1, you are {self.player1}s!\n\n")
        npc_check = str(input("Would you like to play against the computer? y/n? :")).lower()
        if npc_check == "y":
            self.npc = True


# Check if it is Player 1 or Player 2's turn
    def check_player(self):
        if self.player_count % 2 == 0:
            player = 1
            return player, self.player1
        else:
            player = 2
            return player, self.player2


    def take_turn(self):
        selection = []
        if not self.check_npc():
            try:
                self.create_board()
                print(f"Player {self.check_player()[0]}, you're up!")
                raw_selection = str(input(f"Where would you like to go?\nSelect a row using A, B or C and a column : 1, 2 or 3 (etc. 'a1'): ")).lower()

                if raw_selection[0] == 'a':
                    selection = [0, int(raw_selection[1])-1]
                elif raw_selection[0] == 'b':
                    selection = [1, int(raw_selection[1])-1]
                else:
                    selection = [2, int(raw_selection[1])-1]
                if self.board_list[selection[0]][selection[1]] != " ":
                    print(f"\n\n\nWoah there! It looks like that is already taken. Try again!")
                    return
                self.update_board(selection)
                self.create_board()
                self.check_win()
                self.turn_count += 1
                self.check_draw()
                self.player_count += 1
            except IndexError:
                print("That is not a valid cell. Please use the format row+column e.g a1 or c3")
                return
            except ValueError:
                print("That is not a valid cell. Please use the format row+column e.g a1 or c3")
                return
        else:
            npc_move = self.play_npc()
            print(f"Player {self.check_player()[0]}, you're up!\n")
            time.sleep(4)
            print(f"Player 2 has decided to go in {npc_move}")
            raw_selection = npc_move

            if raw_selection[0] == 'a':
                selection = [0, int(raw_selection[1]) - 1]
            elif raw_selection[0] == 'b':
                selection = [1, int(raw_selection[1]) - 1]
            else:
                selection = [2, int(raw_selection[1]) - 1]

            if self.board_list[selection[0]][selection[1]] != " ":
                print(f"Trying to go again")
                return
            self.update_board(selection)
            self.check_win()
            self.turn_count += 1
            self.check_draw()
            self.player_count += 1

    def update_board(self, selection):
        self.board_list[selection[0]][selection[1]] = self.check_player()[1]


    def check_win(self):
        for num in range(3):

            # Straight Line wins
            if self.board_list[0][num] == self.board_list[1][num] == self.board_list[2][num] and self.board_list[0][num] != " ":
                self.tell_win()
            elif self.board_list[num][0] == self.board_list[num][1] == self.board_list[num][2] and self.board_list[num][0] != " ":
                self.tell_win()

            #Diagonal Wins
        if self.board_list[0][0] == self.board_list[1][1] == self.board_list[2][2] and self.board_list[1][1] != " ":
            self.tell_win()
        elif self.board_list[2][0] == self.board_list[1][1] == self.board_list[0][2] and self.board_list[1][1] != " ":
            self.tell_win()


    def tell_win(self):
        self.create_board()
        play_again = str(input(f"\nCongratulations Player {self.check_player()[0]}, you win!\n Would you like to play again? y/n: ")).lower()
        if play_again == "y":
            self.play_again()
        else:
            self.play = False

    def check_draw(self):
        if self.turn_count == 9:
            self.create_board()
            play_again = str(input(f"It's a draw!\nWould you like to play again? y/n: ")).lower()
            if play_again == "y":
                self.play_again()
            else:
                self.play = False


# Starts the game over
    def play_again(self):
        self.board_list = [[" ", " ", " "],[" "," ", " "],[" ", " ", " "]]
        self.player1 = ""
        self.player2 = ""
        self.player_count = 0
        self.turn_count = 0
        print(f"\n"*10)
        self.chose_player()


    def play_npc(self):
        # Vertical lines
        for num in range(3):
            if self.board_list[0][num] == self.board_list[1][num] and self.board_list[1][num] == self.player1 and self.board_list[2][num] != self.player2:
                return f"c{num+1}"
            elif self.board_list[1][num] == self.board_list[2][num] and self.board_list[1][num] == self.player1 and self.board_list[0][num] != self.player2:
                return f"a{num+1}"
            elif self.board_list[0][num] == self.board_list[2][num] and self.board_list[0][num] == self.player1 and self.board_list[1][num] != self.player2:
                return f"b{num+1}"

        # Horizontal Lines
            elif self.board_list[num][0] == self.board_list[num][1] and self.board_list[num][1] == self.player1 and self.board_list[num][2] != self.player2:
                if num == 0:
                    return "a3"
                elif num == 1:
                    return "b3"
                else:
                    return "c3"
            elif self.board_list[num][1] == self.board_list[num][2] and self.board_list[num][1] == self.player1 and self.board_list[num][0] != self.player2:
                if num == 0:
                    return "a1"
                elif num == 1:
                    return "b1"
                else:
                    return "c1"
            elif self.board_list[num][2] == self.board_list[num][0] and self.board_list[num][0] == self.player1 and self.board_list[num][1] != self.player2:
                if num == 0:
                    return "a2"
                elif num == 1:
                    return "b2"
                else:
                    return "c2"

        # Diagonal Lines
        if self.board_list[0][0] == self.board_list[1][1] and self.board_list[1][1] == self.player1 and self.board_list[2][2] != self.player2:
            return "c3"
        elif self.board_list[1][1] == self.board_list[2][2] and self.board_list[1][1] == self.player1 and self.board_list[0][0] != self.player2:
            return "a1"
        elif self.board_list[2][0] == self.board_list[1][1] and self.board_list[1][1] == self.player1 and self.board_list[0][2] != self.player2:
            return "a3"
        elif self.board_list[1][1] == self.board_list[0][2] and self.board_list[1][1] == self.player1 and self.board_list[2][0] != self.player2:
            return "c1"
        elif self.board_list[0][0] == self.board_list[2][2] and self.board_list[0][0] == self.player1 and self.board_list[1][1] != self.player2:
            return "b2"
        elif self.board_list[0][2] == self.board_list[2][0] and self.board_list[0][2] == self.player1 and self.board_list[1][1] != self.player2:
            return "b2"

        # other

        random_choice = str(random.choice("abc")) + str(random.randint(1, 3))
        if random_choice[0] == 'a':
            selection = [0, int(random_choice[1]) - 1]
        elif random_choice[0] == 'b':
            selection = [1, int(random_choice[1]) - 1]
        else:
            selection = [2, int(random_choice[1]) - 1]

        if self.board_list[selection[0]][selection[1]] != " ":
            return self.play_npc()
        else:
            return random_choice



    def check_npc(self):
        if self.check_player()[0] == 1:
            return False
        elif self.check_player()[0] == 2 and not self.npc:
            return False
        else:
            return True