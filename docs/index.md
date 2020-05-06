# RESTest

**Authors**: Kenneth Rosario, Milton Pagan, Dionel Martinez, Javier Cuebas

## Introduction

RESTful (Representational State Transfer) APIs are interfaces that provide
interoperability between computers over the Internet. It is widely used in
a variety of applications that range from simple webpages to more complex
applications like social media networks. Following a client-server model,
it allows the access and manipulation of Web resources through a set of
predefined stateless operations. For example, when using HTTP, operations
like GET, PUT, POST and DELETE are predefined. An important step in
implementing RESTful APIs is testing. This way the correctness of the APIs
operations can be assured, as well as the correctness of the layers
beneath it. To this avail, many libraries provide functionalities that
enable the making of tests for an implementation of a REST API. However,
some of these libraries can be involved and confusing, making developers
spend large amounts of time just learning how to use the library. RESTest
is a programming language created for RESTful API testing. It aims to
provide high-level functionalities that simplify test-making while having
a minimal learning curve. This way, developers can focus on making tests,
as opposed to figuring out how to make them. Many of its features follow
the functional programming model which helps reinforce the simplicity of
the language and allow it to do more with fewer lines of code.

## Motivations

The need for a simple way to test REST APIs came to be as most of our team
members were building APIs in that same semester, ICOM4036/CIIC4030 and a
Motivations tool to automate testing the RESTest was born.

## Language Features

- **Test case definitions**
  - Allow users to create tests with specified before and after procedures
- **Url definitions**
  - Implicit global url definitions
- **Header definitions**
  - Implicit global header definitions
- **Assertions:**
  - Allows verification of conditions
- **Automatic setup of connection to API**
  - Connection and data fetching under the hood
- **Automatic test execution**
  - Automatically executes a set of test cases
- **Formatted prints**
  - Native pretty print
- **Test Summaries**
  - Results after a test execution

## Code example

```
(url "http://localhost:5000/car")



(proc build_car[year]:

    define res {
        "year":"2012",
        "manufacturer":"Ford",
        "make":"Fiesta",
        "model":"S"
    }
    return res

)

before build_car("2018") (test on "/add" test1:
    define res post(before_val)
    verify res.status == 200
)

(test on "/update/{id}" test2:

    define req_car {
        "year":"2020",
        "manufacturer":"Toyota",
        "make":"Corolla",
        "model":"S"
    }


    define req post(req_car, <<"http://localhost:5000/car/add")

    verify req.status == 200

    define after_req get( id<<req.data.id ,<<"http://localhost:5000/car/{id}")

    verify after_req.status == 200

    verify after_req.data.year == req_car.year

    define new_car{
        "year":"2018",
        "make":"Tacoma"
    }

    define update_req put(new_car, id<<after_req.data.id )

    verify update_req.status == 200

    verify update_req.data.year != req_car.year

    define alls get(<<"http://localhost:5000/car/all")


)
```
