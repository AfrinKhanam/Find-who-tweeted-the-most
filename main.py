from collections import Counter
import numpy as np 


def generate_user_tweets_dict(names,tweets):
    '''generate dictionary tweets dictionary, where user is key and number of tweets as value '''
    tweets_dict = {}
    tweets = Counter(tweets)
    for name in names:
        tweets_dict[name] = tweets[name]
    return tweets_dict


def check_all_tweets_score_same(tweets_dict):
    '''checks if users are having same number of tweets and prints all the users in alphabetical order'''
    
    for key in sorted(tweets_dict.keys()):
        print(f'{key} {tweets_dict[key]}')


def check_tweets_score_different(tweets_dict):
    '''Finds the user with max number of tweets and prints user name and total number of tweets.'''
    
    sorted_list = sorted(tweets_dict.items(),key=lambda x: x[1], reverse=True)
    
    if len(sorted_list) is not 1:
        
        for key,value in dict(sorted_list[:len(tweets_dict)-1]).items():
            print(f'{key} {value}')
    else:
        for key,value in dict(sorted_list).items():
            print(f'{key} {value}')


def get_most_tweeted_user(tweets_dict):
    """ identtifys user with max number of tweet and prints user name and total number of tweets """
    score = next(iter(tweets_dict.values()))
    all_equal = all(value == score for value in tweets_dict.values())
    if all_equal:
        check_all_tweets_score_same(tweets_dict)
    else:
        check_tweets_score_different(tweets_dict)


if __name__ == "__main__":

    """Read the input from console"""
    try:
        input_num = int(input())
        tweets = []

        for _ in range(input_num):
            """ Read the number of test cases input from console """
            testcases_num = int(input())
            while testcases_num > 0:
                tweet = input()
                tweets.append(tweet.split(" ")[0])
                testcases_num -= 1
        tweets = np.array(tweets) 
        names = np.unique(tweets)

        tweets_dict = generate_user_tweets_dict(names,tweets)
        get_most_tweeted_user(tweets_dict)
    except Exception as e:
        print(e.args)
    else:
        print("------THANK YOU---------")



