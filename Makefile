SRC=src
OUT=out
BINARY=$(OUT)/a.out

default: out $(BINARY)

out:
	-mkdir $(OUT)

$(BINARY): $(SRC)/*.v
	iverilog -o $@ $^
	
clean:
	rm -if $(OUT)/*
	
run: $(BINARY)
	$<