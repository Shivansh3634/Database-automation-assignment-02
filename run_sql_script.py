import mysql.connector

def run_sql_script(cursor, script_path):
    with open(script_path, 'r') as f:
        sql_commands = f.read().split(';')  # Split commands by ';'
        for command in sql_commands:
            cmd = command.strip()
            if cmd:
                cursor.execute(cmd)

def main():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="companydb"
    )
    cursor = conn.cursor()

    try:
        run_sql_script(cursor, 'sql-scripts/create_projects_table.sql')
        run_sql_script(cursor, 'sql-scripts/add_budget_column.sql')
        conn.commit()
        print("SQL scripts executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
