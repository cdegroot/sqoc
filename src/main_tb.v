module main_tb;

    reg clock = 0;
    reg reset = 0;
    reg [7:0] pc = 0;
    
    // Probe for testing
    always @(posedge clock) 
        assign pc = main.pc;

    // The meat - hook up the cosimulation vars
    initial begin
        $from_myhdl(clock, reset, pc);
        $to_myhdl(pc);
    end

    // Instantiate the DUT
    main main(clock, reset);

endmodule
