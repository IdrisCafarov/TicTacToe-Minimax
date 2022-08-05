import tkinter



gm=tkinter.Tk()
buttt=tkinter.Button(gm,text="",width=1,height=1)



gm.resizable(True,True)

gm.geometry('500x500')

gm.title('X O Oyunu')


play_area=tkinter.Frame(gm,width=400,height=400,bg='white')

status_label = tkinter.Label(gm, text="", font=('Ariel', 15), bg='green', fg='snow')
status_label.pack(fill=tkinter.X)



current_fig="X"

X_points=[]
O_points=[]


def set1(button):
    global l_button
    global current_fig
    
    if button["text"]=="":
        if current_fig=="X":
            button.configure(text=current_fig,bg='snow',fg='black')
           
            info = button.grid_info()
            X_points.append((info['row'],info['column']))
            if info['row']==1 and info['column']==1:
                key=1
            elif info['row']==1 and info['column']==2:
                key=2
            elif info['row']==1 and info['column']==3:
                key=3
            elif info['row']==2 and info['column']==1:
                key=4
            elif info['row']==2 and info['column']==2:
                key=5
            elif info['row']==2 and info['column']==3:
                key=6
            elif info['row']==3 and info['column']==1:
                key=7
            elif info['row']==3 and info['column']==2:
                key=8
            elif info['row']==3 and info['column']==3:
                key=9
            board[key] = "X"
            current_fig="O"
            status_label.configure(text="O's turn")
        elif current_fig=="O":
            info = button.grid_info()
            O_points.append((info['row'],info['column']))
            button.configure(text=current_fig,bg='snow',fg='black')
            current_fig="X"
            status_label.configure(text="X's turn")
    check_win()
    
    

    
        

b1=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b1),set2()])
b1.grid(row=1,column=1)

b2=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b2),set2()])
b2.grid(row=1,column=2)

b3=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b3),set2()])
b3.grid(row=1,column=3)

b4=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b4),set2()])
b4.grid(row=2,column=1)

b5=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b5),set2()])
b5.grid(row=2,column=2)

b6=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b6),set2()])
b6.grid(row=2,column=3)

b7=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b7),set2()])
b7.grid(row=3,column=1)

b8=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b8),set2()])
b8.grid(row=3,column=2)

b9=tkinter.Button(play_area,text="",width=10,height=5,command=lambda :[set1(b9),set2()])
b9.grid(row=3,column=3)

l_button=[b1,b2,b3,b4,b5,b6,b7,b8,b9]





def spaceIsFree(position):
    if board[position] == ' ':
        return True
    
    return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        return



def set2():
    global current_fig
    global l_button
    bestScore = -800
    bestMove = 0
    for key in board.keys():
       if current_fig=="O" and l_button[key-1]["text"]=="":
            l_button[key-1].configure(text=current_fig,bg='snow',fg='black')
            board[key] = "O"
            score = minimax(board, 0, False)
            board[key] = ' '
            l_button[key-1].configure(text="",bg='snow',fg='black')
            if (score > bestScore):
                bestScore = score
                bestMove = key
                
    insertLetter("O", bestMove)
    l_button[bestMove-1].invoke()
    


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon("O")):
        return 1
    elif (checkWhichMarkWon("X")):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = "O"
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = "X"
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore
    
    
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True



def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
        
   

class Winning_possblty:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
    
    def check(self,figr):
        p1_pos= False
        p2_pos= False
        p3_pos= False
        
        
        
        if figr=="X":
            for point in X_points:
                if point[0]==self.x1 and point[1]==self.y1:
                    p1_pos=True
                elif point[0]==self.x2 and point[1]==self.y2:
                    p2_pos=True
                elif point[0]==self.x3 and point[1]==self.y3:
                    p3_pos=True
                    
        elif figr=="O":
            for point in O_points:
                if point[0]==self.x1 and point[1]==self.y1:
                    p1_pos=True
                elif point[0]==self.x2 and point[1]==self.y2:
                    p2_pos=True
                elif point[0]==self.x3 and point[1]==self.y3:
                    p3_pos=True 
                    
        return all([p1_pos,p2_pos,p3_pos])
    
    
win_possobilities=[
    Winning_possblty(1, 1, 1, 2, 1, 3),
    Winning_possblty(2, 1, 2, 2, 2, 3),
    Winning_possblty(3, 1, 3, 2, 3, 3),
    Winning_possblty(1, 1, 2, 1, 3, 1),
    Winning_possblty(1, 2, 2, 2, 3, 2),
    Winning_possblty(1, 3, 2, 3, 3, 3),
    Winning_possblty(1, 1, 2, 2, 3, 3),
    Winning_possblty(3, 1, 2, 2, 1, 3)
        ]
def disable_game():
    b1.configure(state=tkinter.DISABLED)
    b2.configure(state=tkinter.DISABLED)
    b3.configure(state=tkinter.DISABLED)
    b4.configure(state=tkinter.DISABLED)
    b5.configure(state=tkinter.DISABLED)
    b6.configure(state=tkinter.DISABLED)
    b7.configure(state=tkinter.DISABLED)
    b8.configure(state=tkinter.DISABLED)
    b9.configure(state=tkinter.DISABLED)
    
    




def check_win():
    for possb in win_possobilities:
        if possb.check("X"):
            status_label.configure(text="X won")
            disable_game()
            return
        elif possb.check("O"):
            status_label.configure(text="O won")
            disable_game()
            return
        
    if len(X_points)+len(O_points)==9:
        status_label.configure(text="Draw !")
        disable_game()




play_area.pack(pady=10,padx=10)

gm.mainloop()