# lance
lance is a library to generate code from code.

## Usage
Let's see how we can generate code by using lance

## Java
### Class Generation
Here is a json file which is fed to lance library to generate java code
``` json
 {
   "fqcn": "com.susamn.MetaClass",
   "type": "CLASS"
 }
```

generates java code as:

``` java
package com.susamn;

public class MetaClass {

}
```
* _fqcn_ is **Fully Qualified Class Name**

Seems pretty easy right. Let's see some involved code generation which is usable. Here is the json file for that:
``` json
{
  "generate_path": "",
  "classes":[
    {
      "fqcn": "com.susamn.Meta",
      "type": "CLASS",
      "extends": {
        "fqcn": "com.susamn.Parent",
        "generic_types": ["java.lang.Integer"]
      },
      "implements": [
        {
          "fqcn": "java.io.Serializable",
          "generic_types": ["java.lang.Integer"]
        },
        {
          "fqcn": "org.apache.Logger",
          "generic_types": ["com.susamn.Root","java.lang.String"]
        }

      ],
      "annotations": [
        {
          "fqcn": "com.susamn.ClassLevelAnnotation1"
        },
        {
          "fqcn": "com.susamn.ClassLevelAnnotation2",
          "data": {
            "key1": {
             "type": "INTEGER",
             "value": 23
           }
         }
        }
      ],
      "attributes": [
        {
          "name": "logger",
          "mode": "public",
          "type": {
            "of": "CLASS",
            "fqcn": "org.slf4j.api.Logger"
          },
          "accessors": true,
          "initialized_form": {
            "form": "LoggerFactory.getLogger(RiskAssessmentController.class)",
            "imports": ["org.apache.logger.api.LoggerFactory","com.susamn.RiskAssessmentController"]
          }
        },
        {
          "name": "foo",
          "mode": "private",
          "type": {
           "of": "STRING"
          },
          "accessors": true,
          "initialized_form": {
            "form": "\"Foo_Value\"",
            "imports": []
          },
          "annotation_level": "GETTER_ANNOTATION",
          "annotations": [
           {
              "fqcn": "com.susamn.Annotation1",
              "data": {
               "key1": {
                 "type": "INTEGER",
                 "value": 23
                }
             }
           },
            {
             "fqcn": "com.susamn.Annotation2",
              "data": {
                "key1": {
                 "type": "STRING",
                  "value": "String data"
                }
             }
            }
          ]
       },
        {
          "name": "foobar",
          "mode": "private",
         "type": {
           "of": "STRING"
         },
         "accessors": true,
          "annotations": [
            {
              "fqcn": "com.susamn.Annotation3"
            },
            {
              "fqcn": "com.susamn.Annotation4",
              "data": {
               "key1": {
                  "type": "INTEGER",
                  "value": 23
                }
              }
           }
          ]
       },
        {
          "name": "bar",
          "mode": "private",
         "type": {
           "of": "LIST_STRING"
         },
         "accessors": true
       },
        {
         "name": "far",
         "mode": "private",
          "type": {
            "of":"LIST_INTEGER"
          },
         "accessors": true
        },
       {
          "name": "boo",
         "mode": "private",
          "type": {
            "of":"LIST_CLASS",
           "fqcn": "com.susamn.Custom"
          },
          "accessors": true
       },
       {
          "name": "doo",
          "mode": "private",
          "type": {
            "of":"INTEGER"
         },
         "accessors": true
       },
        {
          "name": "dar",
          "mode": "private",
         "type": {
            "of":"FLOAT"
         }
       }
     ],
      "methods": [
       {
         "name": "processRequest",
         "mode": "public",
         "type": {
           "of": "STRING"
         },
         "inputs": [
           {
              "name": "body",
              "type": {
               "of": "STRING",
               "annotations": [
                 {
                    "fqcn": "com.susamn.ResponseBody"
                  }
                ]
              }
            },
            {
              "name": "clazz",
             "type": {
               "of":"LIST_CLASS",
               "fqcn": "com.susamn.Custom2"
              }
           },
           {
             "type": {
               "of": "CLASS",
               "fqcn": "org.springframework.web.mvc.HttpEntity",
               "generic_types": ["java.lang.String"]
             }
           }
         ],
          "annotations": [
            {
              "fqcn": "com.susamn.Annotation11",
             "data": {
               "key1": {
                  "type": "INTEGER",
                  "value": 78.10
               }
              }
            },
            {
              "fqcn": "com.susamn.Annotation10",
              "data": {
                "key1": {
                 "type": "INTEGER",
                 "value": 12.19
               }
              }
            }
          ]
        },
        {
          "name": "syncRequest",
          "mode": "public",
          "type": {
            "of": "CLASS",
            "fqcn": "org.springframework.web.mvc.HttpEntity",
            "generic_types": ["GENERIC"]
          },
          "inputs": [
            {
              "name": "value",
              "type": {
                "of": "STRING",
                "annotations": [
                  {
                    "fqcn": "com.susamn.ResponseBody"
                  }
                ]
              }
            }
          ]
        },
        {
          "name": "deleteRequest",
          "mode": "public",
          "type": {
            "of": "CLASS",
            "fqcn": "org.springframework.web.mvc.HttpEntity",
            "generic_types": ["java.lang.Boolean"]
          },
          "inputs": [
            {
              "type": {
                "of": "STRING",
                "annotations": [
                  {
                    "fqcn": "com.susamn.ResponseBody"
                  }
                ]
              }
            }
          ],
          "body": {
            "form": ["Map<Integer,RiskAssessment> map = new HashMap<>();", "map.put(1, new RiskAssessment());"],
            "imports": ["java.util.Map","java.util.HashMap","com.susamn.RiskAssessment"]
          }
        }
      ]
    }
  ]
}
```

this generates java code:
``` java
package com.susamn;

import com.susamn.Annotation1;
import com.susamn.Annotation10;
import com.susamn.Annotation11;
import com.susamn.Annotation2;
import com.susamn.Annotation3;
import com.susamn.Annotation4;
import com.susamn.ClassLevelAnnotation1;
import com.susamn.ClassLevelAnnotation2;
import com.susamn.Custom;
import com.susamn.Custom2;
import com.susamn.Parent;
import com.susamn.ResponseBody;
import com.susamn.RiskAssessment;
import com.susamn.RiskAssessmentController;
import com.susamn.Root;
import java.io.Serializable;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.apache.Logger;
import org.apache.logger.api.LoggerFactory;
import org.slf4j.api.Logger;
import org.springframework.web.mvc.HttpEntity;


@ClassLevelAnnotation1
@ClassLevelAnnotation2(key1 = 23)
public class Meta extends Parent<Integer> implements Serializable<Integer>, Logger<Root,String> {

    public Logger logger = LoggerFactory.getLogger(RiskAssessmentController.class);
    private List<String> bar;
    private List<Integer> far;
    private List<Custom> boo;
    private int doo;
    private float dar;

    @Annotation1(key1 = 23)
    @Annotation2(key1 = "String data")
    private String foo = "Foo_Value";

    @Annotation3
    @Annotation4(key1 = 23)
    private String foobar;

    public Logger getLogger(){
        return this.logger;
    }
    public void setLogger(Logger logger){
        this.logger = logger;
    }
    public String getFoo(){
        return this.foo;
    }
    public void setFoo(String foo){
        this.foo = foo;
    }
    public String getFoobar(){
        return this.foobar;
    }
    public void setFoobar(String foobar){
        this.foobar = foobar;
    }
    public List<String> getBar(){
        return this.bar;
    }
    public void setBar(List<String> bar){
        this.bar = bar;
    }
    public List<Integer> getFar(){
        return this.far;
    }
    public void setFar(List<Integer> far){
        this.far = far;
    }
    public List<Custom> getBoo(){
        return this.boo;
    }
    public void setBoo(List<Custom> boo){
        this.boo = boo;
    }
    public int getDoo(){
        return this.doo;
    }
    public void setDoo(int doo){
        this.doo = doo;
    }
    @Annotation11(key1 = 78.1)
    @Annotation10(key1 = 12.19)
    public String processRequest(@ResponseBody String body, List<Custom2> clazz, HttpEntity<String> val0){
    }
    public HttpEntity<?> syncRequest(@ResponseBody String value){
    }
    public HttpEntity<Boolean> deleteRequest(@ResponseBody String val0){
        Map<Integer,RiskAssessment> map = new HashMap<>();
        map.put(1, new RiskAssessment());
    }

}
```