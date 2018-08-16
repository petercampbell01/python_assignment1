import os


class MakeUML:
    """
    Converting modules into a UML class diagram using graphviz
    Author: Braeden
    """

    def __init__(self, hide_attributes, hide_methods):
        self.hide_attributes = hide_attributes
        self.hide_methods = hide_methods

    def create_class_diagram(self, modules):
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        path = path.replace("\\", "/")

        # create tmp folder if doesn't exist
        if not os.path.exists(path + '/tmp'):
            os.makedirs(path + '/tmp')

        try:
            with open(path + '/tmp/class.dot', 'w') as out:
                # Output as UML class diagram using DOT (graphviz)
                def line(s):
                    return out.write(s + "\n")

                def class_name_to_dot(name):
                    return name

                # creates row in table with method name
                def write_row(out, method):
                    out.write(method + "\l")

                # styles class table and items for output
                out.write(
                    """
                    digraph G {
                        rankdir=BT
                        node [
                            fontname = "Sans Not-Rotated 8"
                            fontsize = 8
                            shape = "record"
                        ]
                        edge [
                            fontname = "Sans Not-Rotated 8"
                            fontsize = 8
                        ]
                    """
                )

                for (name, module) in modules.items():
                    if len(module) > 1:
                        line("subgraph {")

                    for c in module:
                        line(class_name_to_dot(c.name) + " [")

                        # Class Title
                        out.write("label = \"{" + c.name)

                        out.write("|")

                        # Attributes Start
                        if not self.hide_attributes:
                            for attr in c.attributes:
                                write_row(out, attr.visibility + " " + attr.name)
                        # Attributes End
                        out.write("|")
                        # Functions Start
                        if not self.hide_methods:
                            for func in c.functions:
                                write_row(out, func.visibility + " " + func.name + "(" + func.get_parameters() +")")

                        # Functions End

                        out.write("}\"\n")

                        line("]")

                    if len(module) > 1:
                        line("}")

                out.write("""
                    edge [
                        arrowhead = "empty"
                    ]
                """)

                # draws lines between class boxes
                for module in modules.values():
                    for c in module:
                        if c.super_classes != None:
                            for parent in c.super_classes:
                                line(class_name_to_dot(c.name) + " -> " +
                                    class_name_to_dot(parent.__name__))

                line("}")

                return True
        except OSError:
            print("tmp folder failed to exist, if it has not automatically "
                  "been created in project directory then please create")
            return False
