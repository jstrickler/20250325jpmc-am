# import xml.etree.ElementTree as ET
import lxml.etree as ET

movies_doc = ET.parse('movies.xml')  # read and parse the XML file

movies = movies_doc.getroot()  # get the root element (<movies>)

for movie in movies:  # loop through children of root element
    movie_name = movie.get('name'),  # get 'name' attribute of movie element
    movie_director = movie.findtext('director'),  # get 'director' attribute of movie element
    print(f'{movie_name} by {movie_director}')
