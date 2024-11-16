while True:
    python_info = dict()
    keyword = input("Add any python keyword: ")
    description = input("Describe what does it do? ")

    python_info[keyword] = description 

    for k, v in python_info.items():
        print(f"{k} :- {v}")

    n = input("Do you want to exit? ")
    if n.lower() == 'y':
        exit()