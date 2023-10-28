from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# データベース接続情報
db_url = "postgresql://postgres:postgres@localhost:54322/postgres"

# SQLAlchemyエンジンの作成
engine = create_engine(db_url)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# SQLコマンドの実行
sql_command = text("DROP TABLE pokemons CASCADE;")
session.execute(sql_command)
session.commit()
