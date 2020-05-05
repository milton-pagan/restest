# RESTest Programming Language for testing restful APIs

## Authors : Milton Pagan, Dionel Martinez, Kenneth J. Rosario, Javier Cuebas

Github Site: https://milton-pagan.github.io/restest

* Install package:
```
git clone https://github.com/milton-pagan/restest.git
cd ./restest
pip3 install -e .
```

* Usage:
```
restest [script path]
```

* Example Program:
```
(url "http://localhost:5000/car")


(proc build_car[year]:

    define res {
        "year":year,
        "dimelo":"hola"
    }
    return res

)

before build_car("2018") (test on "/add" test1:
    define res post()
    verify res.status != 200
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
