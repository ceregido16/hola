def announcement(f):
    def wrapper():
        print("Initialazing the function...")
        f()
        print("Function finishing...")
    return wrapper

@announcement
def greet():
    print("Hello, my nigga!")


greet()