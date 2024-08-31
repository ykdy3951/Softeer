from bs4 import BeautifulSoup
import requests
import os
import sys

args = sys.argv

if len(args) < 2:
    print("Please provide the URL")
    sys.exit()

url = args[1]

# README creator

def create_readme(url : str):

    # Get the title, solution and difficulty
    response = requests.get(url)    
    bs = BeautifulSoup(response.text, "html.parser")

    contents = bs.find("div", class_="con__header")
    
    title = contents.find("h3", class_="item-tit").text
    title = title.replace(" ", "_")

    contents_info = contents.find_all("dl", class_="item__data")[0]
    difficulty = contents_info.find("dd", class_="data__txt").text

    problem_info = list(contents.find("div", id="stDetail_tab1").find_all("div", recursive=False))[1:]

    constraint_info = problem_info[0]
    input_info = problem_info[1].find("h1").text
    output_info = problem_info[2].find("h1").text
    examples = problem_info[3:]

    readme = BeautifulSoup("", "html.parser")

    # title tag
    title_tag = readme.new_tag("h2")
    title_txt_tag = readme.new_tag("a", attrs={"href": url})
    title_txt_tag.append(title)

    title_tag.append(title_txt_tag)

    # difficulty tag
    difficulty_tag = readme.new_tag("h3")
    difficulty_tag.append(difficulty)

    # input format tag
    input_format_tag = readme.new_tag("p")
    input_format_content_tag = readme.new_tag("strong")
    input_format_content_tag.append("입력형식")
    input_format_tag.append(input_format_content_tag)

    input_format_content_tag = readme.new_tag("p")
    input_format_content_tag.append(input_info)
    input_format_tag.append(input_format_content_tag)

    # output format tag
    output_format_tag = readme.new_tag("p")
    output_format_content_tag = readme.new_tag("strong")
    output_format_content_tag.append("출력형식")
    output_format_tag.append(output_format_content_tag)

    output_format_content_tag = readme.new_tag("p")
    output_format_content_tag.append(output_info)
    output_format_tag.append(output_format_content_tag)

    # examples tag

    example_list = []

    for idx, example in enumerate(examples):
        example_tag = readme.new_tag("p")
        example_content_tag = readme.new_tag("strong", attrs={"class": "example"})
        example_content_tag.append(f"Example {idx + 1}:")
        example_tag.append(example_content_tag)
        example_tag.append("\n")

        example_content_tag = readme.new_tag("pre")
        example_content_txt = example.find_all("pre")

        example_input_tag = readme.new_tag("strong")
        example_input_tag.append("Input\n")
        example_content_tag.append(example_input_tag)
        example_content_tag.append(example_content_txt[0].text+"\n")
        
        example_output_tag = readme.new_tag("strong")
        example_output_tag.append("\nOutput\n")
        example_content_tag.append(example_output_tag)
        example_content_tag.append(example_content_txt[1].text+"\n")

        example_tag.append(example_content_tag)
        example_list.append(example_tag)

    # Constraints tag
    constraints_tag = readme.new_tag("p")
    constraints_content_tag = readme.new_tag("strong")
    constraints_content_tag.append("Constraints")
    constraints_tag.append(constraints_content_tag)

    ul_tag = readme.new_tag("ul")
    for constraint in constraint_info.find_all("p"):
        li_tag = readme.new_tag("li")
        li_tag.append(constraint)
        ul_tag.append(li_tag)

    constraints_tag.append(ul_tag)

    # Append all tags

    readme.append(title_tag)
    readme.append("\n")
    
    readme.append(difficulty_tag)
    readme.append("\n")

    nbsp_tag = readme.new_tag("br")
    readme.append(nbsp_tag)

    readme.append(input_format_tag)
    readme.append(output_format_tag)
    readme.append("\n")

    nbsp_tag = readme.new_tag("br")
    readme.append(nbsp_tag)
    
    for example in example_list:
        readme.append(example)
        readme.append("\n")
    
    nbsp_tag = readme.new_tag("br")
    readme.append(nbsp_tag)
    readme.append(constraints_tag)

    if not os.path.exists(title):
        os.makedirs(title)

    with open(f"{title}/README.md", "w") as f:
        f.write(str(readme))

    print(f"README.md created for {title}")

create_readme(url)