# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:56:33 2022

@author: wpnat
"""
######GUI LINK https://realpython.com/pysimplegui-python/

class Board(object):
    
    def __init__(self):
      board=[['r','n','b','q','k','b','n','r'],  
             ['p','p','p','p','p','p','p','p'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['P','P','P','P','P','P','P','P'],
             ['R','N','B','Q','K','B','N','R']]
      self.board=board
      
      """Update board takes in the previous x and y coordinates as well as
      the new ones. This will be taken from the new_coord function. It updates
      the board with the most recent coordinates."""
      """There will be another if statement in the main code that checks to make sure
      that your're not trying to replace one of your own pieces, so that wont need to
      be accounted for in this function"""
      
      """#Decide whether we want to keep track of the taken pieces or just end the game when 
      the king gets taken."""
    def update_board(self,x ,y ,x_coord,y_coord):
        current=self.board[x][y]
        next_piece=self.board[x_coord][y_coord]
        lower="p r n b q k"
        upper="P R N B Q K "
        if current in lower:
            if next_piece==".":
                self.board[x_coord][y_coord]=current
                self.board[x][y]="."
            elif next_piece in upper:
                self.board[x_coord][y_coord]=current
                self.board[x][y]="."
                
                
                
        elif current in upper:
            if next_piece==".":
                self.board[x_coord][y_coord]=current
                self.board[x][y]="."
            elif next_piece in lower:
                self.board[x_coord][y_coord]=current
                self.board[x][y]="."
      
        
    """This function returns the current board as a list of lists"""
    def get_current_board(self):
        return self.board
      
        
    def __str__(self):
        """The entire board will be offset  spaces to the right so that it is centered."""
        alpha=" "*49 +"  A"+"   B"+"   C"+"   D"+"   E"+"   F"+"   G"+"   H"
        master=" "*49+("-"*33)+"\n"
        i=0
        while i <=len(self.board)-1:
            string=""
            for j in range(len(self.board[i])):
                if j==len(self.board[i])-1:
                    string=string+" | "+str(self.board[i][j])+" |\n"
                    dash=" "*49+("-"*33)+"\n"
                    string=string+dash
                elif j==0:
                    string=string+(" "*47+"{} | ".format(i+1))+str(self.board[i][j])
                else:
                    string=string+" | "+str(self.board[i][j])
          
            master=master+string 
            i+=1
        master=alpha+"\n"+master
        return str(master)
        
          
"""On the top of the board there is the alphabet denoting the columns of the board
and therefore the dictionary in this function translates the letters to the corresponding
list index. The rows are labeled 1-8 so the function accounts for this by subtracting one."""          
def new_coord(coord):
    x=coord[0]
    y=coord[1]
    dictionary=dict([("a",0),("b",1),("c",2),("d",3),("e",4),("f",5),("g",6),("h",7)])
    y=y.strip()
    y_coord=dictionary.get(y)
    x_coord=x-1
    return x_coord,y_coord

def valid_move(current_piece,current_coord,next_coord,row_max,col_max):
    current_piece=current_piece.lower()
    possible=[]   
    row=current_coord[0]
    col=current_coord[1]
    if current_piece=="p":
        left=(row,col-1)
        right=(row,col+1)
        up=(row-1,col)
        down=(row+1,col)
        if left[1]>=0 and left[1]<=col_max:
            possible.append(left)
        if right[1]>=0 and right[1]<=col_max:
            possible.append(right)
        if up[0]>=0 and up[0]<=row_max:
            possible.append(up)
        if down[0]>=0 and down[0]<=row_max:
            possible.append(down)
        if next_coord in possible:
            return True
        else:
            return False
        
    
    elif current_piece=="r":
        #move down
        j=col
        while j<=7:
            c=(j,col)
            possible.append(c)
            j+=1
        #move right
        i=row
        while i<=7:
            c=(row,i)
            possible.append(c)
            i+=1
        #move left
        i=col
        while i>=0:
            c=(row,i)
            possible.append(c)
            i-=1
        #move up
        j=row
        while i>=0:
            c=(j,col)
            possible.append(c)
            j-=1
        
        if next_coord in possible:
            return True
        else:
            return False
        
        
    elif current_piece=="n":
        coords=[]
        one=(row-1,col-2)
        two=(row-1,col+2)
        three=(row+1,col-2)
        four=(row+1,col+2)
        
        five=(row-2,col-1)
        syx=(row-2,col+1)
        seven=(row+2,col-1)
        eight=(row+2,col+1)
        
        coords.append(one)
        coords.append(two)
        coords.append(three)
        coords.append(four)
        coords.append(five)
        coords.append(syx)
        coords.append(seven)
        coords.append(eight)
        
        for i in range(len(coords)):
            if (coords[i][0]>=0 and coords[i][0]<=row_max) and (coords[i][1]>=0 and coords[i][1]<=col_max):
                possible.append(coords[i])
        
        if next_coord in possible:
            return True
        else:
            return False
    
    
    elif current_piece=="b":
        coords=[]
        #north west
        iterations_nw=col
        #print(iterations_nw)
        
        current_row=row
        current_col=col
        
        i=0
        while i<=iterations_nw-1:
            current_row_nw=current_row-1
            current_col_nw=current_col-1
            
            current_row=current_row_nw
            current_col=current_col_nw
            
            change=(current_row_nw,current_col_nw)
            possible.append(change)
            #print(change)
            i+=1
    
        #south west
        current_row=row
        current_col=col
        
        iterations_sw=col
        i=0
        while i<=iterations_sw-1:
            current_row_sw=current_row+1
            current_col_sw=current_col-1
            
            current_row=current_row_sw
            current_col=current_col_sw
            
            change=(current_row_sw,current_col_sw)
            possible.append(change)
            #print(change)
            i+=1
            
        #north east
        current_row=row
        current_col=col
        
        iterations_ne=7-col
        i=0
        while i<=iterations_ne-1:
            current_row_ne=current_row-1
            current_col_ne=current_col+1
            
            current_row=current_row_ne
            current_col=current_col_ne
            
            
            change=(current_row_ne,current_col_ne)
            possible.append(change)
            #print(change)
            i+=1
            
        #south east
        current_row=row
        current_col=col
        
        iterations_se=7-col
        i=0
        while i<=iterations_se-1:
            current_row_se=current_row+1
            current_col_se=current_col+1
            
            current_row=current_row_se
            current_col=current_col_se
            
            change=(current_row_se,current_col_se)
            possible.append(change)
            #print(change)
            i+=1
            
        if next_coord in possible:
            return True
        else:
            return False
      
        
    elif current_piece=="k":  
        ##paralled movements        
        left=(row,col-1)
        right=(row,col+1)
        up=(row-1,col)
        down=(row+1,col)
        if left[1]>=0 and left[1]<=col_max:
            possible.append(left)
        if right[1]>=0 and right[1]<=col_max:
            possible.append(right)
        if up[0]>=0 and up[0]<=row_max:
            possible.append(up)
        if down[0]>=0 and down[0]<=row_max:
            possible.append(down)    
            
        
        ##diagonal movements
        nw=(row-1,col-1)
        sw=(row+1,col-1)
        ne=(row-1,col+1)
        se=(row+1,col+1)
        possible.append(nw)
        possible.append(sw)
        possible.append(ne)
        possible.append(se)
        
        if next_coord in possible:
            return True
        else:
            return False
    
    
    elif current_piece=="q":
        ##Parallel Moves
        for i in range(9):
            #rows
            c=(i,col)
            possible.append(c)
        
        for j in range(9):
            r=(row,i)
            possible.append(r)
        
        
        ##Diagonal Moves
        iterations_nw=col
        #print(iterations_nw)
        
        current_row=row
        current_col=col
        
        i=0
        while i<=iterations_nw-1:
            current_row_nw=current_row-1
            current_col_nw=current_col-1
            
            current_row=current_row_nw
            current_col=current_col_nw
            
            change=(current_row_nw,current_col_nw)
            possible.append(change)
            #print(change)
            i+=1
    
        #south west
        current_row=row
        current_col=col
        
        iterations_sw=col
        i=0
        while i<=iterations_sw-1:
            current_row_sw=current_row+1
            current_col_sw=current_col-1
            
            current_row=current_row_sw
            current_col=current_col_sw
            
            change=(current_row_sw,current_col_sw)
            possible.append(change)
            #print(change)
            i+=1
            
        #north east
        current_row=row
        current_col=col
        
        iterations_ne=7-col
        i=0
        while i<=iterations_ne-1:
            current_row_ne=current_row-1
            current_col_ne=current_col+1
            
            current_row=current_row_ne
            current_col=current_col_ne
            
            
            change=(current_row_ne,current_col_ne)
            possible.append(change)
            #print(change)
            i+=1
            
        #south east
        current_row=row
        current_col=col
        
        iterations_se=7-col
        i=0
        while i<=iterations_se-1:
            current_row_se=current_row+1
            current_col_se=current_col+1
            
            current_row=current_row_se
            current_col=current_col_se
            
            change=(current_row_se,current_col_se)
            possible.append(change)
            #print(change)
            i+=1
        
        if next_coord in possible:
            return True
        else:
            return False
                
def correct_start_one(initial):
    return initial==(initial.lower()) and initial!="."
        
#print(correct_start_one("p"))
   


def correct_start_two(initial):
    if initial==(initial.upper()) and initial!=".":
        return True
    else:
        return False
     
def own_piece(initial,after):
    if after==".":
        return False
    elif initial==initial.upper() and after==after.upper():
        return True
    elif initial==initial.lower() and after==after.lower():
        return True
    else:
        return False
    
 
def is_blank(initial):
    return initial=="."    

def piece_captured(initial,after, initial_coords,after_coords):
    """The point of this function is to take in the before and after coordinates of a move, if a piece
    is being captured, you check to see what piece is capturing what. For example, if a pawn is 
    attempting to capture a piece, a pawn can only capture pieces diagonaly. And if the king is being captured
    then the game ends. Returns True if the piece is captured, and false if it is not captured."""
    initial_x=initial_coords[0]
    initial_y=initial_coords[1]
    after_x=after_coords[0]
    after_y=after_coords[1]
    possible_captured=[]
    if initial != "." and after!=".":
        if initial.lower=="p":
            
            #north east
            possible_captured.append((initial_x-1,initial_y-1))
            possible_captured.append((initial_x-1,initial_y+1))
            possible_captured.append((initial_x+1,initial_y-1))
            possible_captured.append((initial_x+1,initial_y+1))
            if after_coords in possible_captured:
                return True
            else:
                return False
    else:
        return True
            
            
            
        # in here will be the possible moves for a pawn to capture other things, (Diagonal movement)
        # 

    
    
    
    
if __name__=="__main__":
    
    print("This is a chess match for two players. Would you like to begin?")
    decision=input("(Yes or No):  ").strip()
    print(decision)
    decision=decision.lower()
    if decision=="no":
        print("Okay No Worries")
    elif decision=="yes":
        print("\n\n\n")
        print((" "*40)+"#$%#$% PLAYER ONE WILL PLAY LOWERCASE PIECES #$%#$%")
        print("\n\n")
        print((" "*40)+"#$%#$% PLAYER TWO WILL PLAY UPPERCASE PIECES #$%#$%")
        print("\n")
        
        player_one_captured=[]
        player_two_captured=[]
        """This is the move loop for player one. This loop will continue to loop until the user enters a 
        valid move. If the user enters an invalid move, an error message appears"""
        ###EACH MOVE ENTRY WILL BE CHECKED TO MAKE SURE THAT THE PLAYER ONLY CHOOSES\
        ##THERE OWN PIECES AND ACTUIALLY CHOOSES A PIECE AND NOT A BLANK SPOT FOR THEIR\
        ##INITIAL COORDINATE
        obj=Board()
        king=False
        while king==False:
            Done_one=False
            i=0
            while Done_one==False :
            
                print(obj)
                current_board=obj.get_current_board()
                print(" ")
                
                """This loop makes sure that the user chooses their own piecess"""
                proper_one=False
                while proper_one==False:
                    one_decision=input("Player 1:\nType in the current coordinates of the piece you want to move ex. (1, A):  ")
                    one_coords=one_decision.split(",")
                    one_row=int(one_coords[0])
                    one_col=one_coords[1]
                    #print(one_col)
                    new_one_coord=new_coord((one_row,one_col))
                    print(new_one_coord)
                    one_piece=current_board[new_one_coord[0]][new_one_coord[1]]
                    result=correct_start_one(one_piece)
                    
                    """This if statement checks to see if the first selection is a blank piece"""
                    blank=is_blank(one_piece)
                    if blank==True:
                        print("CANNOT MOVE BLANK PIECE")
                        proper_one=False
                        
                    
                    elif result==True:
                        proper_one=True
                    else:
                        print("\nCHOOSE YOUR OWN PIECES\n\n")
                        print(obj)
                        proper_one=False
            
                after_decision=input("Player 1:\nType in the coordinates of the location that you wish to move to ex.(1, A):  ")
                after_coords=after_decision.split(",")
                after_row=int(after_coords[0])
                after_col=after_coords[1]
        
                new_after_coord=new_coord((after_row,after_col))
                
                """This little section of code will check to make sure that the user doesnt try to replae their own 
                pieces"""
                after_piece=current_board[new_after_coord[0]][new_after_coord[1]]
                own=own_piece(one_piece,after_piece)
                valid=valid_move(one_piece,new_one_coord,new_after_coord,8,8)
                possible_pawn=piece_captured(one_piece,after_piece,new_one_coord,new_after_coord)
                
                if one_piece.lower()=="p":
                    if possible_pawn==False:
                        print("PAWN CAN ONLY CAPTURE DIAGONAL")
                        Done_one=False
                    else:
                       obj.update_board(new_one_coord[0],new_one_coord[1],new_after_coord[0],new_after_coord[1]) 
                       Done_one=valid
                
                elif own==True:
                    print("CANNOT REPLACE OWN PIECE")
                    Done_one=False
                
                elif valid==False:
                    print("\n\n")
                    print("*"*30)
                    print("*"*3+(" "*6)+"INVALID MOVE"+(" "*6)+3*"*")
                          
                    print("*"*30)
                    Done_one=valid
                elif valid==True:
                    obj.update_board(new_one_coord[0],new_one_coord[1],new_after_coord[0],new_after_coord[1])
                    Done_one=valid
                
            
            """This is the move loop for player two. It will continue to loop until player 2
            enter a valid move."""
            Done_two=False
            while Done_two==False:
                print(obj)
                current_board=obj.get_current_board()
                print(" ")
                
                """This loop makes sure that the user chooses their own piece"""
                proper_two=False
                while proper_two==False:
                    
                    one_decision=input("Player 2:\nType in the current coordinates of the piece you want to move ex. (1, A):  ")
                    one_coords=one_decision.split(",")
                    one_row=int(one_coords[0])
                    one_col=one_coords[1]
                    #print(one_col)
                    new_one_coord=new_coord((one_row,one_col))
                    print(new_one_coord)
                    one_piece=current_board[new_one_coord[0]][new_one_coord[1]]
    
                    result=correct_start_two(one_piece)
                    
                    """This if statement checks to see if the first selection is a blank piece"""
                    blank=is_blank(one_piece)
                    
                    
                    if blank==True:
                        print("CANNOT MOVE BLANK PIECE")
                        proper_one=False
                     
                        
                    elif result==True:
                        proper_two=True
                    else:
                        print("\nCHOOSE YOUR OWN PIECES\n\n")
                        print(obj)
                        proper_two=False
                                
                after_decision=input("Player 2:\nType in the coordinates of the location that you wish to move to ex.(1, A):  ")
                after_coords=after_decision.split(",")
                after_row=int(after_coords[0])
                after_col=after_coords[1]
        
                new_after_coord=new_coord((after_row,after_col))
                
                """This little section of code will help to determine whether"""
                after_piece=current_board[new_after_coord[0]][new_after_coord[1]]
                own=own_piece(one_piece,after_piece)
                valid=valid_move(one_piece,new_one_coord,new_after_coord,8,8)
                #print(valid)
                if own==True:
                    print("CANNOT REPLACE OWN PIECE")
                    Done_two=False
                    
                elif valid==False:
                    print("\n\n")
                    print("*"*30)
                    print("*"*3+(" "*6)+"INVALID MOVE"+(" "*6)+3*"*")
                          
                    print("*"*30)
                    Done_two=valid 
                       
                elif valid==True:
                    obj.update_board(new_one_coord[0],new_one_coord[1],new_after_coord[0],new_after_coord[1])
                    Done_two=valid   
            king=False
    
    
    
    

        
        