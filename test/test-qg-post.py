import requests, json

BASE = "http://127.0.0.1:5000"

def test_case(context, answer):
    return f"answer: {answer} context: {context}"

def test_post_api(cas):
    response = requests.post(BASE + "/qg", json={"messages": cas})
    print(response.json())

def test_post_api_fails(cas):
    response = requests.post(BASE + "/qg", json={"massages": cas})
    print(response.json())


mosquito="""
A controversial plan is moving ahead to release genetically modified mosquitoes into the Florida Keys. More than 750,000 of the insects are set to be introduced there. Why? The aedes aegypti mosquito can carry dangerous diseases like the Zika virus, Dengue fever and yellow fever. Officials are looking for new ways to kill of these insects without using pesticides and genetically modified mosquitoes might be a way to do this. Only female mosquitoes bite people. The altered insects that are set to be released in Florida are male. They`ve been modified so that the female offspring they produce will die before they hatch from their eggs and grow big enough to bite people. And the company that developed these GMO mosquitoes say they`ve been very successful in controlling mosquito populations in Panama, Brazil and the Cayman Islands.
"""

genesis1="""
In the beginning God created the heavens and the earth. 2 Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. 3 And God said, “Let there be light,” and there was light. 4 God saw that the light was good, and he separated the light from the darkness. 5 God called the light “day,” and the darkness he called “night.” And there was evening, and there was morning—the first day. 6 And God said, “Let there be a vault between the waters to separate water from water.” 7 So God made the vault and separated the water under the vault from the water above it. And it was so. 8 God called the vault “sky.” And there was evening, and there was morning—the second day. 9 And God said, “Let the water under the sky be gathered to one place, and let dry ground appear.” And it was so. 10 God called the dry ground “land,” and the gathered waters he called “seas.” And God saw that it was good. 
"""

test_cases = [
    test_case("Hello World!", "World"),
    test_case("It seems I am not the only spy.", "spy"),
    test_case("I have no idea.", "idea"),
    test_case("I still want to ask how you are doing.", "how you are doing"),
    test_case("I will have order!", "order"),
    test_case("We should look for a place to take shelter. I'll be fine, but we don't want you catching a cold.", "cold"),
    test_case(mosquito, "controversial plan"),
    test_case(genesis1, "the heavens and the earth")
]

test_post_api(test_cases)
test_post_api_fails(test_cases)
