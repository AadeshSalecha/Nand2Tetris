//Author    : Aadesh Salecha
//Course    : Nand2Tetris
//Date      : March 2016


// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

@LOOP
0;JMP

(LOOP)	
@KBD
D = M

@WHITEN
D;JEQ

@BLACKEN
D;JGT

@LOOP
0;JMP

(WHITEN)
@8192
D = A
@i
M = D

@SCREEN
D = A - 1
@address
M = D
@FORLOOP
0;JMP

(FORLOOP)
@i
D = M

@END
D;JEQ

@address
A = D + M
M = 0

@i
M = M - 1

@FORLOOP
0;JMP


(BLACKEN)
@8192
D = A
@i
M = D

@SCREEN
D = A - 1
@address
M = D 
@FORLOOP1
0;JMP

(FORLOOP1)
@i
D = M

@END
D;JEQ

@address
A = D + M
M = -1

@i
M = M - 1

@FORLOOP1
0;JMP

(END)
@LOOP
0;JMP
