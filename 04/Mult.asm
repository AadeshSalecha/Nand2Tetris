//Author    : Aadesh Salecha
//Course    : Nand2Tetris
//Date      : March 2016


// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@0
D = M
@a
M = D
@1
D = M
@b
M = D
@sum
M = 0

(LOOP)
@b
D = M

@STOP
D;JEQ

@a
D = M
@sum
M = M + D
@b
M = M - 1
@LOOP
0;JMP

(STOP)
@sum
D = M
@2
M = D
@END
0;JMP

(END)
@END
0;JMP