#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int countLineOfFile(FILE *file)
{
    int lCount = 0;
    char c;

    while((c = fgetc(file)) != EOF){
        if (c == '\n')
        {
            lCount++;
        }
    }

    rewind(file);

    return lCount;
}

static void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void bubbleSort(int *tab, int size)
{
    for (int i = size - 1; i > 0; i--)
    {
        bool isSort = true;
        for (int j = 0; j < i; j++)
        {
            if (tab[j + 1] < tab[j])
            {
                swap(&tab[j + 1], &tab[j]);
                isSort = false;
            }
        }

        if (isSort)
        {
            break;
        }
    }
}

int countOcc(int toFind, int *tab, int size)
{
    int result = 0;

    for (int i = 0; i < size; i++)
    {
        if (tab[i] == toFind)
        {
            result++;
        }
    }

    return result;
}

int main(){
    FILE* file;
    file = fopen("input", "r");

    if(file == NULL){
        perror("Error to open input file.");
        return EXIT_FAILURE;
    }

    int lCount = countLineOfFile(file);

    int *tabA = calloc(lCount, sizeof(int));
    int *tabB = calloc(lCount, sizeof(int));
    
    for(int i = 0; i < lCount; i++)
    {
        fscanf(file, "%d %d", &tabA[i], &tabB[i]);
    }

    bubbleSort(tabA, lCount);
    bubbleSort(tabB, lCount);

    int resultP1 = 0;

    for (int i = 0; i < lCount; i++)
    {
        printf("Val1: %d | Val2: %d\n", tabA[i], tabB[i]);
        resultP1 += abs(tabA[i] - tabB[i]);
    }

    printf("ResultP1: %d\n", resultP1);


    // !! PART 2

    int resultP2 = 0;
    for (int i = 0; i < lCount; i++)
    {
        resultP2 += tabA[i] * countOcc(tabA[i], tabB, lCount);
    }

    printf("ResultP2: %d\n", resultP2);

    free(tabA);
    free(tabB);
    fclose(file);
    
    return EXIT_SUCCESS;
}
