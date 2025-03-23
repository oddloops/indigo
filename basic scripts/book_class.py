class book:
  title=""
  type="book"
  author=""
  page=""

  def description(self):
    desc = "%s is a %s written by %s. It has %.0f pages." % (self.title, self.type, self.author, self.page)
    return desc

book1 = book()
book1.title="How to lose."
book1.author="Tom & Jerry"
book1.page=500
print(book1.description())