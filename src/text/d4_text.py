from util.text_utils import (
    process_numbers
)

def create(dice_obj, collection, scale: tuple, offset: float):
    process_numbers(dice_obj, collection, scale, [
        ('1_', (0, 0, -offset), (180, 0, 0)),
        ('2_', (-offset, 0, 0), (0, -90, 0)),
        ('3_', (0, offset, 0),  (90, -90, -180)),
        ('4_', (0, -offset, 0), (90, -90, 0)),
        ('5_', (offset, 0, 0),  (0, 90, 0)),
        ('6_', (0, 0, offset),  (0, 0, 0))
    ])