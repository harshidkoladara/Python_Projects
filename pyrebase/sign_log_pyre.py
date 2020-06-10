import pyrebase


class LogSign():

    def __init__(self):

        config = {
            "apiKey": "AIzaSyC8RZmCNKCGNFUp3HlUFAMTnDfFp5a4phc",
            "authDomain": "hacks-7da44.firebaseapp.com",
            "databaseURL": "https://hacks-7da44.firebaseio.com",
            "storageBucket": "hacks-7da44.appspot.com",
            "serviceAccount": "hacks-7da44-a761e9b53a58.json"
        }

        self.firebase = pyrebase.initialize_app(config)

    def signin_method(self, name,  email, password, img_src):
        auth = self.firebase.auth()
        user = auth.create_user_with_email_and_password(
            email=email, password=password)

        # user1 = auth.sign_in_with_email_and_password(email, password)

        data = {
            'name': name,
            'email': email,
            'password': password
        }
        db = self.firebase.database()
        # db.child('users').child("harshid").set(user1['localId'])
        # result = db.child('users/'+user1['localId']).push(data)

        db.child('users').child(user['localId']).push(data)

        storage = self.firebase.storage()
        storage.child('users').child(
            user['localId']).put(img_src, user['localId'])

        return "Sign in Successfull..."

    def login_method(self, email, password):
        auth = self.firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)

        database = self.firebase.database()
        data = database.child('users').child(user['localId']).get()
        data_dict = data.val()
        dict_values = list(data_dict.values())
        final_data_dict = dict_values[0]

        storage = self.firebase.storage()
        # image = storage.child('users/'+user['localId']).get_url(user['localId'])
        # print(image)

        image = storage.child('users/'+user['localId']).download(
            path='users/'+user['localId'], filename=email+'.jpg')
        print(image)

        data_src = ["Login Successfull....", final_data_dict, email+'.jpg']

        return data_src


if __name__ == "__main__":
    print("---------------File Can't be Accessable---------------")
