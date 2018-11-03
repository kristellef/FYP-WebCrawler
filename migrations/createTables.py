from lib.db import DB

def createTables(db: DB):
    
    commands = []

    # Create rent table
    commands.append("""
        CREATE TABLE IF NOT EXISTS addresses  (
        address VARCHAR NOT NULL,
        name VARCHAR NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT NOW()
        );
    """)

    db.execute(commands,False);