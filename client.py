from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LMNP_EU8rDEfTBDKFPOT5FfTj5nIdCHuT5t-oSENIPzw")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is coding ",
)

print(response.text)