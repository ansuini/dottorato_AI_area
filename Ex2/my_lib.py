# basic tools for excercise 2
def test_funcion(features:list, data, title):
    import matplotlib.pyplot as plt
    fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=False)
    ax0.plot(data,linewidth=.2)
    ax0.set_title("title")
    ax1.errorbar(features, mm, sd, linestyle='None', marker='^')
    ax1.set_title('mean and standard deviation')
    fig.suptitle("X", fontweight ="bold")


