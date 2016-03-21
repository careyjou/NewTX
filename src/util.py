import firebase
import json

class Util:
    url = 'https://boiling-heat-5294.firebaseio.com/'
    secret_key = '5zF8T37NlZB1HBHkb9T1zAZ6c2cPbXiXlzP5yJ8P'
    email = 'emersonhtc@gmail.com'
    fb = None
    authentication = None

    def __init__(self,url,secret_key,email):
        self.authentication = firebase.FirebaseAuthentication(secret_key,email, True, True)
        self.fb = firebase.FirebaseApplication(url, self.authentication)
        self.url = url

    def __str__(self):
        result = self.fb.get('/', None)
        return json.dumps(result, indent=4, sort_keys=True)

    def print_json(self, rest_url):
        result = self.fb.get(rest_url, None)
        print json.dumps(result, indent=4, sort_keys=True)

    def delete(self,key):
        ret = self.fb.delete(self.url,key)

    def put(self,key,value):
        ret = self.fb.put(self.url,key,value)
        if ret == value:
            return True
        else:
            return False

if __name__ == '__main__':
    url = 'https://boiling-heat-5294.firebaseio.com/'
    secret_key = '5zF8T37NlZB1HBHkb9T1zAZ6c2cPbXiXlzP5yJ8P'
    email = 'emersonhtc@gmail.com'
    instance = Util(url,secret_key,email)
    print str(instance)
