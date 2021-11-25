import sqlite3

poop = sqlite3.connect('StandUp.db')
po = poop.cursor()

po.execute(
    """
    CREATE TABLE spreadsheet(
    name TEXT,
    what_did TEXT,
    problem TEXT,
    what_will_do TEXT
    )
    """
)
poop.commit()

def pooppop():
    global what_did, problem ,what_will_do
    name = input('#StandUp\n ')
    what_did = input('Что сделал: ')
    problem = input('Проблемы: ')
    what_will_do = input('Что буду делать: ')

    po.execute(f"INSERT INTO spreadsheet VALUES (?,?,?,?)",
                    (name, what_did, problem ,what_will_do))
    po.execute(f"DELETE FROM spreadsheet WHERE problem = '{problem}'")
    if po.fetchone() is None:
        print(po.fetchone())

    poop.commit()


pooppop()