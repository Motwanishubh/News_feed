class News:
    def __init__(self, title, details, image_path):
        self.title = title
        self.details = details
        self.image_path = image_path


class NewsFeedApp:
    def __init__(self):
        self.news_list = []

    def add_news(self):
        title = input("Enter News Title: ")
        details = input("Enter News Details: ")
        image_path = input("Enter Photo path or URL: ")
        news = News(title, details, image_path)
        self.news_list.append(news)
        print("News added successfully!")

    def list_news(self):
        if not self.news_list:
            print("No news available.")
        else:
            for idx, news in enumerate(self.news_list, start=1):
                print(f"\nNews #{idx}")
                print(f"Title: {news.title}")
                print(f"Details: {news.details}")
                print(f"Image Path/URL: {news.image_path}")

    def run(self):
        while True:
            print("\nSelect your choice:")
            print("1. Add news details")
            print("2. List news")
            print("3. Exit app")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_news()
            elif choice == '2':
                self.list_news()
            elif choice == '3':
                print("Exiting app.")
                break
            else:
                print("Invalid choice. Please try again.")


# Running the app
app = NewsFeedApp()
app.run()
