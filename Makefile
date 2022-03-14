all:myprogram.o mylib.o
        g++ –o myprogram myprogram.o mylib.o
clean:
        $(RM) myprogram