import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

def get_information(name):
    """
    str -> lst
    This function returns a list of information about frinds of chosen account
    """
    lst = []
    for user in js['users']:
        lst.append((user["name"], user['screen_name'], user["id"], user["location"], user["friends_count"], user["followers_count"], user['created_at']))
    return lst


if __name__ == "__main__":
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    account = input('Enter Twitter Account: ')
    spec_inf = str(input("Choose: name, screen_name, id, location, number_of_friends, number_of_followers, created_at: "))

    url = twurl.augment(TWITTER_URL,
                           {'screen_name': account, 'count': '200'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    inside = connection.read().decode()
    js = json.loads(inside)
    print(" ")
    print("The information about " + str(account) + " Twitter friends: " + "\n")
    lst_1 = get_information(account)
    for i in lst_1:
        if spec_inf == "name":
            print("Name: " + str(i[0]))
        elif spec_inf == "screen_name":
            print("Screen name: " + str(i[1]))
        elif spec_inf == "id":
            print("ID of "+ str(i[0]) + " is: " + str(i[2]))
        elif spec_inf == "location":
            print("Location of " + str(i[0]) + " is: " + str(i[3]))
        elif spec_inf == "number_of_friends":
            print("Number of friends of " + str(i[0]) + " is: " + str(i[4]))
        elif spec_inf == "number_of_followers":
            print("Number of followers of " + str(i[0]) + " is: " + str(i[5]))
        elif spec_inf == "created_at":
            print(str(i[0]) + " created account: " + str(i[6]))
        print(" ")