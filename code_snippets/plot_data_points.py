import matplotlib.pyplot as plt

x_number_of_users = [1, 2, 20, 30,35]

# Sync points
y1 = [2.8, 4, 22.6, 38 ,41.4]
plt.plot(x_number_of_users,y1, label="Synchronous approach approach")

# Async points
y2 = [3.4, 3.1, 10.1, 21.2, 23.6]
plt.plot(x_number_of_users, y2, label="Asynchronous approach approach")

# naming the x axis
plt.xlabel('x - number of users')
# naming the y axis
plt.ylabel('y - time')
# giving a title to my graph
plt.title('Sync VS Async user registration with caching (no notification)')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()