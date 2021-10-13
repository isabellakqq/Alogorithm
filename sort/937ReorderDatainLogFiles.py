class Solution:
    def reorderLogFiles(self, logs):
        '''
        time: 11:25
        '''
        def get_key(log):
            _id, rest = log.split(' ', maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        
        return sorted(logs, key=get_key)

            