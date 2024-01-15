from .core import db

conn = db.get_conn()


# ========================×========================
#                 PM PERMIT DATABASE
# ========================×========================

# ========================×========================
#               PM PERMIT MODE DATABASE
# ========================×========================
def get_mode_permit():
    cursor = conn.execute("SELECT mode FROM permit_mode")
    try:
        cur = cursor.fetchone()
        cursor.close()
        return cur[0] if cur is not None else None
    except:
        return None


def set_mode_permit(mode):
    cek = get_mode_permit()
    if cek is not None:
        conn.execute("""UPDATE permit_mode SET mode = ?""", (mode,))
    else:
        conn.execute("""INSERT INTO permit_mode (mode) VALUES(?)""", (mode,))
    conn.commit()


# ========================×========================
#               PM PERMIT USER DATABASE
# ========================×========================
def is_approved() -> list:
    cursor = conn.execute("SELECT user_id FROM permit_user")
    try:
        row = cursor.fetchone()
        cursor.close()
        return eval(row[0]) if row is not None else []
    except:
        return []


def approve(user_id: int):
    x = is_approved()
    if x:
        x.append(user_id)
        conn.execute("""UPDATE permit_user SET user_id = ?""", (str(x),))
    else:
        conn.execute("""INSERT INTO permit_user (user_id) VALUES(?)""", (str([user_id]),))
    conn.commit()


def disapprove(user_id: int):
    x = is_approved()
    if len(x) == 1:
        conn.execute("""DELETE FROM permit_user""")
    else:
        x.remove(user_id)
        conn.execute("""UPDATE permit_user SET user_id = ?""", (str(x),))
    conn.commit()


# ========================×========================
#             PM PERMIT MESSAGE DATABASE
# ========================×========================
def get_permit_message():
    cursor = conn.execute("SELECT permit_msg FROM permit_message")
    try:
        cur = cursor.fetchone()
        cursor.close()
        return cur[0] if cur is not None else None
    except:
        return None


def set_permit_message(permit):
    cek = get_permit_message()
    if cek is not None:
        conn.execute("""UPDATE permit_message SET permit_msg = ?""", (permit,))
    else:
        conn.execute("""INSERT INTO permit_message (permit_msg) VALUES(?)""", (permit,))
    conn.commit()


def del_permit_message():
    cek = get_permit_message()
    if cek is not None:
        conn.execute("DELETE from permit_message")
        conn.commit()
        return True
    else:
        return False
