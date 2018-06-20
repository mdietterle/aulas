
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\Martim\\OneDrive\\Scripts Python\\pyrebase\\extrato-fa645-firebase-adminsdk-8mcxb-190d6c224d.json")
#firebase_admin.initialize_app(cred)

default_app = firebase_admin.initialize_app(cred)
print(default_app)
db = default_app.database()
db_store = db.child("tabela1")
archer = {"name": "Sterling Archer", "agency": "Figgis Agency"} 
db_store.set(archer)
