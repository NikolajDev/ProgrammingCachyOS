#include <stdio.h>
#include <stdbool.h>

// Efektívna kontrola palindrómu bez pow() a bez polí
bool isPalindrome(long long n) {
    if (n < 0) return false;
    long long reversed = 0, original = n;
    while (n > 0) {
        reversed = reversed * 10 + (n % 10);
        n /= 10;
    }
    return original == reversed;
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;

    while (t--) {
        long long y;
        scanf("%lld", &y);
        y++;

        // Ak chceš ostať pri cykle, aspoň optimalizuj isPalindrome
        while (!isPalindrome(y)) {
            // Tu by sa dal doplniť skok (napr. o 10, o 100), 
            // ale pre úplnú efektivitu treba "zrkadlový" algoritmus.
            y++;
        }
        printf("%lld\n", y);
    }
    return 0;
}