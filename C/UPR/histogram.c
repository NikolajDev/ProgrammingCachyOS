#include <stdio.h>

int pocet_cifier(int cislo) {
  int pocet = 0;
  while (cislo > 0) {
    cislo /= 10;
    pocet++;
  }
  return pocet;
}

void hor_histogram_vyspis(int *array, int start_num) {
  int digit_len = pocet_cifier(start_num + 8);
  for (int i = 0; i < 9; i++) {
    printf("%*d", digit_len, start_num + i);
    if (array[i] > 0) {
      printf(" ");
    }
    for (int j = 0; j < array[i]; j++) {
      printf("#");
    }
    printf("\n");
  }
  if (array[9] > 0) {
    printf("invalid: ");
    for (int i = 0; i < array[9]; i++) {
      printf("#");
    }
    printf("\n");
  }
}

void histogram(int pocet_cisel, int start_num, int *array) {
  // vstupy
  int cislo = 0;
  for (int i = 0; i < pocet_cisel; i++) {
    scanf("%d", &cislo);
    if (cislo >= start_num && cislo <= start_num + 8) {
      array[cislo - start_num]++;
    } else {
      array[9]++;
    }
  }
}

int najvacsi(int *array, int dlzka) {
  int top = 0;
  for (int i = 0; i < dlzka; i++) {
    if (array[i] > top) {
      top = array[i];
    }
  }
  return top;
}

void ver_histogram_vypis(int *array) {
  int max_val = najvacsi(array, 10);
  for (int max = max_val; max > 0; max--) {
    // invalid
    if (array[9] >= max) {
      printf("#");
    } else {
      printf(" ");
    }
    for (int index = 0; index < 9; index++) {
      // to iste ako pri invalid nums
      if (array[index] >= max) {
        printf("#");
      } else {
        printf(" ");
      }
    }
    printf("\n");
  }
  printf("i");
  for (int i = 1; i <= 9; i++) {
    printf("%d", i);
  }
}

int main() {
  char mode;
  scanf("%c", &mode);
  int array[10] = {0};
  int start_num = 0;
  int pocet_cisel = 0;
  if (mode == 'h') {
    scanf("%d %d", &pocet_cisel, &start_num);
    histogram(pocet_cisel, start_num, array);
    hor_histogram_vyspis(array, start_num);
  } else if (mode == 'v') {
    scanf("%d %d", &pocet_cisel, &start_num);
    histogram(pocet_cisel, start_num, array);
    ver_histogram_vypis(array);
  } else {
    printf("Neplatny mod vykresleni\n");
    return 1;
  }

  return 0;
}
/* TESTING
for (int i = 0; i < 10; i++) {
  printf("%d\n", array[i]);
}
  histogram_vyspis(array); */
