"""
https://osf.io/upav8/
https://www.youtube.com/watch?v=8qEnExGLZfY

Think when you need an optimization

When you need optimization - you need to profile your code
- use a profiler such as cProfile
- usually almost all execution ime occurs within a small part of your code
- optimize the code and leave rest alone

If you need even better performance:
- redesign the code completely
- but it takes effort and time

Example: Find duplicate movie titles
Read 5000 movie titles
Return a list of movie titles that occur twice
Search is case insensitive
"""
import cProfile, pstats, io


def profile(fnc):
    """A decorator that uses cProfile to profile a function

    Adapted from the Python 3.6 docs:
    https://docs.python.org/3/library/profile.html#profile.Profile
    """

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()


def is_duplicate(needle, haystack):
    for movie in haystack:
        # if needle.lower() == movie.lower():
        if needle == movie:
            return True
    return False


@profile
def find_duplicate_movies(src='movies.txt'):
    # the original function took 1.526 s for 5200 strings
    # we see the problem in is_duplicate it takes 1.507 ms Almost all of execution time is spent there
    # we call 8 037 872 times lower function
    # converting to lower case costs us 0.291 s in total
    # lets optimise
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]  # we call lower only 5200 time rather than 8 037 872 times
    # so it should lead to massive improvement
    # so in result we get 0.101 s for find_duplicate_movies and  is_duplicate still takes 0.095 s
    # BUT THAT'S ALREADY 15x times improvement
    # lets optimize is_duplicate once more time
    # calling is_duplicate is time consuming. We dont need it anymore cause its so simple
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)

    # After removing is_duplicate we go down to as many as 0.033 s for find_duplicate_movies
    # so its 3x times improvement
    # After this step. Seems like its maximum that we can squeeze from this profiling and optimization
    # technic
    # The only thing left is we still want to improve performance is to rethink the approach
    return duplicates


# %time find_duplicate_movies() #  is a magic command. It's a part of IPython.
print(len(find_duplicate_movies()))  # output is 4872


@profile
def find_duplicate_movies_next_gen(src='movies.txt'):
    """New approach for find_duplicate_movies function
    As low as 0.004 s for find_duplicate_movies_next_gen function execution
    SO ITS 10x times faster than lowest values from original find_duplicate_movies
    and in 350x times faster than initial approach"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]  # lowercase everything
    movies.sort()  # sort for easier searching
    # then we slice the arrays
    # and try to find duplicates in sorted arrays. If next element is same as current. It's duplicate
    duplicates = [movie1 for movie1, movie2 in zip(movies[:-1], movies[1:]) if movie1 == movie2]
    return duplicates


print(len(find_duplicate_movies_next_gen()))  # # output is 4872
