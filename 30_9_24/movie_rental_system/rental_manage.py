from catalog_manage import movies_available
from earning import add_earnings

movies_rented={}

def rent_movie(customer, title):
    for i,movie in enumerate(movies_available):
        if movie[0] == title:
            if movie[3]>0:
                movies_available[i]=(movie[0],movie[1],movie[2],movie[3]-1)
                if customer in movies_rented:
                    movies_rented[customer].append(movie)
                else:
                    movies_rented[customer] = [movie]
                add_earnings(movie[2])
                print(f"'{title}' rented to {customer}.")
            else:
                print(f"Movie '{title}' is out of stock.")
            return
    print(f"Movie '{title}' is not available.")
    
    
    
def return_movie(customer,title):
    if customer in movies_rented:
        for movie in movies_rented[customer]:
            if movie[0]==title:
                movies_rented[customer].remove(movie)
                for i, movie in enumerate(movies_available):
                    if movie[0]==title:
                        movies_available[i]=(movie[0], movie[1],movie[2],movie[3]+1)
            
                print(f"'{title}' returned by {customer}")
                if not movies_rented[customer]:
                    del movies_rented[customer]
                return
    print(f"{title} cannot return as it is not rented by {customer}")
    
def display_rented_movies():
    if movies_rented:
        print("List of Rented Movies:")
        for customer,movies in movies_rented.items():
            print(f"{customer} has rented: ")
            for movie in movies:
                print(f" Title:{movie[0]}, Genre: {movie[1]}, Price: ${movie[2]}")
    else:
        print("No rented movies available!")