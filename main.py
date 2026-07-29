from typing import Any

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name
print(get_full_name("verla", "berinyuy"))

def some_function(data: Any):
    print(data)

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
