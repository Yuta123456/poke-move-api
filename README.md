- postgres サーバ起動
  `sudo service postgresql start`
- postgres サーバ停止
  `sudo service postgresql stop`
- postgres 使わず、ローカルで supabase のコンテナを起動
  - `npx supabase {stop / start}`
- サーバ起動
  `uvicorn app.main:app --reload`
- db
  supabase
- deploy 先
  - gcp
  - リージョンが終わってるのでどうにかしたい
- migrate
  - `alembic revision --autogenerate -m ""`
  - `alembic upgrade head`
  <!-- URL: https://poke-move-api-d3y43tvzba-uc.a.run.app/ -->
