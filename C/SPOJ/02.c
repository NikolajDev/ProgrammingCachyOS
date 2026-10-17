// Peter wants to generate some prime numbers for his cryptosystem. Help him!
// Your task is to generate all prime numbers between two given numbers!
//
// Input
// The input begins with the number t of test cases in a single line (t ≤ 10).
// In each of the next t lines there are two numbers m and n (1 ≤ m ≤ n ≤
// 1000000000, n-m ≤ 100000) separated by a space.
//
// Output
// For every test case print all prime numbers p such that m ≤ p ≤ n, one number
// per line, test cases separated by an empty line.
//
// Example
// Input:
// 2
// 1 10
// 3 5
//
// Output:
// 2
// 3
// 5
// 7
//
// 3
// 5

#include <stdbool.h>
#include <stdio.h>

bool is_prime(int a) {
  if (a < 2)
    return false;
  for (int start = 2; start * start <= a; start++) {
    if (a % start == 0) {
      return false;
    }
  }
  return true;
}

int main(void) {
  int pocet_intervalov;
  scanf("%d", &pocet_intervalov);
  int start, stop;
  for (int round = 0; round < pocet_intervalov; round++) {
    int start, stop;
    scanf("%d %d", &start, &stop);
    for (; start <= stop; start++) {
      if (is_prime(start)) {
        printf("%d\n", start);
      }
    }
  }
  return 0;
}
