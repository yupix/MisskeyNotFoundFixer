# Misskey NotFound Fixer

Misskeyでリモートユーザーの画像がおかしくなった際に修正するためのコマンドです。

## インストール

```bash
python setup.py sdist
cd dist && pip install mnff-0.0.1.tar.gz
```

## 使い方

```
mnff --token=token --url wss://example.com/streaming --user_id ユーザーのid
```
