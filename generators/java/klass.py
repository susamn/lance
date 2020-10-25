from generators.java import Generator, class_name_from_package, package_name_from_package
from generators.java.annotations import parse_annotations
from generators.java.attribute import Attribute
from generators.java.method import Method
from generators.java.typs import handle_generic_types


class Klass(Generator):
    def __init__(self, document, folder=None):
        fqcn = document.get("fqcn")
        if fqcn:
            self.class_name = class_name_from_package(fqcn)
            self.package = package_name_from_package(fqcn)
        else:
            raise ValueError("A class must have a fqcn")
        self.imports = set()
        self.attributes = []
        self.methods = []
        self.generate_folder = folder

        # Process inheritance
        extends = document.get("extends")
        self.extends = None
        if extends:
            try:
                extends_class_name = extends.get("fqcn")
                extends_generic_types = extends.get("generic_types")
                if not extends_class_name:
                    raise ValueError("The extends classname is not provided")
                extends_fqcn, imports = handle_generic_types(extends_class_name, extends_generic_types)
                self.extends = extends_fqcn
                self.imports.update(imports)
            except ValueError:
                raise ValueError("Please provide inheritance class and its fqcn")

        # Process class level implementations
        implements = document.get("implements")
        self.implements = None
        if implements and not type(implements) == list:
            raise ValueError("Please provide implementation data properly")
        if implements:
            if len(implements) > 0:
                all_implementation_classes = []
                for i in implements:
                    implements_fqcn_class_name = i.get("fqcn")
                    implements_generic_types = i.get("generic_types")
                    implements_fqcn, imports = handle_generic_types(implements_fqcn_class_name,
                                                                    implements_generic_types)

                    all_implementation_classes.append(implements_fqcn)
                    self.imports.update(imports)
                self.implements = ", ".join(all_implementation_classes)

        # Process class level annotations
        annotations = document.get("annotations")
        self.annotations = parse_annotations(annotations)
        if self.annotations and len(self.annotations) > 0:
            for a in self.annotations:
                if a and a.get_imports() and len(a.get_imports()) > 0:
                    self.imports.update(a.get_imports())

        # Attributes
        attributes = document.get("attributes")
        if attributes:
            for a_doc in attributes:
                attribute = Attribute(a_doc)
                self.add_attribute(attribute)

        # Methods
        methods = document.get("methods")
        if methods:
            for m_doc in methods:
                method = Method(m_doc)
                self.add_method(method)

    def add_method(self, method):
        self.methods.append(method)
        if len(method.get_imports()) > 0:
            self.imports.update(method.get_imports())

    def add_attribute(self, attribute):
        self.attributes.append(attribute)
        if len(attribute.get_imports()) > 0:
            self.imports.update(attribute.get_imports())
        if len(attribute.get_methods()) > 0:
            self.methods.extend(attribute.get_methods())

    def generate(self, indentation=4):
        template = f"public class {self.class_name}"
        if self.extends:
            template = f"{template} extends {self.extends}"
        if self.implements:
            template = f"{template} implements {self.implements}"
        generated = ""
        generated += f'package {self.package};'
        generated += "\n\n"
        self.imports = sorted(self.imports)
        for i in self.imports:
            generated += f'import {i};\n'
        generated += "\n\n"
        if len(self.annotations) > 0:
            generated += "\n".join([x.generate() for x in self.annotations])
        generated += f"\n{template} {{"
        generated += "\n\n"
        self.attributes = sorted(self.attributes)
        for att in self.attributes:
            generated += att.generate(indentation=indentation)
            generated += "\n"
        generated += "\n"
        for meth in self.methods:
            generated += meth.generate(indentation=indentation)
            generated += "\n"
        generated += "\n"
        generated += f"}}"

        if self.generate_folder:
            with open("/".join([self.generate_folder, f'{self.class_name}.java']), "w") as fh:
                fh.write(generated)
                fh.flush()
            print(f'Written java class {self.generate_folder}/{self.class_name}.java')
        else:
            print(generated)