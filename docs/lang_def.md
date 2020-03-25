# RESTest Language Specification

```
    {test_sequence} = {url} {header} {execution}
    | {url}{header}{execution}{test_sequence}

    {url} = LP URL STRING RP

    {header_parameters} = STRING COLON STRING
    | STRING COLON STRING COMMA {header_parameters}

    {header} = LP HEADER LB {header_parameters} RB RP

    {execution} = {test}
    | {procedure}
    | {test} {execution}
    | {procedure} {execution}

    /* TEST */

    {test} = BEFORE {procedure_call} LP TEST IDENTIFIER COLON SEPARATOR {expression} RP AFTER {procedure_call}
    | BEFORE {procedure_call} LP TEST IDENTIFIER COLON SEPARATOR {expression} RP
    | LP TEST IDENTIFIER COLON SEPARATOR {expression} RP AFTER {procedure_call}
    | BEFORE {procedure_call} LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP AFTER {procedure_call}
    | BEFORE {procedure_call} LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP
    | LP TEST ON STRING IDENTIFIER COLON SEPARATOR {expression} RP AFTER {procedure_call}

    /* PROCEDURE */

    {procedure} = LP PROC LB {procedure_parameters} RB COLON SEPARATOR {expression}

    {procedure_parameters} = IDENTIFIER
    | IDENTIFIER COMMA {procedure_parameters}

    {procedure_call} = IDENTIFIER LP {parameters} RP
    | IDENTIFIER LP RP

    {parameters} = STRING
    | NUMBER
    | STRING COMMA {parameters}
    | NUMBER COMMA {parameters}

    /* EXPRESSION */
    {expression} = {line} | {line} {expression}

    {line} = {instruction} | {definition}

    {instruction} = {procedure} 
    | {verify} 
    | {get} 
    | {post} 
    | {put} 
    | {delete}

    {definition} = DEFINE IDENTIFIER STRING 
    | DEFINE IDENTIFIER NUMBER
    | DEFINE IDENTIFIER IDENTIFIER

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
    
    
    {object} = IDENTIFIER 
    | IDENTIFIER DOT {object}

```
