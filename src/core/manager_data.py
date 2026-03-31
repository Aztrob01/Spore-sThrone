import datetime
from root.utils import json_gets

class DataLoader:
    def __init__(self):
        
        self.__common_paths = {
            'player': './src/game/users/save.json',
            'level': './src/game/world/level.json',
            'settings': './src/root/settings.json',
        }

        self.__main_data_save   = json_gets(self.__common_paths['player'], None, True)
        self.__main_data_level    = json_gets(self.__common_paths['level'], None, True)
        self.__main_data_settings = json_gets(self.__common_paths['settings'], None, True)


        self.game = {
            'version': self.__main_data_settings['game']['version'],
            'clock': self.__main_data_settings['game']['clock'],
            'debug': f"{self.__main_data_settings['game']['debug_name']} -> {self.__main_data_settings['game']['debug_mode']}"
        
        }
        self.data_save     = self.__main_data_save
        self.data_player   = self.__main_data_save['player']
        self.data_level    = self.__main_data_level['level']
        self.data_settings = self.__main_data_settings['settings']
        self.last_update   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update(self): #! isnt tested yet, might dont work properly
        self.__main_data_save     = json_gets(self.__common_paths['player'], None, True)
        self.__main_data_level    = json_gets(self.__common_paths['level'], None, True)
        self.__main_data_settings = json_gets(self.__common_paths['settings'], None, True)

        self.last_update = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def tick(self):
        self.last_update = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f'Version: {self.game["version"]} | Framerate: {self.game["clock"]} | Last Update: {self.last_update}'
        print(message)

    



        