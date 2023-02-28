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


def calc_B_hat(x):
    M_hat = calc_M_hat(x)

    first = x - M_hat
    return np.dot(first.T, first) / x.shape[0]


def create_bin_vec(N, p, dims=10):
    return (np.random.random([N, dims]) < p).astype(int)
