#include <iostream>
#include <math.h>
#include <stdio.h>
#include <cuda.h>
#include <thrust/device_vector.h>
#include <thrust/host_vector.h>
#include <thrust/functional.h>
#include <thrust/random.h>
#include <thrust/transform_reduce.h>

struct inside_circle {
	__device__ unsigned int operator()(float2 p) const {
		return (((p.x-0.5)*(p.x-0.5)+(p.y-0.5)*(p.y-0.5))<0.25) ? 1 : 0;
	}
};

struct randomPoint {
	__device__ float2 operator() (const unsigned int n) {
		thrust::default_random_engine rnd;
		rnd.discard(2*n);
		return make_float2 (
			(float)rnd()/thrust::default_random_engine::max,
			(float)rnd()/thrust::default_random_engine::max);
	}
};

int main()
{	
	int N = 1<<20;
	thrust::device_vector<float2> d_random(N);
	thrust::counting_iterator<unsigned int> d_indexSequence(N);
	thrust::transform(d_indexSequence, d_indexSequence + N, d_random.begin(), randomPoint());
	
	
	int sum = thrust::transform_reduce(d_random.begin(), d_random.end(), inside_circle(), 0, thrust::plus<int>());

	
	/*for(int i = 0; i < N; i++)
		std::cout << d_inside[i] << " " << std::endl;*/
	
	std::cout << 4 * (float)sum/N << std::endl;
	
	
	
	/*cudaEvent_t start, stop;
	cudaEventCreate(&start);
	cudaEventCreate(&stop);
	
	int N = 1<<10;
	
	thrust::device_vector <int> calc(N*N);
	
	thrust::device_vector <float> x(N);
	thrust::device_vector <float> y(N);
	
	thrust::sequence (x.begin, x.end, 0, (float)1/N)
	thrust::sequence (y.begin, y.end, 0, (float)1/N)
	
	
	
	cudaEventRecord(start);

	
	cudaEventRecord(stop);
	cudaEventSynchronize(stop);
	float milliseconds = 0;
	cudaEventElapsedTime(&milliseconds, start, stop);
	
	std::cout << "Result: " << result[0] << std::endl;
	std::cout << "Count: " << count[0] << std::endl;
	std::cout << "Pi: " << (float)result[0]/count[0]*4 << std::endl;
	std::cout << "Time: " << milliseconds << std::endl;*/
	
  
	return 0;
}