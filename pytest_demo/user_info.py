def get_user_year():
    year = input("In what year were you born? ")
    star_wars_age = int(year) - 1977
    if star_wars_age > 0:
        return(f"You were born on {star_wars_age} ABY")
    if star_wars_age < 0:
        return(f"You were born on {abs(star_wars_age)} BBY")
    if star_wars_age == 0:
        return(f"You were born on the same year as the Battle of Yavin")

def get_user_info():
    name = input("What is your name? ")
    year = input("In what year were you born? ")
    star_wars_age = int(year) - 1977
    if star_wars_age > 0:
        return(f"{name} was born on {star_wars_age} ABY")
    if star_wars_age < 0:
        return(f"{name} was born on {abs(star_wars_age)} BBY")
    if star_wars_age == 0:
        return(f"{name} was born on the same year as the Battle of Yavin")
    