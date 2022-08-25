with open("Input./Letters./starting_letter.txt") as letter:
    letter_body = letter.read()

with open("Input./Names./invited_names.txt") as data_names:
    list_of_names = (data_names.read()).split("\n")

for name in list_of_names:
    file_name = f"./Output./ReadyToSend./letter_for_{name}.txt"
    body = letter_body.replace("[name]", name)
    with open(file_name, "w") as new_letter:
        new_letter.write(body)
