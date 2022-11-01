// Code for Boolean expression F

module boolean(
	input X=1,Y=1,Z,=1,W=1,
	output F
);

assign F=(X&&!Y)||(X&&!Z&&!W)||(X&&Z&&W)||(!Y&&!Z)||(!X&&Y&&Z&&!W);

endmodule
