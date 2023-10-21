import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Tic-Tac-Toe')
        self.setGeometry(100, 100, 400, 400)
        
        self.layout = QVBoxLayout()
        self.grid_layout = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = 'X'
        
        for row in range(3):
            hbox = QHBoxLayout()
            for col in range(3):
                button = QPushButton('', self)
                button.clicked.connect(lambda checked, row=row, col=col: self.on_button_click(row, col))
                button.setStyleSheet('font-size: 24px; padding: 20px;')
                hbox.addWidget(button)
                self.grid_layout[row][col] = button
            self.layout.addLayout(hbox)
        
        self.setLayout(self.layout)
    
    def on_button_click(self, row, col):
        button = self.grid_layout[row][col]
        if button.text() == '':
            button.setText(self.current_player)
            button.setStyleSheet('font-size: 24px; padding: 20px; color: red;' if self.current_player == 'X' else
                                'font-size: 24px; padding: 20px; color: blue;')
            if self.check_win(row, col):
                self.show_message(f'Player {self.current_player} wins!')
                self.reset_game()
            elif self.check_draw():
                self.show_message("It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_win(self, row, col):
        for i in range(3):
            if self.grid_layout[i][col].text() != self.current_player:
                break
        else:
            return True
        
        for j in range(3):
            if self.grid_layout[row][j].text() != self.current_player:
                break
        else:
            return True
        
        if row == col:
            for i in range(3):
                if self.grid_layout[i][i].text() != self.current_player:
                    break
            else:
                return True
        
        if row + col == 2:
            for i in range(3):
                if self.grid_layout[i][2 - i].text() != self.current_player:
                    break
            else:
                return True
        
        return False
    
    def check_draw(self):
        for row in self.grid_layout:
            for button in row:
                if button.text() == '':
                    return False
        return True
    
    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle('Game Over')
        msg_box.exec_()
    
    def reset_game(self):
        for row in self.grid_layout:
            for button in row:
                button.setText('')
                button.setStyleSheet('font-size: 24px; padding: 20px;')
        self.current_player = 'X'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
