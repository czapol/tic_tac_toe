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
        self.player1moves=set()
        self.player2moves=set()
        
        
    def ask_move(self):
        pass
    
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
            print( f'game {games}, score: {scores}')
    

    