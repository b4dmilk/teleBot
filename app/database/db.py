import sqlite3 as sq

async def db_start():
    global db, cur

with sq.connect('main.db') as db:
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, name TEXT, groups TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS articles(article_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, name TEXT DEFAULT NAME, desc TEXT, article TEXT, FOREIGN KEY (user_id) REFERENCES profile (user_id))")
    db.commit()

#Create profile
async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?)", (user_id, '', ''))
        db.commit()


async def edit_profile(state, user_id):
    data = await state.get_data()
    cur.execute("UPDATE profile SET groups = '{}',  name = '{}' WHERE user_id == '{}'".format(
        data['groups'], data['name'], user_id))
    db.commit()

async def all_profile():
     cur.execute("SELECT * FROM profile")
     result =cur.fetchall()
    
     for result in cur:
         print(result)
     return result
     db.commit()


#Create article
async def create_article(state, user_id):
        data = await state.get_data()
        cur.execute("INSERT INTO articles VALUES( NULL, ?, ?, ?, ?)", ( user_id, data['name'], data['desc'], data['article']))
        db.commit()

#Create article
async def create_table(state):
        data = await state.get_data()
        sql = "CREATE TABLE IF NOT EXISTS " + data['name']  + """  
        (table_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, name TEXT DEFAULT NAME, desc TEXT, article TEXT, FOREIGN KEY (user_id ) REFERENCES profile (user_id))
        """ 
        cur.execute(sql)
        db.commit()
