// Code for Boolean expression F

module boolean(
	input X=1,Y=1,Z,=1,W=1,
	output F
);

assign F=(X&&!Y)||(X&&W)||(Y&&Z)||(Z&&!W);

endmodule
