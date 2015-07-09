'''
Created on July 05 2015

'''


class Publisher:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)

    def publish(self, s):
        for subscriber in list(self.subscribers):
            subscriber(s)

if __name__ == '__main__':
    def multiplier(s):
        print(2*s)

    class SimpleSubscriber:

        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            self.processcount = 0
            self.processlimit = 3
            publisher.subscribe(self.process)

        def process(self, s):
            self.processcount += 1
            print(self, ":", s.upper())
            if self.processcount == self.processlimit:
                print(
                    "Three messages processed! {} has been unsubscribed".format(self))
                self.publisher.unsubscribe(self.process)

        def __repr__(self):
            return self.name

    publisher = Publisher()
    publisher.subscribe(multiplier)

    for i in range(6):
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        publisher.publish(' req'+str(i))