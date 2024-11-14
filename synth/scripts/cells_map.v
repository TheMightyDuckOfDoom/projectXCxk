module \$lut (A, Y);
	parameter WIDTH = 0;
	parameter LUT = 0;
	input [WIDTH-1:0] A;
	output Y;

	LUT #(.K(WIDTH), .INIT(LUT)) _TECHMAP_REPLACE_ (.I(A), .F(Y));
endmodule

module \$_DFF_P_ (input D, C, output Q); DFF #(.ENABLE_USED(1'b0), .RST_USED(1'b0)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .CLK(C)); endmodule
module \$_DFFE_PP_ (input D, C, E, output Q); DFF #(.ENABLE_USED(1'b1), .RST_USED(1'b0)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .CLK(C), .EN(E)); endmodule
module \$_SDFF_PN0_ (input D, C, R, output Q); DFF #(.ENABLE_USED(1'b0), .RST_USED(1'b1)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .CLK(C), .RST_N(R)); endmodule
module \$_SDFFE_PN0P_ (input D, C, E, R, output Q); DFF #(.ENABLE_USED(1'b1), .RST_USED(1'b1)) _TECHMAP_REPLACE_ (.D(D), .Q(Q), .CLK(C), .EN(E), .RST_N(R)); endmodule
