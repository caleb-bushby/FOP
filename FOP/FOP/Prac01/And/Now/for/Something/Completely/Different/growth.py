#
# growth.py - simulation of an unconstrained growth model
#
print("\nSIMULATION - Unconstrained Growth\n")
length = 10
pop = 100
g_rate = 0.1
t_step = 0.5
num_iter = length / t_step
g_step = g_rate * t_step
print("INITIAL VALUES: \n")
print("Simulation Length: ", length)
print("Initial Population:", pop)
print("Growth Rate (per hour):", g_rate)
print("Time Step (part hour per step):", t_step)
print("Num iterations (sim length * time step per hour):", num_iter)
print("Growth step (growth rate per time step):", g_step)
print("\nRESULTS:\n")
print("Time: ", 0 , " \tGrowth: ", 0 , " \tPopulation: ", 100)
for i in range(1, int(num_iter) + 1):
    growth = g_step * pop
    pop = pop + growth
    time = i * t_step
    print("Time: ", time, " \tGrowth: ", growth, "\tPopulation", pop)
print("\nPROCESSING COMPLETE.\n")
