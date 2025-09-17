import streamlit as st
from chatbot import get_response as external_get_response

st.set_page_config(page_title="Mini ChatGPT", layout="wide")


# ---------------------------
# 1) Başlangıç / session state
# ---------------------------
def init_state():
    if "chats" not in st.session_state:
        st.session_state.chats = {}
    if "current_chat" not in st.session_state:
        st.session_state.current_chat = None
    if "chat_counter" not in st.session_state:
        st.session_state.chat_counter = 0
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""


# ---------------------------
# 2) Chat yönetimi
# ---------------------------
def new_chat(title=None):
    st.session_state.chat_counter += 1
    chat_id = f"chat_{st.session_state.chat_counter}"
    st.session_state.chats[chat_id] = {
        "title": title or f"Sohbet {st.session_state.chat_counter}",
        "messages": []
    }
    st.session_state.current_chat = chat_id
    st.rerun()  # yeni sohbet anında görünür
    return chat_id


def delete_chat(chat_id):
    if chat_id in st.session_state.chats:
        del st.session_state.chats[chat_id]
        # Eğer silinen chat seçili ise boşalt
        if st.session_state.current_chat == chat_id:
            st.session_state.current_chat = None
        st.rerun()  # sidebar ve main panel anında güncellensin


def select_chat(chat_id):
    if chat_id in st.session_state.chats:
        st.session_state.current_chat = chat_id
        st.rerun()  # mesajlar hemen görünür


def add_message(chat_id, role, text):
    chat = st.session_state.chats.get(chat_id)
    if chat:
        chat["messages"].append({"role": role, "text": text})
        st.session_state.chats[chat_id] = chat  # session_state güncelle


def call_bot(user_text):
    try:
        return external_get_response(user_text)
    except Exception as e:
        return f"[Bot cevap verirken hata oluştu: {e}]"


# ---------------------------
# 3) UI render
# ---------------------------
def render_sidebar():
    with st.sidebar:
        st.title("Sohbetler")
        if st.button("➕ Yeni Sohbet"):
            new_chat()

        st.markdown("---")
        chat_ids = list(st.session_state.chats.keys())
        for cid in chat_ids:
            chat = st.session_state.chats[cid]
            col1, col2 = st.columns([0.82, 0.18])
            with col1:
                if st.button(chat["title"], key=f"select_{cid}"):
                    select_chat(cid)
            with col2:
                if st.button("🗑", key=f"delete_{cid}"):
                    delete_chat(cid)


def render_messages(chat: dict):
    """
    Mesajları direkt st.chat_message ile gösterir.
    Kullanıcı: "user", Bot: "assistant"
    """
    for msg in chat["messages"]:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["text"])
        elif msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(msg["text"])


def render_main_panel():
    st.title("Mini Chatbot")
    if st.session_state.current_chat is None:
        st.info("Lütfen bir sohbet seçin veya yeni sohbet başlatın.")
        return

    chat = st.session_state.chats[st.session_state.current_chat]

    # 1) Mesajları göster
    render_messages(chat)

    # 2) Kullanıcı mesaj girişi (hem Enter hem buton)
    user_text = st.chat_input("Mesajınızı yazın...")

    if user_text:
        add_message(st.session_state.current_chat, "user", user_text)
        with st.spinner("Bot cevap yazıyor..."):
            bot_reply = call_bot(user_text)
        # Burada artık role "assistant"
        add_message(st.session_state.current_chat, "assistant", bot_reply)
        st.rerun()
# ---------------------------
# 4) App akışı
# ---------------------------
def main():
    init_state()
    render_sidebar()
    render_main_panel()


if __name__ == "__main__":
    main()
