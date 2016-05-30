import requests

def do_stuff(event, context):

    test_url = 'https://o6ivr8pze8.execute-api.us-east-1.amazonaws.com/testing/pets'

    r = requests.get(test_url)

    return r.json()


if __name__ == '__main__':
    r = do_stuff(0,0)
    print r
