class Post:
    def __init__(self, Name, Text, SenderName, Date, *Tags):
        self.Name = Name
        self.Text = Text
        self.SenderName = SenderName
        self.Date = Date
        self.Tags = []

        for tag in Tags:
            Tags.append(tag)
