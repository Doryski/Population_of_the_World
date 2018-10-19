"""
Banglash Thana, a disctrict of Dhaka, Bangladesh is one of the most densely populated areas in the world.
In 2001, due to statistics, lived there 178 241 people within the are of 1,2 sq km,
which gives the population density equal to 148 535 people per sq km.
I'll round it up to 200 000 people per sq km and take it as the limit of population density.

World's land area is 148.94 million sq km.
However I docked the area of Antarctida equal to 14 million sq km and
I got the hypothetical land livable area of 135 million sq km.

Then I multiplied max population density (200 000 people per sq km) by 135 million sq km.
and I got the result 27 trillion people which is the number of maximum world's population.

I count 27 trillion as 100%.
Now I'm going to make predictions on world's population and find out how the percentage (x_population / max_population) will change over time.
"""
land_area = 135 * 1000000
print("Hypothetical land livable area equals to " + str(land_area // 1000000) + " million sq km.")
max_density = 200000
print("Today's maximum population density equals to about " + str(max_density) + " people per sq km.")
max_pop = land_area * max_density # 27 * 10^12
trillion = 10 ** 12
max_pop_short = str(max_pop // trillion) + " trillion people"
print("Maximum World's reachable population equals to " + str(max_pop_short) + ".")
