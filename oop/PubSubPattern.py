class PushNotification:
    @classmethod
    def notify(user_id, message):
        print("user_id" + message)

class PubSubPattern:
    channel_dic = {}
    def __init__(self) -> None:
        pass
    def subscribe(self, channel, user_id):
        if channel not in self.channel_dic:
            self.channel_dic[channel] = set()
            self.channel_dic[channel].add(user_id)
    
    def unsubscribe(self, channel, user_id):
        if channel in self.channel_dic and user_id in self.channel_dic[channel]:
            self.channel_dic[channel].remove(user_id)
    
    def publish(self, channel, massage):
        if channel in self.channel_dic and len(self.channel_dic[channel] > 0):
            for id in self.channel_dic[channel]:
                PushNotification.notify(id, message="thank you!")


