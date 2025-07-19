from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreate
from backend.utils.security import hash_password

ADMIN_CODE = "Ahn2588"
MAX_FAIL = 5
admin_code_fail_count = {}

def create_user(db: Session, user_in: UserCreate):
    username = user_in.username

    #Sign up validation
    if db.query(User).filter(User.username == username).first():
        return None, "Username already exists"

    # admin code validation
    role = "user"
    fail_count = admin_code_fail_count.get(username, 0)
    if user_in.admin_code:
        if user_in.admin_code == ADMIN_CODE:
            role = "admin"
            admin_code_fail_count.pop(username, None)
        else:
            fail_count += 1
            admin_code_fail_count[username] = fail_count
            if fail_count >= MAX_FAIL:
                role = "user"
            else:
                return None, f"Wrong admin code. Attempts left: {MAX_FAIL - fail_count}"

    password_hash = hash_password(user_in.password)

    db_user = User(username=username, password_hash=password_hash, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user, None
