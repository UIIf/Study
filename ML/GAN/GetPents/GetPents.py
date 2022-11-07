import requests
import numpy as np
import datetime

route = 'http://ciaccodavi.de/qbdp/acg/alchemymod.php?id=' #1461564041

folder_name = '/home/uiif/GitRepos/Study/ML/GAN/GetPents/Pics'
# print(requests.get(route + '1461564041').content)

count = int(3500*0.75)


numbers = [str(i) for i in range(10)]

ids = list(set(["".join(np.random.choice(numbers, 10)) for i in range(count)]))

count = float(len(ids))

step = 0.01
prev = 0

start_time = datetime.datetime.now()

for i in range(len(ids)):
	if(i/count >= step + prev):
		print(f"Current: {round(i/count,2)}, Remainning time - {(datetime.datetime.now() - start_time)*(count - i)/i}")
		prev += step
	with open(f"{folder_name}/images{ids[i]}.jpg", "wb+") as f:
		f.write(requests.get(route + str(ids[i])).content)
