SOUCE=reverselist

OUTPUT=${SOUCE}

CPP=${SOUCE}.cpp

OBJS=${SOUCE}.o

CC=g++

.cpp.o:
	${CC} -c ${CPP} -std=c++11 

${OUTPUT}:${OBJS}
	${CC} -o $@ $^

clean:
	rm -f *.o ${OUTPUT}

all:
	make clean & make 
