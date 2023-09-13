## COMPSCI 130 ASSIGNMENT MAIN - MICOLE LAUREN MARQUEZ mmar250 324117389

# class to implement connect 4 game board
class GameBoard:
    # intialise values
    def __init__(self, size):
        self.size = size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2

    #returns no. free positions in the specified column        
    def num_free_positions_in_column(self, column):
        a_list = self.items[column]
        self.num_free_pos_in_col = self.size
        self.num_free_pos_in_col = self.num_free_pos_in_col - len([i for i, e in enumerate(a_list) if e != 0])
        return self.num_free_pos_in_col

    # returns list of slots that have space to add disc(s) in order from centre most to outer, left to right
    def free_slots_as_close_to_middle_as_possible(self):
        free_slots = [] # list that will be returned at end of method of free slots in order from centre out
        preferedlist = [] # list of all columns in preferred order from centre out
        while True:
            if ((self.size/2).is_integer()):
                a = (int(self.size/2)-1)
            else:
                a= (int(self.size/2))
            preferedlist.append(a)
            for i in range(1,a+2):
                try:
                    if (self.size % 2) == 0: # even
                        preferedlist.append(a+i)
                        preferedlist.append(a-i)
                    else:   # odd
                        preferedlist.append(a-i)
                        preferedlist.append(a+i)
                except:
                    break
            break
        for col in preferedlist:
            if col < 0:
                preferedlist.remove(col)            
            #if preferedlist has free slot then store to list
            elif GameBoard.num_free_positions_in_column(self, col) > 0:
                free_slots.append(col)
        return free_slots

    # returns true if game is over (ie. board is full)
    def game_over(self):
        answer = 0
        for column in self.items:
            num = self.size - len([i for i, e in enumerate(column) if e != 0])
            if num == 0:
                answer += 1
        if answer == self.size:
            return True        
        else:
            return False

    # check the horizontal, vertical and diagonal for consecutive sequences and count the total no. of pts gained 
    def num_new_points(self, column, row, player):
        # initialise local variable to store point and counter
        # counter will count the number of same piece in a row
        point = 0
        counter = 0
        # check horizontal row for same piece and count
        for s in range(-3,1):
            counter = 0
            for k in range(s,s+4):
                try:
                    if column+k >= 0 and ((player == 1 and self.items[column+k][row] == 1) or (player == 2 and self.items[column+k][row] == 2)):
                        counter += 1
                        if counter == 4:
                            point += 1
                            counter = 0
                except:
                    pass
        counter = 0 # reinitialise the counter
        # check vertical row for same piece and count
        for k in range(-3,1):
            try:
                if row+k >= 0 and ((player == 1 and self.items[column][row+k] == 1) or (player == 2 and self.items[column][row+k] == 2)):
                    counter += 1
                    if counter == 4:
                        point += 1
                        counter = 0
            except:
                pass
        # check diagonal row for same piece and count e.g.
##             x
##            X
##           x
##          x
        for s in range(-3,1):
            counter = 0
            for k in range(s,s+4):
                try:
                    if column+k >= 0 and row+k >= 0 and ((player == 1 and self.items[column+k][row+k] == 1) or (player == 2 and self.items[column+k][row+k] == 2)):
                        counter += 1
                        if counter == 4:
                            point += 1
                            counter = 0
                except:
                    pass
         # check diagonal row for same piece and count e.g.
##        x
##         X
##          x
##           x
        for s in range(-3,1):
            counter = 0
            for k in range(s,s+4):
                try:
                    if column+k >= 0 and row-k >=0 and ((player == 1 and self.items[column+k][row-k] == 1) or (player == 2 and self.items[column+k][row-k] == 2)):
                        counter += 1
                        if counter == 4:
                            point += 1
                            counter = 0
                except:
                    pass
         # return the total no. of points scored
        return point

    # when a new disc (player number) is to be added to the list of items
    def add(self, column, player):
        if self.num_entries[column] > self.size or column < 0 or column >= self.size:
            return False
        else:
            try:
                #iteration stops when the value of the list item in the column is 0
                for item in self.items[column]:
                    #only adds to list if the column has space
                    if item == 0:
                        row = self.items[column].index(item) # sets the row to the index of the next free row in that column
                self.items[column][row] = player
                self.num_entries[column] += 1
                #calculate and add the number of new points attained from added disc
                self.points[player-1] += GameBoard.num_new_points(self, column, row, player)
                return True
            except:
                pass

    #deletes the temporary value in the items list (used for when finding out the column resulting in max pts
    def delete(self, column, row):
        if self.num_entries[column] > self.size or column < 0 or column >= self.size:
            return False
        else:
            try:
                self.items[column][row] = 0
                self.num_entries[column] -= 1
                return True
            except:
                pass

    #prints the game board with updated values 
    def display(self):
        items = []
        for column in self.items:
            for i in column:
                if i == 0: # empty 
                    items += ' '
                elif i == 1: # player 1 value
                    items += 'o'
                elif i == 2: # player 2 value
                    items += 'x'
        row = []
        to_print = []
        count = self.size
        while count != 0:
            row.append(items[::self.size])
            items.remove(items[0])
            count -= 1
        to_print += row
       
        for line in to_print[::-1]:
            print(' '.join(line))    
        print("-"*((2*self.size)-1))
        for i in range(self.size):
            print('{} '.format(i), end='')
        #updated values for points
        print("\nPoints player 1:", self.points[0])
        print("Points player 2:", self.points[1])

    # computes slot into which player needs to insert a disc in order to obtain max pts
    def column_resulting_in_max_points(self, player):
        max_points = 0 #make the default 0, this var will be compared to, to find which is maximum
        #get list of free slots, so that it only iterates through the ones that have room for more discs
        free_slots = GameBoard.free_slots_as_close_to_middle_as_possible(self)
        if free_slots == []: #if no free slots, game over
            return GameBoard.game_over
        slot_number_for_max_points = free_slots[0] #slot with most middle free
        for col in free_slots:
            points = self.points[player-1]
            column = self.items[col]
            for i in range(len(column)):
                if column[i] == 0:
                    row = i
                    break
                else:
                    pass
            self.add(col, player)
            potential_points = self.points[player-1] - points
            # deletes the disc because it hasn't actually been added yet
            self.delete(col, row)
            self.points[player-1] -= potential_points
            # if the no. pts for this slot is > currently stored in max_points, will replace slot no. to this col
            if potential_points > max_points:
                slot_number_for_max_points = col
                max_points = potential_points
        return (slot_number_for_max_points, max_points)

# given class to play the game modified for pygame GUI
class FourInARow:
    def __init__(self, size):
        self.board=GameBoard(size)
    def play(self):
        print("*****************NEW GAME*****************")
        self.board.display()
        player_number=0
        moves = 0
        print()
        while not self.board.game_over():
            print("Player ",player_number+1,": ")
            if player_number==0:
                valid_input = False
                while not valid_input:
                    try:
                        column = int(input("Please input slot: "))       
                    except ValueError:
                        print("Input must be an integer in the range 0 to ", self.board.size-1 )
                    else:
                        if column<0 or column>=self.board.size:
                            print("Input must be an integer in the range 0 to", self.board.size-1 )
                        else:
                            if self.board.add(column, player_number+1):
                                valid_input = True
                            else:
                                print("Column ", column, "is already full. Please choose another one.")
            else:
                # Choose move which maximises new points for computer player
                (best_column, max_points)=self.board.column_resulting_in_max_points(2)
                if max_points>0:
                    column=best_column
                else:
                    # if no move adds new points choose move which minimises points opponent player gets
                    (best_column, max_points)=self.board.column_resulting_in_max_points(1)
                    if max_points>0:
                        column=best_column
                    else:
                        # if no opponent move creates new points then choose column as close to middle as possible
                        column = self.board.free_slots_as_close_to_middle_as_possible()[0]
                self.board.add(column, player_number+1)
                moves += 1
                print("On move", moves ,"The AI chooses column ", column)
            
            self.board.display()
            player_number=(player_number+1)%2
            
        if (self.board.points[0]>self.board.points[1]):
            print("Player 1 (circles) wins!")
        elif (self.board.points[0]<self.board.points[1]):    
            print("Player 2 (crosses) wins!")
        else:  
            print("It's a draw!")

# ask player for game board size until valid input of 1 - 10
valid_input = False
while not valid_input:
    try:
        size = int(input("Choose a game board size between 1 and 10: "))
    except ValueError:
        print("Input must be an integer between 1 and 10 (inclusive)")
    else:
        if size < 1 or size > 10:
            print("Input must be an integer between 1 and 10 (inclusive)")
        elif size >= 1 and size <= 10:
            valid_input = True

game = FourInARow(size)
game.play()  
