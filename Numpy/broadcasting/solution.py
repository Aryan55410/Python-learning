import numpy as np

prices = np.array([100, 200, 300])
discounts = 10
final_prices = prices - (prices * discounts / 100)
print(final_prices) 