#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE 52 // 50 znaků + '\0' + rezerva

int main(void) {
  char line[MAX_LINE];

  // načtení n
  fgets(line, MAX_LINE, stdin);
  int n = atoi(line);

  for (int i = 0; i < n; i++) {
    fgets(line, MAX_LINE, stdin);

    // --- statistika původního řádku ---
    int low_before = 0, up_before = 0, sp_before = 0;
    for (int j = 0; line[j] != '\0'; j++) {
      if (line[j] >= 'a' && line[j] <= 'z')
        low_before++;
      else if (line[j] >= 'A' && line[j] <= 'Z')
        up_before++;
      else if (line[j] == ' ')
        sp_before++;
    }

    // --- normalizace ---
    char result[MAX_LINE] = "";
    int r = 0;   // délka výsledku
    int pos = 0; // pozice v původním řádku

    while (line[pos] != '\0') {
      // přeskočit mezery (a odřádkování)
      if (line[pos] == ' ' || line[pos] == '\n') {
        pos++;
        continue;
      }

      // načtení jednoho slova
      char word[MAX_LINE];
      int w = 0;
      int has_upper = 0;
      while (line[pos] != '\0' && line[pos] != ' ' && line[pos] != '\n') {
        if (line[pos] >= 'A' && line[pos] <= 'Z')
          has_upper = 1;
        word[w++] = line[pos++];
      }
      word[w] = '\0';

      // normalizace velikosti písmen
      for (int j = 0; j < w; j++) {
        if (has_upper) {
          if (j == 0)
            word[j] = toupper(word[j]);
          else
            word[j] = tolower(word[j]);
        } else {
          word[j] = toupper(word[j]);
        }
      }

      // odstranění opakujících se znaků za sebou
      char clean[MAX_LINE];
      int c = 0;
      for (int j = 0; j < w; j++) {
        if (j == 0 || word[j] != word[j - 1]) {
          clean[c++] = word[j];
        }
      }
      clean[c] = '\0';

      // přidání do výsledku (s mezerou před slovem, pokud není první)
      if (r > 0)
        result[r++] = ' ';
      for (int j = 0; j < c; j++) {
        result[r++] = clean[j];
      }
      result[r] = '\0';
    }

    // --- statistika znormalizovaného řádku ---
    int low_after = 0, up_after = 0, sp_after = 0;
    for (int j = 0; result[j] != '\0'; j++) {
      if (result[j] >= 'a' && result[j] <= 'z')
        low_after++;
      else if (result[j] >= 'A' && result[j] <= 'Z')
        up_after++;
      else if (result[j] == ' ')
        sp_after++;
    }

    // --- výpis ---
    printf("%s\n", result);
    printf("lowercase: %d -> %d\n", low_before, low_after);
    printf("uppercase: %d -> %d\n", up_before, up_after);
    printf("spaces: %d -> %d\n", sp_before, sp_after);
    printf("\n");
  }

  return 0;
}
