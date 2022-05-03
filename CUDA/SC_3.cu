#include <chrono>
#include <iostream>
#include <cstring>
#include <string>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <vector_types.h>

#include "openMP.hpp"
#include "CUDA_wrappers.hpp"
#include "common/image_helpers.hpp"

template <class T1, class T2>
void prepareImagePointers(	const char * const inputImageFileName,
							cv::Mat& inputImage, 
							T1** inputImageArray, 
							cv::Mat& outputImage,
							T2** outputImageArray, 
							const int outputImageType)
{
	using namespace std;
	using namespace cv;

	inputImage = imread(inputImageFileName, IMREAD_COLOR);

	if (inputImage.empty()) 
	{
		cerr << "Couldn't open input file." << endl;
		exit(1);
	}

	//allocate memory for the output
	outputImage.create(inputImage.rows, inputImage.cols, outputImageType);

	cvtColor(inputImage, inputImage, cv::COLOR_BGR2BGRA);

	*inputImageArray = (T1*)inputImage.ptr<char>(0);
	*outputImageArray  = (T2*)outputImage.ptr<char>(0); 
}




using namespace cv;
using namespace std;

int main( int argc, char** argv )
{
  using namespace std::chrono;

  if( argc != 2)
  {
    cout <<" Usage: convert_to_grayscale imagefile" << endl;
    return -1;
  }

  Mat image, imageGray;
  uchar4 *imageArray;
  unsigned char *imageGrayArray;

  prepareImagePointers(argv[1], image, &imageArray, imageGray, &imageGrayArray, CV_8UC1);

  int numRows = image.rows, numCols = image.cols;

  auto start = system_clock::now();
  RGBtoGrayscaleOpenMP(imageArray, imageGrayArray, numRows, numCols);
  auto duration = duration_cast<milliseconds>(system_clock::now() - start);
  cout<<"OpenMP time (ms):" << duration.count() << endl;

  memset(imageGrayArray, 0, sizeof(unsigned char)*numRows*numCols);  

  RGBtoGrayscaleCUDA(imageArray, imageGrayArray, numRows, numCols);

  return 0;
}