from chess import getCellBounds
def drawSplashMain(app,canvas): #draws the buttons and text in those buttons on the title screen
    width=100
    height=50
    canvas.create_rectangle(500-width,500-height,500+width,500+height,width=2)
    canvas.create_text(500,500,text="player vs. Computer", font=("Helvetica", "12", "bold"))
    canvas.create_rectangle(500-width,700-height,500+width,700+height,width=2)
    canvas.create_text(500,700,text="player vs. player", font=("Helvetica", "12", "bold"))
def drawTitle(app,canvas):      #draws the title on the title screen
    canvas.create_rectangle(0,0,1000,1000, fill="grey69")
    canvas.create_text(500,200,text="chess:",font=("Helvetica", "64", "bold"))
    canvas.create_text(500,300,text="A 15112 Term Project by Brandon Fafata",font=("Helvetica", "18", "bold"))
def drawPvCSplash(app,canvas):  #draws the buttons and text in those buttons on the PVC option screen
    width=100
    height=30
    canvas.create_text(500,400,text="choose your Opponent:",font=("Helvetica", "12", "bold"))
    canvas.create_rectangle(500-width,500-height,500+width,500+height,width=2)
    canvas.create_text(500,500,text="Minimax",font=("Helvetica", "12", "bold"))
    canvas.create_rectangle(500-width,600-height,500+width,600+height,width=2)
    canvas.create_text(500,600,text="agressive Minimax",font=("Helvetica", "12", "bold"))
    canvas.create_rectangle(500-width,700-height,500+width,700+height,width=2)
    canvas.create_text(500,700,text="A-B Pruning",font=("Helvetica", "12", "bold"))
    canvas.create_rectangle(500-width,800-height,500+width,800+height,width=2)
    canvas.create_text(500,800,text="agressive A-B Pruning",font=("Helvetica", "12", "bold"))
def drawPvPSplash(app,canvas):  #draws the buttons and text in those buttons on the PVP option screen
    width=100
    height=50
    canvas.create_text(500,400,text="make sure you have a Friend :)",font=("Helvetica", "12", "bold"))
    canvas.create_rectangle(500-width,500-height,500+width,500+height,width=2)
    canvas.create_text(500,500,text="play !",font=("Helvetica", "12", "bold"))
"""Section 5.2 Splash controller"""
def button(app,x,y):            #deals with all the buttons in all the splash screens:
#                               changes app as a function of where the player clicks
#                               given what screen they are on
    if app.mainsplash:
        if 400<x<600 and 450<y<550:
            app.mainsplash=False
            app.PvCsplash=True
            return
        if 400<x<600 and 650<y<750:
            app.mainsplash=False
            app.PvPsplash=True
            return
    if app.PvCsplash:
        if 400<x<600 and 470<y<530:
            app.gameactive=True
            app.PvCsplash=False
            app.title=False
            app.pvc=True
            app.minimaxstandard=True
            return
        if 400<x<600 and 570<y<630:
            app.gameactive=True
            app.PvCsplash=False
            app.title=False
            app.pvc=True
            app.minimaxagressive=True
            return
        if 400<x<600 and 670<y<730:
            app.gameactive=True
            app.PvCsplash=False
            app.title=False
            app.pvc=True
            app.abstandard=True
            return
        if 400<x<600 and 770<y<830:
            app.gameactive=True
            app.PvCsplash=False
            app.title=False
            app.pvc=True
            app.abagressive=True
            return
    if app.PvPsplash:
        if 400<x<600 and 450<y<550:
            app.gameactive=True
            app.PvPsplash=False
            app.title=False
            app.pvp=True
            return
"""Section 5.3 Game elements Draw"""
def drawIndicators(app,canvas): #draws the squares on your active piece, where it can move, what it can take
    if app.activepiece!=None:
        (x0,y0,x1,y1)=getCellBounds(app,app.activepiece.x,app.activepiece.y)
        canvas.create_rectangle(x0-2,y0+1,x1-2,y1+1,outline="red",width=2)
        for destsquare in app.activepiece.movelist():
            if destsquare!=None:
                (x0,y0,x1,y1)=getCellBounds(app,destsquare[0],destsquare[1])
                canvas.create_rectangle(x0-2,y0+1,x1-2,y1+1,outline="yellow",width=2)
        for destsquare in app.activepiece.takelist():
            if destsquare!=None:
                (x0,y0,x1,y1)=getCellBounds(app,destsquare[0],destsquare[1])
                canvas.create_rectangle(x0-2,y0+1,x1-2,y1+1,outline="orange",width=2)
def drawPiecesVisual(app,canvas):#draws the images of the pieces
    for row in range(8):
        for col in range(8):
            (x0,y0,x1,y1)=getCellBounds(app,row,col)
            piecename=board[row][col]
            if piecename==None:
                pass
            else:
                canvas.create_image(
                    x0+36,
                    y0-38,
                    image=ImageTk.PhotoImage(
                        app.imagedict[f"{piecename.color}_{piecename.ty}"]))
def otherGameItems(app,canvas): #draws the box and message under the board
    canvas.create_rectangle(100,720,700,980,fill="grey90")
    if app.pvp:
        if app.whitesmove:
            canvas.create_text(400,740,text=f'White:', font=("Helvetica", "12", "bold"))
        else:
            canvas.create_text(400,740,text=f'Black:', font=("Helvetica", "12", "bold"))
    canvas.create_text(400,780,text=f'{app.message}', font=("Helvetica", "12", "bold"))
def drawPlayers(app,canvas):    #draws the players, seen to the right of the board
    canvas.create_text(800,140,text=f'Black:', font=("Helvetica", "12", "bold"))
    if app.pvc:
        if app.abstandard:
            canvas.create_text(800,160,text=f'AB standard', font=("Helvetica", "12", "bold"))
        if app.abagressive:
            canvas.create_text(800,160,text=f'AB agressive', font=("Helvetica", "12", "bold"))
        if app.minimaxstandard:
            canvas.create_text(800,160,text=f'Minimax standard', font=("Helvetica", "12", "bold"))
        if app.minimaxagressive:
            canvas.create_text(800,160,text=f'Minimax agressive', font=("Helvetica", "12", "bold"))
    if app.pvp:
        canvas.create_text(800,160,text=f'friend', font=("Helvetica", "12", "bold"))
    canvas.create_text(800,640,text=f'White:', font=("Helvetica", "12", "bold"))
    canvas.create_text(800,660,text=f'You', font=("Helvetica", "12", "bold"))