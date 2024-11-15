module LUT #(
	parameter K = 4,
	parameter [2**K-1:0] INIT = 0
) (
	input I0, I1, I2, I3, I4,
	output O
);

endmodule

module DFF #(
	parameter ENABLE_USED = 1'b0,
	parameter RST_USED = 1'b0
) (
	input C, D, CE, RD,
	output reg Q
);
	initial Q = 1'b0;
	always @(posedge C) begin
		if (RST_USED && !RD)
			Q <= 1'b0;
		else if (!ENABLE_USED || (ENABLE_USED && CE))
			Q <= D;
	end
endmodule

module IOB #(
	parameter INPUT_USED = 1'b0,
	parameter OUTPUT_USED = 1'b0,
	parameter ENABLE_USED = 1'b0
) (
	(* iopad_external_pin *) inout PAD,
	input O, EN,
	output I
);
	generate if (OUTPUT_USED && ENABLE_USED)
		assign PAD = EN ? O : 1'bz;
	else if (OUTPUT_USED)
		assign PAD = O;
	endgenerate

	generate if (INPUT_USED)
		assign I = PAD;
	endgenerate
endmodule

module IBUF (
	(* iopad_external_pin *) input I,
	output O
);
	IOB #(
		.INPUT_USED(1'b1)
	) _TECHMAP_REPLACE_ (
		.PAD(PAD),
		.O(),
		.EN(1'b1),
		.I(O)
	);
endmodule

module OBUF (
	(* iopad_external_pin *) output O,
	input I
);
	IOB #(
		.OUTPUT_USED(1'b1)
	) _TECHMAP_REPLACE_ (
		.PAD(PAD),
		.O(I),
		.EN(),
		.I()
	);
endmodule
