import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def calculate_probabilities():
    # Define the desired probability and find the corresponding mu_1 and sigma_1
    mu_1, sigma_1 = 0, 1

    # Define the parameters for the second normal distribution
    mu_2, sigma_2 = 175, 3

    # Define the range for x values
    x1 = np.linspace(mu_1 - 4 * sigma_1, mu_1 + 4 * sigma_1, 1000)
    x2 = np.linspace(mu_2 - 4 * sigma_2, mu_2 + 4 * sigma_2, 1000)

    # Calculate the probabilities
    pdf1 = norm.pdf(x1, mu_1, sigma_1)
    pdf2 = norm.pdf(x2, mu_2, sigma_2)
    #finds the CDF, the other graphs shown in the assigment.
    cdf1 = norm.cdf(x1, mu_1, sigma_1)
    cdf2 = norm.cdf(x2, mu_2, sigma_2)

    return (x1, pdf1, cdf1), (x2, pdf2, cdf2), mu_1, sigma_1, mu_2, sigma_2

#does the math to plot everything
def plot(stats1, stats2, mu_1, sigma_1, mu_2, sigma_2):
    (x1, pdf1, cdf1), (x2, pdf2, cdf2) = stats1, stats2

    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot for P(x<1|N(0,1)) this is right with the online thing i found
    axes[0, 0].plot(x1, pdf1, 'k')
    axes[0, 0].fill_between(x1, pdf1, where=(x1 < 1), color="skyblue", alpha=0.5)
    axes[0, 0].set_title('P(x<1|N(0,1))')
    axes[0, 0].text(-3, 0.2, f"P(x<1|N(0,1)) ≈ {norm.cdf(1, mu_1, sigma_1):.4f}", fontsize=12)

    # Plot for P(x>μ+2σ|N(175, 3)). this is right with the online thing i found
    axes[0, 1].plot(x2, pdf2, 'k')
    axes[0, 1].fill_between(x2, pdf2, where=(x2 > mu_2 + 2 * sigma_2), color="skyblue", alpha=0.5)
    axes[0, 1].set_title('P(x>μ+2σ|N(175, 3))')
    axes[0, 1].text(180, 0.05,f"P(x>{mu_2}+2*{sigma_2}|N({mu_2},{sigma_2})) ≈ {1 - norm.cdf(mu_2 + 2 * sigma_2, mu_2, sigma_2):.4f}", fontsize=12)

    # Plot CDF for N(0,1). the scatter funtion does the actual cdf stuff.
    axes[1, 0].plot(x1, cdf1, 'k')
    axes[1, 0].scatter([1], [norm.cdf(1, mu_1, sigma_1)], marker='H')
    axes[1, 0].text(1, norm.cdf(1, mu_1, sigma_1), f"{norm.cdf(1, mu_1, sigma_1):.4f}", fontsize=12)
    axes[1, 0].set_title('CDF for N(0,1)')

    # Plot CDF for N(175, 3) the scatter funtion does the actual cdf stuff.
    axes[1, 1].plot(x2, cdf2, 'k')
    axes[1, 1].scatter([mu_2 + 2 * sigma_2], [norm.cdf(mu_2 + 2 * sigma_2, mu_2, sigma_2)], marker='H')
    axes[1, 1].text(mu_2 + 2 * sigma_2, norm.cdf(mu_2 + 2 * sigma_2, mu_2, sigma_2),f"{norm.cdf(mu_2 + 2 * sigma_2, mu_2, sigma_2):.4f}", fontsize=12)
    axes[1, 1].set_title('CDF for N(175, 3)')
    #cdf was found using chatgpt.
    plt.tight_layout()
    plt.show()


# Main function
if __name__ == "__main__":
    stats1, stats2, mu_1, sigma_1, mu_2, sigma_2 = calculate_probabilities()
    plot(stats1, stats2, mu_1, sigma_1, mu_2, sigma_2)
