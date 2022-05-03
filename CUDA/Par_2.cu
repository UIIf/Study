#include <iostream>
#include <math.h>
#include <stdio.h>

#include <cuda.h>
#include <curand_kernel.h>

#define CUDA_CALL(x) do { if((x) != cudaSuccess) { \
    printf("Error at %s:%d\n",__FILE__,__LINE__); \
    return EXIT_FAILURE;}} while(0)

// Kernel function to add the elements of two arrays
__global__ 
void setup_kernel(curandState *state, int N)
{
    int id = threadIdx.x + blockIdx.x * blockDim.x;
    /* Each thread gets same seed, a different sequence
       number, no offset */
	if(id < N)
		curand_init(1234, id, 0, &state[id]);
}

__global__ 
void generate_kernel(curandState *state, unsigned int *result, int N)
{
    int id = threadIdx.x + blockIdx.x * blockDim.x;
    float x, y;
	
	if(id < N){
		curandState localState = state[id];
		x = curand_uniform(&localState);
		y = curand_uniform(&localState);
		
		state[id] = localState;
		
		result[id] = x*x + y*y <= 1;
	}
		
}

int main(void)
{	
	int N = 1<<20;
	
	unsigned int threadsPerBlock = 256;
    unsigned int blockCount = N/256 + 1;
		
	curandState *devStates;
	unsigned int *result;
		
	CUDA_CALL(cudaMallocManaged(&result, N*sizeof(unsigned int)));
	CUDA_CALL(cudaMallocManaged(&devStates, N*sizeof(curandState)));

  // Run kernel on 1M elements on the GPU
	setup_kernel<<<blockCount, threadsPerBlock>>>(devStates, N);
	cudaDeviceSynchronize();
	
	generate_kernel<<<blockCount, threadsPerBlock>>>(devStates, result, N);
	cudaDeviceSynchronize();

	float sum = 0;
	for (int i = 0; i < N; i++)
		sum += result[i] * 4;
	
	std::cout << "Sum: " << sum << std::endl;
	std::cout << "N: " << N << std::endl;
	std::cout << "BC: " << blockCount << std::endl;
	std::cout << "Sum/N: " << sum/(float)N << std::endl;

  // Free memory
	cudaFree(devStates);
	cudaFree(result);
  
  return 0;
}