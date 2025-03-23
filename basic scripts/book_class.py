class book:
  def __init__(self, title="", author="", page=0):
    self.title=title
    self.type="book"
    self.author=author
    self.page=page

  def description(self):
    desc = f"{self.title} is a {self.type} written by {self.author}. It has {self.page} pages."
    return desc

class Magazine(book):
  def __init__(self, title, author, page, edition=0, volume=0, category=""):
    super().__init__(title, author, page)
    self.type="magazine"
    self.edition=edition
    self.volume=volume
    self.category=category

  def description(self):
    desc = f"{self.title} is a {self.type} written by {self.author}. It has {self.page} pages. It is the {self.edition} edition, volume {self.volume}, category: {self.category}"
    return desc

book1 = book("How to lose.", "Tom & Jerry", 500)
print(book1.description())

magazine = Magazine(title="How to Win", author="Homer Simpson", page=10, edition=1, volume=1, category='DUFF')
print(magazine.description())