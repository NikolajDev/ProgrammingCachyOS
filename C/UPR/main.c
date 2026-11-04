#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>

void kebab_to_camel(const char *src, char *dest) {
  size_t j = 0;

  for (size_t i = 0; src[i] != '\0'; ++i) {
    if (src[i] == '-' && i > 0 && src[i + 1] != '\0') {
      ++i; // preskoč '-'
      dest[j++] = (char)toupper((unsigned char)src[i]);
    } else {
      dest[j++] = src[i];
    }
  }

  dest[j] = '\0';
}

int main(void) {
  char line[128];
  char out[128]; // výstup je vždy kratší alebo rovnako dlhý ako vstup

  while (fgets(line, sizeof line, stdin) != NULL) {
    line[strcspn(line, "\n")] = '\0'; // odstráň '\n'

    kebab_to_camel(line, out);
    printf("%s\n", out);
  }

  return 0;
}
