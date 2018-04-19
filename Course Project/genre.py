
import json

def parse():
        movie=(raw_input("Movie name: "))

        aword=[]
        aline=open('movies.dat.txt', 'r').readlines()
        result=[]
        for x in aline:
                movie_dat=x.split('::')[1]
                s_movie=movie_dat[:-7]
                if s_movie.lower() == movie.lower():
                    genre = x.split('::')[2]
                    print "Genre:"
                    print genre


parse()
