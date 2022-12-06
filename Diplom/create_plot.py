from random import randrange

f = open("s:\Study\Diplom\graph_0.grph", "r")
lines = f.readlines()
f.close()

lines = [line[:-1].split(" ") for line in lines]
ierarhy = {lines[0][0]: lines[0][0]}
for line in lines:
    # print(line[1], line[0])
    ierarhy[line[1]] = line[0]

# print(ierarhy)

for k in ierarhy.keys():
    ret = ierarhy[k] + "\n"
    for i in range(randrange(20, 40, 2)):
        ret += k + "\n"
    f = open(f"s:\Study\Diplom\plot_{k}.plt", "w")
    f.write(ret[:-1])
    f.close()
