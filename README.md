# Movie Trailer Website
This program creates a website that displays the set of movies and there trailers. The list of movies are shown as posters and when clicked, the movie plays the movie trailer.

##### Here we use 3 files:
1. entertainment_center.py
2. fresh_tomatoes.py
3. media.py

### Code Details:
[media.py](https://github.com/SKowshik4614/ud036_StarterCode_santosh/blob/master/media.py) is the python module that contains the code to _movie_ class, which stores movie title, storyline, ports and trailer url. Also this module plays the movie trailer in web browser.
[entertainment_center.py](https://github.com/SKowshik4614/ud036_StarterCode_santosh/blob/master/entertainment_center.py) is the python file that contains code to input the move details and creates a **list** os movies and passes this list as parameter to `open_movies_page` function in _fresh_tomatoes_ module.
[fresh_tomatoes.py](https://github.com/SKowshik4614/ud036_StarterCode_santosh/blob/master/fresh_tomatoes.py) is the python module that has code that takes list of movie details as input and displays the movie details and trailer on the browser.

### Execution of the code:
* Download all the files to your local computer.
* Make necessary changes to the code (if required, such as _path, movie details, poster, etc._)
* run `entertainment_center.py`
* If run without errors this will open the browser and display the movie details on webpage as poster when clicked will play the movie trailer.
#### function `open_movies_page`
```
output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_page_content.format(
    movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head + rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
```
#### List created and passed as parameter as below.
```
movies_list = [shawshank, titanic, Batman, Avengers, Witch_Mountain, Wall_Street]

fresh_tomatoes.open_movies_page(movies_list)
```
#### Tools required:
1. Web-browser
2. Python 2.6 or higher
3. Any coding tool (like notepad++, sublime-text, atom) IDLE preferred.
#### Contribution:
Please feel free to make changes to the code and [contribute](https://github.com/SKowshik4614/ud036_StarterCode_santosh/tree/master/contribute) to make the code work better.