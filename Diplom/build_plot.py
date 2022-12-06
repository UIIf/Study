import matplotlib.pyplot as plt

f = open("s:\Study\Diplom\graph_0.grph", "r")
lines = f.readlines()
f.close()

lines = [line[:-1].split(" ") for line in lines]


def add_to_plot(lines, index=0, offset=0):

    print(index)
    if index >= len(lines):
        return index
    f = open(f"s:\Study\Diplom\plot_{lines[index][0]}.plt", "r")
    readed = f.readlines()[:-1]
    readed = [read[:-1] for read in readed]
    f.close()
    print(readed)
    x = [i + offset for i in range(len(readed))]
    y = [int(i) for i in readed]
    plt.plot(x, y)
    ti = index
    print(len(lines))
    while ti < len(lines) and lines[ti][0] == lines[index][0]:
        ti += 1
    print(ti)
    delta = ti - index
    index = ti

    for i in range(delta):
        ti = add_to_plot(lines, ti, len(x) - 1)

    return index


add_to_plot(lines)
print(lines)
plt.show()
