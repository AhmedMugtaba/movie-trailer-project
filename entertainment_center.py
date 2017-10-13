import media
import fresh_tomatoes


# Movies objects


imitation_game = media.Movie('Imitation Game',
                             'A movie about Alan cracking Nazi codes',
                             'https://goo.gl/KQX8L3',
                             'https://goo.gl/d8EB44')

sully = media.Movie('Sully',
                    'A movie about landing in the Hudson River',
                    'https://goo.gl/X8P647',
                    'https://goo.gl/ohWpiM')

get_out = media.Movie('Get Out',
                      'A movie about a boy meeting his girlfriend family',
                      'https://goo.gl/3ekHHi',
                      'https://goo.gl/abiKgw')

the_martian = media.Movie('The Martian',
                          'A movie about leaving an astronauts behind in Mars',
                          'https://goo.gl/NCoiMv',
                          'https://goo.gl/M3Sj21')

unbroken = media.Movie('Unbroken',
                       'A movie about Zamperini an oplymic runner',
                       'https://goo.gl/4hYRkq',
                       'https://goo.gl/dmSTTq')

the_prestige = media.Movie('The Prestige',
                           'A movie about an illusion gone horribly wrong',
                           'https://goo.gl/vyDsdQ',
                           'https://goo.gl/v81Gpt')

# List or array of movies as an input for the open_movies_page function

movies = [imitation_game,
          sully,
          get_out,
          the_martian,
          unbroken,
          the_prestige]

fresh_tomatoes.open_movies_page(movies)
