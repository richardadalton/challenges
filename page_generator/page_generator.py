from pages import page_definitions

for file_name, page_config in page_definitions.items():
    with open(page_config["template"], "r") as input_file:
        html_code = input_file.read()
    
    for k, v in page_config["tags"].items():
        html_code = html_code.replace(k, v)  

    with open(file_name, "w") as output_file:
        output_file.write(html_code)


