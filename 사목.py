import random
from tkinter import*
import tkinter.simpledialog

class Samoc:
    def again(self):
        for r in range(6):
             for c in range(7):
                 self.buttonList[r*7+c].configure(image=self.imageList[2])
                 self.buttonList[r*7+c].configure(text=' ')
    def pressed(self,r,c):
        for i in range(5,-1,-1) : #5 4 3 2 1 0
            if self.result == True:
                if self.buttonList[i*7+c]['text'] ==' ':
                    if self.turn: #o차례
                        self.buttonList[i * 7 + c].configure(image=self.imageList[0])
                        self.buttonList[i*7+c].configure(text='O')
                    else:
                        self.buttonList[i * 7 + c].configure(image=self.imageList[1])
                        self.buttonList[i * 7 + c].configure(text='X')
                    self.turn = not self.turn
                    if self.buttonList[41]['text'] == 'O' and self.buttonList[40]['text'] == 'O' and self.buttonList[39]['text'] == 'O' and self.buttonList[38]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[40]['text'] == 'O' and self.buttonList[39]['text'] == 'O' and self.buttonList[38]['text'] == 'O' and self.buttonList[37]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[39]['text'] == 'O' and self.buttonList[38]['text'] == 'O' and self.buttonList[37]['text'] == 'O' and self.buttonList[36]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[38]['text'] == 'O' and self.buttonList[37]['text'] == 'O' and self.buttonList[36]['text'] == 'O' and self.buttonList[35]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[34]['text'] == 'O' and self.buttonList[33]['text'] == 'O' and self.buttonList[32]['text'] == 'O' and self.buttonList[31]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[33]['text'] == 'O' and self.buttonList[32]['text'] == 'O' and self.buttonList[31]['text'] == 'O' and self.buttonList[30]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[32]['text'] == 'O' and self.buttonList[31]['text'] == 'O' and self.buttonList[30]['text'] == 'O' and self.buttonList[29]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[31]['text'] == 'O' and self.buttonList[30]['text'] == 'O' and self.buttonList[29]['text'] == 'O' and self.buttonList[28]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[27]['text'] == 'O' and self.buttonList[26]['text'] == 'O' and self.buttonList[25]['text'] == 'O' and self.buttonList[24]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[26]['text'] == 'O' and self.buttonList[25]['text'] == 'O' and self.buttonList[24]['text'] == 'O' and self.buttonList[23]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[25]['text'] == 'O' and self.buttonList[24]['text'] == 'O' and self.buttonList[23]['text'] == 'O' and self.buttonList[22]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[24]['text'] == 'O' and self.buttonList[23]['text'] == 'O' and self.buttonList[22]['text'] == 'O' and self.buttonList[21]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[20]['text'] == 'O' and self.buttonList[19]['text'] == 'O' and self.buttonList[18]['text'] == 'O' and self.buttonList[17]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[19]['text'] == 'O' and self.buttonList[18]['text'] == 'O' and self.buttonList[17]['text'] == 'O' and self.buttonList[16]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[18]['text'] == 'O' and self.buttonList[17]['text'] == 'O' and self.buttonList[16]['text'] == 'O' and self.buttonList[15]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[17]['text'] == 'O' and self.buttonList[16]['text'] == 'O' and self.buttonList[15]['text'] == 'O' and self.buttonList[14]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[13]['text'] == 'O' and self.buttonList[12]['text'] == 'O' and self.buttonList[11]['text'] == 'O' and self.buttonList[10]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[12]['text'] == 'O' and self.buttonList[11]['text'] == 'O' and self.buttonList[10]['text'] == 'O' and self.buttonList[9]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[11]['text'] == 'O' and self.buttonList[10]['text'] == 'O' and self.buttonList[9]['text'] == 'O' and self.buttonList[8]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[10]['text'] == 'O' and self.buttonList[9]['text'] == 'O' and self.buttonList[8]['text'] == 'O' and self.buttonList[7]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[6]['text'] == 'O' and self.buttonList[5]['text'] == 'O' and self.buttonList[4]['text'] == 'O' and self.buttonList[3]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[5]['text'] == 'O' and self.buttonList[4]['text'] == 'O' and self.buttonList[3]['text'] == 'O' and self.buttonList[2]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[4]['text'] == 'O' and self.buttonList[3]['text'] == 'O' and self.buttonList[2]['text'] == 'O' and self.buttonList[1]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[3]['text'] == 'O' and self.buttonList[2]['text'] == 'O' and self.buttonList[1]['text'] == 'O' and self.buttonList[0]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result =False
                    if self.buttonList[41]['text'] == 'X' and self.buttonList[40]['text'] == 'X' and self.buttonList[39]['text'] == 'X' and self.buttonList[38]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[40]['text'] == 'X' and self.buttonList[39]['text'] == 'X' and self.buttonList[38]['text'] == 'X' and self.buttonList[37]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[39]['text'] == 'X' and self.buttonList[38]['text'] == 'X' and self.buttonList[37]['text'] == 'X' and self.buttonList[36]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[38]['text'] == 'X' and self.buttonList[37]['text'] == 'X' and self.buttonList[36]['text'] == 'X' and self.buttonList[35]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[34]['text'] == 'X' and self.buttonList[33]['text'] == 'X' and self.buttonList[32]['text'] == 'X' and self.buttonList[31]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[33]['text'] == 'X' and self.buttonList[32]['text'] == 'X' and self.buttonList[31]['text'] == 'X' and self.buttonList[30]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[32]['text'] == 'X' and self.buttonList[31]['text'] == 'X' and self.buttonList[30]['text'] == 'X' and self.buttonList[29]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[31]['text'] == 'X' and self.buttonList[30]['text'] == 'X' and self.buttonList[29]['text'] == 'X' and self.buttonList[28]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[27]['text'] == 'X' and self.buttonList[26]['text'] == 'X' and self.buttonList[25]['text'] == 'X' and self.buttonList[24]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[26]['text'] == 'X' and self.buttonList[25]['text'] == 'X' and self.buttonList[24]['text'] == 'X' and self.buttonList[23]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[25]['text'] == 'X' and self.buttonList[24]['text'] == 'X' and self.buttonList[23]['text'] == 'X' and self.buttonList[22]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[24]['text'] == 'X' and self.buttonList[23]['text'] == 'X' and self.buttonList[22]['text'] == 'X' and self.buttonList[21]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[20]['text'] == 'X' and self.buttonList[19]['text'] == 'X' and self.buttonList[18]['text'] == 'X' and self.buttonList[17]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[19]['text'] == 'X' and self.buttonList[18]['text'] == 'X' and self.buttonList[17]['text'] == 'X' and self.buttonList[16]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[18]['text'] == 'X' and self.buttonList[17]['text'] == 'X' and self.buttonList[16]['text'] == 'X' and self.buttonList[15]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[17]['text'] == 'X' and self.buttonList[16]['text'] == 'X' and self.buttonList[15]['text'] == 'X' and self.buttonList[14]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[13]['text'] == 'X' and self.buttonList[12]['text'] == 'X' and self.buttonList[11]['text'] == 'X' and self.buttonList[10]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[12]['text'] == 'X' and self.buttonList[11]['text'] == 'X' and self.buttonList[10]['text'] == 'X' and self.buttonList[9]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[11]['text'] == 'X' and self.buttonList[10]['text'] == 'X' and self.buttonList[9]['text'] == 'X' and self.buttonList[8]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[10]['text'] == 'X' and self.buttonList[9]['text'] == 'X' and self.buttonList[8]['text'] == 'X' and self.buttonList[7]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[6]['text'] == 'X' and self.buttonList[5]['text'] == 'X' and self.buttonList[4]['text'] == 'X' and self.buttonList[3]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[5]['text'] == 'X' and self.buttonList[4]['text'] == 'X' and self.buttonList[3]['text'] == 'X' and self.buttonList[2]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[4]['text'] == 'X' and self.buttonList[3]['text'] == 'X' and self.buttonList[2]['text'] == 'X' and self.buttonList[1]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[3]['text'] == 'X' and self.buttonList[2]['text'] == 'X' and self.buttonList[1]['text'] == 'X' and self.buttonList[0]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False


                    elif self.buttonList[0]['text'] == 'X' and self.buttonList[7]['text'] == 'X' and self.buttonList[14]['text'] == 'X' and self.buttonList[21]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[7]['text'] == 'X' and self.buttonList[14]['text'] == 'X' and self.buttonList[21]['text'] == 'X' and self.buttonList[28]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False
                    elif self.buttonList[14]['text'] == 'X' and self.buttonList[21]['text'] == 'X' and self.buttonList[28]['text'] == 'X' and self.buttonList[35]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result =False


                    elif self.buttonList[1]['text'] == 'X' and self.buttonList[8]['text'] == 'X' and \
                            self.buttonList[15]['text'] == 'X' and self.buttonList[22]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[8]['text'] == 'X' and self.buttonList[15]['text'] == 'X' and \
                            self.buttonList[22]['text'] == 'X' and self.buttonList[29]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[15]['text'] == 'X' and self.buttonList[22]['text'] == 'X' and \
                            self.buttonList[29]['text'] == 'X' and self.buttonList[36]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[2]['text'] == 'X' and self.buttonList[9]['text'] == 'X' and \
                            self.buttonList[16]['text'] == 'X' and self.buttonList[23]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[9]['text'] == 'X' and self.buttonList[16]['text'] == 'X' and \
                            self.buttonList[23]['text'] == 'X' and self.buttonList[30]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[16]['text'] == 'X' and self.buttonList[23]['text'] == 'X' and \
                            self.buttonList[30]['text'] == 'X' and self.buttonList[37]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[3]['text'] == 'X' and self.buttonList[10]['text'] == 'X' and \
                            self.buttonList[17]['text'] == 'X' and self.buttonList[24]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[10]['text'] == 'X' and self.buttonList[17]['text'] == 'X' and \
                            self.buttonList[24]['text'] == 'X' and self.buttonList[31]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[17]['text'] == 'X' and self.buttonList[24]['text'] == 'X' and \
                            self.buttonList[31]['text'] == 'X' and self.buttonList[38]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[4]['text'] == 'X' and self.buttonList[11]['text'] == 'X' and \
                            self.buttonList[18]['text'] == 'X' and self.buttonList[25]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[11]['text'] == 'X' and self.buttonList[18]['text'] == 'X' and \
                            self.buttonList[25]['text'] == 'X' and self.buttonList[32]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[18]['text'] == 'X' and self.buttonList[25]['text'] == 'X' and \
                            self.buttonList[32]['text'] == 'X' and self.buttonList[39]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[5]['text'] == 'X' and self.buttonList[12]['text'] == 'X' and \
                            self.buttonList[19]['text'] == 'X' and self.buttonList[26]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[12]['text'] == 'X' and self.buttonList[19]['text'] == 'X' and \
                            self.buttonList[26]['text'] == 'X' and self.buttonList[33]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[19]['text'] == 'X' and self.buttonList[26]['text'] == 'X' and \
                            self.buttonList[33]['text'] == 'X' and self.buttonList[40]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[6]['text'] == 'X' and self.buttonList[13]['text'] == 'X' and \
                            self.buttonList[20]['text'] == 'X' and self.buttonList[27]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[13]['text'] == 'X' and self.buttonList[20]['text'] == 'X' and \
                            self.buttonList[27]['text'] == 'X' and self.buttonList[34]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[20]['text'] == 'X' and self.buttonList[27]['text'] == 'X' and \
                            self.buttonList[34]['text'] == 'X' and self.buttonList[41]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False




                    elif self.buttonList[1]['text'] == 'O' and self.buttonList[8]['text'] == 'O' and \
                            self.buttonList[15]['text'] == 'O' and self.buttonList[22]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[8]['text'] == 'O' and self.buttonList[15]['text'] == 'O' and \
                            self.buttonList[22]['text'] == 'O' and self.buttonList[29]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[15]['text'] == 'O' and self.buttonList[22]['text'] == 'O' and \
                            self.buttonList[29]['text'] == 'O' and self.buttonList[36]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[2]['text'] == 'O' and self.buttonList[9]['text'] == 'O' and \
                            self.buttonList[16]['text'] == 'O' and self.buttonList[23]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[9]['text'] == 'O' and self.buttonList[16]['text'] == 'O' and \
                            self.buttonList[23]['text'] == 'O' and self.buttonList[30]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[16]['text'] == 'O' and self.buttonList[23]['text'] == 'O' and \
                            self.buttonList[30]['text'] == 'O' and self.buttonList[37]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[3]['text'] == 'O' and self.buttonList[10]['text'] == 'O' and \
                            self.buttonList[17]['text'] == 'O' and self.buttonList[24]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[10]['text'] == 'O' and self.buttonList[17]['text'] == 'O' and \
                            self.buttonList[24]['text'] == 'O' and self.buttonList[31]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[17]['text'] == 'O' and self.buttonList[24]['text'] == 'O' and \
                            self.buttonList[31]['text'] == 'O' and self.buttonList[38]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[4]['text'] == 'O' and self.buttonList[11]['text'] == 'O' and \
                            self.buttonList[18]['text'] == 'O' and self.buttonList[25]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[11]['text'] == 'O' and self.buttonList[18]['text'] == 'O' and \
                            self.buttonList[25]['text'] == 'O' and self.buttonList[32]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[18]['text'] == 'O' and self.buttonList[25]['text'] == 'O' and \
                            self.buttonList[32]['text'] == 'O' and self.buttonList[39]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[5]['text'] == 'O' and self.buttonList[12]['text'] == 'O' and \
                            self.buttonList[19]['text'] == 'O' and self.buttonList[26]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[12]['text'] == 'O' and self.buttonList[19]['text'] == 'O' and \
                            self.buttonList[26]['text'] == 'O' and self.buttonList[33]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[19]['text'] == 'O' and self.buttonList[26]['text'] == 'O' and \
                            self.buttonList[33]['text'] == 'O' and self.buttonList[40]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[6]['text'] == 'O' and self.buttonList[13]['text'] == 'O' and \
                            self.buttonList[20]['text'] == 'O' and self.buttonList[27]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[13]['text'] == 'O' and self.buttonList[20]['text'] == 'O' and \
                            self.buttonList[27]['text'] == 'O' and self.buttonList[34]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[20]['text'] == 'O' and self.buttonList[27]['text'] == 'O' and \
                            self.buttonList[34]['text'] == 'O' and self.buttonList[41]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False




                    elif self.buttonList[39]['text'] == 'O' and self.buttonList[31]['text'] == 'O' and \
                            self.buttonList[23]['text'] == 'O' and self.buttonList[15]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[31]['text'] == 'O' and self.buttonList[23]['text'] == 'O' and \
                            self.buttonList[15]['text'] == 'O' and self.buttonList[7]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[38]['text'] == 'O' and self.buttonList[30]['text'] == 'O' and \
                            self.buttonList[22]['text'] == 'O' and self.buttonList[14]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[40]['text'] == 'O' and self.buttonList[32]['text'] == 'O' and \
                            self.buttonList[24]['text'] == 'O' and self.buttonList[16]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[32]['text'] == 'O' and self.buttonList[24]['text'] == 'O' and \
                            self.buttonList[16]['text'] == 'O' and self.buttonList[8]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[24]['text'] == 'O' and self.buttonList[16]['text'] == 'O' and \
                            self.buttonList[8]['text'] == 'O' and self.buttonList[0]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[41]['text'] == 'O' and self.buttonList[33]['text'] == 'O' and \
                            self.buttonList[25]['text'] == 'O' and self.buttonList[17]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[33]['text'] == 'O' and self.buttonList[25]['text'] == 'O' and \
                            self.buttonList[17]['text'] == 'O' and self.buttonList[9]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[25]['text'] == 'O' and self.buttonList[17]['text'] == 'O' and \
                            self.buttonList[9]['text'] == 'O' and self.buttonList[1]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[27]['text'] == 'O' and self.buttonList[18]['text'] == 'O' and \
                            self.buttonList[11]['text'] == 'O' and self.buttonList[3]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[34]['text'] == 'O' and self.buttonList[26]['text'] == 'O' and \
                            self.buttonList[18]['text'] == 'O' and self.buttonList[10]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[26]['text'] == 'O' and self.buttonList[18]['text'] == 'O' and \
                            self.buttonList[10]['text'] == 'O' and self.buttonList[2]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False




                    elif self.buttonList[39]['text'] == 'X' and self.buttonList[31]['text'] == 'X' and \
                            self.buttonList[23]['text'] == 'X' and self.buttonList[15]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[31]['text'] == 'X' and self.buttonList[23]['text'] == 'X' and \
                            self.buttonList[15]['text'] == 'X' and self.buttonList[7]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[38]['text'] == 'X' and self.buttonList[30]['text'] == 'X' and \
                            self.buttonList[22]['text'] == 'X' and self.buttonList[14]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[40]['text'] == 'X' and self.buttonList[32]['text'] == 'X' and \
                            self.buttonList[24]['text'] == 'X' and self.buttonList[16]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[32]['text'] == 'X' and self.buttonList[24]['text'] == 'X' and \
                            self.buttonList[16]['text'] == 'X' and self.buttonList[8]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[24]['text'] == 'X' and self.buttonList[16]['text'] == 'X' and \
                            self.buttonList[8]['text'] == 'X' and self.buttonList[0]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[41]['text'] == 'X' and self.buttonList[33]['text'] == 'X' and \
                            self.buttonList[25]['text'] == 'X' and self.buttonList[17]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[33]['text'] == 'X' and self.buttonList[25]['text'] == 'X' and \
                            self.buttonList[17]['text'] == 'X' and self.buttonList[9]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[25]['text'] == 'X' and self.buttonList[17]['text'] == 'X' and \
                            self.buttonList[9]['text'] == 'X' and self.buttonList[1]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[27]['text'] == 'X' and self.buttonList[18]['text'] == 'X' and \
                            self.buttonList[11]['text'] == 'X' and self.buttonList[3]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[34]['text'] == 'X' and self.buttonList[26]['text'] == 'X' and \
                            self.buttonList[18]['text'] == 'X' and self.buttonList[10]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[26]['text'] == 'X' and self.buttonList[18]['text'] == 'X' and \
                            self.buttonList[10]['text'] == 'X' and self.buttonList[2]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X 가 이겼습니다.")
                        self.result = False





















                    elif self.buttonList[21]['text'] == 'O' and self.buttonList[15]['text'] == 'O' and \
                            self.buttonList[9]['text'] == 'O' and self.buttonList[3]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[28]['text'] == 'O' and self.buttonList[22]['text'] == 'O' and \
                            self.buttonList[16]['text'] == 'O' and self.buttonList[10]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[22]['text'] == 'O' and self.buttonList[16]['text'] == 'O' and \
                            self.buttonList[10]['text'] == 'O' and self.buttonList[4]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[35]['text'] == 'O' and self.buttonList[29]['text'] == 'O' and \
                            self.buttonList[23]['text'] == 'O' and self.buttonList[17]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[29]['text'] == 'O' and self.buttonList[23]['text'] == 'O' and \
                            self.buttonList[17]['text'] == 'O' and self.buttonList[11]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[23]['text'] == 'O' and self.buttonList[17]['text'] == 'O' and \
                            self.buttonList[11]['text'] == 'O' and self.buttonList[5]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[36]['text'] == 'O' and self.buttonList[30]['text'] == 'O' and \
                            self.buttonList[24]['text'] == 'O' and self.buttonList[18]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[30]['text'] == 'O' and self.buttonList[24]['text'] == 'O' and \
                            self.buttonList[18]['text'] == 'O' and self.buttonList[12]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[24]['text'] == 'O' and self.buttonList[18]['text'] == 'O' and \
                            self.buttonList[12]['text'] == 'O' and self.buttonList[6]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[37]['text'] == 'O' and self.buttonList[31]['text'] == 'O' and \
                            self.buttonList[25]['text'] == 'O' and self.buttonList[19]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[31]['text'] == 'O' and self.buttonList[25]['text'] == 'O' and \
                            self.buttonList[19]['text'] == 'O' and self.buttonList[13]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[38]['text'] == 'O' and self.buttonList[32]['text'] == 'O' and \
                            self.buttonList[26]['text'] == 'O' and self.buttonList[20]['text'] == 'O':
                        tkinter.messagebox.showinfo("승리", "O가 이겼습니다.")
                        self.result = False




                    elif self.buttonList[21]['text'] == 'X' and self.buttonList[15]['text'] == 'X' and \
                            self.buttonList[9]['text'] == 'X' and self.buttonList[3]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[28]['text'] == 'X' and self.buttonList[22]['text'] == 'X' and \
                            self.buttonList[16]['text'] == 'X' and self.buttonList[10]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[22]['text'] == 'X' and self.buttonList[16]['text'] == 'X' and \
                            self.buttonList[10]['text'] == 'X' and self.buttonList[4]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[35]['text'] == 'X' and self.buttonList[29]['text'] == 'X' and \
                            self.buttonList[23]['text'] == 'X' and self.buttonList[17]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[29]['text'] == 'X' and self.buttonList[23]['text'] == 'X' and \
                            self.buttonList[17]['text'] == 'X' and self.buttonList[11]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[23]['text'] == 'X' and self.buttonList[17]['text'] == 'X' and \
                            self.buttonList[11]['text'] == 'X' and self.buttonList[5]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False

                    elif self.buttonList[36]['text'] == 'X' and self.buttonList[30]['text'] == 'X' and \
                            self.buttonList[24]['text'] == 'X' and self.buttonList[18]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[30]['text'] == 'X' and self.buttonList[24]['text'] == 'X' and \
                            self.buttonList[18]['text'] == 'X' and self.buttonList[12]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[24]['text'] == 'X' and self.buttonList[18]['text'] == 'X' and \
                            self.buttonList[12]['text'] == 'X' and self.buttonList[6]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False


                    elif self.buttonList[37]['text'] == 'X' and self.buttonList[31]['text'] == 'X' and \
                            self.buttonList[25]['text'] == 'X' and self.buttonList[19]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[31]['text'] == 'X' and self.buttonList[25]['text'] == 'X' and \
                            self.buttonList[19]['text'] == 'X' and self.buttonList[13]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X가 이겼습니다.")
                        self.result = False
                    elif self.buttonList[38]['text'] == 'X' and self.buttonList[32]['text'] == 'X' and \
                            self.buttonList[26]['text'] == 'X' and self.buttonList[20]['text'] == 'X':
                        tkinter.messagebox.showinfo("승리", "X 가 이겼습니다.")
                        self.result = False



                    break
    def __init__(self):
        window = Tk()
        self.imageList = []
        self.imageList.append(PhotoImage(file='image/o.gif'))
        self.imageList.append(PhotoImage(file='image/x.gif'))
        self.imageList.append(PhotoImage(file='image/empty.gif'))
        self.buttonList =[]
        self.turn = True # True  = o차례 , False = x차례
        self.result = True
        self.Hocount =0
        self.Hxcount =0
        frame1 = Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.buttonList.append(\
                    Button(frame1,text=' ',image=self.imageList[2],command=lambda Row=r, Col=c:self.pressed(Row,Col)))
                self.buttonList[r*7+c].grid(row=r,column=c)
        frame2 = Frame(window)
        frame2.pack()
        self.explain=Button(frame2,text="새로시작",command=self.again)
        self.explain.pack()
        window.mainloop()
Samoc()