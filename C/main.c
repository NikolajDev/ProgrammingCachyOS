#include <stdio.h>
int main (void) {
    char prvni;
    int n,m; //n pocet cisel m nejmensi cislo
    scanf ("%c", &prvni);
    if (prvni != 'v' && prvni != 'h') {
        printf ("Neplatny mod vykresleni");
        return 1;
    }
    scanf("%d%d",&n, &m);
    int druha [10] ={0};
    for (int i = 0; i < n; i++) {
        int cislo;
    if   (scanf("%d", &cislo) != 1)
        return 1;
    }

    int indexy;
    if (int cislo > = m && cislo < = m + 8) {index = cislo - m;
        } else {
            druha[9]++;
        }

    if (prvni == 'v') {
         for (int i = 0; i < 10; i++) {
            if (i < 9) {
                printf("%d ", m + i);
            } else {
                printf("blbe\n ");
            }

            for (int j = 0; j < druha[i]; j++) {
                printf("#\n");
            }
        }
    } else if (prvni == 'h') {
        int nejvetsi = 0;

        for (int i = 0; i < 10; i++) {

        for (int i = 0; i < 10; i++) {
            if (druha[i] > nejvetsi) {
                nejvetsi = druha[i];
            }
        }

        for (int i = nejvetsi; i > 0; i--) {
            for (int j = 0; j < 10; j++) {
                if (druha[j] >= i) {
                    printf("# ");
                } else {
                    printf("  ");
                }
            }
            printf("\n");
        }
        for (int i = 0; i < 10; i++) {
            if (i < 9) {
                printf("%d ", m + i);
            } else {
                printf("blbe\n");
            }
        }
    }
  }

    return 0;
}