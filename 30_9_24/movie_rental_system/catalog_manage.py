movies_available=[]

def add_movie(title,genre,price,quantity):
    movies_available.append((title,genre,price,quantity))
    print(f"{title} successfully added!")
    
def display_available_movies():
    if movies_available:
        print("Available Movies: ")
        for a in movies_available:
            print(f"Title: {a[0]}, Genre: {a[1]}, Price: {a[2]}, Quantity: {a[3]}")
    else:
        print("Currently no movies available.")