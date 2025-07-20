import mysql.connector

def main():
    conn = mysql.connector.connect(
        host="127.0.0.1",        # yahan 'mysql' ki jagah localhost use karo
        user="root",
        password="root",
        database="companydb"
    )
    cursor = conn.cursor()

    with open("sql-scripts/add_departments.sql", "r") as file:
        sql_script = file.read()

    for result in cursor.execute(sql_script, multi=True):
        pass

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
