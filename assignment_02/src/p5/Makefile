CC = gcc
CFLAGS = -I.
DEPS = common.h

%.o : %.c $(DEPS)
		$(CC) -C -O $@ $< $(CFLAGS)

sort_exe : main.c quickSort.c bubble.c insertion.c print_array.c selection.c`
		$(CC) -O main.c quickSort.c bubble.c insertion.c print_array.c selection.c $(CFLAG)