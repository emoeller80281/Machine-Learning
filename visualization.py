import matplotlib.pyplot as plt

def show_heatmaps(matrices, xlabel, ylabel, titles=None, figsize=(2.5, 2.5),
                  cmap='Reds'):
    """Show heatmaps of matrices."""
    num_rows, num_cols, _, _ = matrices.shape
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize,
                                 sharex=True, sharey=True, squeeze=False)
    for i, (row_axes, row_matrices) in enumerate(zip(axes, matrices)):
        for j, (ax, matrix) in enumerate(zip(row_axes, row_matrices)):
            pcm = ax.imshow(matrix, cmap=cmap)
            if i == num_rows - 1:
                ax.set_xlabel(xlabel)
                ax.tick_params(axis='x', labelbottom=False, labeltop=False, bottom=False, top=False)
                ax.xaxis.set_label_position('top')
            if j == 0:
                ax.set_ylabel(ylabel)
                ax.tick_params(axis='y', labelleft=False, labelright=False, left=False, right=False)
            if titles:
                ax.set_title(titles[j])
