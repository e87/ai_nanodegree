# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

print("\n Using a while loop \n")

counter = 0
while counter < len(headlines):
    news_ticker += headlines[counter] + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
    counter += 1

print(news_ticker)
