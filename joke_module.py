from joke.jokes import *
from random import choice

def tell_joke():
    joke = choice([geek, icanhazdad, chucknorris, icndb])()
    return joke
