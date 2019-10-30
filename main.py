from jinja2 import Template


def main():

    template = Template('Hello {{ name }}')
    template.render(name= input("Name:"))

if __name__ == "__main__":
    main()