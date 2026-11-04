#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int pocet_malych(char text[]) {
    int pocet = 0;

    for (int i = 0; text[i] != '\0'; i++) {
        if (islower(text[i])) {
            pocet++;
        }
    }

    return pocet;
}

int pocet_velkych(char text[]) {
  int pocet = 0;

    for (int i = 0; text[i] != '\0'; i++) {
        if (isupper(text[i])) {
            pocet++;
        }
    }

    return pocet;
}

int pocet_mezer(char text[]) {
    int pocet = 0;

    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] == ' ') {
            pocet++;
        }
    }

    return pocet;
}

void normalizace_radku(char text[]) {
    int i = 0;
    int j = 0;

    while (text[i] != '\0') {

        while (text[i] == ' ') {
            i++;
        }

        if (text[i] == '\0') {
            break;
        }

        int zacatek = i;
        int velke = 0;

        while (text[i] != '\0' && text[i] != ' ') {
            if (isupper(text[i])) {
                velke = 1;
            }
            i++;
        }

        if (j > 0) {
            text[j] = ' ';
            j++;
        }

        char predchozi = '\0';
        int prvni = 1;

        for (int k = zacatek; k < i; k++) {
            char znak = text[k];

            if (velke == 1) {
                if (prvni == 1) {
                    if (islower(znak)) {
                        znak = znak - 32;
                    }
                } else {
                    if (isupper(znak)) {
                        znak = znak + 32;
                    }
                }
            } else {
                if (islower(znak)) {
                    znak = znak - 32;
                }
            }

            if (prvni == 1 || znak != predchozi) {
                text[j] = znak;
                j++;
            }

            predchozi = znak;
            prvni = 0;
        }
    }

    text[j] = '\0';
}

int main(void) {
    char text[51];
    int n;

    fgets(text, sizeof(text), stdin);
    n = atoi(text);

    for (int i = 0; i < n; i++) {
        fgets(text, sizeof(text), stdin);

        for (int j = 0; text[j] != '\0'; j++) {
            if (text[j] == '\n' || text[j] == '\r') {
                text[j] = '\0';
                break;
            }
        }

        int male_pred = pocet_malych(text);
        int velke_pred = pocet_velkych(text);
        int mezery_pred = pocet_mezer(text);

        normalizace_radku(text);

        int male_po = pocet_malych(text);
        int velke_po = pocet_velkych(text);
        int mezery_po = pocet_mezer(text);

        printf("%s\n", text);
        printf("lowercase: %d -> %d\n", male_pred, male_po);
        printf("uppercase: %d -> %d\n", velke_pred, velke_po);
        printf("spaces: %d -> %d\n", mezery_pred, mezery_po);

        if (i < n - 1) {
            printf("\n");
        }
    }

    return 0;
}


