#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main(){
    char c[50] = "BYBHBASDSA    ASDASDA";
    
    strtok(c, " ");
    printf("%s\n", c[1]);
    return 0;
}