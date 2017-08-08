import media
import fresh_tomatoes

imitation_game = media.Movie('Imitation Game',
    'A movie about mathematics Alan cracking Nazi codes',
    'https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg',
    'https://www.youtube.com/watch?v=S5CjKEFb-sM')

sully = media.Movie ('Sully',
    'A movie about capt.Cheskey making an emergency landing in New Yorks Hudson River',
    'https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg',
    'https://www.youtube.com/watch?v=mjKEXxO2KNE')

get_out = media.Movie ('Get Out',
    'A movie about a boy meeting his girlfriend family',
    'https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png',
    'https://www.youtube.com/watch?v=DzfpyUB60YY')

the_martian = media.Movie ('The Martian',
    'A movie about leaving an astronauts behind in Mars',
    'https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg',
    'https://www.youtube.com/watch?v=ej3ioOneTy8')

unbroken = media.Movie ('Unbroken','A movie about Zamperini an oplymic runner',
    'https://upload.wikimedia.org/wikipedia/en/7/76/Unbroken_poster.jpg',
    'https://www.youtube.com/watch?v=XrjJbl7kRrI')

the_prestige = media.Movie ('The Prestige','A movie about an illusion gone horribly wrong',
    'https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg',
    'https://www.youtube.com/watch?v=o4gHCmTQDVI')

movies = [imitation_game, sully, get_out, the_martian, unbroken, the_prestige]
fresh_tomatoes.open_movies_page(movies)
