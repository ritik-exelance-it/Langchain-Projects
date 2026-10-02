from agent import createAgent
from openrouter.errors import PaymentRequiredResponseError
import streamlit as st


if "agent" not in st.session_state:
    st.session_state.agent = createAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []


st.subheader("AI Task Manager")

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]

    st.chat_message(role).markdown(content)


query = st.chat_input("Manage your task ...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    try:
        res = st.session_state.agent.invoke(
            {"messages": [{"role": "user", "content": query}]},
            {"configurable": {"thread_id": "1"}},
        )
    except PaymentRequiredResponseError:
        st.error(
            "OpenRouter doesn't have enough available credits for this request. "
            "Reduce the model's token limit or add credits to your OpenRouter account."
        )
    else:
        answer = res["messages"][-1].content
        st.session_state.messages.append({"role": "ai", "content": answer})
        st.chat_message("ai").markdown(answer)