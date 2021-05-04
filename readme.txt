Chess
Brandon Fafata's 15-112 Term Project

Simply run chess.py to play the game!

Description: 


Required modules:
PIL and cmu_112_graphics
(cmu_112_graphics included)

Code glossary:
Section 1. Setup
    Section 1.1 Variable Assignment
    Section 1.2 Piece Class and objects
    Section 1.3 Board Creation
Section 2. Game controller
    Section 2.1 Moving
    Section 2.2 Taking
    Section 2.3 Helpers
Section 3. AI
    Section 3.1 Evaluation
    Section 3.2 Minimax
    Section 3.3 AB pruning
    Section 3.4 Eval Helpers
    Section 3.5 AI Helpers
Section 4. Turn controllers:
    Section 4.1 Selectors
    Section 4.2 Player move controllers
    Section 4.3 Computer move controller
    Section 4.4 Helpers
Section 5. GUI
    Section 5.1 Splash
    Section 5.2 Splash Controller
    Section 5.3 Game Elements
    Section 5.4 Debug (To see debug information in game, press "d")
    Section 5.5 redrawAll


Citations:


General: Claude Shannon, Programming a Computer for Playing Chess (1950)
http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf
General: Cornell CS, AI Chess Algorithms 
https://www.cs.cornell.edu/boom/2004sp/ProjectArch/Chess/algorithms.html

General design inspiration:
https://www.chess.com/ and https://lichess.org/

General help: the Chess Programming Wiki
https://www.chessprogramming.org/

Images:
From https://imgbin.com/

cmu_112_graphics:
From https://www.cs.cmu.edu/~112/ and https://docs.python.org/3/library/tkinter.html

positionvalues.py:
The "standard" position values are from https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/.
There are many different options for doing this, see https://www.chessprogramming.org/Piece-Square_Tables
But since I was looking at that ariticle, I used the given piece square table.
The "agressive" position values are my own.

Section 3.1's otherEvaluation:
Inspired by https://www.chessprogramming.org/Evaluation_of_Pieces

Section 3.2 Minimax:
Made with the help of https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/

Section 4.1 Selectors
getCellBounds and getCell directly from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html