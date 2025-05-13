from gradio_client import Client

client = Client("Jofthomas/Chat_template_viewer")

result = client.predict(
	model_name="meta-llama/Meta-Llama-3-8B-Instruct",
	test_conversation=[
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": "Hi there!"},
        {"role": "assistant", "content": "Hello, human!"},
        {"role": "user", "content": "Can I ask a question?"}
    ],
    add_generation_prompt=False,
    cleanup_whitespace=True,
    hf_token="Hello!!",
    api_name="/apply_chat_template"
)

print(result)