module LUT #(
	parameter K = 4,
	parameter [2**K-1:0] INIT = 0
) (
	input [K-1:0] I,
	output F
);
	wire [K-1:0] I_pd;

	genvar ii;
	generate
		for (ii = 0; ii < K; ii = ii + 1'b1)
			assign I_pd[ii] = (I[ii] === 1'bz) ? 1'b0 : I[ii];
	endgenerate

	assign F = INIT[I_pd];
endmodule

module DFF #(
	parameter ENABLE_USED = 1'b0,
	parameter RST_USED = 1'b0
) (
	input CLK, D, EN, RST_N,
	output reg Q
);
	initial Q = 1'b0;
	always @(posedge CLK) begin
		if (RST_USED && !RST_N)
			Q <= 1'b0;
		else if (!ENABLE_USED || (ENABLE_USED && EN))
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
	(* iopad_external_pin *) input PAD,
	output I
);
	IOB #(
		.INPUT_USED(1'b1)
	) _TECHMAP_REPLACE_ (
		.PAD(PAD),
		.O(),
		.EN(1'b1),
		.I(I)
	);
endmodule

module OBUF (
	(* iopad_external_pin *) output PAD,
	input O
);
	IOB #(
		.OUTPUT_USED(1'b1)
	) _TECHMAP_REPLACE_ (
		.PAD(PAD),
		.O(O),
		.EN(),
		.I()
	);
endmodule
