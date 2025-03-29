#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int evalRPN(char** tokens, int tokensSize) {
    int result;
    int* stack = (int*)malloc(tokensSize * sizeof(int));
    int top = -1;

    for (int i = 0; i < tokensSize; i++) 
    {
        if ((strcmp(tokens[i], "+") == 0) || (strcmp(tokens[i], "-") == 0) ||
            (strcmp(tokens[i], "*") == 0) || (strcmp(tokens[i], "/") == 0)) 
        {
            int y = stack[top--];
            int x = stack[top--];

            if (strcmp(tokens[i], "+") == 0)
                result = x + y;
            if (strcmp(tokens[i], "-") == 0)
                result = x - y;
            if (strcmp(tokens[i], "*") == 0)
                result = x * y;
            if (strcmp(tokens[i], "/") == 0)
                result = trunc(x / y);

            stack[++top] = result;
        }

        else
        {
            stack[++top] = atoi(tokens[i]);
        }
    }

    int final_result = stack[top];
    free(stack);
    return final_result;
}
