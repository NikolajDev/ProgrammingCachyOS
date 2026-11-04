#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_upper(char *str) {
  int count = 0;
  for (int i = 0; i < strlen(str); i++) {
    if (isupper((unsigned char)(str[i]))) {
      count++;
    }
  }
  return count;
}

int count_lower(char *str) {
  int count = 0;
  for (int i = 0; i < strlen(str); i++) {
    if (islower((unsigned char)(str[i]))) {
      count++;
    }
  }
  return count;
}

int count_spaces(char *str) {
  int count = 0;
  for (int i = 0; i < strlen(str); i++) {
    if ((str[i]) == ' ') {
      count++;
    }
  }
  return count;
}

void first_up(char *str) {
  int i = 0;
  while (i < strlen(str)) {
    if (i == 0) {
      str[i] = toupper((unsigned char)(str[i]));
    } else {
      str[i] = tolower((unsigned char)(str[i]));
    }
    i++;
  }
}

void all_upper(char *str) {
  int i = 0;
  while (i < strlen(str)) {
    str[i] = toupper((unsigned char)(str[i]));
    i++;
  }
}

void remove_same_chars(char *str) {
  int len = strlen(str);

  int zapis = 1; // ratame s tym ze prvy bude vzdy "specificky"
  for (int porovnaj = 1; porovnaj < len; porovnaj++) {
    if (str[porovnaj] != str[zapis - 1]) {
      str[zapis] = str[porovnaj];
      zapis++;
    }
  }
  str[zapis] = '\0';
}

void normalizuj_slovo(char *str) {
  if (count_upper(str) > 0) {
    first_up(str);
  } else {
    all_upper(str);
  }

  remove_same_chars(str);
}

void normalizuj(char *str) {
  size_t len = strlen(str);
  if (len > 0 && str[len - 1] == '\n') {
    str[len - 1] = '\0';
    len--;
  }

  char vystup[51];
  int out_idx = 0;
  char slovo[51];
  int idx = 0;

  for (size_t i = 0; i <= len; i++) {
    if (str[i] != ' ' && str[i] != '\0') {
      slovo[idx] = str[i];
      idx++;
    } else if (idx > 0) {
      slovo[idx] = '\0';
      normalizuj_slovo(slovo);
      if (out_idx > 0) {
        vystup[out_idx] = ' ';
        out_idx++;
      }
      for (int j = 0; slovo[j] != '\0'; j++) {
        vystup[out_idx] = slovo[j];
        out_idx++;
      }
      idx = 0;
    }
  }
  vystup[out_idx] = '\0';
  strcpy(str, vystup);
}

int main() {
  char input_line[51];
  fgets(input_line, sizeof(input_line), stdin);
  int n = atoi(input_line);

  // printf("%d", n);
  for (int i = 0; i < n; i++) {
    fgets(input_line, sizeof(input_line), stdin);
    // stats:
    int upper_b, lower_b, spaces_b;
    int upper_a, lower_a, spaces_a;

    // Pred (before)
    upper_b = count_upper(input_line);
    lower_b = count_lower(input_line);
    spaces_b = count_spaces(input_line);

    normalizuj(input_line);

    // Po (after)
    upper_a = count_upper(input_line);
    lower_a = count_lower(input_line);
    spaces_a = count_spaces(input_line);

    if (i > 0) {
      printf("\n");
    }
    printf("%s\nlowercase: %d -> %d\nuppercase: %d -> %d\nspaces: %d -> %d\n",
           input_line, lower_b, lower_a, upper_b, upper_a, spaces_b, spaces_a);
  }

  return 0;
}
