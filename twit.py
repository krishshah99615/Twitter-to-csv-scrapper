import tweepy
import csv
c=''
c_s=''
a=''
a_s=''


def s_hash(h,c,c_s,a,a_s):
    #creating authentication for accessing twitter
    auth = tweepy.OAuthHandler(c,c_s)
    auth.set_access_token(a,a_s)
    print('done auth')
    #initializing tweepy api
    api = tweepy.API(auth)
    #for t in tweepy.Cursor(api.search,q=h,lang='en',tweet_mode='extended').items(1):
    #    print(t)

    with open('data.csv','w') as file:
        w = csv.writer(file)
        w.writerow(['timestamp','tweet_text','username','all_hashtags'])
        for t in tweepy.Cursor(api.search,q=h,lang='en',tweet_mode='extended').items(100):

            w.writerow([t.created_at,
                        t.full_text.replace('\n','').encode('utf-8'),
                        t.user.screen_name.encode('utf-8'),
                        [e['text'] for e in t._json['entities']['hashtags']]])
s_hash('batman',c,c_s,a,a_s)
