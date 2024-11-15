module \$lut (A, Y);
	parameter WIDTH = 0;
	parameter LUT = 0;
	input [WIDTH-1:0] A;
	output Y;

	if (WIDTH == 1)
		LUT #(.K(1), .INIT(LUT)) _TECHMAP_REPLACE_ (.I0(A), .F(Y));
	else if (WIDTH == 2)
		LUT #(.K(2), .INIT(LUT)) _TECHMAP_REPLACE_ (.I0(A[0]), .I1(A[1]), .O(Y));
	else if (WIDTH == 3)
		LUT #(.K(3), .INIT(LUT)) _TECHMAP_REPLACE_ (.I0(A[0]), .I1(A[1]), .I2(A[2]), .O(Y));
	else if (WIDTH == 4)
		LUT #(.K(4), .INIT(LUT)) _TECHMAP_REPLACE_ (.I0(A[0]), .I1(A[1]), .I2(A[2]), .I3(A[3]), .O(Y));
	else if (WIDTH == 5)
		LUT #(.K(5), .INIT(LUT)) _TECHMAP_REPLACE_ (.I0(A[0]), .I1(A[1]), .I2(A[2]), .I3(A[3]), .I4(A[4]), .O(Y));

endmodule

module \$_DFF_P_ (input D, C, output Q); DFF #(.ENABLE_USED(1'b0), .RST_USED(1'b0)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .C(C)); endmodule
module \$_DFFE_PP_ (input D, C, E, output Q); DFF #(.ENABLE_USED(1'b1), .RST_USED(1'b0)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .C(C), .CE(E)); endmodule
//module \$_SDFF_PN0_ (input D, C, R, output Q); DFF #(.ENABLE_USED(1'b0), .RST_USED(1'b1)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .C(C), .RD(R)); endmodule
//module \$_SDFFE_PN0P_ (input D, C, E, R, output Q); DFF #(.ENABLE_USED(1'b1), .RST_USED(1'b1)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .C(C), .CE(E), .RD(R)); endmodule
