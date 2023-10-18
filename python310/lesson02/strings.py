this_is_a_string = "My name is Luis"

# This is also valid code
"My name is Luis"

'My name is Luis'

"""
This is a multi-line string,
in which you can write as much 
as you want without needing to do anything special.
"""

intro_string = """ No problem.
This is a multi-line string,
in which you can write as much 
as you want without needing to do anything special.
"""

'''
This is also a valid
multi-line string
'''
print(intro_string)

# "Conejo" means "Rabbit" in Spanish
print('"Conejo" means "Rabbit" in Spanish')
print("'Conejo' means 'Rabbit' in Spanish")

sample_names = "Miguel, Chris, Paul, Ayda, Luis"
print(sample_names)
list_of_names = sample_names.split(", ")
print(list_of_names)
new_list_of_names = "Miguel, Chris, Paul, Ayda, Luis".split(", ")
print(new_list_of_names)
print("Miguel, Chris, Paul, Ayda, Luis".split(", "))

weather_example = "It was a beautiful, yet chilly day in Oregon"
print(weather_example.lower())
print(weather_example.upper())

all_uppercase = weather_example.upper()
print(all_uppercase.swapcase())
print(weather_example.swapcase())

employee_id = "123a3567"
print(employee_id.isnumeric())

# The $ makes the string non-alfanumeric
drivers_license = "A23C4$23"
print(drivers_license.isalnum())

favorite_song = "My heart will go on"
print(favorite_song.title())

sample_list = "find your light".split(" ")
print(sample_list)

# Removing the space in the split() method
#sample_list = "find your light".split("")
#print(sample_list)

sample_list = ["This", "is", "a", "list", "of", "strings"]
new_string = "-space-".join(sample_list)
print(new_string)

new_string = weather_example.join(sample_list)
#print(new_string)

# We need to get the words on this sentence a list, removing spaces, dashes and commas
complex_string = "This is a so-called complex string, in which non-clear divisions between words are present"
word_list = complex_string.replace(",", "").replace(" ", "-").split("-")
print(word_list)

tabbed_string = "This\tstring\tis\tseparated\tby\ttabs"
print(tabbed_string)
weekend_weather = "Friday\t\tSaturday\tSunday"
weather_values = "Rainy\t\tSunny\t\tCloudy"
print(weekend_weather)
print(weather_values)

# \n means new line
greeting = "Hello\nHow are you?"
print(greeting)

# \r means carriage return, write "on top" of the previous text
greeting = "Hello\rHow are you?"
print(greeting)

# The following two lines will be printed with an empty line.
# aftewards. This is because print() adds a carriage return
print("This is\n")
print("another greeting")

# The new line character is counted as a single character
string_length = len("hello\n")
print(string_length)

weather_report = "Current temperature is %iF and %s" % (62, "cloudy")
print(weather_report)

weather_report = "Current temperature is {:d}F and {:s}".format(62, "cloudy")
print(weather_report)

current_temperature = 62
cloud_coverage = "cloudy"
# You can only use F-string with Python 3.10 or higher
weather_report = f"Current temperature is {current_temperature}F and {cloud_coverage}"
print(weather_report)