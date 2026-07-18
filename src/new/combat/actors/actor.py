class Actor:
    def __init__(self):
        self.main   = { }
        self.object = { }

    def __gen_main(self, origin):
        #TODO: "from XXX import" maindata and objectdata
        from profiles import Profiles

        self.main = { 

            'origin': origin, 'name': origin.data['name'],
            
            'sprite': None, 'hitbox': None, 'state': True, 'type': origin.data['type'],
            'profile': Profiles(), 'brain': None, 'history': None,

         }

    def set_OID(self, prev_id=False):
        import uuid
        # self.object['oid'] = uuid.uuid4().hex[:8] if isinstance(prev_id, int) is False else prev_id
        self.object['oid']   = uuid.uuid4().hex[:8] if prev_id is False else prev_id

    def __gen_object(self, link_state=False):
        import uuid
        
        self.object = { 
            
            'oid': self.set_OID(link_state), 'eid': None, #TODO
            'link': link_state,

        }

    def genenerate(self, origin, link_state):
        if isinstance(self.main, dict) is False:
            self.main = { }
        
        if len(self.main) > 1:
            print('01L - MainData in Actor is already generated.')
            return False
        else:
            print('Entity first generation is loading.')
            self.__gen_main(origin)
        
        # ------------

        if isinstance(self.object, list) is False:
            self.object = { }
        if len(self.object) > 1:
            print('02L - The Actor already has an ObjectData.')
            return False
        else:
            self.__gen_object(link_state)

        return True

    def update(self):
        pass