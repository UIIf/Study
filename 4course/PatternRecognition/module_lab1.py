# %% [markdown]
# # Петров Сергей Дмитриевич, Вариант 5

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## Начальные условия и прочее

# %%
# N = 200
# dims = 2

# Вектора математических ожиданий
M1 = np.array([0, 0])
M2 = np.array([1, 1])
M3 = np.array([-1, 1])

# Матрицы корреляции
B_diag_symm = np.array([[0.1, 0], [0, 0.1]])

B_diag_asymm = np.array([[0.01, 0], [0, 0.06]])

# Случайные вектора из нормального распределения
# var_xi = np.random.randn(N, dims)
def create_xi(N):
    return np.random.randn(N, 2)


# %% [markdown]
# ## Функции для получения векторов имеющих нормальное распределение

# %%
def create_a(B):

    # Частный случай для двумерных векторов
    a = np.array(
        [
            [np.sqrt(B[0][0]), 0],
            [B[0][1] / np.sqrt(B[0][0]), np.sqrt(B[1][1] - B[0][1] ** 2 / B[0][0])],
        ]
    )

    return a


def calc_x(var_xi, M, B):
    a = create_a(B)
    return np.dot(var_xi, a) + M


# %% [markdown]
# ## Метрики

# %%
def calc_p_b(M1, M2, B1, B2):
    b_sum = (B2 + B1) / 2
    inv_b_sum = np.linalg.inv(b_sum)
    m_diff = M2 - M1
    return (
        np.dot(np.dot(m_diff.T, inv_b_sum), m_diff) / 4
        + np.log(np.linalg.det(b_sum) / np.sqrt(np.linalg.det(B1) * np.linalg.det(B2)))
        / 2
    )


# %% [markdown]
# ## Вспомогательные функции

# %%
def show_pair_of_vectors(var_xi, M1, M2, B1, B2):
    x1 = calc_x(var_xi, M1, B1)
    x2 = calc_x(var_xi, M2, B2)

    add_x_on_plot(x1)
    add_x_on_plot(x2)

    pb = calc_p_b(M1, M2, B1, B2)

    print(f"Pb = {pb}")

    plt.show()


def diag_flip(matrix):
    m = matrix.copy()
    m[0][0], m[1][1] = m[1][1], m[0][0]
    return m


def add_x_on_plot(x, ax=plt):
    ax.scatter(x[:, 0], x[:, 1])


def calc_M_hat(x):
    return x.sum(axis=0) / x.shape[0]


def calc_B_hat(x, M=1.0):
    if type(M) is float:
        M = calc_M_hat(x)
    M_hat = M
    first = x - M_hat
    return np.dot(first.T, first) / x.shape[0]


def create_bin_vec(N, p, dims=10):
    return (np.random.random([N, dims]) < p).astype(int)


def accuracy(y_target, y_pred):
    return (y_target == y_pred).sum() / y_target.shape[0]


def plot_dots(vectors, borders, steps=None):

    if steps == None:
        plt.xlim(borders[0])
        plt.ylim(borders[1])
        for target, vec in enumerate(vectors):
            vec = np.array(vec)
            plt.scatter(vec[:, 0], vec[:, 1], label=target)
    else:
        plt.xlim(0, steps[0])
        plt.ylim(0, steps[1])
        ...

        for target, vec in enumerate(vectors):
            vec = np.array(vec)

            vec[:, 0] = (
                (vec[:, 0] - borders[0][0]) / (borders[0][1] - borders[0][0]) * steps[0]
            )
            vec[:, 1] = (
                (vec[:, 1] - borders[1][0]) / (borders[1][1] - borders[1][0]) * steps[1]
            )
            plt.scatter(vec[:, 0], vec[:, 1], label=target)


def create_pred_img(pred_func, borders, steps=[16, 10], cmap="viridis"):

    x_linspace = np.linspace(borders[0][0], borders[0][1], steps[0])
    y_linspace = np.linspace(borders[1][0], borders[1][1], steps[1])

    lam = lambda x, y: pred_func(np.array([x, y]))

    matrix = np.array([[lam(x, y) for x in x_linspace] for y in y_linspace])

    plt.figure(figsize=(16, 9))
    plt.imshow(matrix, cmap=cmap, origin="lower")


def find_borders(vectors):
    x_min = min([min(vec[:, 0]) for vec in vectors])
    x_max = max([max(vec[:, 0]) for vec in vectors])

    y_min = min([min(vec[:, 1]) for vec in vectors])
    y_max = max([max(vec[:, 1]) for vec in vectors])

    return ([x_min, x_max], [y_min, y_max])


def plot_classifier_field(vectors, pred_func, steps=[100, 100], cmap="viridis"):
    borders = find_borders(vectors)
    create_pred_img(pred_func, borders, steps, cmap=cmap)
    plot_dots(vectors, borders, steps=steps)
