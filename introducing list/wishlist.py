books = [
    "Automate the Boring stuff with python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",

]


video_games = [
    "The Legend of Zelda: Breath of the Wild"
    "Splatoon 2"
    "Super Mario Odyssey"
]

print("Suggested gift: {}".format(books[0]))

print("books:")
for book in books:
    print("* " + book)

def display_wishlist(display_name, wishes):
    items = w
    print(display_name + ":")
    suggested_gift = items.pop(0)
    print("======>", suggested_gift, "<======")
    for item in items:
        print("* " + item)
        print()

display_wishlist("Books", books)
display_wishlist("video games", video_games)