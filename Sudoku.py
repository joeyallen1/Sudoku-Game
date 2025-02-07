import pygame
import numpy as np
import copy
import time
pygame.init()

# constants for setting up the screen and board
BOARD_SIZE = 750
SCREEN = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
SIDE_BUFFER = BOARD_SIZE/10
SQUARE_SIZE = (BOARD_SIZE-(2*SIDE_BUFFER)) /9

class Sudoku:
    '''Sudoku board generator and solver'''
    def __init__(self):
        self.solved_board = np.zeros((9,9))
        self.solve(self.solved_board)
        self.copy_of_solved_board = copy.deepcopy(self.solved_board)
        self.remove_values(self.copy_of_solved_board,5)
        self.unsolved_board = self.copy_of_solved_board
    
    def solve(self,board):
        '''Randomly solves the given sudoku board'''
        for row in range(9):
            for col in range(9):
                if board[row,col]==0:
                    values = list(range(1,10))
                    values = np.random.permutation(values)
                    for value in values:
                        if self.possible(row,col,value,board):
                            board[row,col] = value
                            if self.solve(board):
                                return True
                            else:
                                board[row,col] = 0
                    return False
        return True
    
    def possible(self,row,col,value,board):
        '''Is the given value possible for the given location in the board (according to sudoku rules)'''
        return np.all(board[row,:] != value) and np.all(board[:,col] != value) and np.all(board[(row//3)*3:(row//3)*3+3,(col//3)*3:(col//3)*3+3] != value)
    
    def remove_values(self,board,num_attempts_to_remove):
        '''Removes values from a fully solved board to create the puzzle (variable is used to keep track of how many times removing a number results in multiple solutions)'''
        if num_attempts_to_remove == 0:
            return 
        row = np.random.randint(0,9)
        col = np.random.randint(0,9)
        if board[row,col] != 0:
            num_solutions = 0
            values = list(range(1,10))
            values = np.random.permutation(values)
            backup_value = board[row,col]
            for value in values:
                temp_board = copy.deepcopy(board)
                temp_board[row,col] = 0
                if self.possible(row,col,value,temp_board):
                    temp_board[row,col] = value
                    if self.solve(temp_board):
                        num_solutions +=1
                    continue
            if num_solutions == 1:
                board[row,col] = 0
                self.remove_values(board,num_attempts_to_remove)
            else:
                board[row,col] = backup_value
                self.remove_values(board,num_attempts_to_remove-1)
        else:
            self.remove_values(board,num_attempts_to_remove)


def input_value(pos,num):
    '''Adds numbers to the board'''
    if (SIDE_BUFFER<pos[0]<BOARD_SIZE-SIDE_BUFFER and SIDE_BUFFER<pos[1]<BOARD_SIZE-SIDE_BUFFER):
        font = pygame.font.SysFont("Arial", 30, bold=False)
        row = int(pos[1]//SQUARE_SIZE - 1)
        col = int(pos[0]//SQUARE_SIZE - 1)
        if row<9 and col<9:
            if current_game.unsolved_board[row,col] == 0:
                pygame.draw.rect(SCREEN, (255, 255, 255), (SQUARE_SIZE*col+SIDE_BUFFER+5, SQUARE_SIZE*row+SIDE_BUFFER+5, SQUARE_SIZE-5, SQUARE_SIZE-5))
                color = (0,0,255) if current_game.solved_board[row,col] == num else (255,0,0)
                text_image = font.render(f'{num}',True,color)
                SCREEN.blit(text_image,(SQUARE_SIZE*col+SIDE_BUFFER+(0.5*SQUARE_SIZE)-(text_image.get_width()/2),SQUARE_SIZE*row+SIDE_BUFFER+(0.5*SQUARE_SIZE)-(text_image.get_height()/2)))



#setup the board
current_game = Sudoku()
SCREEN.fill((255,255,255))
button1 = pygame.Rect(175,BOARD_SIZE-60,100,50)
button2 = pygame.Rect(300,BOARD_SIZE-60,100,50)
button3 = pygame.Rect(425,BOARD_SIZE-60,100,50)
startTime = time.time()

def clear_board():
    '''Clears all user inputted numbers on the board'''
    for row in range(9):
        for col in range(9):
            if current_game.unsolved_board[row,col] == 0:
                pygame.draw.rect(SCREEN, (255, 255, 255), (SQUARE_SIZE*col+SIDE_BUFFER+5, SQUARE_SIZE*row+SIDE_BUFFER+5, SQUARE_SIZE-5, SQUARE_SIZE-5))

def new_game():
    '''Starts a new game by resetting the timer and creating a new random puzzle'''
    global current_game
    current_game = Sudoku()
    global startTime
    startTime = time.time()
    for row in range(9):
        for col in range(9):
                pygame.draw.rect(SCREEN, (255, 255, 255), (SQUARE_SIZE*col+SIDE_BUFFER+5, SQUARE_SIZE*row+SIDE_BUFFER+5, SQUARE_SIZE-5, SQUARE_SIZE-5))


def finish():
    '''Freezes timer and board when user finishes the game'''
    global startTime
    cur_state = True
    while cur_state:
        startTime = time.time()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if button2.collidepoint(pos):
                    cur_state = False
                    new_game()
            elif event.type == pygame.QUIT:
                pygame.quit()


# main loop
while True:
    pygame.display.set_caption('Sudoku!')

    # setup and display buttons
    pygame.draw.rect(SCREEN,(173,216,230),button1)
    pygame.draw.rect(SCREEN,(255,204,203),button2)
    pygame.draw.rect(SCREEN,(0,255,0),button3)
    font1 = pygame.font.SysFont("Arial",15)
    text1 = font1.render("Clear Board",True,(0,0,0))
    SCREEN.blit(text1,(185,BOARD_SIZE-50))
    text2 = font1.render("New Game",True,(0,0,0))
    SCREEN.blit(text2,(310,BOARD_SIZE-50))
    text3 = font1.render("Finish!",True,(0,0,0))
    SCREEN.blit(text3,(445,BOARD_SIZE-50))


    # setup and display timer
    pygame.draw.rect(SCREEN,(255,255,255),(320,20,100,50))
    cur_total_seconds = int(time.time()-startTime)
    if cur_total_seconds//60 <10:
        cur_minutes = f'0{cur_total_seconds//60}'
    else:
        cur_minutes = f'{cur_total_seconds//60}'
    if cur_total_seconds%60 <10:
        cur_seconds = f'0{cur_total_seconds%60}'
    else:
        cur_seconds = f'{cur_total_seconds%60}'
    cur_time = f'{cur_minutes}:{cur_seconds}'
    timer_font = pygame.font.SysFont("Arial",30,bold=False)
    timer = timer_font.render(cur_time,True,(0,0,0))
    SCREEN.blit(timer,(320,20))

    # display board
    for i in range(10):
        line_thickness = 2 if i%3 == 0 else 1
        pygame.draw.line(SCREEN,(0,0,0),(SIDE_BUFFER, SIDE_BUFFER+ SQUARE_SIZE*i),(BOARD_SIZE-SIDE_BUFFER,SIDE_BUFFER+ SQUARE_SIZE*i),width=line_thickness)
        pygame.draw.line(SCREEN,(0,0,0),(SIDE_BUFFER+SQUARE_SIZE*i,SIDE_BUFFER),(SIDE_BUFFER+SQUARE_SIZE*i,BOARD_SIZE-SIDE_BUFFER),width=line_thickness)
    font2 = pygame.font.SysFont("Arial", 30, bold=True)
    for row in range(9):
        for col in range(9):
            if current_game.unsolved_board[row,col] != 0:
                text_image = font2.render(f'{int(current_game.unsolved_board[row,col])}', True, (0,0,0))
                SCREEN.blit(text_image,(SQUARE_SIZE*col+SIDE_BUFFER+(0.5*SQUARE_SIZE)-(text_image.get_width()/2),SQUARE_SIZE*row+SIDE_BUFFER+(0.5*SQUARE_SIZE)-(text_image.get_height()/2)))
    
    # handles key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if button1.collidepoint(pos):
                clear_board()
            elif button2.collidepoint(pos):
                new_game()
            elif button3.collidepoint(pos):
                finish()
        keys = pygame.key.get_pressed()
        for num in range(1,10):
            if keys[pygame.K_1 + num - 1]:
                input_value(pos,num)
    pygame.display.update()