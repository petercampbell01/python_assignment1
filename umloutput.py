# Produce UML diagram using GraphViz dot

import sys

class MakeUML:
    
    def __init__(self):
        pass

    def create_class_diagram(self, modules):
        out = sys.stdout
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
                for attr in c.attributes:
                    write_row(out, attr.name)
                # Attributes End
                out.write("|")
                # Functions Start
                for func in c.functions:
                    write_row(out, func.name + "(" + "params" +")")

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
                for parent in c.super_classes:
                    line(class_name_to_dot(c.name) + " -> " +
                         class_name_to_dot(parent.__name__))

        line("}")
