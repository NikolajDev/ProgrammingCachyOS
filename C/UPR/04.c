#include <stdio.h>

void div(int numer, int denom, int *ratio, int *rem) {
  *ratio = numer / denom;
  if (rem != NULL) {
    *rem = numer % denom;
  }
}

void init_array(int *array, int size) {
  for (int i = 0; i < 10; i++) {
    *(array + i) = i * i;
  }
}

void print_array(int *array, int size) {
  for (int i = 0; i < 10; i++) {
    printf("%d\n", *(array + i));
  }
}

int main(void) {
  int ratio = 0;
  int rem = 0;
  div(14, 5, &ratio, &rem);
  printf("14 / 5 = %d rem = %d", ratio, rem);
  int var = 0;
  // inicializace pole
  int array[10] = {0};

  *array = 1;

  printf("%d\n", *array);

  for (int i = 0; i < 10; i++) {
    *(array + i) = i * i;
  }
  return 0;
}
