import pyrebase

config = {
    "apiKey": "AIzaSyBxImDeaOZY4GmKlaHt5638SScn-IELxwM",
    "authDomain": "extrato-fa645.firebaseapp.com",
    "databaseURL": "https://extrato-fa645.firebaseio.com",
    "projectId": "extrato-fa645",
    "storageBucket": "extrato-fa645.appspot.com",
    "messagingSenderId": "1053515432794"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
archer = {"name": "Sterling Archer", "agency": "Figgis Agency"} 
db_store = db.child("tabela1")
dados={"chave": "valor"}
db_store.set(archer)
