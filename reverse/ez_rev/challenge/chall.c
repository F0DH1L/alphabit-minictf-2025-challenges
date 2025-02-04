#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

int data() {
    int array[70];

    array[0] = 108241;
    array[1] = 295936;
    array[2] = 318096;
    array[3] = 274576;
    array[4] = 239121;
    array[5] = 244036;
    array[6] = 279841;
    array[7] = 341056;
    array[8] = 383161;
    array[9] = 171396;
    array[10] = 67081;
    array[11] = 352836;
    array[12] = 67081;
    array[13] = 329476;
    array[14] = 335241;
    array[15] = 259081;
    array[16] = 229441;
    array[17] = 62001;
    array[18] = 335241;
    array[19] = 229441;
    array[20] = 67081;
    array[21] = 376996;
    array[22] = 229441;
    array[23] = 201601;
    array[24] = 59536;
    array[25] = 184041;
    array[26] = 229441;
    array[27] = 285156;
    array[28] = 346921;
    array[29] = 72361;
    array[30] = 77841;
    array[31] = 229441;
    array[32] = 306916;
    array[33] = 67081;
    array[34] = 67081;
    array[35] = 254016;
    array[36] = 229441;
    array[37] = 77841;
    array[38] = 59536;
    array[39] = 229441;
    array[40] = 329476;
    array[41] = 67081;
    array[42] = 352836;
    array[43] = 67081;
    array[44] = 329476;
    array[45] = 335241;
    array[46] = 67081;
    array[47] = 229441;
    array[48] = 341056;
    array[49] = 274576;
    array[50] = 67081;
    array[51] = 229441;
    array[52] = 59536;
    array[53] = 163216;
    array[54] = 259081;
    array[55] = 329476;
    array[56] = 239121;
    array[57] = 77841;
    array[58] = 62001;
    array[59] = 59536;
    array[60] = 306916;
    array[61] = 175561;
    array[62] = 395641;
    for (int i = 0; i < 63; i++) {
        printf("%d ", array[i]);
    }

    return 0;
}

int main() {
    const char* flag = "fakeflag";
    int array_size = strlen(flag);    
    int* array = (int*)malloc(array_size * sizeof(int));
    
    for(int i = 0; i < array_size; i++) {
        array[i] = (int)pow((flag[i] * 5) + 4, 2); 
    }    

    free(array);
    data();
    return 0;
}

