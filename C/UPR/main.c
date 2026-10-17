#include <stdio.h>

int main(int argc, char *argv[]) {
  int val = 42;
  int *ptr_val = &val;
  printf("%d\n", *ptr_val);

  // vytovrim si pole, s pointerom *p, ten
  // mi oznacuje index na ktory ukazujem
  // pri incializaci, zadam pole
  // to znamena ze ukazujem na pole[0]

  int pole[] = {10, 20, 30};
  int *index = pole;

  printf("%d\n", *index);
  printf("%d\n", *(index + 1));

  return 0;
}
