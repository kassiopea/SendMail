class Letter:
    def __init__(self,
                 to: str = None,
                 author: str = None,
                 subject: str = None,
                 message: str = None
                 ) -> None:
        self.to = to
        self.author = author
        self.subject = subject
        self.message = message

    def __eq__(self, other):
        return self.to == other.to \
               and self.author == other.author\
               and self.subject == other.subject \
               and self.message == other.message

