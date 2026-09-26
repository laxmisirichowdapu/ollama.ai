'''import streamlit as st
import ollama 
st.title("AI Chatbot")
st.write("AI CHATBOT")
#st.sidebar.button("DROP")
text=st.text_input("Ask me anything")
if st.button("send"):
    response=ollama.chat(
        model="llama3.2",
        messages=[

            {"role":"user",
            "content":"prompt"}
        ]
    )
    st.write(response["message"]["prompt"])'''
#a=st.text_area("ASKKKK")

'''import ollama
print("i am ai chatbot with q&a")
print("type exit to terminate\n")
while True:
    question = input("you: ")
    if question.lower() == "exit":
        print("bot: goodbye")
        break
    response = ollama.chat(
        model = "llama3.2",
        messages = [
            {
            "role" : "user",
            "content" : question
            }
        ]
    )
    print("bot:",response["message"]["content"])'''

'''import ollama
print("i am ai chatbot with q&a")
print("Type exit to terminate\n")
responses=[]
while True:
    question =input("you: ")
    if question.lower() == "exit":
        print("bot: exited")
        break
    response = ollama.chat(
        model = "llama3.2",
        messages = [
            {
                "role" : "user",
                "content" : question
                }
            ]
    )
    responses.append(response)
    print("bot:",response["message"]["content"])
print(responses)'''
