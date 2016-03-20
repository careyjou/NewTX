import firebase
import json

def print_json(rest_url):
    MYURL  = 'https://boiling-heat-5294.firebaseio.com/'
    EMAIL  = 'emersonhtc@gmail.com'
    SECRET = '5zF8T37NlZB1HBHkb9T1zAZ6c2cPbXiXlzP5yJ8P'

    authentication = firebase.FirebaseAuthentication(SECRET,EMAIL, True, True)
    fb = firebase.FirebaseApplication(MYURL, authentication)
    result = fb.get(rest_url, None)
    print json.dumps(result, indent=4, sort_keys=True)

if __name__ == '__main__':
    print_json("/2016/")
    print_json("/2016/03/")
