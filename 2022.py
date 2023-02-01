class Document:
    def __init__(self,authors,date):
        self.authors=authors
        self.date=date
    def getDate(self):
        return self.date
    def getAuthors(self):
        return self.authors
    def addAuthors(self,name):
        if type(name)== str:
            self.auth.append(name)
class Book(Document):
    def __init__(self,title,authors,date):
        super.__init__(authors,date)
        self.title=title
    def getTitle(self):
        return self.title
class Email(Document):
    def __init__(self,subject,to,authors,date,title):
        self.subject=subject
        self.to=to
        super.__init__(authors,date)
    def getSubject(self):
        return self.subject
    def getTo(self):
        return self.to

email=Email("Kendrick","12/20/2022","random",["random"],"Tony")