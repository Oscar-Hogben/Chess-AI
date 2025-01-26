# IMPORTANT: Image files of chess pieces are required to be in a pieces folder in the same directory as the python script

import copy, abc, pygame, random, time


DEPTH = 3
FILE_NAME_LOAD = 'board.txt'
FILE_NAME_SAVE = 'board.txt'

ANSI_codes = {'RED':'\033[91m', 'GREEN':'\033[92m', 'YELLOW':'\033[93m', 'BLUE':'\033[94m', 'MAGENTA':'\033[95m', 'CYAN':'\033[96m', 'WHITE':'\033[97m', 'END':'\033[0m'}

class UserInterface():
    def __init__(self):
        LIGHT_COLOUR = (246, 213, 180)
        DARK_COLOUR = (202, 157, 111)
        EDGE_COLOUR = (0,0,0)

        pygame.init()
        pygame.font.init()

        self.__screen = pygame.display.set_mode((680,680))
        pygame.display.set_caption("AI Chess Game")

        margin = pygame.Surface((680,680))
        margin.fill(DARK_COLOUR)
        self.__screen.blit(margin, (0, 0))

        margin2 = pygame.Surface((602,602))
        margin2.fill(EDGE_COLOUR)
        self.__screen.blit(margin2, (39, 39))


        font = pygame.font.SysFont('arialblack.ttf', 32)
        for i in range(8):
            letter = font.render(chr(i+65),True,EDGE_COLOUR)
            number = font.render(str(8-i),True,EDGE_COLOUR)
            self.__screen.blit(letter, (i*75+70, 10))
            self.__screen.blit(number, (15, i*75+65))

        board = pygame.Surface((600, 600))

        for x in range(0,8,2):
            for y in range(0,8,2):
                pygame.draw.rect(board, LIGHT_COLOUR, (x*75, y*75, 75, 75))
        for x in range(1,8,2):
            for y in range(1,8,2):
                pygame.draw.rect(board, LIGHT_COLOUR, (x*75, y*75, 75, 75))

        for x in range(1,8,2):
            for y in range(0,8,2):
                pygame.draw.rect(board, DARK_COLOUR, (x*75, y*75, 75, 75))
        for x in range(0,8,2):
            for y in range(1,8,2):
                pygame.draw.rect(board, DARK_COLOUR, (x*75, y*75, 75, 75))
        self.__screen.blit(board, (40, 40))

        pygame.display.update()
    
    def update_board(self,board_to_use,green_highlight=[],red_highlight=[]):
        LIGHT_COLOUR = (246, 213, 180)
        DARK_COLOUR = (202, 157, 111)
        EDGE_COLOUR = (0,0,0)

        margin = pygame.Surface((680,680))
        margin.fill(DARK_COLOUR)
        self.__screen.blit(margin, (0, 0))

        margin2 = pygame.Surface((602,602))
        margin2.fill(EDGE_COLOUR)
        self.__screen.blit(margin2, (39, 39))


        font = pygame.font.SysFont('arialblack.ttf', 32)
        for i in range(8):
            letter = font.render(chr(i+65),True,EDGE_COLOUR)
            number = font.render(str(8-i),True,EDGE_COLOUR)
            self.__screen.blit(letter, (i*75+70, 10))
            self.__screen.blit(number, (15, i*75+65))

        board = pygame.Surface((600, 600))

        for x in range(0,8,2):
            for y in range(0,8,2):
                pygame.draw.rect(board, LIGHT_COLOUR, (x*75, y*75, 75, 75))
        for x in range(1,8,2):
            for y in range(1,8,2):
                pygame.draw.rect(board, LIGHT_COLOUR, (x*75, y*75, 75, 75))

        for x in range(1,8,2):
            for y in range(0,8,2):
                pygame.draw.rect(board, DARK_COLOUR, (x*75, y*75, 75, 75))
        for x in range(0,8,2):
            for y in range(1,8,2):
                pygame.draw.rect(board, DARK_COLOUR, (x*75, y*75, 75, 75))
        
        self.__screen.blit(board, (40, 40))

        for square in green_highlight:
            x = square[0]
            y = square[1]
            green_square = pygame.Surface((75,75),pygame.SRCALPHA,32)
            green_square = green_square.convert_alpha()
            green_square.fill((0,200,0,50))
            self.__screen.blit(green_square, (75*x + 40, 75*y + 40))
        
        for square in red_highlight:
            x = square[0]
            y = square[1]
            green_square = pygame.Surface((75,75),pygame.SRCALPHA,32)
            green_square = green_square.convert_alpha()
            green_square.fill((255,0,0,50))
            self.__screen.blit(green_square, (75*x + 40, 75*y + 40))

        for row in range(8):
            for column in range(8):
                square = board_to_use[row][column]
                if square != None:
                    t = square.get_type().lower()
                    c = square.get_colour().lower()
                    image_obj = pygame.image.load(f'pieces/{t}_{c}.webp')
                    image_obj = pygame.transform.scale(image_obj,(80,80))
                    self.__screen.blit(image_obj, (75*column+37, 75*row+35))

        pygame.display.update()
    
    def show_dificulty(self):
        grey_background = pygame.Surface((680,680),pygame.SRCALPHA,32)
        grey_background = grey_background.convert_alpha()
        grey_background.fill((0, 0, 0,150))
        self.__screen.blit(grey_background, (0, 0))

        difficulty_window = pygame.Surface((400,180))
        difficulty_window.fill((246, 213, 180))
        self.__screen.blit(difficulty_window, (140, 250))

        font = pygame.font.SysFont('arialblack.ttf', 32)
        difficulty_title = font.render('Choose a difficulty level:',True,(0,0,0))
        self.__screen.blit(difficulty_title,(150,260))

        low_difficulty = pygame.Surface((100,50))
        low_difficulty.fill((202, 157, 111))
        self.__screen.blit(low_difficulty, (180, 330))
        low_difficulty_title = font.render('Easy',True,(0,0,0))
        self.__screen.blit(low_difficulty_title,(205,345))

        mid_difficulty = pygame.Surface((100,50))
        mid_difficulty.fill((202, 157, 111))
        self.__screen.blit(mid_difficulty, (290, 330))
        mid_difficulty_title = font.render('Med',True,(0,0,0))
        self.__screen.blit(mid_difficulty_title,(320,345))

        high_difficulty = pygame.Surface((100,50))
        high_difficulty.fill((202, 157, 111))
        self.__screen.blit(high_difficulty, (400, 330))
        high_difficulty_title = font.render('Hard',True,(0,0,0))
        self.__screen.blit(high_difficulty_title,(425,345))

        pygame.display.update()

    def show_promotion(self,colour):
        grey_background = pygame.Surface((680,680),pygame.SRCALPHA,32)
        grey_background = grey_background.convert_alpha()
        grey_background.fill((0, 0, 0,150))
        self.__screen.blit(grey_background, (0, 0))

        window = pygame.Surface((400,180))
        window.fill((246, 213, 180))
        self.__screen.blit(window, (140, 250))

        font = pygame.font.SysFont('arialblack.ttf', 32)
        title = font.render('Choose a piece to promote to:',True,(0,0,0))
        self.__screen.blit(title,(150,260))

        knight = pygame.Surface((80,80))
        knight.fill((202, 157, 111))
        self.__screen.blit(knight, (200, 330))
        knight_image = pygame.transform.scale(pygame.image.load(f'pieces/n_{colour.lower()}.webp'),(80,80))
        self.__screen.blit(knight_image,(200, 330))

        queen = pygame.Surface((80,80))
        queen.fill((202, 157, 111))
        self.__screen.blit(queen, (400, 330))
        queen_image = pygame.transform.scale(pygame.image.load(f'pieces/q_{colour.lower()}.webp'),(80,80))
        self.__screen.blit(queen_image,(400,330))

        pygame.display.update()

    def show_game_end(self,colour=None):
        grey_background = pygame.Surface((680,680),pygame.SRCALPHA,32)
        grey_background = grey_background.convert_alpha()
        grey_background.fill((0, 0, 0,150))
        self.__screen.blit(grey_background, (0, 0))

        font = pygame.font.SysFont('arialblack.ttf', 32)
        if colour == 'B':
            window = pygame.Surface((500,60))
            window.fill((246, 213, 180))
            self.__screen.blit(window, (90, 310))
            end_game_title = font.render('Checkmate against Black, White Wins!',True,(0,0,0))
            self.__screen.blit(end_game_title,(130,327))
        elif colour == 'W':
            window = pygame.Surface((500,60))
            window.fill((246, 213, 180))
            self.__screen.blit(window, (90, 310))
            end_game_title = font.render('Checkmate against White. Black Wins!',True,(0,0,0))
            self.__screen.blit(end_game_title,(130,327))
        else:
            window = pygame.Surface((200,60))
            window.fill((246, 213, 180))
            self.__screen.blit(window, (240, 310))
            end_game_title = font.render('Stalemate, Draw!',True,(0,0,0))
            self.__screen.blit(end_game_title,(250,327))
            
        pygame.display.update()

    def load_menu(self):
        grey_background = pygame.Surface((680,680),pygame.SRCALPHA,32)
        grey_background = grey_background.convert_alpha()
        grey_background.fill((0, 0, 0,150))
        self.__screen.blit(grey_background, (0, 0))

        window = pygame.Surface((400,180))
        window.fill((246, 213, 180))
        self.__screen.blit(window, (140, 250))

        font = pygame.font.SysFont('arialblack.ttf', 32)
        title = font.render('Load previous game?',True,(0,0,0))
        self.__screen.blit(title,(150,260))

        yes_btn = pygame.Surface((120,50))
        yes_btn.fill((202, 157, 111))
        self.__screen.blit(yes_btn, (190, 335))
        yes_title = font.render('Yes',True,(0,0,0))
        self.__screen.blit(yes_title,(230,350))

        no_btn = pygame.Surface((120,50))
        no_btn.fill((202, 157, 111))
        self.__screen.blit(no_btn, (370, 335))
        no_title = font.render('No',True,(0,0,0))
        self.__screen.blit(no_title,(418,350))

        pygame.display.update()

class Game():
    def __init__(self):
        self.__game_end = False
        
        UI = UserInterface()
        board = Board()
        UI.load_menu()
        self.__loading_from_file = False
        self.__difficulty_open = False
        self.__game_started = False
        self.__promotion_open = False
        self.__piece_to_promote = None
        self.__exit_game = False
        self.__load_open = True

        self.__difficulty = -1
        turn = 'W' # White goes first
        coords_old = None
        coords_new = None
        pressed = False
        
        while not self.__exit_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if self.__load_open:
                if pygame.mouse.get_pressed()[0] and not pressed:
                    pressed = True
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]
                    if x_pos > 190 and x_pos < 310 and y_pos > 335 and y_pos < 385:
                        self.__loading_from_file = True
                        UI.update_board(board.get_board())
                        self.__load_open = False
                        UI.show_dificulty()
                        self.__difficulty_open = True
                    elif x_pos > 370 and x_pos < 490 and y_pos > 335 and y_pos < 385:
                        self.__loading_from_file = False
                        UI.update_board(board.get_board())
                        self.__load_open = False
                        UI.show_dificulty()
                        self.__difficulty_open = True

            elif self.__difficulty_open: # Difficulty not selected
                if pygame.mouse.get_pressed()[0] and not pressed:
                    pressed = True
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]
                    if x_pos > 180 and x_pos < 280 and y_pos > 330 and y_pos < 380:
                        self.__difficulty = 0
                        UI.update_board(board.get_board())
                        self.__difficulty_open = False
                    elif x_pos > 290 and x_pos < 390 and y_pos > 330 and y_pos < 380:
                        self.__difficulty = 1
                        UI.update_board(board.get_board())
                        self.__difficulty_open = False
                    elif x_pos > 400 and x_pos < 500 and y_pos > 330 and y_pos < 380:
                        self.__difficulty = 2
                        UI.update_board(board.get_board())
                        self.__difficulty_open = False

            elif not self.__game_started: # Game not started but needs to start
                player1 = User('W')
                player2 = Computer('B',self.__difficulty,depth=DEPTH)
                self.__game_started = True
                if self.__loading_from_file:
                    turn = board.load_board(FILE_NAME_LOAD)
                    UI.update_board(board.get_board())
            
            elif self.__promotion_open:
                if pygame.mouse.get_pressed()[0] and not pressed:
                    pressed = True
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]
                    if x_pos > 200 and x_pos < 280 and y_pos > 330 and y_pos < 410:
                        self.__piece_to_promote.promote('N')
                        UI.update_board(board.get_board())
                        self.__promotion_open = False

                    elif x_pos > 400 and x_pos < 480 and y_pos > 330 and y_pos < 410:
                        self.__piece_to_promote.promote('Q')
                        UI.update_board(board.get_board())
                        self.__promotion_open = False
                    
                    if self.__promotion_open == False:
                        if board.valid_moves(turn, check=True) == []:
                            king = None
                            for row in board.get_board():
                                for square in row:
                                    if square != None:
                                        if square.get_type() == 'K' and square.get_colour() == turn:
                                            king = square
                                            break
                            if board.check_for_check(king):
                                self.__end_game(turn)
                                UI.show_game_end(turn)
                            else:
                                self.__end_game()
                                UI.show_game_end()

            elif not self.__game_end: # Game Started
                player_turn = player1
                if player1.get_colour() == turn:
                    player_turn = player1
                else:
                    player_turn = player2

                if pygame.mouse.get_pressed()[0] and not pressed and player_turn.get_type() == 'User':

                    pressed = True
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]
                    if x_pos > 40 and x_pos < 640 and y_pos > 40 and y_pos < 640:
                        x = ((x_pos-40) // 75)
                        y = ((y_pos-40) // 75)
                        square = board.get_board()[y][x]
                        if square != None:
                            colour = square.get_colour()
                            if colour.upper() == turn and coords_old == None:
                                coords_old = board.calculate_coordinates(x=x,y=y)
                                #print(f'Playing: {coords_old}')
                                UI.update_board(board.get_board(),green_highlight=[[x,y]])
                            elif colour.upper() == turn and coords_old != None:
                                x_old,y_old = board.calculate_coordinates(coord=coords_old)
                                if board.get_board()[y][x].get_type() == 'K' and board.get_board()[y_old][x_old].get_type() == 'R':
                                    if board.move_piece(coords_old,None,castle=True):
                                        print('Castling')
                                        board.check_pos()
                                        coords_old = None
                                        coords_new = None
                                        UI.update_board(board.get_board(),red_highlight=[[x_old,y_old],[x,y]])
                                        if turn == 'B':
                                            turn = 'W'
                                        else:
                                            turn = 'B'
                                        if board.valid_moves(turn, check=True) == []:
                                            king = None
                                            for row in board.get_board():
                                                for square in row:
                                                    if square != None:
                                                        if square.get_type() == 'K' and square.get_colour() == turn:
                                                            king = square
                                                            break
                                            if board.check_for_check(king):
                                                self.__end_game(turn)
                                                UI.show_game_end(turn)
                                            else:
                                                self.__end_game()
                                                UI.show_game_end()
                                        else:
                                            board.save_board(name=FILE_NAME_SAVE,turn=turn)
                                        
                                    else:
                                        coords_old = None
                                        coords_new = None
                                        UI.update_board(board.get_board())
                                else:
                                    coords_old = None
                                    coords_new = None
                                    UI.update_board(board.get_board())

                        if coords_new == None and coords_old != None:
                                if square != None:
                                    if square.get_colour() != turn:
                                        coords_new = board.calculate_coordinates(x=x,y=y)
                                        #print(f'To: {coords_new}')
                                        if board.move_piece(coords_old,coords_new):
                                            board.check_pos()
                                            x_old,y_old = board.calculate_coordinates(coord=coords_old)
                                            coords_old = None
                                            coords_new = None
                                            UI.update_board(board.get_board(),red_highlight=[[x_old,y_old],[x,y]])
                                            if board.promotion_check(x,y)[0]:
                                                UI.show_promotion(turn)
                                                self.__piece_to_promote = board.promotion_check(x,y)[1]
                                                self.__promotion_open = True
                                            if turn == 'B':
                                                turn = 'W'
                                            else:
                                                turn = 'B'
                                            if board.valid_moves(turn, check=True) == []:
                                                king = None
                                                for row in board.get_board():
                                                    for square in row:
                                                        if square != None:
                                                            if square.get_type() == 'K' and square.get_colour() == turn:
                                                                king = square
                                                                break
                                                if board.check_for_check(king):
                                                    self.__end_game(turn)
                                                    UI.show_game_end(turn)
                                                else:
                                                    self.__end_game()
                                                    UI.show_game_end()
                                            else:
                                                board.save_board(name=FILE_NAME_SAVE,turn=turn)
                                            
                                        else:
                                            coords_old = None
                                            coords_new = None
                                            UI.update_board(board.get_board())
                                else:
                                    coords_new = board.calculate_coordinates(x=x,y=y)
                                    #print(f'To: {coords_new}')
                                    if board.move_piece(coords_old,coords_new):
                                        board.check_pos()
                                        x_old,y_old = board.calculate_coordinates(coord=coords_old)
                                        coords_old = None
                                        coords_new = None
                                        UI.update_board(board.get_board(),red_highlight=[[x_old,y_old],[x,y]])
                                        if board.promotion_check(x,y)[0]:
                                            UI.show_promotion(turn)
                                            self.__piece_to_promote = board.promotion_check(x,y)[1]
                                            self.__promotion_open = True
                                        if turn == 'B':
                                            turn = 'W'
                                        else:
                                            turn = 'B'
                                        if board.valid_moves(turn, check=True) == []:
                                            king = None
                                            for row in board.get_board():
                                                for square in row:
                                                    if square != None:
                                                        if square.get_type() == 'K' and square.get_colour() == turn:
                                                            king = square
                                                            break
                                            if board.check_for_check(king):
                                                self.__end_game(turn)
                                                UI.show_game_end(turn)
                                            else:
                                                self.__end_game()
                                                UI.show_game_end()
                                        else:
                                            board.save_board(name=FILE_NAME_SAVE,turn=turn)
                                        
                                    else:
                                        coords_old = None
                                        coords_new = None
                                        UI.update_board(board.get_board())

                elif player_turn.get_type() == 'Computer':
                    done = False
                    x_old,y_old,x_new,y_new = player_turn.get_move(board.get_board(),board)
                    start_square = board.get_board()[y_old][x_old]
                    try:
                        end_square = board.get_board()[y_new][x_new]
                    except:
                        end_square = None
                    try:
                        if end_square == None and start_square.get_type() == 'R':
                            if board.move_piece(board.calculate_coordinates(x=x_old,y=y_old),None,castle=True):
                                board.check_pos()
                                UI.update_board(board.get_board(),red_highlight=[[x_old,y_old],[4,y_old]])
                                if turn == 'B':
                                    turn = 'W'
                                else:
                                    turn = 'B'
                                if board.valid_moves(turn, check=True) == []:
                                    king = None
                                    for row in board.get_board():
                                        for square in row:
                                            if square != None:
                                                if square.get_type() == 'K' and square.get_colour() == turn:
                                                    king = square
                                                    break
                                    if board.check_for_check(king):
                                        self.__end_game(turn)
                                        UI.show_game_end(turn)
                                    else:
                                        self.__end_game()
                                        UI.show_game_end()
                                else:
                                    board.save_board(name=FILE_NAME_SAVE,turn=turn)
                                done = True
                    except: pass
                            
                    if not done:
                        if board.move_piece(board.calculate_coordinates(x=x_old,y=y_old),board.calculate_coordinates(x=x_new,y=y_new)):
                            board.check_pos()
                            if board.promotion_check(x_new,y_new)[0]:
                                board.promotion_check(x_new,y_new)[1].promote('Q')
                            UI.update_board(board.get_board(),red_highlight=[[x_old,y_old],[x_new,y_new]])
                            if turn == 'B':
                                turn = 'W'
                            else:
                                turn = 'B'
                            if board.valid_moves(turn, check=True) == []:
                                king = None
                                for row in board.get_board():
                                    for square in row:
                                        if square != None:
                                            if square.get_type() == 'K' and square.get_colour() == turn:
                                                king = square
                                                break
                                if board.check_for_check(king):
                                    self.__end_game(turn)
                                    UI.show_game_end(turn)
                                else:
                                    self.__end_game()
                                    UI.show_game_end()
                            else:
                                board.save_board(name=FILE_NAME_SAVE,turn=turn)

            elif self.__game_end:
                continue
            
            if not pygame.mouse.get_pressed()[0] and pressed:
                pressed = False

    def __end_game(self, colour=None):
        self.__game_end = True
        if colour == 'B':
            print('Black has lost, WHITE WINS')
        elif colour == 'W':
            print('White has lost. BLACK WINS')
        else:
            print('Game Over. DRAW')

class Board():
    def __init__(self):
        self.__setup_board()

    def display_board(self, board_to_use=None):
        if board_to_use == None:
            board_to_use = self.__board_array

        pieces = {'BP':'♟', 'WP':'♙', 'BR':'♜', 'WR':'♖', 'BN':'♞', 'WN':'♘', 'BB':'♝', 'WB':'♗', 'BQ':'♛', 'WQ':'♕', 'BK':'♚', 'WK':'♔'}
        print('  a  b  c  d  e  f  g  h')
        for row in range(8):
            print(8-row, end='')
            for column in range(8):
                square = board_to_use[row][column]
                if square != None:
                    search_string = f'{square.get_colour()}{square.get_type()}'
                    print(f'[{pieces[search_string]}]',end='')
                else:
                    print('[ ]',end='')
            print()
    
    def __setup_board(self):
        self.__board_array = [
            [Piece('R','a8', 'B'),Piece('N','b8', 'B'),Piece('B','c8', 'B'),Piece('Q','d8', 'B'),Piece('K','e8', 'B'),Piece('B','f8', 'B'),Piece('N','g8', 'B'),Piece('R','h8', 'B')],
            [Piece('P','a7', 'B'),Piece('P','b7', 'B'),Piece('P','c7', 'B'),Piece('P','d7', 'B'),Piece('P','e7', 'B'),Piece('P','f7', 'B'),Piece('P','g7', 'B'),Piece('P','h7', 'B')],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [Piece('P','a2', 'W'),Piece('P','b2', 'W'),Piece('P','c2', 'W'),Piece('P','d2', 'W'),Piece('P','e2', 'W'),Piece('P','f2', 'W'),Piece('P','g2', 'W'),Piece('P','h2', 'W')],
            [Piece('R','a1', 'W'),Piece('N','b1', 'W'),Piece('B','c1', 'W'),Piece('Q','d1', 'W'),Piece('K','e1', 'W'),Piece('B','f1', 'W'),Piece('N','g1', 'W'),Piece('R','h1', 'W')]
        ]

    def save_board(self, board=None, turn='W', name='board.txt'):
        if board == None:
            board = self.__board_array
        
        final_save = f'{turn} '
        
        for row in board:
            for square in row:
                if square == None:
                    final_save = f'{final_save}[None] '
                else:
                    final_save = f'{final_save}[{square.get_type()} {square.get_location()} {square.get_colour()}] '

        file = open(name,'w')
        file.write(final_save)
        file.close()

    def load_board(self, name='board.txt'): # Loads the board into place and returns whos turn your on
        file = open(name,'r') 
        text = file.read()
        file.close()

        if text == '':
            print('The file is empty.')
            exit()

        new_board = [
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None]
        ]

        turn = text[:text.find(' ')]
        text = text[text.find(' ')+1:]

        if text == '':
            print('The file is empty.')
            exit()

        while text != '':
            object_str = text[text.find('[')+1:text.find(']')]
            text = text[text.find(']')+2:]

            if object_str == 'None':
                continue
            else:
                piece_type = object_str[:object_str.find(' ')]
                object_str = object_str[object_str.find(' ')+1:]
                piece_loc = object_str[:object_str.find(' ')]
                object_str = object_str[object_str.find(' ')+1:]
                piece_colour = object_str

                if not (piece_colour == 'W' or piece_colour == 'B'):
                    print("The colour of a piece is invalid.")
                    exit()
                
                if not (piece_type == 'P' or piece_type == 'R' or piece_type == 'N' or piece_type == 'B' or piece_type == 'Q' or piece_type == 'K'):
                    print("The type of a piece is invalid.")
                    exit()

                try:
                    x,y = self.calculate_coordinates(coord=piece_loc)
                except:
                    print("The coordinates of a piece are invalid.")
                    exit()

                try:
                    new_board[y][x] = Piece(piece_type,piece_loc,piece_colour)
                except:
                    print('There was an error creating a piece.')
                    exit()
        
        self.__board_array = copy.deepcopy(new_board)
        return turn

    def calculate_coordinates(self,coord=None,x=None,y=None):
        if coord != None:
            x = coord[0]
            y = int(coord[1])
            return (ord(x)-97), 7-(y-1)
        elif x != None and y != None:
            return f'{(chr(x+97))}{7-(y-1)}'

    def move_piece(self, coord_old, coord_new, castle=False):
        x_old, y_old = self.calculate_coordinates(coord_old)
        if not castle:
            x_new, y_new = self.calculate_coordinates(coord_new)
        else:
            x_new = None
            y_new = None

        piece_type = self.__board_array[y_old][x_old].get_type()
        piece_colour = self.__board_array[y_old][x_old].get_colour()

        validation = self.validate_move(x_old,y_old,x_new,y_new,castle)

        if validation and castle:
            if x_old == 0:
                self.__board_array[y_old][3] = self.__board_array[y_old][x_old]
                self.__board_array[y_old][3].change_location(f'd{abs(y_old-8)}')
                self.__board_array[y_old][x_old] = None
                self.__board_array[y_old][2] = self.__board_array[y_old][4]
                self.__board_array[y_old][2].change_location(f'c{abs(y_old-8)}')
                self.__board_array[y_old][4] = None
                
                self.__board_array[y_old][3].register_moved()
                self.__board_array[y_old][2].register_moved()
            elif x_old == 7:
                self.__board_array[y_old][5] = self.__board_array[y_old][x_old]
                self.__board_array[y_old][5].change_location(f'f{abs(y_old-8)}')
                self.__board_array[y_old][x_old] = None
                self.__board_array[y_old][6] = self.__board_array[y_old][4]
                self.__board_array[y_old][6].change_location(f'g{abs(y_old-8)}')
                self.__board_array[y_old][4] = None
                
                self.__board_array[y_old][5].register_moved()
                self.__board_array[y_old][6].register_moved()

            for row in self.__board_array:
                for piece in row:
                    if piece != None:
                        piece.amend_en_passant(False)
            return True

        elif validation == True:
            
            self.__board_array[y_new][x_new] = self.__board_array[y_old][x_old]
            self.__board_array[y_new][x_new].change_location(coord_new)
            self.__board_array[y_old][x_old] = None

            self.__board_array[y_new][x_new].register_moved()

            for row in self.__board_array:
                for piece in row:
                    if piece != None:
                        piece.amend_en_passant(False)

            if piece_type == 'P' and abs(y_new-y_old) == 2:
                self.__board_array[y_new][x_new].amend_en_passant(True)

            return True
        
        elif validation == (True,True):

            self.__board_array[y_new][x_new] = self.__board_array[y_old][x_old]
            self.__board_array[y_new][x_new].change_location(coord_new)
            self.__board_array[y_old][x_old] = None
            self.__board_array[y_old][x_new] = None

            self.__board_array[y_new][x_new].register_moved()

            for row in self.__board_array:
                for piece in row:
                    if piece != None:
                        piece.amend_en_passant(False)

            return True

        else:
            return False

    def validate_move(self, x_old, y_old, x_new, y_new, castle=False, board=None):
        
        if board == None:
            board = self.__board_array

        if board[y_old][x_old] != None:
            piece_type = board[y_old][x_old].get_type()
            piece_colour = board[y_old][x_old].get_colour()

        coord_new = self.calculate_coordinates(x=x_new,y=y_new)

        if castle and board[y_old][4] == None:
            return False
        elif castle:
            if board[y_old][4].get_type() != 'K' or board[y_old][4].get_colour() != piece_colour:
                return False

        new_board = copy.deepcopy(board)
        if not castle:
            new_board[y_new][x_new] = new_board[y_old][x_old]
            new_board[y_old][x_old] = None
            new_board[y_new][x_new].change_location(coord_new)
        elif x_old == 0:
            new_board[y_old][3] = new_board[y_old][x_old]
            new_board[y_old][3].change_location(f'd{abs(y_old-8)}')
            new_board[y_old][x_old] = None
            new_board[y_old][2] = new_board[y_old][4]
            new_board[y_old][2].change_location(f'c{abs(y_old-8)}')
            new_board[y_old][4] = None
        else:
            new_board[y_old][5] = new_board[y_old][x_old]
            new_board[y_old][5].change_location(f'f{abs(y_old-8)}')
            new_board[y_old][x_old] = None
            new_board[y_old][6] = new_board[y_old][4]
            new_board[y_old][6].change_location(f'g{abs(y_old-8)}')
            new_board[y_old][4] = None

        new_king = False
        for row in new_board:
            for pieceCol in row:
                if pieceCol != None:
                    if pieceCol.get_type() == 'K' and pieceCol.get_colour() == piece_colour:
                        new_king = pieceCol
                        break
            if new_king != False:
                break

        king = False
        for row in board:
            for pieceCol in row:
                if pieceCol != None:
                    if pieceCol.get_type() == 'K' and pieceCol.get_colour() == piece_colour:
                        king = pieceCol
                        break
            if king != False:
                break
        if self.check_for_check(new_king, new_board):
            return False

        # SEPERATE VALIDATION FOR CASTLING
        if castle:
            if self.check_for_check(king, board):
                return False
            piece = board[y_old][x_old]
            if piece_type != 'R' or piece.get_moved():
                return False
            
            king_slot = board[y_old][4]
            if king_slot != None:
                if king_slot.get_type() == 'K' and not king_slot.get_moved():
                    if x_old == 0:
                        for i in range(1,4):
                            if board[y_old][i] != None:
                                return False
                        return True
                    elif x_old == 7:
                        for i in range(5,7):
                            if board[y_old][i] != None:
                                return False
                        return True
            return False
        
        end_square_entity = board[y_new][x_new]

        if board[y_new][x_new] != None:
            if board[y_new][x_new].get_colour().upper() == piece_colour:
                return False
        
        if x_new < 0 or x_new > 7 or y_new < 0 or y_new > 7:
            return False

        if y_old == y_new and x_old == x_new:
            return False
        
        if piece_type == 'P' and piece_colour == 'W': # White Pawn Validation
            if x_old == x_new and y_old == y_new + 1 and end_square_entity == None:
                return True
            elif (x_old == x_new - 1 or x_old == x_new + 1) and y_old == y_new + 1 and end_square_entity != None:
                return True
            elif x_old == x_new and y_old == y_new + 2 and end_square_entity == None and y_old == 6 and board[y_old-1][x_old] == None:
                return True
            # EN PASSANT:
            elif (x_old == x_new + 1 or x_old == x_new - 1) and y_old == y_new + 1 and end_square_entity == None and self.__board_array[y_old][x_new] != None:
                if board[y_old][x_new].get_colour() != piece_colour and  self.__board_array[y_old][x_new].get_en_passant() == True and self.__board_array[y_old][x_new].get_type() == 'P':
                    return True, True
        
        elif piece_type == 'P' and piece_colour == 'B': # Black Pawn Validation
            if x_old == x_new and y_old == y_new - 1 and end_square_entity == None:
                return True
            elif (x_old == x_new - 1 or x_old == x_new + 1) and y_old == y_new - 1 and end_square_entity != None:
                return True
            elif x_old == x_new and y_old == y_new - 2 and end_square_entity == None and y_old == 1  and board[y_old+1][x_old] == None:
                return True
            # EN PASSANT:
            elif (x_old == x_new + 1 or x_old == x_new - 1) and y_old == y_new - 1 and end_square_entity == None and self.__board_array[y_old][x_new] != None:
                if board[y_old][x_new].get_colour() != piece_colour and  self.__board_array[y_old][x_new].get_en_passant() == True and self.__board_array[y_old][x_new].get_type() == 'P':
                    return True, True
        
        elif piece_type == 'R': # All Rook Validation
            if x_old == x_new and y_old < y_new:
                blocker = False
                for i in range(y_old+1,y_new):
                    if board[i][x_old] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif x_old == x_new and y_old > y_new:
                blocker = False
                for i in range(y_new+1,y_old):
                    if board[i][x_old] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif y_old == y_new and x_old < x_new:
                blocker = False
                for i in range(x_old+1,x_new):
                    if board[y_old][i] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif y_old == y_new and x_old > x_new:
                blocker = False
                for i in range(x_new+1,x_old):
                    if board[y_old][i] != None:
                        blocker = True
                if not blocker:
                    return True

        elif piece_type == 'N': # All Knight Validation
            if x_old == x_new-1 and y_old == y_new+2:
                return True
            elif x_old == x_new-2 and y_old == y_new+1:
                return True
            elif x_old == x_new-2 and y_old == y_new-1:
                return True
            elif x_old == x_new-1 and y_old == y_new-2:
                return True
            elif x_old == x_new+1 and y_old == y_new-2:
                return True
            elif x_old == x_new+2 and y_old == y_new-1:
                return True
            elif x_old == x_new+2 and y_old == y_new+1:
                return True
            elif x_old == x_new+1 and y_old == y_new+2:
                return True

        elif piece_type == 'B': # All Bishop Validation
            if x_old - x_new == y_old - y_new:
                blocker = False
                if x_old > x_new:
                    for i in range(1,x_old-x_new):
                        if board[y_old-i][x_old-i] != None:
                            blocker = True
                else:
                    for i in range(1,x_new-x_old):
                        if board[y_old+i][x_old+i] != None:
                            blocker = True
                if not blocker:
                    return True
            elif x_old - x_new == -(y_old - y_new):
                blocker = False
                if x_old > x_new:
                    for i in range(1,x_old-x_new):
                        if board[y_old+i][x_old-i] != None:
                            blocker = True
                else:
                    for i in range(1,x_new-x_old):
                        if board[y_old-i][x_old+i] != None:
                            blocker = True
                if not blocker:
                    return True
        
        elif piece_type == 'Q': # All Queen Validation
            if x_old == x_new and y_old < y_new:
                blocker = False
                for i in range(y_old+1,y_new):
                    if board[i][x_old] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif x_old == x_new and y_old > y_new:
                blocker = False
                for i in range(y_new+1,y_old):
                    if board[i][x_old] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif y_old == y_new and x_old < x_new:
                blocker = False
                for i in range(x_old+1,x_new):
                    if board[y_old][i] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif y_old == y_new and x_old > x_new:
                blocker = False
                for i in range(x_new+1,x_old):
                    if board[y_old][i] != None:
                        blocker = True
                if not blocker:
                    return True
            
            elif x_old - x_new == y_old - y_new:
                blocker = False
                if x_old > x_new:
                    for i in range(1,x_old-x_new):
                        if board[y_old-i][x_old-i] != None:
                            blocker = True
                else:
                    for i in range(1,x_new-x_old):
                        if board[y_old+i][x_old+i] != None:
                            blocker = True
                if not blocker:
                    return True
            elif x_old - x_new == -(y_old - y_new):
                blocker = False
                if x_old > x_new:
                    for i in range(1,x_old-x_new):
                        if board[y_old+i][x_old-i] != None:
                            blocker = True
                else:
                    for i in range(1,x_new-x_old):
                        if board[y_old-i][x_old+i] != None:
                            blocker = True
                if not blocker:
                    return True

        elif piece_type == 'K': # All King Validation
            if abs(x_new - x_old) <= 1 and abs(y_new-y_old) <= 1:
                return True

        return False

    def check_for_check(self, king, board_to_use=None, display=False): # Checks for check for the passed king
        self.check_pos()
        if board_to_use == None:
            board_to_use = self.__board_array

        location  = king.get_location()
        x, y = self.calculate_coordinates(location)
        colour = king.get_colour()

        # Pawn for Black King
        if colour == 'B':
            try:
                if board_to_use[y+1][x-1] != None and y+1 <= 7 and x-1 >= 0:
                    if board_to_use[y+1][x-1].get_type() == 'P' and board_to_use[y+1][x-1].get_colour() == 'W':
                        if display:
                            print(f'Pawn at {board_to_use[y+1][x-1].get_location()} is checking king')
                        #print(f'Pawn at {board_to_use[y+1][x-1].get_location()} is checking king')
                        return True
            except: pass
            try:
                if  board_to_use[y+1][x+1] != None and y+1 <= 7 and x+1 <= 7:
                    if board_to_use[y+1][x+1].get_type() == 'P' and board_to_use[y+1][x+1].get_colour() == 'W':
                        if display:
                            print(f'Pawn at {board_to_use[y+1][x+1].get_location()} is checking king')
                        #print(f'Pawn at {board_to_use[y+1][x+1].get_location()} is checking king')
                        return True
            except: pass
        # Pawn for White King
        if colour == 'W':
            try:
                if board_to_use[y-1][x-1] != None and y-1 >= 0 and x-1 >= 0:
                    if board_to_use[y-1][x-1].get_type() == 'P' and board_to_use[y-1][x-1].get_colour() == 'B':
                        if display:
                            print(f'Pawn at {board_to_use[y-1][x-1].get_location()} is checking king')
                        #print(f'Pawn at {board_to_use[y-1][x-1].get_location()} is checking king')
                        return True
            except: pass
            try:
                if  board_to_use[y-1][x+1] != None and y-1 >= 0 and x+1 <= 7:
                    if board_to_use[y-1][x+1].get_type() == 'P' and board_to_use[y-1][x+1].get_colour() == 'B':
                        if display:
                            print(f'Pawn at {board_to_use[y-1][x+1].get_location()} is checking king')
                        #print(f'Pawn at {board_to_use[y-1][x+1].get_location()} is checking king')
                        return True
            except: pass
        # Rook (+queen)
        row = y
        while row < 7:
            row += 1
            square = board_to_use[row][x]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'R' or square.get_type() == 'Q':
                        if display:
                            print(f'Rook (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        row = y
        while row > 0:
            row -= 1
            square = board_to_use[row][x]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'R' or square.get_type() == 'Q':
                        if display:
                            print(f'Rook (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        column = x
        while column < 7:
            column += 1
            square = board_to_use[y][column]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'R' or square.get_type() == 'Q':
                        if display:
                            print(f'Rook (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        column = x
        while column > 0:
            column -= 1
            square = board_to_use[y][column]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'R' or square.get_type() == 'Q':
                        if display:
                            print(f'Rook (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        # Bishop (+queen)
        row = y
        column = x
        while row < 7 and column < 7:
            row += 1
            column += 1
            square = board_to_use[row][column]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'B' or square.get_type() == 'Q':
                        if display:
                            print(f'Bishop (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        row = y
        column = x
        while row > 0 and column > 0:
            row -= 1
            column -= 1
            square = board_to_use[row][column]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'B' or square.get_type() == 'Q':
                        if display:
                            print(f'Bishop (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        row = y
        column = x
        while row > 0 and column < 7:
            row -= 1
            column += 1
            square = board_to_use[row][column]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'B' or square.get_type() == 'Q':
                        if display:
                            print(f'Bishop (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        row = y
        column = x
        while row < 7 and column > 0:
            row += 1
            column -= 1
            square = board_to_use[row][column]
            if square != None:
                if square.get_colour() == colour:
                    break
                else:
                    if square.get_type() == 'B' or square.get_type() == 'Q':
                        if display:
                            print(f'Bishop (or queen) at {square.get_location()} is checking king')
                        return True
                    else:
                        break
        # Knight
        spaces = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        for space in spaces:
            yAdd = space[0]
            xAdd = space[1]
            if xAdd+x <= 7 and xAdd+x >=0 and yAdd+y <= 7 and yAdd+y >= 0:
                square = board_to_use[y+yAdd][x+xAdd]
                if square != None:
                    if square.get_type() == 'N' and square.get_colour() != colour:
                        if display:
                            print(f'Knight at {square.get_location()} is checking king')
                        #print(f'Knight at {square.get_location()} is checking king')
                        return True

        # King on King
        spaces  = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        for space in spaces:
            yAdd = space[0]
            xAdd = space[1]
            if xAdd+x <= 7 and xAdd+x >=0 and yAdd+y <= 7 and yAdd+y >= 0:
                square = board_to_use[y+space[0]][x+space[1]]
                if square != None:
                    if square.get_type() == 'K' and square.get_colour() != colour:
                        if display:
                            print(f'King at {square.get_location()} is checking king')
                        return True
        return False

    def promotion_check(self,x,y):
        piece = self.__board_array[y][x]

        if (y == 7 or y == 0) and piece.get_type() == 'P':
            return True, piece
        else:
            return False, None

    def valid_moves(self, colour, board=None, check=False, order=False, des=True,display=False): # Returns valid moves in the form [[x_old,y_old,x_new,y_new],[x_old,y_old,x_new,y_new],...]
        valid_moves = []
        if board == None:
            board = self.__board_array
        
        for y in range(8):
            for x in range(8):
                square = board[y][x]
                if square != None:
                    t = square.get_type()
                    c = square.get_colour()
                    if c == colour:
                        if t == 'P':
                            if c == 'W':
                                try:
                                    if board[y-1][x] == None and y-1 >= 0:
                                        valid_moves.append([x,y,x,y-1])
                                except: pass
                                try:
                                    if board[y-1][x-1] != None and y-1>=0 and x-1>=0:
                                        if board[y-1][x-1].get_colour() != c:
                                            valid_moves.append([x,y,x-1,y-1])
                                except: pass
                                try:
                                    if board[y-1][x+1] != None and y-1>=0 and x+1<=7:
                                        if board[y-1][x+1].get_colour() != c:
                                            valid_moves.append([x,y,x+1,y-1])
                                except: pass
                                try:
                                    if board[y-2][x] == None and board[y-1][x] == None and y==6:
                                        valid_moves.append([x,y,x,y-2])
                                except: pass
                                try:
                                # EN PASSANT
                                    if board[y][x-1] != None:
                                        if board[y][x-1].get_type() == 'P' and board[y][x-1].get_colour() != c and board[y][x-1].get_en_passant():
                                            valid_moves.append([x,y,x-1,y-1])
                                except: pass
                                try:
                                    if board[y][x+1] != None:
                                        if board[y][x+1].get_type() == 'P' and board[y][x+1].get_colour() != c and board[y][x+1].get_en_passant():
                                            valid_moves.append([x,y,x+1,y-1])
                                except: pass

                            if c == 'B':
                                try:
                                    if board[y+1][x] == None and y+1 <= 7:
                                        valid_moves.append([x,y,x,y+1])
                                except: pass
                                try:
                                    if board[y+1][x-1] != None and y+1<=7 and x-1>=0:
                                        if board[y+1][x-1].get_colour() != c:
                                            valid_moves.append([x,y,x-1,y+1])
                                except: pass
                                try:
                                    if board[y+1][x+1] != None and y+1<=7 and x+1<=7:
                                        if board[y+1][x+1].get_colour() != c:
                                            valid_moves.append([x,y,x+1,y+1])
                                except: pass
                                try:
                                    if board[y+2][x] == None and board[y+1][x] == None and y==1:
                                        valid_moves.append([x,y,x,y+2])
                                except: pass
                                try:
                                # EN PASSANT
                                    if board[y][x-1] != None:
                                        if board[y][x-1].get_type() == 'P' and board[y][x-1].get_colour() != c and board[y][x-1].get_en_passant():
                                            valid_moves.append([x,y,x-1,y+1])
                                except: pass
                                try:
                                    if board[y][x+1] != None:
                                        if board[y][x+1].get_type() == 'P' and board[y][x+1].get_colour() != c and board[y][x+1].get_en_passant():
                                            valid_moves.append([x,y,x+1,y+1])
                                except: pass

                        elif t == 'R' or t == 'Q':
                            for i in range(x+1,8):
                                if board[y][i] == None:
                                    valid_moves.append([x,y,i,y])
                                elif board[y][i].get_colour() != c:
                                    valid_moves.append([x,y,i,y])
                                    break
                                else:
                                    break
                            
                            for i in range(x-1,-1,-1):
                                if board[y][i] == None:
                                    valid_moves.append([x,y,i,y])
                                elif board[y][i].get_colour() != c:
                                    valid_moves.append([x,y,i,y])
                                    break
                                else:
                                    break
                            
                            for i in range(y+1,8):
                                if board[i][x] == None:
                                    valid_moves.append([x,y,x,i])
                                elif board[i][x].get_colour() != c:
                                    valid_moves.append([x,y,x,i])
                                    break
                                else:
                                    break
                            
                            for i in range(y-1,-1,-1):
                                if board[i][x] == None:
                                    valid_moves.append([x,y,x,i])
                                elif board[i][x].get_colour() != c:
                                    valid_moves.append([x,y,x,i])
                                    break
                                else:
                                    break

                        if t == 'B' or t == 'Q':
                            row = y
                            column = x
                            while row < 7 and column < 7:
                                row += 1
                                column += 1
                                if board[row][column] == None:
                                    valid_moves.append([x,y,column,row])
                                elif board[row][column].get_colour() != c:
                                    valid_moves.append([x,y,column,row])
                                    break
                                else:
                                    break
                            
                            row = y
                            column = x
                            while row > 0 and column < 7:
                                row -= 1
                                column += 1
                                if board[row][column] == None:
                                    valid_moves.append([x,y,column,row])
                                elif board[row][column].get_colour() != c:
                                    valid_moves.append([x,y,column,row])
                                    break
                                else:
                                    break
                            
                            row = y
                            column = x
                            while row > 0 and column > 0:
                                row -= 1
                                column -= 1
                                if board[row][column] == None:
                                    valid_moves.append([x,y,column,row])
                                elif board[row][column].get_colour() != c:
                                    valid_moves.append([x,y,column,row])
                                    break
                                else:
                                    break

                            row = y
                            column = x
                            while row < 7 and column > 0:
                                row += 1
                                column -= 1
                                if board[row][column] == None:
                                    valid_moves.append([x,y,column,row])
                                elif board[row][column].get_colour() != c:
                                    valid_moves.append([x,y,column,row])
                                    break
                                else:
                                    break

                        elif t == 'N':
                            spaces = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
                            for space in spaces:
                                y_add = space[0]
                                x_add = space[1]
                                if x_add+x <= 7 and x_add+x >=0 and y_add+y <= 7 and y_add+y >= 0:
                                    if board[y_add+y][x_add+x] == None:
                                        valid_moves.append([x,y,x_add+x,y_add+y])
                                    elif board[y_add+y][x_add+x].get_colour() != c:
                                        valid_moves.append([x,y,x_add+x,y_add+y])
                        
                        elif t == 'K':
                            spaces  = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
                            for space in spaces:
                                y_add = space[0]
                                x_add = space[1]
                                if x_add+x <= 7 and x_add+x >=0 and y_add+y <= 7 and y_add+y >= 0:
                                    if board[y_add+y][x_add+x] == None:
                                        valid_moves.append([x,y,x_add+x,y_add+y])
                                    elif board[y_add+y][x_add+x].get_colour() != c:
                                        valid_moves.append([x,y,x_add+x,y_add+y])

                        if t == 'R' and board[y][4] != None:
                            valid = False
                            if x==0 and board[y][4].get_type() == 'K':
                                valid = True
                                for check_x in range(1,4):
                                    if board[y][check_x] != None:
                                        valid = False
                                king = board[y][4]
                                if self.check_for_check(king,board):
                                    valid = False
                                if king.get_moved():
                                    valid = False
                            elif x==7 and board[y][4].get_type() == 'K':
                                valid = True
                                for check_x in range(5,7):
                                    if board[y][check_x] != None:
                                        valid = False
                                king = board[y][4]
                                if self.check_for_check(king,board):
                                    valid = False
                                if king.get_moved():
                                    valid = False
                            if square.get_moved():
                                valid = False
                            if valid:
                                valid_moves.append([x,y,None,None])

        for move in valid_moves:
            try:
                if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7 or move[2] < 0 or move[2] > 7 or move[3] < 0 or move[3] > 7:
                    valid_moves.remove(move)
            except: pass

        if check:
            valid_moves_old = copy.deepcopy(valid_moves)
            for move in valid_moves_old:
                new_board = copy.deepcopy(board)
                if move[2] != None:
                    new_board[move[3]][move[2]] = new_board[move[1]][move[0]]
                    new_board[move[1]][move[0]] = None
                    new_board[move[3]][move[2]].change_location(self.calculate_coordinates(x=move[2],y=move[3]))
                else:
                    if move[0] == 0:
                        new_board[move[1]][3] = new_board[move[1]][move[0]]
                        new_board[move[1]][3].change_location(f'c{abs(move[1]-8)}')
                        new_board[move[1]][move[0]] = None
                        new_board[move[1]][2] = new_board[move[1]][4]
                        new_board[move[1]][2].change_location(f'd{abs(move[1]-8)}')
                        new_board[move[1]][4] = None
                    else:
                        new_board[move[1]][5] = new_board[move[1]][move[0]]
                        new_board[move[1]][5].change_location(f'f{abs(move[1]-8)}')
                        new_board[move[1]][move[0]] = None
                        new_board[move[1]][6] = new_board[move[1]][4]
                        new_board[move[1]][6].change_location(f'g{abs(move[1]-8)}')
                        new_board[move[1]][4] = None

                new_king = False
                for row in new_board:
                    for pieceCol in row:
                        if pieceCol != None:
                            if pieceCol.get_type() == 'K' and pieceCol.get_colour() == colour:
                                new_king = pieceCol
                                break
                    if new_king != False:
                        break
                
                if new_king == False:
                    print(f'''FATAL ERROR: NEW KING NOT FOUND
                          BOARD:''')
                    self.display_board(board_to_use=new_board)
                
                if self.check_for_check(new_king,new_board):
                    if display:
                        print(f"Move {move} is invalid as it puts king in check")
                    valid_moves.remove(move)

        if order:
            score_array = []
            new_valid_moves = []
            for move in valid_moves:
                new_board = self.sim_move(move,board)
                score = self.evaluate(colour=colour,board=new_board,check=False,checkmate=False)
                done = False
                for score_i in score_array:
                    if done:
                        break
                    index = score_array.index(score_i)
                    if des:
                        if score_i < score:
                            score_array.insert(index,score)
                            new_valid_moves.insert(index,move)
                            done = True
                    else:
                        if score_i > score:
                            score_array.insert(index,score)
                            new_valid_moves.insert(index,move)
                            done = True
                if not done:
                    score_array.append(score)
                    new_valid_moves.append(move)
            valid_moves = new_valid_moves

        return valid_moves

    def get_board(self):
        return self.__board_array

    def check_pos(self):
        for y in range(8):
            for x in range(8):
                square = self.__board_array[y][x]
                if square != None:
                    x1,y1 = self.calculate_coordinates(square.get_location())
                    if x != x1 or y != y1:
                        print(f'{square.get_colour()}{square.get_type()} at {x},{y} thinks its at {square.get_location()}')
                        square.change_location(self.calculate_coordinates(x=x,y=y))

    def evaluate(self,colour='W',board=None,check=False,checkmate=False): # Colour passed represents positive score
        POSSETION_WIEGHT = 0
        POSSETION_BONUS = 0.1
        PAWN_ADVANCEMENT_WIEGHT = 0.2
        CHECK_WIEGHT = 0
        CHECKMATE_WIEGHT = 9999
        STALEMATE_WIEGHT = -1
        PAWN_CENTRE_WIEGHT = 1
        
        score = 0
        if board == None:
            board = self.__board_array

        for row in board:
            for square in row:
                if square != None:
                    if square.get_type() == 'P':
                        if square.get_colour() == colour:
                            score += 1 + POSSETION_WIEGHT+POSSETION_BONUS
                            if board.index(row) >= 3 and board.index(row) <= 4 and row.index(square) >= 3 and row.index(square) <= 4:
                                score += PAWN_CENTRE_WIEGHT
                            if colour == 'W':
                                score += (6-board.index(row)) * PAWN_ADVANCEMENT_WIEGHT
                            else:
                                score += (board.index(row)-1) * PAWN_ADVANCEMENT_WIEGHT
                        else:
                            score -= 1 + POSSETION_WIEGHT
                            if board.index(row) >= 3 and board.index(row) <= 4 and row.index(square) >= 3 and row.index(square) <= 4:
                                score -= PAWN_CENTRE_WIEGHT
                            if square.get_colour() == 'W':
                                score -= (6-board.index(row)) * PAWN_ADVANCEMENT_WIEGHT
                            else:
                                score -= (board.index(row)-1) * PAWN_ADVANCEMENT_WIEGHT
                    elif square.get_type() == 'R':
                        if square.get_colour() == colour:
                            score += 5 + POSSETION_WIEGHT+POSSETION_BONUS
                        else:
                            score -= 5 + POSSETION_WIEGHT
                    elif square.get_type() == 'N':
                        if square.get_colour() == colour:
                            score += 3 + POSSETION_WIEGHT+POSSETION_BONUS
                        else:
                            score -= 3 + POSSETION_WIEGHT
                    elif square.get_type() == 'B':
                        if square.get_colour() == colour:
                            score += 3 + POSSETION_WIEGHT+POSSETION_BONUS
                        else:
                            score -= 3 + POSSETION_WIEGHT
                    elif square.get_type() == 'Q':
                        if square.get_colour() == colour:
                            score += 10 + POSSETION_WIEGHT+POSSETION_BONUS
                        else:
                            score -= 10 + POSSETION_WIEGHT
                    elif square.get_type() == 'K':
                        if square.get_colour() == colour:
                            score += 100 + POSSETION_WIEGHT+POSSETION_BONUS
                        else:
                            score -= 100 + POSSETION_WIEGHT
                        
                        if check:
                            if self.check_for_check(square,board):
                                if square.get_colour() == colour:
                                    score -= CHECK_WIEGHT
                                    if checkmate:
                                        if self.valid_moves(square.get_colour(),board,check=True)==[]:
                                            score -= CHECKMATE_WIEGHT
                                else:
                                    score += CHECK_WIEGHT
                                    if checkmate:
                                        if self.valid_moves(square.get_colour(),board,check=True)==[]:
                                            score += CHECKMATE_WIEGHT
                            else:
                                if square.get_colour() == colour:
                                    if self.valid_moves(square.get_colour(),board,check=True)==[]:
                                        score += STALEMATE_WIEGHT
                                else:
                                    if self.valid_moves(square.get_colour(),board,check=True)==[]:
                                        score -= STALEMATE_WIEGHT

        return score

    def sim_move(self,move,board):
        new_board = copy.deepcopy(board)
        if move[2] != None:
            new_board[move[3]][move[2]] = new_board[move[1]][move[0]]
            new_board[move[1]][move[0]] = None
            new_board[move[3]][move[2]].change_location(self.calculate_coordinates(x=move[2],y=move[3]))

            if (move[3] == 0 or move[3] == 7) and new_board[move[3]][move[2]].get_type() == 'P':
                new_board[move[3]][move[2]].promote('Q')
        else:
            if move[0] == 0:
                new_board[move[1]][3] = new_board[move[1]][move[0]]
                new_board[move[1]][3].change_location(f'd{abs(move[1]-8)}')
                new_board[move[1]][move[0]] = None
                new_board[move[1]][2] = new_board[move[1]][4]
                new_board[move[1]][2].change_location(f'c{abs(move[1]-8)}')
                new_board[move[1]][4] = None
            else:
                new_board[move[1]][5] = new_board[move[1]][move[0]]
                new_board[move[1]][5].change_location(f'f{abs(move[1]-8)}')
                new_board[move[1]][move[0]] = None
                new_board[move[1]][6] = new_board[move[1]][4]
                new_board[move[1]][6].change_location(f'g{abs(move[1]-8)}')
                new_board[move[1]][4] = None
        return new_board

class Piece():
    def __init__(self, piece_type, location, colour):
        self.__type = piece_type
        self.__location = location
        self.__colour = colour
        self.__en_passant_sus = False # True when pawn is suseptable to en passant
        self.__moved = False
    
    def get_colour(self):
        return self.__colour
    
    def get_type(self):
        return self.__type
    
    def get_location(self):
        return self.__location
    
    def change_location(self, coords):
        self.__location = coords

    def promote(self, piece):
        if self.__type == 'P':
            self.__type = piece

    def register_moved(self):
        self.__moved = True

    def amend_en_passant(self, status):
        if status != self.__en_passant_sus:
            self.__en_passant_sus = status
    
    def get_en_passant(self):
        return self.__en_passant_sus
    
    def get_moved(self):
        return self.__moved

class Player(abc.ABC):
    def __init__(self, colour):
        self.__colour = colour
    
    def get_colour(self):
        return self.__colour
    
    def get_move(self):
        return
    
    def get_type(self):
        return None

class User(Player):
    def __init__(self, colour):
        super().__init__(colour)
    
    def get_type(self):
        return 'User'

class Computer(Player):
    def __init__(self, colour, difficulty, depth):
        super().__init__(colour)
        self.__difficulty = difficulty
        self.__colour = colour
        self.__DEPTH = depth

        self.__initial_depth = -1

    def get_move(self, board_to_use,board):
        if self.__difficulty == 0:
            print('Random move')
            return self.__random_move(board_to_use,board)
        elif self.__difficulty == 1:
            print('Basic move')
            return self.__basic_move(board_to_use,board)
        elif self.__difficulty == 2:
            print('Advanced move')
            return self.__adv_move(board_to_use,board)
    
    def __random_move(self, board_to_use,board):
        valid_moves = board.valid_moves(self.__colour,board=board_to_use,check=True)
        chosen = random.choice(valid_moves)
        return chosen[0],chosen[1],chosen[2],chosen[3]

    def __basic_move(self,board_to_use,board):
        valid_moves = board.valid_moves(self.__colour,board=board_to_use,check=True)
        top_score = float('-inf')
        top_move = None
        top_moves = []
        for move in valid_moves:
            new_board = board.sim_move(move,board_to_use)
            score = board.evaluate(self.__colour,new_board,check=True,checkmate=True)
            if score > top_score:
                top_score = score
                top_move = move
                top_moves = [top_move]
            elif score == top_score:
                top_moves.append(move)
        if len(top_moves) > 1:
            top_move = random.choice(top_moves)
        return top_move[0],top_move[1],top_move[2],top_move[3]

    def __adv_move(self,board_to_use,board):
        if self.__DEPTH == -1:
            length = len(board.valid_moves(self.__colour,check=True))
            if length <= 10:
                depth = 3
            else:
                depth = 2
        else:
            depth = self.__DEPTH
        self.__initial_depth = depth
        timeStart = time.time()
        score,top_move = self.__min_max(board_to_use,board,depth,float('-inf'),float('+inf'))
        print()
        print(f'DEPTH: {depth}')
        print(f'TOP SCORE: {score}')
        print(f'TIME TAKEN: {time.time()-timeStart}')
        return top_move[0],top_move[1],top_move[2],top_move[3]

    def __min_max(self,board_to_use,board,depth,alpha,beta,maximising=True): # maximising is true for maximising and false for minimising. SHOULD ALWAYS START AS TRUE
        if depth == 0:
            return board.evaluate(colour=self.__colour,board=board_to_use,check=True,checkmate=True), None

        if maximising:
            max_score = float('-inf')
            max_score_move = None

            order = False
            if depth > 1:
                order = True

            possible_moves = board.valid_moves(self.__colour, board=board_to_use, check=True,order=order,des=True)
            for move in possible_moves:
                if self.__initial_depth == depth:
                    index = possible_moves.index(move)
                    length = len(possible_moves)
                    print('|'+('#'*(index+1))+('-'*(length-(index+1)))+'|',end='\r')

                new_board = board.sim_move(move,board_to_use)
                score,m = self.__min_max(new_board,board,depth-1,alpha,beta,maximising=False)

                if score > max_score:
                    max_score = score
                    max_score_move = move
                if alpha<max_score:
                    alpha = max_score
                if beta <= alpha:
                    break
            if max_score_move == None:
                return board.evaluate(colour=self.__colour,board=board_to_use,check=True,checkmate=True), None
            return max_score,max_score_move
        else:
            min_score = float('+inf')
            min_score_move = None

            if self.__colour == 'W':
                colour = 'B'
            else:
                colour = 'W'

            order = False
            if depth > 1:
                order = True

            possible_moves = board.valid_moves(colour, board=board_to_use, check=True,order=order,des=False)
            for move in possible_moves:
                new_board = board.sim_move(move,board_to_use)
                
                score,m = self.__min_max(new_board,board,depth-1,alpha,beta,maximising=True)
                if score < min_score:
                    min_score = score
                    min_score_move = move
                if beta>min_score: 
                    beta = min_score
                if beta <= alpha:
                    break
            if min_score_move == None:
                return board.evaluate(colour=self.__colour,board=board_to_use,check=True,checkmate=True), None
            return min_score,min_score_move
                    
    def get_type(self):
        return 'Computer'

def MainProgram():
    main_board = Game()

if __name__ == '__main__':
    MainProgram()
