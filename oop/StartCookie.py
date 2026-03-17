class StarCookie:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

star_cookie1 = StarCookie(15, "Red")
print(star_cookie1)

class Youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers
    def setSubsribers(self, subscribers):
        self.subscribers = subscribers

user1 = Youtube('Eren')
print(user1.subscribers)
user1.setSubsribers(10)
print(user1.subscribers)

