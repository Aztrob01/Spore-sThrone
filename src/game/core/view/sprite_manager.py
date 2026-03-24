import pygame


class SpriteManager:
    def __init__(self, user, data):
        self.user  = user
        self.image = None
        self.rect  = None
        self.size  = None

        self.static = {
            'explore': {
                'idle': data['explore']['idle'], # will return an path
                'walk_up': data['explore']['walk_up'],
                'walk_down': data['explore']['walk_down'],
                'walk_side': data['explore']['walk_side'],
                'dead': data['explore']['dead'],
            },
            'fight': {
                'idle': data['fight']['idle'],
                'running': data['fight']['running'],
                'acting': data['fight']['acting'],

                'stuned': data['fight']['stuned'],
                'hitted': data['fight']['hitted'],
                'low': data['fight']['low'],
                'dead': data['fight']['dead'],
            },
            'size': {
                'default': data['default'],
                'others': data['others'],
            }
        }

    def image_update(self, path, key_words):
        """
            dict: Update the sprite image and size based on a list of keys
                #### path -> a system path where the png belongs
                #### key_words -> keys used to find path into self.static sprites.
        """
        self.image = pygame.image.load(path)

        if self.static['size']['others'] is not None:
            for nums, lists in self.static['size']['others']:
                for num, items in enumerate(lists):
                    if items[0] == key_words:
                        self.image = pygame.transform.scale(self.image, self.static['size']['others'][nums][1])
        else:
            self.image = pygame.transform.scale(self.image, self.static['size']['default'])

    
    def static_update(self, key_state):
        for keys in self.static:
            if key_state[0] == keys:
                for num, key in enumerate(self.static[keys]):
                    if key_state[1] == key:
                        if self.static[keys][key] is not None:
                            self.image_update(self.static[keys][key], key_state)
                        else:
                            print(f"An error occurred rendering {self.user.codename}'s model {key_state}.")
                            self.image_update(self.static['fight']['idle'], ['fight', 'idle']) 
                        break
                break


