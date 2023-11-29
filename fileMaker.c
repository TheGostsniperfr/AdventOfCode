#include <stdio.h>
#include <stdlib.h>
#include <err.h>
#include <sys/types.h>
#include <sys/stat.h>

#define NB_OF_DAYS 25
#define BUFFER_SIZE 50

void cp(char* filename, char* dir){
    FILE* templateFile = fopen(filename, "r");
    if(filename == NULL){
        perror("Error to open template file.");
        exit(EXIT_FAILURE);
    }



    FILE* cpFile = fopen(dir, "w+");
    if(cpFile == NULL){
        perror("Error to create copy file.");
        exit(EXIT_FAILURE);
    }

    if (chmod(dir, 0777) != 0) {
        perror("Error setting file permissions.");
        exit(EXIT_FAILURE);
    }



    char buffer[BUFFER_SIZE];

    while(fgets(buffer, BUFFER_SIZE, templateFile) != NULL){
        fputs(buffer, cpFile);
    }

    fclose(cpFile);
    fclose(templateFile);
}

int main(int argc, char* argv[]){
    if(argc != 2){
        printf
        (
            "Usage : fileMaker [int: year] ->"
            "reate file for an Advent of Code Year.\n"
        );

        exit(EXIT_SUCCESS);
    }

    int year = atoi(argv[1]);

    printf("Start to create files for Advent of Code %d\n", year);

    char buffer[BUFFER_SIZE];


    if(snprintf(buffer, BUFFER_SIZE, "%d", year) < 0){
        errx(EXIT_FAILURE, "Error to format string.");
    }

    if(mkdir(buffer, 0777) != 0){
            errx(EXIT_FAILURE, "Error to create folder %s.", buffer);
    }

    for (int i = 1; i <= 25; i++)
    {
        if(snprintf(buffer, BUFFER_SIZE, "%d/Day%d", year, i) < 0){
            errx(EXIT_FAILURE, "Error to format string.");
        }
        if(mkdir(buffer, 0777) != 0){
            errx(EXIT_FAILURE, "Error to create folder %s.", buffer);
        }

        if(snprintf(buffer, BUFFER_SIZE, "%d/Day%d/main.c", year, i) < 0){
            errx(EXIT_FAILURE, "Error to format string.");
        }

        cp("templates/C/template.c", buffer);

        if(snprintf(buffer, BUFFER_SIZE, "%d/Day%d/Makefile", year, i) < 0){
            errx(EXIT_FAILURE, "Error to format string.");
        }

        cp("templates/C/Makefile", buffer);
    }

    printf("Success to create files for Advent of Code %d\n", year);
}