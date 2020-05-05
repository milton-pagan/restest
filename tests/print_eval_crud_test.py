from util.api.base.base_instruction import BaseInstruction
from pprint import pprint


def test1():

    inst = BaseInstruction(
        base_url="http://localhost:5000/disasterStorage/products",
        header={"Content-Type": "application/json", "Accept": "*/*"},
        get_proc=None,
        name="Hola",
    )

    pprint(inst.eval_crud(("get",)))
    pprint(
        inst.eval_crud(
            (
                "post",
                (
                    "crudbody",
                    '{"product_name": "mineral water","product_description": "bottle","product_price": 0,"product_quantity": 100,"latitude": 50,"longitude": 100.5,"category": "water","category_attributes": {"water_exp_date": "2020-05-20","water_volume_ml": 500}}',
                ),
            )
        )
    )
