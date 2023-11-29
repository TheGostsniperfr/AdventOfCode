# Makefile

CC = gcc
CPPFLAGS = -MMD
CFLAGS = -Wall -Wextra
LDFLAGS =
LDLIBS =

SRC = fileMaker.c
OBJ = ${SRC:.c=.o}
DEP = ${SRC:.c=.d}

all: fileMaker

print_page: ${OBJ}

-include ${DEP}

.PHONY: clean

clean:
	${RM} ${OBJ}
	${RM} ${DEP}
	${RM} fileMaker

# END