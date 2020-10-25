import unittest

from generators.java import TYPE_INTEGER, TYPE_FLOAT, TYPE_STRING, TYPE_EVALUATED
from generators.java.annotations import Annotation


class TestAnnotations(unittest.TestCase):

    def test_simple_annotation(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1"
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)

    def test_annotation_with_data_primitive_int(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": TYPE_INTEGER,
                    "value": 23
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)

    def test_annotation_with_data_primitive_float(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": TYPE_FLOAT,
                    "value": 23.90
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)

    def test_annotation_with_data_string(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": TYPE_STRING,
                    "value": "Some data"
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)

    def test_annotation_with_data_evaluated(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": TYPE_EVALUATED,
                    "value": "RequestConstants.HTTP_CODE",
                    "imports": ["org.spring.RequestConstants"]
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)



    def test_annotation_with_data_class(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "CLASS",
                    "value": "com.susamn.SomeClass",
                    "imports":["com.susamn.SomeClass"]
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)

    def test_annotation_with_data_annotation(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "ANNOTATION",
                    "value": {
                        "fqcn": "com.susamn.Annotation1",
                        "data": {
                            "key12": {
                                "type": "INTEGER",
                                "value": 23
                            }
                        }
                    }
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)


    def test_annotation_with_data_nested_annotation(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "ANNOTATION",
                    "value": {
                        "fqcn": "com.susamn.Annotation1",
                        "data": {
                            "key11": {
                                "type": "ANNOTATION",
                                "value": {
                                    "fqcn": "com.susamn.Annotation2",
                                    "data": {
                                        "key111": {
                                            "type": "INTEGER",
                                            "value": 23
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)


    def test_annotation_with_data_list_annotation(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "LIST_ANNOTATION",
                    "value": [
                        {
                            "fqcn": "com.susamn.Annotation1",
                            "data": {
                                "key1": {
                                    "type": "FLOAT",
                                    "value": 23.20
                                },
                                "key2":{
                                    "type": "CLASS",
                                    "value": "com.susamn.Comcast",
                                    "imports":["com.susamn.Comcast"]
                                }
                            }
                        },
                        {
                            "fqcn": "com.susamn.Annotation2",
                            "data": {
                                "key1": {
                                    "type": "INTEGER",
                                    "value": 67
                                }
                            }
                        }
                    ]
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)



    def test_annotation_with_data_list_primitive(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "LIST_INTEGER",
                    "value": [12, 23, 34]
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)



    def test_annotation_with_data_list_class(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "LIST_CLASS",
                    "value": ["com.susamn.Comcast","com.susamn.SomeClass"],
                    "imports": ["com.susamn.Comcast","com.susamn.SomeClass"]
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)


    def test_annotation_with_data_list_string(self):
        doc = {
            "fqcn": "com.susamn.ClassLevelAnnotation1",
            "data": {
                "key1": {
                    "type": "LIST_STRING",
                    "value": ["some string 1","some string 2"]
                }
            }
        }
        m = Annotation(doc)
        print(m.get_imports())
        g = m.generate(4)
        print(g)



if __name__ == '__main__':
    unittest.main()
