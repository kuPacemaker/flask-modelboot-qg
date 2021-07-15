import requests

def test_case(context, answer):
    BASE = "http://127.0.0.1:5000"
    query = f"answer: {answer} context: {context}"
    response = requests.get(BASE + "/qg/" + query)
    print(response.json())

test_case("Hello World!", "World")

test_case("It seems I am not the only spy.", "spy")

test_case("I have no idea.", "idea")

test_case("I still want to ask how you are doing.", "how you are doing")

test_case("I will have order!", "order")

test_case("We should look for a place to take shelter. I'll be fine, but we don't want you catching a cold.", "cold")
