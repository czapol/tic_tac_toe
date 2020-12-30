class Game:
    
    def __init__(self):
        self.player1=input("What is player one's name?"\n)
        self.player2=input("What is player one's name?"\n)
        self.game_counter=0
        self.scores={}
     
        
    
    def play(self):
        
        """
        Start tic tac toe session
        
        Args:
        None
        Returns: 
        none
        
        """
        self.moves = {'A':'A','B':'B','C':'C',
                     'D':'D','E':'E','F':'F',
                     'G':'G','H':'H','I':'I'
                     }
        self.player_moves={self.player1:set(),self.player:set()}
        self.stop = False 
        self.switch = True
        self.round = 0
      
       
        
        while not self.stop:
            self.print_board
            if self.switch=True:
                player = self.player1
            else:
                player = self.player2
            
           move=self.ask_move(player)
           self.player_moves[player].add(move)
            
           self.round +=1
           if self.round >=5:
                is_winner=self.check_status(self.player_moves[player])
                if is_winner:
                    self.stop=True
                    print(f'{player} won')
                    continue
                
                
          
            
        self.game_counter +=1
        self.scores[self.game_counter]=player
        
    def ask_move(self,player):
        valid_move = False
        move = insert(f'what is your next move {player}')
        
        while not valid_move:
            if move == 'stop':
                self.stop = True
                valid_move = True 
                
            elif move not in ('ABCDEFGHI'):
                move=insert('This not a valid field, choose again')
            elif self.moves[move]=='o' or self.moves[move]=='x':
                move=insert('This field is taken, choose again')
            else:
                valid_move = True
        if player == self.player1:
            self.moves[move]='o'
        else:
            self.moves[move]='x'
            
        return move 
                
            
  
        
    
    def print_board(self):
        """
        prints the board 
        
        Args:
        None
        Returns: 
        none
        
        """
        print(f"{self.moves['A']}|{self.moves['B']}|{self.moves['C']}")
        print(f"{self.moves['D']}|{self.moves['E']}|{self.moves['F']}")
        print(f"{self.moves['G']}|{self.moves['H']}|{self.moves['I']}")
        
    
    def check_status(self,player_moves):
        winning_combinations = [{'A','B','C'},{'A','E','I'},{'G','E','C'},{'D','E','F'},{'A','D','G'},{'B','E','H'},{'I','F','C'}]
        for combination in winning_combinations:
            if combination-player_moves == set():
                return True
        return False 
        
    def print_results(self):
        
        """
        prints the scores
        
        Args:
        None
        Returns: 
        none
        
        """
        for game,scores in self.scores.items():
            print( f'game {games}, winner: {scores}')
    

    