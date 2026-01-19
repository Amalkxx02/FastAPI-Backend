from firebase_admin import (
    get_app,
    credentials,
    initialize_app,
    firestore_async,
    auth,
    messaging,
)
from app.core.config import secrets


def get_firebase_app():
    try:
        return get_app()
    except ValueError:
        cred = credentials.Certificate(secrets.FIREBASE_CRED)
        return initialize_app(cred)
    except Exception as e:
        pass


def firebase_firestore():
    """Return async Firestore client."""
    app = get_firebase_app()
    return firestore_async.client(app)


def firebase_messaging():
    get_firebase_app()
    return messaging

def firebase_auth():
    get_firebase_app()
    return auth
    
