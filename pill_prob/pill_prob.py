from random import randint
import numpy as np
import matplotlib.pyplot as plt


def draw_pills(
    pills: int = 30,
    results: np.array = None,
):
    whole = pills
    cut = 0
    total = whole + cut
    draw_num = 0

    while total > 0:
        draw = randint(1, total)
        cut_prob = cut / total
        results[draw_num] = cut_prob

        if draw <= whole:
            whole += -1
            cut += 1
        else:
            cut += -1

        total = whole + cut
        draw_num += 1
        # print(draw_num, total, whole, cut, cut_prob)


def pill_prob(
    runs: int = 1000,
    pills: int = 30,
):

    results = np.zeros((runs, pills * 2))
    run = 0

    while run < runs:
        draw_pills(pills=pills, results=results[run])
        run += 1

    output = np.mean(results, axis=0)
    plt.plot(output)
    plt.show()
    # print(output)
    #


pill_prob(
    runs=10000,
    pills=50,
)
