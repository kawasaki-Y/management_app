※ボタンを2回クリックしないと先に進めない現象が生じており（deployしたstreamlitの問題？）、アプリの画面遷移はコードレビュー時に説明します。
ログインや削除といったボタンは2回クリックする必要がある状態です。

コードレビューで使用するファイルは次の通りです
・tags_and_target.py
・sales_management.py
・dashboard.py
・database.py

今回の課題を作る上で参考にした書籍

https://amzn.asia/d/2UIVGKj
「Streamlit入門　Pythonで学ぶデータ可視化＆アプリ開発ガイド」
https://amzn.asia/d/5rObAgS
「PythonとStreamlit でデータ分析をWebアプリ化: データサイエンティストのためのWebアプリ入門」
https://amzn.asia/d/ea74Dma
「Python,Pandas,Streamlitで体験するインタラクティブダッシュボード開発入門 」
https://amzn.asia/d/8OK4WEj
「PythonでまなぶSQLiteデータベース入門」


# ①課題番号-プロダクト名

- 課題番号：9 　pythonとライブラリを活用した経営管理アプリの続き

## ②課題内容（どんな作品か）

この課題はPythonで作成しており、PHPとPythonの連携は分からなかったので、データベース操作にはsqlite3を使っています。
今回は前回の課題にユーザー登録機能、ログイン機能、DB編集及び削除（sales_management.pyの売上管理のところ）を加えています。

データベースの設計はdatabase.pyファイルをご覧ください。
コンセプトは売上管理、原価管理、販管費管理、利益管理、資金管理の各ページで数値データをグラフ反映するなど、経営データを効果的に管理・可視化するためのダッシュボードを想定したものです。
課題提出にあたり、以下の機能を備えています：

【課題提出上、必須の機能】

・ユーザー登録機能とログイン機能の設定　⇨　dashboard.pyファイルで設定。def関数を使って設定。
・ユーザー登録機能とログイン機能の表示　⇨　同上
def login_page():
    st.title("ログイン")
⇨login_pageという名前の関数を定義して、呼び出すことでログインページのUIを表示します。

・DB登録項目の削除と編集機能　⇨ ・tags_and_target.py ファイルとsales_management.pyファイルで設定。


その他
・データの登録・参照　⇨　sqlite3をdatabase.pyでインポートしてます。このことで、売上管理等で入力したデータが、データベースに登録・参照されます。
・データのSQLファイルエクスポート機能　⇨ SQLファイルの提出が必須とのことで、ダウンロードする機能を設けました。ダウンロードすると、現在蓄積されたDB内容が確認はできます。この点についてはコードレビュー会で説明いたします。
・データベースの内容はdashboard_data.dbに蓄積するのですが、内容が文字として確認できないです。SQLファイルを見る限りは、入力内容は蓄積されているので登録と参照はされている様子です。

※今回データベースの登録と参照は左メニューの売上管理で実装してます。参照ファイルはsales_management.pyです。売上管理のページのうち、売上データの項目でデータベースの登録と参照を反映してます。

- deployはstreamlit Cloudから行いました。
streamlit Cloud : https://streamlit.io/generative-ai

## ③DEMO


## ④作ったアプリケーション用のIDまたはPasswordがある場合

なし

## ⑤工夫した点・こだわった点
・関数の定義は


## ⑥難しかった点・次回トライしたいこと(又は機能)

・グラフの PowerPoint エクスポートの実装が今回うまくいきませんでした。altanaという使ったことのないライブラリを使ってみたところ、環境構築に不備があって動作しなかったためです。次回は違うライブラリを使おうと思います。
・デプロイ時のエラーが頻発しました。requirements.txtの記載ミスでした。これは、StreamlitCloudにdeployする時の独特のルールです。
・卒業制作のデプロイを考えて、今回はFlaskのフレームワークを使って制作を進めていましたが、学習が間に合いませんでした。よって、フレームワークは前回と同じStreamlitで、サーバーもStreamlitCloudを使いました。Pythonはさくらサーバーでdeployするとファイルが非表示になってしまうため、Pythonと相性の良い環境を模索中です。


## ⑦質問・疑問・感想、シェアしたいこと等なんでも

❶条件分岐
if st.button("ログイン", key="login_button"):
    user = Database.fetch_data(
        "SELECT * FROM users WHERE username = ? AND password = ?", (username, password)
    )
    if user:
        st.success("ログイン成功！")

if文で条件を指定するだけで簡単に分岐処理を実現して、
英語を読むような感覚で「もしボタンが押されたら…」というロジックにより、ログインボタンがクリックされたときに処理を実行します

また if-elif-else構文を使って、複数の条件を処理しています。

if menu == "初期設定登録":
    tags_and_target_page()
elif menu == "売上管理":
    sales_management_page()
elif menu == "ログアウト":
    st.session_state["authenticated"] = False



❷オブジェクトの構築
Database.execute_query(
    "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
)
*Database**はクラス（オブジェクト）を設定して、execute_queryというメソッドを呼び出してSQLを実行。


def login_page():
    st.title("ログイン")
    username = st.text_input("ユーザー名", key="login_username")
    password = st.text_input("パスワード", type="password", key="login_password")
    if st.button("ログイン", key="login_button"):
        user = Database.fetch_data(
            "SELECT * FROM users WHERE username = ? AND password = ?", (username, password)
        )
        if user:
            st.success("ログイン成功！")
クラスではなくてdefキーワードを使ってオブジェクトの構築を多用してます

❸


❸（前回に引き続き）本プロジェクトでは、効率的なデータ操作と拡張性を考慮した SQLite を使用し、以下のテーブルを設計しました：

「sales（売上データ）」
案件ごとの売上情報を管理。
タグで売上データを分類し、タグ別の集計や分析を容易に。

id (主キー): 一意のIDで各データを識別。
project (案件名): 案件を識別するための名称。
tag (タグ): 売上データを分類するためのカテゴリ。
revenue (売上高): 収益データ。
date (日付): 売上が発生した日。

「target_revenue（目標売上）」

年間の目標売上高を管理。
売上データと比較して予実分析を可能に。

id (主キー): 一意のID。
amount (目標金額): 千円単位の目標売上。

「tags（タグ情報）」

分類用タグを登録。
売上データの柔軟な集計や可視化を実現。

id (主キー): 一意のID。
tag_name (タグ名): タグの名前。

「その他の管理テーブル」

原価管理（costs）、販管費管理（sg_a_costs）、利益管理（profits）、資金管理（cashflow）のためのテーブルを設計しました。
各テーブルは独立してデータを管理しながらも、売上データと連携可能してます。


❹（前回に引き続き）Python 構文の活用
このプロジェクトでは、Pythonの豊富な構文やデザインパターンを活用して、効率的で拡張性の高いコードを構築しました。
1. クラス設計（Database クラス）
役割:
データベース操作を一元管理。
各種クエリ（登録・参照・更新・削除）の汎用メソッドを提供。
主なメソッド:
init_db(): 必要なテーブルを作成し、アプリケーション初期化時にデータベースをセットアップ。
execute_query(query, params): 動的なクエリ実行を可能にするメソッド。
fetch_data(query, params): データ取得用の汎用メソッド。

2. 繰り返し処理（FOR文の活用）
売上データの表示・操作を効率化するため、 FOR文 を活用。

各データ行に対して修正ボタンや削除ボタンを動的に生成する仕組みを実装。

3. DICT関数の活用
データ操作やグラフ生成で、 DICT関数 を使用して簡潔なデータ構造を実現。
グラフ用データを辞書形式で生成し、DataFrameに変換。

4. モジュール分割
各機能（売上管理、原価管理など）を独立したファイルに分割。
コードの見通しが良くなり、保守性が向上。
