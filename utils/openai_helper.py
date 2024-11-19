from openai import OpenAI
# from models.json_schema import GeneratedJSON
import os

api_key = os.getenv("OPENAI_API_KEY")
# def query_openai(prompt: str) -> str:
#     """Query the OpenAI API with a prompt and return the response."""
#     openai.api_key = 
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=1000
#     )
#     return response.choices[0].text.strip()
# def query_openai(prompt: str) -> str:
#     api_key =
#     client = OpenAI(
#         api_key=api_key,  # This is the default and can be omitted
#     )
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#          ],
#         model="gpt-4o-mini",
#         response_format=GeneratedJSON,
#     )
#     print(chat_completion.choices[0].message.content.strip())
#     return chat_completion.choices[0].message.content.strip()
# def query_openai(prompt: str) -> str:
#     api_key = 
#     client = OpenAI(
#         api_key=api_key,  # This is the default and can be omitted
#     )
#     chat_completion = client.beta.chat.completions.parse(
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#          ],
#         model="gpt-4o-mini",
#         response_format=GeneratedJSON,
#     )
#     print(chat_completion.choices[0].message.content.strip())
#     return chat_completion.choices[0].message.content.strip()
def query_openai(prompt: str, response_format=None):
    client = OpenAI(
        api_key=api_key,  # This is the default and can be omitted
    )
    
    if response_format is None:
        response_format = "text"  
    print('kkk',response_format);  
    chat_completion = client.beta.chat.completions.parse(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
         ],
        model="gpt-4o-mini",
        response_format=response_format,
    )
    print(chat_completion.choices[0].message.content.strip())
    return chat_completion.choices[0].message.parsed
