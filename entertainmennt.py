#!/usr/bin/env python
print("Content-type:text/html \n")

import media
import fresh_tomatoes



rouge = media.Movie("rouge","https://i.ytimg.com/vi/RmsVI_kEWO0/maxresdefault.jpg",
                    "https://youtu.be/ii_KxlHcm3A")

tamasha = media.Movie("tamasha","https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Tamasha_%28film_poster%29.jpg/220px-Tamasha_%28film_poster%29.jpg",
                      "https://youtu.be/o-e5eWVCzx8")

arya2 = media.Movie("arya2","https://upload.wikimedia.org/wikipedia/en/b/bc/Arya2_poster2.jpg",
                    "https://youtu.be/vpfXFqlLA3A")

ban = media.Movie("bharath ane nenu","https://i3.behindwoods.com/telugu-movies/bharat-ane-nenu/stills-photos-pictures/thumbnails/bharat-ane-nenu-stills-photos-pictures-33.jpg",
                  "https://youtu.be/KMWS5y2gZ6E")

Rangasthalam = media.Movie("rangasthalam","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2vntwFDoqLy0MRHlMXSgZTmu6iOc2n-3M4W2gosjcix7rFXwG",
                           "https://youtu.be/mhhb6JAJKbE")

# rangastalam.show_trailer()

movies = [rouge,tamasha,arya2,ban,Rangasthalam]
fresh_tomatoes.open_movies_pages(movies)

