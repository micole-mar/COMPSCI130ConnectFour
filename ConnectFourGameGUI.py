## COMPSCI 130 ASSIGNMENT COOL EXTENSION with pygame - MICOLE LAUREN MARQUEZ mmar250 324117389

# imports
import pygame # opensource code for creating game, sourced from https://www.pygame.org/contribute.html
import math

# colours used 
black = (0,0,0)
white = (255,255,255)
darkgrey = (202, 202, 202)
grey = (92, 92, 92)
cream = (238, 236, 232)
red = (177, 76, 59)
lightred = (229, 159, 148)
green = (155, 202, 152)
lightgreen = (193, 224, 200)

# class to implement connect 4 game board
class GameBoard:
    # intialise values
    def __init__(self, size):
        self.size=size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] *2

    # main game board set up
    def create_board(self, screen, myfont, game_over = False, error_msg = None):
        for c in range(len(self.items)):
            for r in range(len(self.items)):
                # draws each rectangle and circle on screen
                pygame.draw.rect(screen, cream, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, darkgrey, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
                # draw score board background
                pygame.draw.rect(screen, white, ((len(self.items))*SQUARESIZE, r*SQUARESIZE, 2*SQUARESIZE, height))
                                
        for c in range(len(self.items)):
            for r in range(len(self.items)):
                # player 1 discs
                if self.items[c][r] == 1:
                    pygame.draw.circle(screen, green, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                # player 2 discs
                elif self.items[c][r] == 2: 
                    pygame.draw.circle(screen, grey, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        # show scores only if the size of the board is at least 2, otherwise it won't fit and is unnecessary             
        if self.size >= 2 :
            player1score = myfont.render("Player 1 Score: {}".format(self.points[0]), 1, black)
            player2score = myfont.render("Player 2 Score: {}".format(self.points[1]), 1, black)
            screen.blit(player1score, ((len(self.items))*SQUARESIZE, r*SQUARESIZE))
            screen.blit(player2score, ((len(self.items))*SQUARESIZE, r*SQUARESIZE+(SQUARESIZE/2)))
        # error message appears if player tries to drop a disc in a full column or out of bounds (white area)
        if error_msg != None:
            screen.blit(error_msg, ((len(self.items))*SQUARESIZE, r*SQUARESIZE+SQUARESIZE))
            pygame.display.update()
            pygame.time.wait(500) #error mssg appears for enough time for user to read
        # winner message when the board is full   
        if game_over == True:
            if (self.points[0]>self.points[1]):
                winner_msg = myfont.render("Player 1 WINS!", 1, green) # in colour of winning player
            elif (self.points[0]<self.points[1]):    
                winner_msg = myfont.render("Player 2 WINS", 1, grey) # in colour of winning player
            else:
                winner_msg = myfont.render("IT'S A DRAW!", 1, black)
            screen.blit(winner_msg, ((len(self.items))*SQUARESIZE, r*SQUARESIZE+SQUARESIZE))
        pygame.display.update() # update the draw board

    # after a full game, take user to restart page to ask if they want to play again or exit
    def restart_page(self, screen, myfont):
        pygame.draw.rect(screen, darkgrey, (0,0, width, height))
        pygame.draw.rect(screen, cream, (0,height/3, width, height/3))
        restart_q = myfont.render("Would you like to play again?", 1, black)
        screen.blit(restart_q, (0,height/3))
        yes = myfont.render("YES", 1, black)
        no = myfont.render("NO", 1, black)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #if the mouse is clicked on the no button the game is terminated
                    if width/4 <= mouse[0] <= width/4+width/8 and height/2 <= mouse[1] <= height/2+40:
                        pygame.quit()
                        exit()
                    #if mouse clicked on the yes button the game starts again
                    elif 3*width/4-width/8 <= mouse[0] <= 3*width/4 and height/2 <= mouse[1] <= height/2+40:
                        game = FourInARow(self.size)
                        game.play(self.size)

            # stores the (x,y) coordinates into the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # adjust the height of the button to be responsive to the size of the screen
            if self.size >= 7:
                btn_height = 60
            elif self.size >= 4:
                btn_height = 40
            else:
                btn_height = 20
          
            # if mouse is hovered on a button it changes to lighter shade
            # no button
            if width/4 <= mouse[0] <= width/4+width/8 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,red,[width/4,height/2,width/8,btn_height])
            else:
                pygame.draw.rect(screen,lightred,[width/4,height/2,width/8,btn_height])
            # yes button
            if 3*width/4-width/8 <= mouse[0] <= 3*width/4 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,green,[3*width/4-width/8,height/2,width/8,btn_height])
            else:
                pygame.draw.rect(screen,lightgreen,[3*width/4-width/8,height/2,width/8,btn_height])
            # superimposing the text onto our button
            screen.blit(no , (width/4,height/2))
            screen.blit(yes , (3*width/4-width/8,height/2))
            # updates the frames of the game
            pygame.display.update()   

    # check if location is valid, if value at location is 0
    def valid_location(self, col):
        return 0 in self.items[col]

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
                    if (self.size % 2) == 0:    # even
                        preferedlist.append(a+i)
                        preferedlist.append(a-i)
                    else:               # odd
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

    # returns true if game is over (ie. board is full, all slots have been allocated a value)
    def game_over(self):
        # initialise local variable to store the current no. of items
        answer = 0
        for column in self.items:
            num = self.size - len([i for i, e in enumerate(column) if e != 0])
            if num == 0:
                answer += 1
        # game over if items is the same as the actual size
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

    # computes slot into which player needs to insert a disc in order to obtain max pts
    def column_resulting_in_max_points(self, player):
        max_points = 0 #make the default 0, this var will be compared to, to find which is maximum
        #get list of free slots, so that it only iterates through the ones that have room for more discs
        free_slots = GameBoard.free_slots_as_close_to_middle_as_possible(self)
        #if no free slots, game over
        if free_slots == []:
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
        return (slot_number_for_max_points, max_points) # return tuple of slot no. and max pts

# given class to play the game modified for pygame visualisation
class FourInARow:
    def __init__(self, size):
        self.board=GameBoard(size)
    def play(self, size):
        player_number=0
        moves = 0
        game_over = False
        turn = 0
        #initalize pygame and font
        pygame.init()        
        screen = pygame.display.set_mode(boardsize)
        screen.fill(darkgrey)
        myfont = pygame.font.SysFont("arial", 15)
        
        #Calling function create_board again
        self.board.create_board(screen, myfont)
        pygame.display.update()
        
        while not self.board.game_over():
            
                # for each motion of the mouse
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # allows game to properly exit out
                        pygame.quit()
                        exit()

                    # when player hovers along different columns
                    if event.type == pygame.MOUSEMOTION:
                        # top rectangle where the disc moves along
                        pygame.draw.rect(screen, darkgrey, (0,0, (size * SQUARESIZE), SQUARESIZE))
                        posx = event.pos[0]
                        # player's disc that moves along the top
                        pygame.draw.circle(screen, green, (posx, int(SQUARESIZE/2)), RADIUS)
                        # white rectangle to cover the top right corner, otherwise it will be patchy with the green circle
                        pygame.draw.rect(screen, white, (len(self.board.items)*SQUARESIZE, 0, (size * SQUARESIZE), SQUARESIZE))
                    pygame.display.update()

                    # player 1's turn
                    if player_number == 0:
                        
                        # when player wants to drop a disc down a column                        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.draw.rect(screen, darkgrey, (0,0, width, SQUARESIZE))
                            posx = event.pos[0]
                            col = int(math.floor(posx/SQUARESIZE)) #takes column number as input

                            try:
                                if self.board.valid_location(col):
                                    self.board.add(col, player_number+1)
                                    valid_input = True
                                    # change to next player only when valid column is selected
                                    player_number=(player_number+1)%2
                                else:
                                    error_msg = myfont.render("Column is full", 1, black)
                                    self.board.create_board(screen, myfont, False, error_msg)
                            except:
                                error_msg = myfont.render("Out of bounds", 1, black)

                                self.board.create_board(screen, myfont, False, error_msg)
                                
                    # computer's turn (player 2)
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
                        # change to next player
                        player_number=(player_number+1)%2
                    # update game board
                    self.board.create_board(screen, myfont)
        # when loop is broken, game over - board is full
        game_over = True
        self.board.create_board(screen, myfont, game_over)
        if game_over == True:
            # give user time to see results of the winner before moving onto next page
            pygame.time.wait(4000)
            # would you like to play again screen
            self.board.restart_page(screen, myfont)


        
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

#define our screen size in pixels
SQUARESIZE = 80

#define width and height of board
width = (size * SQUARESIZE) + 2*SQUARESIZE 
height = (size+1) * SQUARESIZE 
 
boardsize = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)

game = FourInARow(size)
game.play(size)  
