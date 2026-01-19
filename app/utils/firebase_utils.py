from app.core.firebase.firebase import firebase_auth, firebase_firestore
from app.core.firebase.firestore_path import Collections
from pydantic import EmailStr


class FirebaseAuth:
    @staticmethod
    def verify_id_token(id_token: str)->dict:
        """Verify Firebase ID token and return user base data (uid, name, email,...)."""
        return firebase_auth().verify_id_token(id_token)

    @staticmethod
    def get_user(uid: str)->dict:
        """Get user details from Firebase Auth by uid."""
        return firebase_auth().get_user(uid)

    @staticmethod
    def get_user_by_email(email_id: EmailStr)->dict:
        """Get user details from Firebase Auth by email."""
        return firebase_auth().get_user_by_email(email_id)
    
    @staticmethod
    def generate_email_verification_link(email_id: EmailStr):
        """Generate email verification link from Firebase Auth by email."""
        return firebase_auth().generate_email_verification_link(email_id)
    
    @staticmethod
    def generate_password_reset_link(email_id: EmailStr):
        """Generate password reset link from Firebase Auth by email."""
        return firebase_auth().generate_password_reset_link(email_id)


class FirebaseDB:
    @staticmethod
    def firestore_user():
        return firebase_firestore().collection(Collections.C1)

    @staticmethod
    def firestore_profile():
        return firebase_firestore().collection(Collections.C2)
