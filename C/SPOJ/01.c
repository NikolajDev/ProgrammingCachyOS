// Your program is to use the brute-force
// approach in order to find the Answer to Life,
// the Universe, and Everything. More precisely...
// rewrite small numbers from input to output.
// Stop processing input after reading in the number 42.
// All numbers at input are integers of one or two digits.

// Example
// intput:
// 1
// 2
// 88
// 42
// 99

// Output:
//  1
//  2
//  88
//

#include <stdio.h>

int main() {
  int num;

  // Čítame v cykle, kým scanf úspešne prečíta jedno celé číslo (%d)
  while (scanf("%d", &num) == 1) {
    if (num == 42) {
      break;
    } else {
      printf("%d\n", num);
    }
    // Sem si doplň podmienku:
    // Ak je prečítané číslo rovné 42, vyskoč z cyklu (break).
    // Inak číslo vypíš pomocou printf.
  }

  return 0;
}
