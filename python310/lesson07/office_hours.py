text = 'Hello'
spaces = 6
target_string = f"{text:<{spaces}} John"
#print(target_string)

target_string = f"{'John,':<{spaces}}{text}"
print(target_string)
