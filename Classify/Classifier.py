import numpy as np


class GenreClassifier:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    __music_correlation = {'hip_hop': np.array([-18, 21, 4, 0, 14]), 'pop': np.array([-16, 20, 2, 23, 13]),
                           'dance': np.array([-15, 22, 2, 6, 9]),
                           'soundtrack': np.array([5, 14, 20, 0, -5]),
                           'rock': np.array([-4, 2, 20, 7, 6]),
                           'metal': np.array([-4, 10, -4, -18, 5]),
                           'classical': np.array([20, -8, 15, 2, 9]),
                           }
    __film_correlation = {'action': np.array([130, 0, -30, -14, 21]), 'comedy': np.array([-47, 199, -76, 137, 14]),
                          'documentary': np.array([100, 63, 269, 73, -27]), 'drama': np.array([-75, 113, 163, 87, 120]),
                          'horror': np.array([-95, -27, 128, -64, 40]),
                          'romance': np.array([-109, -266, 111, 278, 111]),
                          'sci_fi': np.array([-179, -139, 216, -85, 81])
                          }

    def __fix_genres(self, data, compared_to):
        result = []
        for _ in data:
            for word in _.split():
                for genre in compared_to:
                    if genre.rstrip().lower() in word.rstrip().lower():
                        result.append(genre)
        return result

    def __classify_one(self, data, correlation_dict):
        correlation = np.array([0, 0, 0, 0, 0])

        for element in data:
            if element in correlation_dict:
                elem = correlation_dict[element]
                correlation += elem

        return correlation

    def __classify_data(self, music, films):
        music = self.__fix_genres(music, self.__music_correlation.keys())

        films = self.__fix_genres(films, self.__film_correlation.keys())

        return np.argmax(self.__classify_one(music, self.__music_correlation) +
                         self.__classify_one(films, self.__film_correlation))

    def __str_fixer(self, data):
        result = []
        should_append = False
        str_to_append = ""
        for sym in data:
            if should_append and sym != '\'':
                str_to_append += sym
            if sym == '\'':
                if should_append:
                    result.append(str_to_append.replace(' ', '_').replace('-', '_'))
                    str_to_append = ""
                should_append = not should_append
        return result

    def get_psycho(self):
        result = []
        for index, row in self.data_frame.iterrows():
            music_ = self.__str_fixer(row['genres_of_music'])
            films_ = self.__str_fixer(row['genres_of_films'])
            result.append(self.__classify_data(music_, films_))
        return result
