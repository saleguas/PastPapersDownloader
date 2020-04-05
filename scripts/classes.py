class linkClass:

    def __init__(self, name, link):
        self.name = name
        self.url = link

    def getAttr(self):
        return self.name, self.url

    def __repr__(self):
        return self.name + ' - ' + self.url


'''
Used for associating the file name with the link
'''
