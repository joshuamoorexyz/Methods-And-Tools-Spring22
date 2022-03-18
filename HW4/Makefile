#Author: Joshua Moore
#Description: Makefile for Methods and Tools in SW Development: Spring 2022.

#target: dependencies
#	action



all: main

main: main.o greeting.o
	g++ -o output main.o greeting.o

#makes object files
greeting.o: greeting.cpp greeting.h
	g++ -c greeting.cpp

main.o: main.cpp
	g++ -c main.cpp

clean: clean
	rm *.o output hello
