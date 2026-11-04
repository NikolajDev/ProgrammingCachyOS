#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef int AircraftID;

void process_aircraft(AircraftID id);

typedef struct Turtle {
  int32_t x;
  int32_t y;
  char dir;
};

void print_turtle(Turtle t1) {
  printf("Turtle: {.x=%d, y=%d .dir=%c", t1.x, t1.y, t1.dir);
}

int main(int argc, char *argv[]) {
  for (int i = 0; i < argc; ++i) {
    printf("[%d] %s\n", i, argv[i]);
  }

  if (argc < 3) {
    puts("At least two arguments expected.");
    return -1;
  }

  int fst = atoi(argv[1]);
  int snd = atoi(argv[2]);

  printf("%d + %d = %d", fst, snd, fst + snd);

  print_turtle((struct Turtle) {
    x = 40;
    y = 20;
    dir = 'l';
  });
  return 0;
}
