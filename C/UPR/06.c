#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void init_array(int *array, size_t size) {
  for (size_t i = 0; i < size; i++) {
    array[i] = 0;
  }
}

int *create_array(size_t size) {
  int *array = (int *)malloc(size * size_of(int));

  init_array(array, size);
}

void print_array(int *array, size_t size) {
  for (size_t i = 0; i < size; i++) {
    printf("array[%zu] = %d\n", i, array[i]);
  }
}

int main() {
  void *ptr = malloc(1024);
  free(ptr);

  int *int_ptr = (int *)malloc(sizeof(int) * 10);
  return 0;
}
