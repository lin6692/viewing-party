# Testing connection
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title == None or genre == None or rating == None:
        return None

    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title): 
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    rating_lst = []
    for movie in user_data["watched"]:
        rating_lst.append(movie["rating"])
    
    if len(rating_lst) == 0: 
        return 0

    return sum(rating_lst)/len(rating_lst)

def get_most_watched_genre(user_data):
    
    watched_lst = user_data["watched"]
    genre_freq = {}
    most_watched_count = 0
    most_watched_genre = ""

    # Check empty watched list
    if not watched_lst:
        return None
    
    for movie in watched_lst:
        genre = movie["genre"]

        # Count genre frequency
        if genre not in genre_freq.keys():
            genre_freq[genre] = 1
        else:
            genre_freq[genre] += 1
        
        # Update the most_watched_count and most_watched_genre
        if genre_freq[genre] > most_watched_count:
            most_watched_count = genre_freq[genre]
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_watched = user_data["watched"]                                     # A list of movies that user watched                      
    friends_watched = get_friends_watched_movies(user_data)                 # A list of movies that friends watched                  
    user_unique_watched = ele_in_a_not_b(user_watched, friends_watched)     # A list of movies that ONLY user watched

    return user_unique_watched          

def get_friends_unique_watched(user_data):

    user_watched = user_data["watched"]                                     # A list of movies that user watched                      
    friends_watched = get_friends_watched_movies(user_data)                 # A list of movies that friends watched 
    friends_unique_watched = ele_in_a_not_b(friends_watched, user_watched)

    return friends_unique_watched 

#                                               *********** WAVE 3 Helper Functions **********
def ele_in_a_not_b(a_lst, b_lst):
    '''
    Parameters: two lists
    Return: a single list that contains elements in a_list but not in b_list 
            the return list has no duplications
    '''
    output = []
    for ele in a_lst:
        if ele not in b_lst and ele not in output:                          # remove output duplications
            output.append(ele)
    return output

def get_friends_watched_movies(user_data):
    '''
    Parameter: one user_data
    Return: a single list that contains all friends watched movies, allow duplicated values
    '''
    friends_watched = []               

    for friend in user_data["friends"]:                                     # user_data["friends"] is a list of dict,  dict key: "watched" - value: a list of watched movies 
        for movie in friend["watched"]:
                friends_watched.append(movie)

    return friends_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    recs = []
    user_hosts = user_data['subscriptions']
    friend_watched = get_friends_unique_watched(user_data)

    for movie in friend_watched:
        if movie['host'] in user_hosts:
            recs.append(movie)

    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    friend_unique_watched = get_friends_unique_watched(user_data)          # movies that friends watched but user has not                                          
    most_watched_genre = get_most_watched_genre(user_data)
    recs = []

    # build the rec list: movies friends have already watched, and its genre is same as the users most freq genre
    for movie in friend_unique_watched:
        if movie['genre'] == most_watched_genre:
            recs.append(movie)

    return recs

def get_rec_from_favorites(user_data):
    user_fav = user_data["favorites"]

    # use the WAVE_03 help function (get_friends_watched_movies) to get the list of movies that friends have watched
    friend_watched = get_friends_watched_movies(user_data)
    
    # use the WAVE_03 help function (ele_in_a_not_b) to get the list of movies that in user_favorite but friends haven't watched
    recs = ele_in_a_not_b(user_fav, friend_watched)                         

    return recs
