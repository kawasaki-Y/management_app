import streamlit as st
from login import login_page, account_registration_page
from sales_management import sales_management_page

def main():
    # ログイン状態をチェック
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        page = st.sidebar.radio("メニュー", ["ログイン", "アカウント登録"])
        if page == "ログイン":
            login_page()
        elif page == "アカウント登録":
            account_registration_page()
    else:
        st.sidebar.title("メニュー")
        menu = ["ホーム", "売上管理", "ログアウト"]
        choice = st.sidebar.selectbox("選択してください", menu)

        if choice == "ホーム":
            st.title(f"ようこそ, {st.session_state['username']} さん！")
        elif choice == "売上管理":
            sales_management_page()
        elif choice == "ログアウト":
            st.session_state["logged_in"] = False
            st.session_state["username"] = None
            st.experimental_rerun()

if __name__ == "__main__":
    Database.init_db()  # データベース初期化
    main()
