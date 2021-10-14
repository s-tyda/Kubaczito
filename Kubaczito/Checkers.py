from IPython.external.qt_for_kernel import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QWidget
import sys


class Square(QLabel):
    def __init__(self, parent, row, column, color):
        super().__init__(parent)
        self.row = row
        self.column = column
        self.color = color
        self.setGeometry(column * 100, row * 100, 100, 100)
        self.show()


class Checker(QLabel):
    def __init__(self, parent, row, column, color):
        super().__init__(parent)
        self.parent = parent
        self.row = row
        self.column = column
        self.color = color
        self.setGeometry(column * 100 + 5, row * 100 + 5, 90, 90)
        self.setScaledContents(True)
        self.setPixmap(QtGui.QPixmap(f'./assets/{color}_checkers.png'))
        self.show()

    def position(self, row, column):
        self.setGeometry(column * 100 + 5, row * 100 + 5, 90, 90)
        self.row = row
        self.column = column

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            pos = event.windowPos()
            x = pos.x()
            y = pos.y()
            self.move(x - 40, y - 40)

    def move_checker(self, x, y):
        self.parent.checkers[y][x] = self.parent.checkers[self.row][self.column]
        self.parent.checkers[self.row][self.column] = None
        self.position(y, x)
        self.row = y
        self.column = x
        self.parent.gracz = not self.parent.gracz
        if self.color == 'red':
            self.parent.setWindowTitle(f"GREEN TURN")
        else:
            self.parent.setWindowTitle(f"RED TURN")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        pos = event.windowPos()
        x = pos.x()
        y = pos.y()
        x = int(x // 100)
        y = int(y // 100)
        board = self.parent.board
        deltay = self.row - y
        deltax = self.column - x
        d = abs(deltax) == abs(deltay)
        one_square_move = abs(deltax) == 1
        two_square_move = abs(deltax) == 2

        if board[y][x].color == "black" \
                and ((self.color == "red" and not self.parent.gracz)
                     or (self.color == "green" and self.parent.gracz)) \
                and 8 > x > -1 \
                and 8 > y > -1 \
                and self.parent.checkers[y][x] is None \
                and d:
            if one_square_move \
                    and ((self.color == "red" and deltay < 0)
                         or (self.color == "green" and deltay > 0)):
                self.move_checker(x, y)
            elif two_square_move \
                    and self.parent.checkers[int(y + deltay / 2)][int(x + deltax / 2)] is not None \
                    and self.parent.checkers[int(y + deltay / 2)][int(x + deltax / 2)].color != self.color:
                self.parent.checkers[int(y + deltay / 2)][int(x + deltax / 2)].hide()
                self.parent.checkers[int(y + deltay / 2)][int(x + deltax / 2)] = None
                self.move_checker(x, y)
            else:
                self.position(self.row, self.column)
        else:
            self.position(self.row, self.column)

        red_win = True
        green_win = True
        for i in range(len(self.parent.checkers)):
            for j in range(len(self.parent.checkers)):
                if self.parent.checkers[i][j] is None:
                    continue
                if self.parent.checkers[i][j].color == "red":
                    green_win = False
                if self.parent.checkers[i][j].color == "green":
                    red_win = False

        if green_win:
            QMessageBox.warning(self.parent, "Win!", "Green player won!", QMessageBox.Ok)
            sys.exit(app.exec())
        if red_win:
            QMessageBox.warning(self.parent, "Win!", "Red player won!", QMessageBox.Ok)
            sys.exit(app.exec())


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.gracz = True
        self.title = "GREEN TURN"
        self.top = 0
        self.left = 0
        self.width = 800
        self.height = 800
        self.setWindowIcon(QtGui.QIcon("./assets/icon.png"))
        self.setWindowTitle(self.title)
        self.gui = QLabel(self)
        self.gui.setPixmap(QtGui.QPixmap('assets/field.png'))
        self.gui.setScaledContents(True)
        self.gui.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.board = self.make_board()
        self.checkers = self.make_checkers()

    def make_board(self):
        board = []
        black = False
        for row_number in range(8):
            row = []
            for column in range(8):
                if black:
                    row.append(Square(self, row_number, column, "black"))
                    black = not black
                else:
                    row.append(Square(self, row_number, column, "white"))
                    black = not black
            black = not black
            board.append(row)
        return board

    def make_checkers(self):
        checkers = []
        for row_number in range(8):
            row = []
            for column in range(8):
                if row_number < 3 and self.board[row_number][column].color == "black":
                    row.append(Checker(self, row_number, column, "red"))
                elif row_number > 4 and self.board[row_number][column].color == "black":
                    row.append(Checker(self, row_number, column, "green"))
                else:
                    row.append(None)
            checkers.append(row)
        return checkers


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
