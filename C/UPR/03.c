#include <stdio.h>

int max(int num1, int num2) {
  if (num1 > num2) {
    return num1;
  }
  return num2;
}

int fact(int n) {
  if (n <= 1) {
    return 1;
  }
  else {
    return n * fact(n - 1);
  }
}

int power(int base, int exp) {
  int result = 1;
  for (;exp > 0; --exp) {
    result *= base;
  }
  return result;
}

void print_max(int num1, int num2) {
  printf("max of %d and %d is: %d\n", num1, num2, max(num1, num2));
}

int main()
{
  printf("%d\n", power(2, 10));
  print_max(6, 22);
  printf("%d", fact(5));
  return 0;
}
