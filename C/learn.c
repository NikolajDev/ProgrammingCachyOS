#include <stdio.h>

int main() {
  int castka;
  scanf("%d", &castka);

  printf("Bankovka 5000: %d", castka % 5000)
  castka /= 5000;
  printf("Bankovka 2000: %d", castka % 2000)
  castka /= 2000;
  printf("Bankovka 1000: %d", castka % 1000)
  castka /= 1000;
  printf("Bankovka 500: %d", castka % 500)
  castka /= 500;
  printf("Bankovka 200: %d", castka % 200)
  castka /= 200;
  printf("Bankovka 100: %d", castka % 100)
  castka /= 100;
  printf("Bankovka 50: %d", castka % 50)
  castka /= 50;
  printf("Bankovka 20: %d", castka % 20)
  castka /= 20;
  printf("Bankovka 10: %d", castka % 10)
  castka /= 10;
  printf("Bankovka 5: %d", castka % 5)
  castka /= 5;
  printf("Bankovka 2: %d", castka % 2)
  castka /= 2;
  printf("Bankovka 1: %d", castka % 1)
  castka /= 1;
  return 0;
}