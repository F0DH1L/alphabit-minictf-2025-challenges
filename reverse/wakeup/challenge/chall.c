#include <stdio.h>
#include <string.h>
#include <unistd.h>
//gcc -o chall chall.c -no-pie
//or
//gcc -02 -s -fvisibility=hidden -fPIC -o chall chall.c -no-pie
char *finic1943() {
    unsigned char p1[] = {0x41};  
    unsigned char p2[] = {0x6C};  
    unsigned char p3[] = {0x70, 0x68};  
    unsigned char p4[] = {0x61};  
    unsigned char p5[] = {0x62};  
    unsigned char p6[] = {0x69};  
    unsigned char p7[] = {0x74};  
    unsigned char p8[] = {0x7B};  
    unsigned char p9[] = {0x30};  
    unsigned char p10[] = {0x78};  
    unsigned char p11[] = {0x39};  
    unsigned char p12[] = {0x30};  
    unsigned char p13[] = {0x5F};  
    unsigned char p14[] = {0x31};  
    unsigned char p15[] = {0x73};  
    unsigned char p16[] = {0x5F};  
    unsigned char p17[] = {0x74};  
    unsigned char p18[] = {0x68};  
    unsigned char p19[] = {0x33};  
    unsigned char p20[] = {0x5F};  
    unsigned char p21[] = {0x6E};  
    unsigned char p22[] = {0x30};  
    unsigned char p23[] = {0x70};  
    unsigned char p24[] = {0x5F};  
    unsigned char p25[] = {0x31};  
    unsigned char p26[] = {0x6E};  
    unsigned char p27[] = {0x73};  
    unsigned char p28[] = {0x74};  
    unsigned char p29[] = {0x72};  
    unsigned char p30[] = {0x75};  
    unsigned char p31[] = {0x63};  
    unsigned char p32[] = {0x74};  
    unsigned char p33[] = {0x31};  
    unsigned char p34[] = {0x30};  
    unsigned char p35[] = {0x6E};  
    unsigned char p36[] = {0x7D};  
    static char result[50];
    int i = 0;

    unsigned char *parts[] = {
        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14,
        p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26,
        p27, p28, p29, p30, p31, p32, p33, p34, p35, p36
    };

    for (int j = 0; j < 36; j++) {
        result[i++] = parts[j][0];
    }
    result[i] = '\0';  

    return result;
}

void f1(unsigned char *d, size_t l, unsigned char k1) {
    for (size_t i = 0; i < l; i++) {
        d[i] ^= k1;
        d[i] = (d[i] * 2 - 5) / 2; 
    }
}

unsigned char p1[] = {0x41, 0x78, 0x4e};  
unsigned char p2[] = {0x62};               
unsigned char p3[] = {0x7B, 0x33, 0x30};   
unsigned char p4[] = {0x5F};               
unsigned char p5[] = {0x5F, 0x73};         
unsigned char p6[] = {0x5F, 0x73};         
unsigned char p7[] = {0x5F, 0x63};         
unsigned char p8[] = {0x74, 0x73};         
unsigned char p9[] = {0x31};         

unsigned char k = 0xAA; 

char *f2() {
    static char f[50];
    unsigned char *p[] = {p1, p2, p3, p4, p5, p6, p7, p8, p9};
    size_t len[] = {sizeof(p1), sizeof(p2), sizeof(p3), sizeof(p4), sizeof(p5), sizeof(p6), sizeof(p7), sizeof(p8), sizeof(p9)};
    
    
    for (int i = 0; i < 9; i++) {
        f1(p[i], len[i], k);
    }

    
    unsigned char *tmp;
    tmp = (unsigned char *)p1; 
    for (int i = 0; i < sizeof(p1); i++) f[i] = tmp[i];
    tmp = (unsigned char *)p2; 
    for (int i = 0; i < sizeof(p2); i++) f[sizeof(p1) + i] = tmp[i];
    tmp = (unsigned char *)p3; 
    for (int i = 0; i < sizeof(p3); i++) f[sizeof(p1) + sizeof(p2) + i] = tmp[i];
    tmp = (unsigned char *)p4; 
    for (int i = 0; i < sizeof(p4); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + i] = tmp[i];
    tmp = (unsigned char *)p5; 
    for (int i = 0; i < sizeof(p5); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + i] = tmp[i];
    tmp = (unsigned char *)p6; 
    for (int i = 0; i < sizeof(p6); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + i] = tmp[i];
    tmp = (unsigned char *)p7; 
    for (int i = 0; i < sizeof(p7); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + sizeof(p6) + i] = tmp[i];
    tmp = (unsigned char *)p8; 
    for (int i = 0; i < sizeof(p8); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + sizeof(p6) + sizeof(p7) + i] = tmp[i];
    tmp = (unsigned char *)p9; 
    for (int i = 0; i < sizeof(p9); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + sizeof(p6) + sizeof(p7) + sizeof(p8) + i] = tmp[i];
    
    return finic1943();
}

#include <stdio.h>
#include <string.h>
#include <unistd.h>
void o_7168262a1231a255d89b3fb32cd32e78(unsigned char* o_b92231cb0b4e50200ef99dd3fa2c8784,size_t o_3775b8f10acbb6914da02de20b56a5e1,unsigned char o_2ed0d5aee15363fbc44338b7c3f22121){for (size_t o_823c99ff86e5cb817dd711c6cd854238=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_823c99ff86e5cb817dd711c6cd854238 < o_3775b8f10acbb6914da02de20b56a5e1) & !!(o_823c99ff86e5cb817dd711c6cd854238 < o_3775b8f10acbb6914da02de20b56a5e1);o_823c99ff86e5cb817dd711c6cd854238++){o_b92231cb0b4e50200ef99dd3fa2c8784[o_823c99ff86e5cb817dd711c6cd854238] ^= o_2ed0d5aee15363fbc44338b7c3f22121;o_b92231cb0b4e50200ef99dd3fa2c8784[o_823c99ff86e5cb817dd711c6cd854238] = (o_b92231cb0b4e50200ef99dd3fa2c8784[o_823c99ff86e5cb817dd711c6cd854238] * (0x0000000000000004 + 0x0000000000000202 + 0x0000000000000802 - 0x0000000000000A06) - (0x000000000000000A + 0x0000000000000205 + 0x0000000000000805 - 0x0000000000000A0F)) / (0x0000000000000004 + 0x0000000000000202 + 0x0000000000000802 - 0x0000000000000A06);};};unsigned char o_40c27aedfa65a53f2c748be5c5ffc0d4[]={0x41, 0x68, 0x61};unsigned char o_1876ea04ddbea85983709af21f74a79d[]={0x62};unsigned char o_71d0bdb0478a3a4b369df95b104f3b68[]={0x7B, 0x39, 0x30};unsigned char o_a2a099cdc89b3a97d4406b9f609e5887[]={0x5F};unsigned char o_4d212805b28f0f036f6414f7320ebfd4[]={0x5F, 0x33};unsigned char o_017d7ebdfebb2de91987f599a0fd73ac[]={0x5F, 0x70};unsigned char o_11f4dd323284e6a69ec8447554da73b4[]={0x5F, 0x73};unsigned char o_29bad6b1930f2901ae709bcacce7ab76[]={0x74, 0x63};unsigned char o_df65a784f61fbeda6320150556d39b00[]={0x31, 0x7D};unsigned char o_c50138ce0e7cb16092e5e98f698d6604=(0x0000000000000154 + 0x00000000000002AA + 0x00000000000008AA - 0x0000000000000BFE);char * o_a244e04c8d45919eba3778253bfb787a(){static char o_d92a88bba5f737545b97c476632bf0fe[(0x0000000000000064 + 0x0000000000000232 + 0x0000000000000832 - 0x0000000000000A96)];unsigned char * o_037bd1253bd4c720e334f92f9a523aed[]={p1, p2, p3, p4, p5, p6, p7, p8, p9};size_t o_a3895d4db48ffb278ccabe10226f8887[]={sizeof(p1), sizeof(p2), sizeof(p3), sizeof(p4), sizeof(p5), sizeof(p6), sizeof(p7), sizeof(p8), sizeof(p9)};for (int o_710069d902291fac81440b3318c6c8c3=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_710069d902291fac81440b3318c6c8c3 < (0x0000000000000012 + 0x0000000000000209 + 0x0000000000000809 - 0x0000000000000A1B)) & !!(o_710069d902291fac81440b3318c6c8c3 < (0x0000000000000012 + 0x0000000000000209 + 0x0000000000000809 - 0x0000000000000A1B));o_710069d902291fac81440b3318c6c8c3++){o_7168262a1231a255d89b3fb32cd32e78(o_037bd1253bd4c720e334f92f9a523aed[o_710069d902291fac81440b3318c6c8c3],o_a3895d4db48ffb278ccabe10226f8887[o_710069d902291fac81440b3318c6c8c3],o_c50138ce0e7cb16092e5e98f698d6604);};unsigned char* o_a8daea662573534b70144a981106c27d;o_a8daea662573534b70144a981106c27d = (unsigned char* )o_40c27aedfa65a53f2c748be5c5ffc0d4;for (int o_d30e401701d183e076d5dd4592547ffc=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_d30e401701d183e076d5dd4592547ffc < sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4))) & !!(o_d30e401701d183e076d5dd4592547ffc < sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)));o_d30e401701d183e076d5dd4592547ffc++)o_d92a88bba5f737545b97c476632bf0fe[o_d30e401701d183e076d5dd4592547ffc] = o_a8daea662573534b70144a981106c27d[o_d30e401701d183e076d5dd4592547ffc];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_1876ea04ddbea85983709af21f74a79d;for (int o_df398d8baafa602f230dcfabe84d1ffc=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_df398d8baafa602f230dcfabe84d1ffc < sizeof((o_1876ea04ddbea85983709af21f74a79d))) & !!(o_df398d8baafa602f230dcfabe84d1ffc < sizeof((o_1876ea04ddbea85983709af21f74a79d)));o_df398d8baafa602f230dcfabe84d1ffc++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + o_df398d8baafa602f230dcfabe84d1ffc] = o_a8daea662573534b70144a981106c27d[o_df398d8baafa602f230dcfabe84d1ffc];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_71d0bdb0478a3a4b369df95b104f3b68;for (int o_88eed1fc1672780e1a071e5b22c1ba3c=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_88eed1fc1672780e1a071e5b22c1ba3c < sizeof((o_71d0bdb0478a3a4b369df95b104f3b68))) & !!(o_88eed1fc1672780e1a071e5b22c1ba3c < sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)));o_88eed1fc1672780e1a071e5b22c1ba3c++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + o_88eed1fc1672780e1a071e5b22c1ba3c] = o_a8daea662573534b70144a981106c27d[o_88eed1fc1672780e1a071e5b22c1ba3c];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_a2a099cdc89b3a97d4406b9f609e5887;for (int o_c4e659bc245521613bd0c6995712ae9b=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_c4e659bc245521613bd0c6995712ae9b < sizeof((o_a2a099cdc89b3a97d4406b9f609e5887))) & !!(o_c4e659bc245521613bd0c6995712ae9b < sizeof((o_a2a099cdc89b3a97d4406b9f609e5887)));o_c4e659bc245521613bd0c6995712ae9b++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)) + o_c4e659bc245521613bd0c6995712ae9b] = o_a8daea662573534b70144a981106c27d[o_c4e659bc245521613bd0c6995712ae9b];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_4d212805b28f0f036f6414f7320ebfd4;for (int o_e7e004ae0ff3fcc2ec9b6df84addaab0=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_e7e004ae0ff3fcc2ec9b6df84addaab0 < sizeof((o_4d212805b28f0f036f6414f7320ebfd4))) & !!(o_e7e004ae0ff3fcc2ec9b6df84addaab0 < sizeof((o_4d212805b28f0f036f6414f7320ebfd4)));o_e7e004ae0ff3fcc2ec9b6df84addaab0++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)) + sizeof((o_a2a099cdc89b3a97d4406b9f609e5887)) + o_e7e004ae0ff3fcc2ec9b6df84addaab0] = o_a8daea662573534b70144a981106c27d[o_e7e004ae0ff3fcc2ec9b6df84addaab0];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_017d7ebdfebb2de91987f599a0fd73ac;for (int o_c7d66e51ccf40d166c84d95923143fab=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_c7d66e51ccf40d166c84d95923143fab < sizeof((o_017d7ebdfebb2de91987f599a0fd73ac))) & !!(o_c7d66e51ccf40d166c84d95923143fab < sizeof((o_017d7ebdfebb2de91987f599a0fd73ac)));o_c7d66e51ccf40d166c84d95923143fab++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)) + sizeof((o_a2a099cdc89b3a97d4406b9f609e5887)) + sizeof((o_4d212805b28f0f036f6414f7320ebfd4)) + o_c7d66e51ccf40d166c84d95923143fab] = o_a8daea662573534b70144a981106c27d[o_c7d66e51ccf40d166c84d95923143fab];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_11f4dd323284e6a69ec8447554da73b4;for (int o_a175ad1a06c2618507b2e4d1f3dca65c=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_a175ad1a06c2618507b2e4d1f3dca65c < sizeof((o_11f4dd323284e6a69ec8447554da73b4))) & !!(o_a175ad1a06c2618507b2e4d1f3dca65c < sizeof((o_11f4dd323284e6a69ec8447554da73b4)));o_a175ad1a06c2618507b2e4d1f3dca65c++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)) + sizeof((o_a2a099cdc89b3a97d4406b9f609e5887)) + sizeof((o_4d212805b28f0f036f6414f7320ebfd4)) + sizeof((o_017d7ebdfebb2de91987f599a0fd73ac)) + o_a175ad1a06c2618507b2e4d1f3dca65c] = o_a8daea662573534b70144a981106c27d[o_a175ad1a06c2618507b2e4d1f3dca65c];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_29bad6b1930f2901ae709bcacce7ab76;for (int o_3af9feb4d944d1cbb9c868d03735bbad=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_3af9feb4d944d1cbb9c868d03735bbad < sizeof((o_29bad6b1930f2901ae709bcacce7ab76))) & !!(o_3af9feb4d944d1cbb9c868d03735bbad < sizeof((o_29bad6b1930f2901ae709bcacce7ab76)));o_3af9feb4d944d1cbb9c868d03735bbad++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)) + sizeof((o_a2a099cdc89b3a97d4406b9f609e5887)) + sizeof((o_4d212805b28f0f036f6414f7320ebfd4)) + sizeof((o_017d7ebdfebb2de91987f599a0fd73ac)) + sizeof((o_11f4dd323284e6a69ec8447554da73b4)) + o_3af9feb4d944d1cbb9c868d03735bbad] = o_a8daea662573534b70144a981106c27d[o_3af9feb4d944d1cbb9c868d03735bbad];o_a8daea662573534b70144a981106c27d = (unsigned char* )o_df65a784f61fbeda6320150556d39b00;for (int o_e3654837bbb384bd596145b909329f18=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_e3654837bbb384bd596145b909329f18 < sizeof((o_df65a784f61fbeda6320150556d39b00))) & !!(o_e3654837bbb384bd596145b909329f18 < sizeof((o_df65a784f61fbeda6320150556d39b00)));o_e3654837bbb384bd596145b909329f18++)o_d92a88bba5f737545b97c476632bf0fe[sizeof((o_40c27aedfa65a53f2c748be5c5ffc0d4)) + sizeof((o_1876ea04ddbea85983709af21f74a79d)) + sizeof((o_71d0bdb0478a3a4b369df95b104f3b68)) + sizeof((o_a2a099cdc89b3a97d4406b9f609e5887)) + sizeof((o_4d212805b28f0f036f6414f7320ebfd4)) + sizeof((o_017d7ebdfebb2de91987f599a0fd73ac)) + sizeof((o_11f4dd323284e6a69ec8447554da73b4)) + sizeof((o_29bad6b1930f2901ae709bcacce7ab76)) + o_e3654837bbb384bd596145b909329f18] = o_a8daea662573534b70144a981106c27d[o_e3654837bbb384bd596145b909329f18];return f2();};

char *f3(){
    static char f[50];
    unsigned char *p[] = {p1, p2, p3, p4, p5, p6, p7, p8, p9};
    size_t len[] = {sizeof(p1), sizeof(p2), sizeof(p3), sizeof(p4), sizeof(p5), sizeof(p6), sizeof(p7), sizeof(p8), sizeof(p9)};
    
    
    for (int i = 0; i < 9; i++) {
        f1(p[i], len[i], k);
    }

    
    unsigned char *tmp;
    tmp = (unsigned char *)p1; 
    for (int i = 0; i < sizeof(p1); i++) f[i] = tmp[i];
    tmp = (unsigned char *)p2; 
    for (int i = 0; i < sizeof(p2); i++) f[sizeof(p1) + i] = tmp[i];
    tmp = (unsigned char *)p3; 
    for (int i = 0; i < sizeof(p3); i++) f[sizeof(p1) + sizeof(p2) + i] = tmp[i];
    tmp = (unsigned char *)p4; 
    for (int i = 0; i < sizeof(p4); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + i] = tmp[i];
    tmp = (unsigned char *)p5; 
    for (int i = 0; i < sizeof(p5); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + i] = tmp[i];
    tmp = (unsigned char *)p6; 
    for (int i = 0; i < sizeof(p6); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + i] = tmp[i];
    tmp = (unsigned char *)p7; 
    for (int i = 0; i < sizeof(p7); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + sizeof(p6) + i] = tmp[i];
    tmp = (unsigned char *)p8; 
    for (int i = 0; i < sizeof(p8); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + sizeof(p6) + sizeof(p7) + i] = tmp[i];
    tmp = (unsigned char *)p9; 
    for (int i = 0; i < sizeof(p9); i++) f[sizeof(p1) + sizeof(p2) + sizeof(p3) + sizeof(p4) + sizeof(p5) + sizeof(p6) + sizeof(p7) + sizeof(p8) + i] = tmp[i];
    return f2();
}

char *wakeup() {
  void (*ptr)(void);

    return f3();
}

char *utilsfunc() {
  void (*ptr)(void);

return wakeup();
}

char *function2005() {
  void (*ptr)(void);

return utilsfunc();
}

int main() {
    FILE *file;
    char *flag = function2005();
    size_t flag_len = strlen(flag);
    alarm(50);
    for (size_t i = 0; i <= flag_len; i++) {
         
        for (size_t j = 0; j < i; j++) {
            printf("%c", flag[j]);
        }
        printf("\n");
        sleep(5); 
    }

    return 0;
}

