from matplotlib import pyplot as plt
import requests, json, sys

youtubersName = str(input("Name:  "))
key = str("AIzaSyBa9unHzuRzr44urHFSiiKIgHpQkXZIwWo")
time = int(input("Time:  "))
staticTime = int(0)
apiUrl = str("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={}&key={}".format(youtubersName, key))
print("\n---------------------------------")

rawApiData = requests.get(apiUrl).content
staticSubscribers = int(json.loads(rawApiData)["items"][0]["statistics"]["subscriberCount"])

plt.style.use("ggplot")
plt.figure("{} Subscribers".format(youtubersName))
plt.title("Youtube API Data")

while time != 0:
    try:
        rawApiData = requests.get(apiUrl).content
        subscribers = int(json.loads(rawApiData)["items"][0]["statistics"]["subscriberCount"])

        plt.scatter(staticTime, abs(subscribers - staticSubscribers), marker = "+")

        sys.stdout.write("\r" + "Remaining Time:  " + str(time))
        sys.stdout.flush()

        staticTime += 1; time -= 1
        staticSubscribers = int(subscribers)

        plt.pause(1)
    except:
        print("Internal Error ! ! ! !")
        quit()

plt.show()
print("\n\nFinished ! ! ! !")
