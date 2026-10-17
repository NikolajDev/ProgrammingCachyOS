#include "drawing.h"

void cara(int x, int y, int len) {
  for (int i = 0; i <= len * 2; i++) {
    move_to(x, y);
    set_blue_color();
    draw_pixel();
    y += 2;
  }
}

void schod(int x, int y) {
  for (int i = 0; i < 3; i++) {
    move_to(x, y + i);
    set_yellow_color();
    draw_pixel();
  }
  y += 3;
  for (int i = 0; i < 3; i++) {
    move_to(x + i, y);
    set_yellow_color();
    draw_pixel();
  }
  x += 3;
}

void schody(int x, int y, int pocet) {
  for (int i = 0; i < pocet; i++) {
    schod(x + (3 * i), y + (3 * i));
  }
}

// vyska je urcovana x a sirka y, takze presne naopak ako to je pri suradnicovom
// systeme dufam

// kvet bude stvorec

void kvet(int x, int y, int sirka_y, int vyska_x) {
  for (int line = 0; line < vyska_x; line++) {
    for (int column = 0; column < sirka_y; column++) {
      move_to(x + line, y + column);
      set_yellow_color();
      draw_pixel();
    }
  }
}

void rostlina(int x, int y, int sirka_y, int vyska_x) {
  // zavolam kvet s upravenou vyskou pre mna stopka bude dlha 3
  kvet(x, y, sirka_y, vyska_x - 3);
  // vypocet stredu rastliny - ratam s tym ze to bude vdzy liche cislo
  int mid = y + (sirka_y / 2);
  int helper = 0;
  x += vyska_x - 3;
  while (helper < 3) {
    move_to(x + helper, mid);
    set_green_color();
    draw_pixel();
    helper++;
  }
}

void zahrada(int x, int y, int pocet_radku, int pocet_stloupcu, int sirka_y,
             int vyska_x) {
  int y_reset = y;
  for (int pocet_r = 0; pocet_r < pocet_radku; pocet_r++) {
    for (int pocet_s = 0; pocet_s < pocet_stloupcu; pocet_s++) {
      rostlina(x, y, sirka_y, vyska_x);
      y += sirka_y + 1;
    }
    x += vyska_x + 1;
    y = y_reset;
  }
}

void DVD(int x, int y) {
  int x_add = 1;
  int y_add = 1;
  while (1) {
    clear_screen();
    move_to(x, y);
    set_green_color();
    draw_pixel();
    animate_ms(125);
    if (x + x_add == 1) {
      x_add *= -1;
    } else if (y + y_add >= 20) {
      y_add *= -1;
    } else if ((x + x_add) >= 20) {
      x_add *= -1;
    } else if (y + y_add >= 35) {
      y_add *= -1;
    }
    x += x_add;
    y += y_add;
  }
}

void animace(int x, int y, int sirka_y, int vyska_x) {
  while (x + vyska_x != 20) {
    clear_screen();
    rostlina(x, y, sirka_y, vyska_x);
    animate();
    x += 1;
  }
}

int main() {
  // Keep this line here
  clear_screen();

  // Load the input - what should be drawn.
  int drawing = 0;
  scanf("%d", &drawing);

  // Put your drawing code here
  if (drawing == 0) {
    cara(5, 7, 13);
    cara(10, 11, 13);
    cara(1, 1, 13);
  } else if (drawing == 1) {
    schody(4, 1, 4);
    schody(1, 1, 6);
  } else if (drawing == 2) {
    rostlina(1, 1, 7, 7);
  } else if (drawing == 3) {
    zahrada(1, 1, 2, 5, 7, 7);
  } else if (drawing == 4) {
    animace(1, 1, 4, 6);
  } else {
    // ked das nieco mimo range tak ide nekonecny loop
    DVD(1, 1);
  }

  // Keep this line here
  end_drawing();

  return 0;
}
