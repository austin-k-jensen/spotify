from random import randint
import numpy as np
import matplotlib.pyplot as plt


def draw_pills(start_num: int = 30, results: np.array = None):
    whole = start_num
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


def pill_prob(runs: int = 10000, start_num: int = 100):

    results = np.zeros((runs, start_num * 2))
    run = 0

    while run < runs:
        draw_pills(start_num=start_num, results=results[run])
        run += 1

    output = np.mean(results, axis=0)
    plt.plot(output)
    plt.show()
    # print(output)
    #


pill_prob()
