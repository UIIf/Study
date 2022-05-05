#include <iostream>
#include <string>

using namespace std;

typedef struct
{
    unsigned int    bfType;
    unsigned long   bfSize;
    unsigned int    bfReserved1;
    unsigned int    bfReserved2;
    unsigned long   bfOffBits;
} BITMAPFILEHEADER;
 
typedef struct
{
    unsigned int    biSize;
    int             biWidth;
    int             biHeight;
    unsigned short  biPlanes;
    unsigned short  biBitCount;
    unsigned int    biCompression;
    unsigned int    biSizeImage;
    int             biXPelsPerMeter;
    int             biYPelsPerMeter;
    unsigned int    biClrUsed;
    unsigned int    biClrImportant;
} BITMAPINFOHEADER;
 
typedef struct
{
    int   b;
    int   g;
    int   r;
    int   grayScale;
} RGBQUAD;

static unsigned short read_u16(FILE *fp)
{
    unsigned char b0, b1;
 
    b0 = getc(fp);
    b1 = getc(fp);
 
    return ((b1 << 8) | b0);
}

static unsigned int read_u32(FILE *fp)
{
    unsigned char b0, b1, b2, b3;
 
    b0 = getc(fp);
    b1 = getc(fp);
    b2 = getc(fp);
    b3 = getc(fp);
 
    return ((((((b3 << 8) | b2) << 8) | b1) << 8) | b0);
}
 
static int read_s32(FILE *fp)
{
    unsigned char b0, b1, b2, b3;
 
    b0 = getc(fp);
    b1 = getc(fp);
    b2 = getc(fp);
    b3 = getc(fp);
 
    return ((int)(((((b3 << 8) | b2) << 8) | b1) << 8) | b0);
}

static void write_u16(FILE *fp, unsigned short val)
{
    for(int i = 0; i < 2; i++){
        putc(val >> 8*i, fp);
    }
}
 
 
static void write_u32(FILE *fp, unsigned int val)
{
    for(int i = 0; i < 4; i++){
        putc(val >> 8*i, fp);
    }
}
 
 
static void write_s32(FILE *fp, int val)
{
    for(int i = 0; i < 4; i++){
        putc(val >> 8*i, fp);
    }
}

RGBQUAD ** read_bmp(BITMAPFILEHEADER &header, BITMAPINFOHEADER &bmiHeader, string &eOfStr, string &str){
    FILE * pFile = fopen("image.bmp", "rb");
    RGBQUAD **rgb;
    str = "";
    eOfStr = "";

    header.bfType      = read_u16(pFile);
    header.bfSize      = read_u32(pFile);
    header.bfReserved1 = read_u16(pFile);
    header.bfReserved2 = read_u16(pFile);
    header.bfOffBits   = read_u32(pFile);    

    bmiHeader.biSize          = read_u32(pFile);
    bmiHeader.biWidth         = read_s32(pFile);
    bmiHeader.biHeight        = read_s32(pFile);
    bmiHeader.biPlanes        = read_u16(pFile);
    bmiHeader.biBitCount      = read_u16(pFile);
    bmiHeader.biCompression   = read_u32(pFile);
    bmiHeader.biSizeImage     = read_u32(pFile);
    bmiHeader.biXPelsPerMeter = read_s32(pFile);
    bmiHeader.biYPelsPerMeter = read_s32(pFile);
    bmiHeader.biClrUsed       = read_u32(pFile);
    bmiHeader.biClrImportant  = read_u32(pFile);

    cudaMallocManaged(&rgb, bmiHeader.biWidth*sizeof(RGBQUAD*));
    for (int i = 0; i < bmiHeader.biWidth; i++) {

        cudaMallocManaged(&rgb[i], bmiHeader.biHeight*sizeof(RGBQUAD));

        for (int j = 0; j < bmiHeader.biHeight; j++) {
            rgb[i][j].b = getc(pFile);
            rgb[i][j].g = getc(pFile);
            rgb[i][j].r = getc(pFile);
        }

        // if(bmiHeader.biWidth%4 != 0){
        //     for(int j = 0; j < bmiHeader.biWidth%4; j++){
        //         getc(pFile);
        //     }
        // }

    }

    while(!feof(pFile)){
        str += getc(pFile);
    }

    fclose(pFile);
    return rgb;
}

void write_bmp(RGBQUAD **rgb, BITMAPFILEHEADER &header, BITMAPINFOHEADER &bmiHeader, string eOfStr, string str){
    FILE * pFile = fopen("gr_image.bmp", "wb");


    write_u16(pFile, header.bfType);
    write_u32(pFile, header.bfSize);
    write_u16(pFile, header.bfReserved1);
    write_u16(pFile, header.bfReserved2);
    write_u32(pFile, header.bfOffBits);

    write_u32(pFile, bmiHeader.biSize);
    write_s32(pFile, bmiHeader.biWidth);
    write_s32(pFile, bmiHeader.biHeight);
    write_u16(pFile, bmiHeader.biPlanes);
    write_u16(pFile, bmiHeader.biBitCount);
    write_u32(pFile, bmiHeader.biCompression);
    write_u32(pFile, bmiHeader.biSizeImage);
    write_s32(pFile, bmiHeader.biXPelsPerMeter);
    write_s32(pFile, bmiHeader.biYPelsPerMeter);
    write_u32(pFile, bmiHeader.biClrUsed);
    write_u32(pFile, bmiHeader.biClrImportant);

    for (int i = 0; i < bmiHeader.biWidth; i++) {

        for (int j = 0; j < bmiHeader.biHeight; j++) {
            putc(rgb[i][j].grayScale, pFile);
            putc(rgb[i][j].grayScale, pFile);
            putc(rgb[i][j].grayScale, pFile); 
        }

        // if(bmiHeader.biWidth%4 != 0){
        //     for(int j = 0; j < bmiHeader.biWidth % 4; j++){
        //         putc(0, pFile);
        //     }
        // }
        
    }
    for(int i = 0; i < str.length(); i++){
        putc(str[i], pFile);
    }

    fclose(pFile);
}