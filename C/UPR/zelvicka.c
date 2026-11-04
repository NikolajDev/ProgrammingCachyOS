#include <stdio.h>
#include <stdlib.h>

void platno(char *canvas, int radky, int stloupce) {
  for (int i = 0; i < radky * stloupce; i++) {
    canvas[i] = '.';
  }
}

void doleva(int *dir) {
  if (*dir == 0) {
    *dir = 3;
  } else {
    *dir = (*dir - 1) % 4;
  }
}

void doprava(int *dir) { *dir = (*dir + 1) % 4; }

void dopredu(int *r, int *s, int *dir, int stloupce, int radky) {
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

void kresli(char *canvas, int *r, int stloupce, int *s) {
  int index = (*r) * stloupce + (*s);
  if (canvas[index] == 'o') {
    canvas[index] = '.';
  } else {
    canvas[index] = 'o';
  }
}

int main() {
  int radky = 0;
  int stloupce = 0;
  scanf("%d %d", &radky, &stloupce);
  char *canvas = malloc(radky * stloupce * sizeof(char));
  // platno
  platno(canvas, radky, stloupce);

  // max 3 zlevicky pre kazdu si vytvorim premeu r a s (riadok stlpec, a
  // podla vstupu upravim pohyb/smer); dir = 0 doprava (stlpec + 1) dir = 1
  // dole    (riadok + 1) dir = 2 dolava  (stlpec - 1) dir = 3 hore (ridok -
  // 1)
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
        doprava(dir);
      } else if (ukon == 'l') {
        doleva(dir);
      } else if (ukon == 'm') {
        // pouzijem case pre lepsie citanie tak switch
        // https://www.w3schools.com/c/c_switch.php
        dopredu(r, s, dir, stloupce, radky);
      } else if (ukon == 'o') {
        // 1 - rozmerne pole, a da se to napisa na m x n, kazdy novy riadok je m
        // * nas radek + stlpec
        kresli(canvas, r, stloupce, s);
      }
    }
  }

  for (int riadok = 0; riadok < radky; riadok++) {
    for (int stlpec = 0; stlpec < stloupce; stlpec++) {
      // vytiahne 'char', ktory sa nachadza na danej adrese
      putchar(canvas[riadok * stloupce + stlpec]);
    }
    printf("\n");
  }

  free(canvas);
  return 0;
}
