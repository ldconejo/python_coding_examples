def times_two(x):
    return x * 2

#print(times_two(4))

#print(list(map(times_two, range(10))))

#def times_three(x):
#    return x * 3

#times_three = lambda x:x * 3

#print(list(map(times_three, range(10))))

#sum_a_b = lambda x,y:x + y
#print(sum_a_b(2,5))

#def weather_today(day, weather, temperature):
#    return f"On {day}, the weather will be {weather} with an average temperature of {temperature}F"

#weather_today = lambda day, weather, temperature: f"On {day}, the weather will be {weather} with an average temperature of {temperature}F"

#print(weather_today("Tuesday", "cloudy", "56"))

print((lambda day, weather, temperature: f"On {day}, the weather will be {weather} with an average temperature of {temperature}F")("Sunday", "cloudy", "56"))