#include <alloca.h>
#include <iconv.h>
#include <emmintrin.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <immintrin.h>
#include <xmmintrin.h>

void who(char *buf, unsigned long size) {
    __m128i zero = _mm_setzero_si128();
    char *tmp = alloca(size);
    char *local = alloca(size);
    unsigned toread = size, readin;
    readin = read(0, local, toread);
    for (int i = 0; i < size; i += 16)
        _mm_store_si128((__m128i *)(local + i), zero);
    __m128i mask = _mm_set1_epi8(0x80);
    for (int i = 0; i < size; i += 16) {
        __m128i data = _mm_load_si128((const __m128i *)(local + i));
        __m128i result = _mm_and_si128(mask, data);
        if (_mm_movemask_epi8(result)) {
            goto convert;
        }
    }
testname:
    printf("Do you confirm? [y/n] ");
    char c = getchar();
    getchar(); // discard \n
    if (c == 'n')
        readin = read(0, local, toread & 0xf8);
    else if (c != 'y')
        goto testname;
    // c == 'y'
    memcpy(buf, local, readin);
    return;
convert:
    memcpy(tmp, local, size);
    puts("The input contains non-ascii chars!");
    puts("It is needed to be converted to ISO-2022-CN-EXT.");
    iconv_t cd = iconv_open("ISO-2022-CN-EXT", "UTF-8");
    char *pbuf = local, *ptmp = tmp;
    size_t inval = readin, outval = readin;
    iconv(cd, &ptmp, &inval, &pbuf, &outval);
    iconv_close(cd);
}
