from OpenAI import OpenAI

def call_openai_api(prompt, model="gpt-3.5-turbo"):
    try:
        client = OpenAI()._client  # Access the OpenAI client instance directly
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response.choices[0].message.content
        print(f"OpenAI Response: {response_text}")
        return response_text
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None


call_openai_api("Hello World")