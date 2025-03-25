from jinja2 import Environment, FileSystemLoader
from president import President

env = Environment(
    loader = FileSystemLoader(searchpath="templates")
)

list_template = env.get_template("president_list.html")
detail_template = env.get_template("president_detail.html")

presidents = [President(i) for i in range(1, 47)]  # get list of presidents

president_list = list_template.render(title="PRESIDENT LIST", presidents=presidents)
print(president_list)
print('-' * 60)

president_details = detail_template.render(title="PRESIDENT DETAILS:", presidents=presidents)
print(president_details)
