def times_two(x):
    return x * 2

list(map(times_two, range(10)))

times_three = lambda x:x * 3

list(map(times_three, range(10)))

list(map(lambda x:x * 4, range(10)))

sum_a_b = lambda x,y:x + y

weather_today = lambda day, weather, temperature: f"On {day} the weather will be {weather} with an average temperature of {temperature}"

say_hello = lambda :"How are you? "

'''
This course is a little bit like taking you to a Python store. 
You will see many different tools in the store, some you will use right away, some less often. 
Regardless of that, you should know that those tools are available, how to use them
and how to recognize them when you see them in someone else's code.

Lambda allows you to declare anonymous functions. For those of you who have worked with
Lisp, another programming language, the concept is similar. As you will see in the following
examples, using Lambda will allow you to create functions in a different way, sometimes with
less lines of code. Let's get started
'''
