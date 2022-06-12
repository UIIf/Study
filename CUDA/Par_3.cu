#include <iostream>
#include <math.h>
#include <stdio.h>
#include <cuda.h>

__global__ 
void calculate(int *result, int *count, int N)
{
	int idx = threadIdx.x;
	int idy = blockIdx.x;
	
	if(idx < N && idy < N){
	
		if(idx*idx + idy*idy > N*N){
			atomicAdd(result, 1);
		}
		
		atomicAdd(count, 1);
	}
}

int main(void)
{
	cudaEvent_t start, stop;
	cudaEventCreate(&start);
	cudaEventCreate(&stop);
	
	int N = 1<<10;
	
	unsigned int threadsPerBlock  = N;
    unsigned int blockCount = N;
		
	int *result = 0;
	int count = N*N;
	
	cudaEventRecord(start);
		
	cudaMallocManaged(&result, sizeof(int));
	cudaMallocManaged(&count, sizeof(int));
	
	calculate<<<blockCount, threadsPerBlock>>>(result, count, N);
	cudaDeviceSynchronize();
	
	cudaEventRecord(stop);
	cudaEventSynchronize(stop);
	float milliseconds = 0;
	cudaEventElapsedTime(&milliseconds, start, stop);
	
	result[0] = count - result[0];

	std::cout << "Result: " << result[0] << std::endl;
	std::cout << "Count: " << count << std::endl;
	std::cout << "Pi: " << (float)result[0]/count*4 << std::endl;
	std::cout << "Time: " << milliseconds << std::endl;
	

	cudaFree(result);
  
	return 0;
}