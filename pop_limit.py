land_area = 135 * 1000000
print("Hypothetical land livable area equals to " + str(land_area // 1000000) + " million sq km.")
max_density = 200000
print("Today's maximum population density equals to about " + str(max_density) + " people per sq km.")
max_pop = land_area * max_density # 27 * 10^12
trillion = 10 ** 12
max_pop_short = str(max_pop // trillion) + " trillion people"
print("Maximum World's reachable population equals to " + str(max_pop_short) + ".")
