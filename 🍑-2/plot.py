import numpy.random as npr
import matplotlib.pyplot as plot
mu, sigma = 0, 5
s = npr.normal(mu, sigma, 1000)
plot.hist(s , bins = 100 , color = "blueviolet" , edgecolor = "green")
plot.xlabel("X")
plot.ylabel("Y")
plot.title("Hist")
plot.show()
