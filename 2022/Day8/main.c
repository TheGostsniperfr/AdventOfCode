#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 50

int main(){
    FILE* file;
    file = fopen("input", "r");

    if(file == NULL){
        perror("Error to open input file.");
        return EXIT_FAILURE;
    }

    char buffer[BUFFER_SIZE];

    while(fgets(buffer, BUFFER_SIZE, file) != NULL){
        printf("%s", buffer);
    }


    fclose(file);
    return EXIT_SUCCESS;
}
