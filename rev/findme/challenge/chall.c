#include <stdio.h>
#include <string.h>

//clang -S -emit-llvm chall.c -o chall.ll

void string_to_hex(const char* str, char* hex_str) {
    int i;
    int j = 0;
    int len = strlen(str);

    // Iterate through each character in the string
    for (i = 0; i < len; i++) {
        // Print each character as two hexadecimal digits
        sprintf(&hex_str[j], "%02x", (unsigned char)str[i]);
        j += 2;  // Move to the next spot in the output hex string
    }
    hex_str[j] = '\0';  // Null-terminate the hex string
}

int checkflag(const char *inp) {
    int m[] = {301, 728, 546, 315, 756, 497, 315, 658, 301, 322, 770, 315, 623, 532, 315, 742, 756, 315, 763, 315, 728, 343, 322, 770, 301, 294, 728};
    if (strncmp(inp, "Alphabit{", 9) != 0 || inp[69] != '}') {
        return 0;
    }
    for (int i = 9; i < 35; i++) {
        if ((inp[i] - 6) * 7 != m[i - 9]) {
            return 0;
        }
    }
    if (inp[36] != '_' || inp[39] != '_' || inp[43] != '_' || inp[47] != '_' || inp[53] != '_' || inp[61] != '_') {
        return 0;
    }
    char hex_string [20];
    string_to_hex(inp + 62,hex_string);
    if (strcmp(hex_string, "6d346368316e337d") != 0) {
        return 0;
    }
    int n[] = {123, 54, 119, 121, 122, 57, 113};
    for (int i = 54; i < 60; i++) {
        if (inp[i] + 5 != n[i - 54]) {
            return 0;
        }
    }
    char middle_part[17] = {0}; // 16 characters + null terminator
    for (int i = 37; i < 53; i++) {
        middle_part[i - 37] = inp[i];
    }
    if (strcmp(middle_part, "0f_Th3_l0w_l3v3l") != 0) {
        return 0;
    }
    return 1;
}

int main() {
    printf("Now The Challenge is renamed to Crack me\n");
    char kaka[100]; // Assuming the input will not exceed 100 characters
    printf("please give me the flag : ");
    fgets(kaka, sizeof(kaka), stdin);
    kaka[strcspn(kaka, "\n")] = 0; // Remove newline character from input
    if (checkflag(kaka)) {
        printf("Correct Flag!\n");
    } else {
        printf("Try Again\n");
    }
    return 0;
}

