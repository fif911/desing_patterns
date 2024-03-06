def get_outliers(data):
    window_size = 10

    outliers = []
    for i in range(window_size, len(data)):
        window = data[i - window_size:i]
        mean = sum(window) / window_size
        std_dev = (sum([(x - mean) ** 2 for x in window]) / (window_size - 1)) ** 0.5
        if abs(data[i] - mean) > 3 * std_dev:
            outliers.append(i)

    return outliers


if __name__ == '__main__':
    # generate some sinusoidal data with noise
    import numpy as np
    import matplotlib.pyplot as plt
    np.random.seed(42)  # Seed for reproducibility

    # Generating x values
    x = np.linspace(0, 100, 300)

    # Adding random noise with mean 0 and standard deviation 0.2
    y = np.sin(x / 10) + np.random.normal(0, 0.15, 300)  # Multiply x by a factor to reduce the period

    # Introducing rare outliers
    num_outliers = 8
    outlier_indices = np.random.choice(np.arange(300), size=num_outliers,
                                       replace=False)  # Selecting 5 indices for outliers
    y[outlier_indices] += np.random.normal(0, 2, size=num_outliers)  # Adding significant offset to the selected points

    outliers = get_outliers(y)
    print(outliers)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    # plot the outliers
    plt.scatter(x[outliers], y[outliers], c='r', label='outliers')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
