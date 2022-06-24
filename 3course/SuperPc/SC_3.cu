#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string>

#include <cuda.h>
#include "SC_3.h"

using namespace std;


 
 
static unsigned short read_u16(FILE *fp);
static unsigned int   read_u32(FILE *fp);
static int            read_s32(FILE *fp);

static void write_u16(FILE *fp, unsigned short val);
static void write_u32(FILE *fp, unsigned int val);
static void write_s32(FILE *fp, int val);



__global__ 
void make_gray_scale(RGBQUAD **rgb,int height, int N)
{
    int id = threadIdx.x + blockIdx.x * blockDim.x;
	
    int x = id/height;
    int y = id%height;

	if(id < N){
        rgb[x][y].grayScale = char(0.299*rgb[x][y].r + 0.587*rgb[x][y].g + 0.114*rgb[x][y].b);
	}
		
}

int main()
{
    BITMAPFILEHEADER header __attribute__((unused));
    BITMAPINFOHEADER bmiHeader;

    string eOfStr;
    string ending;

    RGBQUAD **rgb = read_bmp(header, bmiHeader, eOfStr,ending);

    cout<<"Read"<<endl;

    int N = bmiHeader.biHeight * bmiHeader.biWidth;

    int threadsCount = 512;
    int blockCount = N/threadsCount + 1;

    cout<<rgb[0][0].r<<' '<<rgb[0][0].g<<' '<<rgb[0][0].b<<endl;
    make_gray_scale<<<blockCount, threadsCount>>>(rgb, bmiHeader.biHeight, N);
    cudaDeviceSynchronize();
    cout<<rgb[0][0].grayScale<<endl;
    cout<<"Gray"<<endl;

    write_bmp(rgb, header, bmiHeader, eOfStr,ending);

    cout<<"Write"<<endl;

    for(int i = 0; i < bmiHeader.biWidth; i++){
        cudaFree(rgb[i]);
    }
    cudaFree(rgb);

    return 0;
}
 
 

 
 