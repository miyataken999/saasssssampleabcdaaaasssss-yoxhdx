import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        dbname="neondb",
        user="miyataken999",
        password="yz1wPf4KrWTm",
        host="ep-odd-mode-93794521.us-east-2.aws.neon.tech",
        port=5432,
        sslmode="require"
    )
    return conn