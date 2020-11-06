# ECart
Simple implementation and design of an online cart.


# Requirements
python3


# Usecase
```shell
python3 cont.py -USD -order T-shirt Shoes Shoes T-shirt Jacket ...
```


Current active catalog and modifiers:
```python
catalog = {
    'T-shirt': 10.99,
    'Pants': 14.99,
    'Jacket': 19.99,
    'Shoes': 24.99
}

mods = {
    'Shoes': 0.1,
    'Jacket': 0.5,
    'Taxes': 1.14
}
```
