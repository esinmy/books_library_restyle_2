from jinja2 import Environment, FileSystemLoader, select_autoescape
from json import load
from math import ceil
import argparse
import os
from livereload import Server
from environs import Env

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 10000
DEFAULT_JSON_PATH = "books.json"


def create_parser():
    parser = argparse.ArgumentParser(description="""This app allows you to run offline library""")
    parser.add_argument("-J", "--json_path",
                        help="provide a path to .json file with information about library")
    parser.add_argument("-H", "--host",
                        help="provide a host")
    parser.add_argument("-P", "--port", type=int,
                        help="provide a port")

    return parser


def on_reload(books, template_link, index_link):
    """Re-render pages if changes applied to template.

    Args:
        books (dict): info about books, such as title, author, etc.
        template_link (str): link to template.html.
        index_link (str): link to index{}.html blueprint.

    Returns:
        None

    """
    template = env.get_template(template_link)
    books_per_page = 20
    total_pages = ceil(len(books) / books_per_page)
    for cur_page, cur_book in enumerate(range(0, len(books), books_per_page), 1):
        rendered_page = template.render(total_pages=total_pages,
                                        cur_page=cur_page,
                                        books=books[cur_book:cur_book + books_per_page])
        if cur_page == 1:
            write_render("", rendered_page, index_link)
        write_render(cur_page, rendered_page, index_link)


def write_render(page_number, render, index_link):
    index_path = os.path.join("pages", index_link.format(page_number))
    with open(index_path, 'w', encoding="utf8") as file:
        file.write(render)


if __name__ == '__main__':
    template_link = "template.html"
    index_link = "index{}.html"

    env_vars = Env()
    env_vars.read_env()

    parser = create_parser()
    namespace = parser.parse_args()
    host = env_vars("HOST", DEFAULT_HOST) if namespace.host is None else namespace.host
    port = env_vars.int("PORT", DEFAULT_PORT) if namespace.port is None else namespace.port
    books_path = env_vars("JSON_FILE", DEFAULT_JSON_PATH) if namespace.json_path is None else namespace.json_path

    with open(books_path, "r", encoding="utf-8") as file:
        books = load(file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    server = Server()
    server.watch(template_link, lambda: on_reload(books, template_link, index_link))
    server.serve(root='.', host=host, port=port)
