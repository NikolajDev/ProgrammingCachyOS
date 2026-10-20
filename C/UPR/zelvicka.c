#include <stdio.h>
#include <stdlib.h>

int main() {
  int radky = 0;
  int stloupce = 0;
  scanf("%d %d", &radky, &stloupce);
  char *canvas = malloc(radky * stloupce * sizeof(char));
  // platno
  for (int i = 0; i < radky * stloupce; i++) {
    canvas[i] = '.';
  }

  // max 3 zlevicky pre kazdu si vytvorim premeu r a s (riadok stlpec, a podla
  // vstupu upravim pohyb/smer);
  // dir = 0 doprava (stlpec + 1)
  // dir = 1 dole    (riadok + 1)
  // dir = 2 dolava  (stlpec - 1)
  // dir = 3 hore    (ridok - 1)
  int r1 = 0, s1 = 0, dir1 = 0;
  int r2 = 0, s2 = 0, dir2 = 0;
  int r3 = 0, s3 = 0, dir3 = 0;

  // vzdy je jedna na zaciatku
  int pocet = 1;

  char ukon;
  while (scanf("%c", &ukon) == 1 && ukon != 'x') {
    if (pocet < 3 && ukon == 'f') {
      pocet++;
    }
    // pre kazdu zelvu od 1 az po pocet zelv, budeme menit jej
    // poziciu alebo smer podla pismena
    for (int zelv = 1; zelv <= pocet; zelv++) {
      int *r, *s, *dir;
      // kedze loopujem cez kazdu zelvicku, kazdy loop reprezentuje
      // riadok (rn), stlpec (sn) a smer (dirn), kde n je cislo korytancky
      if (zelv == 1) {
        r = &r1;
        s = &s1;
        dir = &dir1;
      } else if (zelv == 2) {
        r = &r2;
        s = &s2;
        dir = &dir2;
      }
      // posledna je 3 viac ako 3 nebudu (1 podmienka)
      else {
        r = &r3;
        s = &s3;
        dir = &dir3;
      }

      if (ukon == 'r') {
        *dir = (*dir + 1) % 4; // vysvetlene pri definovani preco % 4
      } else if (ukon == 'l') {
        *dir = (*dir - 1) % 4;
      } else if (ukon == 'm') {
        // pouzijem case pre lepsie citanie tak switch
        // https://www.w3schools.com/c/c_switch.php
        switch (*dir) {
        case 0:
          // korytnacka →
          (*s)++;
          break;
        case 1:
          // korytnacka ↓
          (*r)++;
          break;
        case 2:
          // korytnacka ←
          (*s)--;
          break;
        case 3:
          // korytnacka ↑
          (*r)--;
          break;
        }
        // overflow
        if (*s >= stloupce) {
          *s = 0;
        }
        if (*s < 0) {
          *s = stloupce - 1;
        }
        if (*r >= radky) {
          *r = 0;
        }
        if (*r < 0) {
          *r = radky - 1;
        }
      }
    }
  }
  return 0;
}
