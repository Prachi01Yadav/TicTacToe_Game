import math

class Game:
    def __init__(self):
        self.board = [""] * 9
        self.turn = "O"  # Human = 'O', AI = 'X'
        self.winner = None
        self.ai_difficulty = "hard"  # easy, medium, hard

    def make_move(self, index):
        if self.board[index] == "" and self.winner is None:
            self.board[index] = self.turn
            self.check_winner()
            if self.winner is None:
                self.turn = "X" if self.turn == "O" else "O"
                if self.turn == "X":
                    self.ai_move()
            return True
        return False

    def check_winner(self):
        win_patterns = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for a,b,c in win_patterns:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.board[a]
                return
        if all(cell != "" for cell in self.board):
            self.winner = "Draw"

    def ai_move(self):
        if self.ai_difficulty == "easy":
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    break
        elif self.ai_difficulty == "medium":
            import random
            empty = [i for i,v in enumerate(self.board) if v == ""]
            if random.random() < 0.5:
                self.board[random.choice(empty)] = "X"
            else:
                move = self.best_move()
                if move is not None:
                    self.board[move] = "X"
        else:
            move = self.best_move()
            if move is not None:
                self.board[move] = "X"
        self.check_winner()
        self.turn = "O"

    def best_move(self):
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"
                score = self.minimax(False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def minimax(self, is_max):
        winner = self.check_winner_for_minimax()
        if winner == "X": return 1
        if winner == "O": return -1
        if winner == "Draw": return 0

        if is_max:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    score = self.minimax(False)
                    self.board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    score = self.minimax(True)
                    self.board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner_for_minimax(self):
        win_patterns = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for a,b,c in win_patterns:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if all(cell != "" for cell in self.board):
            return "Draw"
        return None
