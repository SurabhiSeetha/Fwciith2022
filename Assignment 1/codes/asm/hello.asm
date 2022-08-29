.include "/home/surabhi_22/test/codes/m328Pdef.inc"
 
.def X = R26 
.def Y = R25 
.def Z = R18 
.def W = R19 
.def F = R20 
.def t = R21
.def k = R22 
.def mask = R23 
.def result = R24 
 
ldi R16, 0b00000000 
out DDRD, R16 
ldi R16, 0b00100000 
out DDRB, R16 
 
ldi mask, 0b00000001 
 
start: 
 
in R17, PIND 
lsr R17 
lsr R17 
mov X, R17 
and X, mask 
lsr R17 
mov Y, R17 
and Y, mask 
lsr R17 
mov Z, R17 
and Z, mask 
lsr R17 
mov W, R17 
and W, mask 

mov result, X ; result = X
mov t, Y
eor t, mask ; result = Y’
and result, t ; result = XY’

mov t, X ; temp =  X
mov k, Z
eor k, mask ; temp = Z’
and t, k ; temp = XZ’
mov k, W
eor k, mask ; temp1 = W’
and t, k ; temp = XZ’W’
or result, t ; result = XY’ + XZ’W’

mov t, X ; temp = X
and t, Z ; temp = XZ
and t, W ; temp = XZW
or result, t ; result = XY’ + XZ’W’ + XZW

mov t, Y ; temp = Y
eor t, mask ; temp = Y’
mov k, Z ; temp1= Z
eor k, mask ; temp1 = Z’
and t, k ; temp=Y’Z’
or result, t ; result =  XY’ + XZ’W’ + XZW + Y’Z’

mov t, X ; temp = X
eor t, mask ; temp = X’
and t, Y ; temp =X’Y
and t, Z ; temp = X’YZ
mov k, W
eor k, mask ; temp1 = W’
and t, k ;  temp = X’YZW’
or result, t ; result = XY’ + XZ’W’ + XZW + Y’Z’
lsl result 
lsl result 
lsl result 
lsl result 
lsl result
out PORTB, result
