models = ["agent_wait_time", "zendesk_ticket_data"]

for model in models:
    try:
        print(f"Checking: {model}")
        expected = open(f"fal_output/{model}_expected", "r").read()
        current = open(f"fal_output/{model}", "r").read()
        assert expected == current
    except AssertionError:
        print("ERROR:")
        print(f"Expected: {expected}")
        print(f"Got: {current}")
        raise Exception("Did not get expected output")

print("Success!")
