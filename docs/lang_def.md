# RESTest Language Specification

```
      {test_sequence} = {url} SEPARATOR {header} SEPARATOR {execution}
    | {url} SEPARATOR {header} SEPARATOR {execution}{test_sequence}
    | {url} SEPARATOR {execution}
    | {url} SEPARATOR {execution}{test_sequence}

    {url} = LP URL STRING RP

    {header_parameters} = STRING COLON STRING
    | STRING COLON STRING COMMA {header_parameters}

    {header} = LP HEADER LB {header_parameters} RB RP

    {execution} = {test}
    | {procedure}
    | {test} SEPARATOR {execution}
    | {procedure} SEPARATOR {execution}

    /* TEST */

    {test} = {before} LP TEST IDENTIFIER COLON SEPARATOR {expression} RP {after}
    | {before} LP TEST IDENTIFIER COLON SEPARATOR {expression} RP
    | LP TEST IDENTIFIER COLON SEPARATOR {expression} RP {after}
    | {before} LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP {after}
    | {before} LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP
    | LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP {after}
    | LP TEST IDENTIFIER COLON SEPARATOR {expression} RP
    | LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP

    {before} = BEFORE {procedure_call}
    {after} = AFTER {procedure_call}

    /* PROCEDURE */

    {procedure} = LP PROC IDENTIFIER LB {procedure_parameters} RB COLON SEPARATOR {expression} RP

    {procedure_parameters} = IDENTIFIER
    | IDENTIFIER COMMA {procedure_parameters}

    {procedure_call} = IDENTIFIER LP {parameters} RP
    | IDENTIFIER LP RP

    {parameters} = STRING
    | NUMBER
    | STRING COMMA {parameters}
    | NUMBER COMMA {parameters}

    /* EXPRESSION */
    {expression} = {line}
    | {line} SEPARATOR {expression}

    {line} = {instruction}
    | {definition}

    {instruction} = {procedure_call}
    | {verify}
    | {crud}

    {definition} = DEFINE IDENTIFIER STRING
    | DEFINE IDENTIFIER NUMBER
    | DEFINE IDENTIFIER IDENTIFIER
    | DEFINE IDENTIFIER {procedure_call}
    | DEFINE IDENTIFIER {crud}

    {verify} = VERIFY {object} EQ {object}
    | VERIFY {math_expression} EQ {object}
    | VERIFY {object} EQ {math_expression}
    | VERIFY {object} EQ STRING
    | VERIFY STRING EQ {object}
    | VERIFY {math_expression} NEQ {object}
    | VERIFY {object} NEQ {math_expression}
    | VERIFY {object} NEQ STRING
    | VERIFY STRING NEQ {object}}
    | VERIFY {object} NEQ {object}
    | VERIFY {math_expression} LT {object}
    | VERIFY {object} LT {math_expression}
    | VERIFY {object} LT STRING
    | VERIFY STRING LT {object}
    | VERIFY {math_expression} GT {object}
    | VERIFY {object} GT {math_expression}
    | VERIFY {object} GT STRING
    | VERIFY STRING GT {object}
    | VERIFY {math_expression} GEQ {object}
    | VERIFY {object} GEQ {math_expression}
    | VERIFY {object} GEQ STRING
    | VERIFY STRING GEQ {object}
    | VERIFY {math_expression} LEQ {object}
    | VERIFY {object} LEQ {math_expression}
    | VERIFY {object} LEQ STRING
    | VERIFY STRING LEQ {object}

    /* OBJECT */

    {object} = IDENTIFIER
    | IDENTIFIER DOT {object}

    /* MATH */

    {math_expression} = {math_expression} PLUS {math_term}
    | {math_expression} MINUS {math_term}
    | {math_term}

    {math_term} = {math_term} MULT {math_factor}
    | {math_term} DIV {math_factor}
    | {math_factor}

    {math_factor} = NUMBER
    | LP {math_expression} RP

    /* CRUD Operations */
    {crud} =
    {get}
    | {post}
    | {put}
    | {delete}

    {get} = GET LP RP
    | GET LP {crud_body} RP
    | GET LP {crud_body} COMMA {crud_args} RP
    | GET LP {crud_args} RP

    {post} = POST LP {crud_body} RP
    | POST LP {crud_body} COMMA {crud_args} RP
    | POST LP {crud_args} RP

    {put} = PUT LP {crud_body} RP
    | PUT LP {crud_body} COMMA {crud_args} RP
    | PUT LP {crud_args} RP
    | PUT LP RP

    {delete} = DELETE LP RP
    | DELETE LP {crud_args} RP
    | DELETE LP {crud_body} RP
    | DELETE LP {crud_body} COMMA {crud_args} RP

    {crud_body} = {object}
    | STRING

    {crud_args} = {crud_args} COMMA {crud_args}
    | IDENTIFIER LT LT {object}
    | IDENTIFIER LT LT STRING
    | IDENTIFIER LT LT NUMBER

```
