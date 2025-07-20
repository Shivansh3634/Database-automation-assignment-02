import mysql.connector

def main():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="companydb"
    )
    cursor = conn.cursor()

    with open("sql-scripts/add_departments.sql", "r") as file:
        sql_script = file.read()

    statements = sql_script.split(';')
    for statement in statements:
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
