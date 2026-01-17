

from typing import Optional


PRODUCTS = [
    {"id": 1, "name": "Aloo", "aliases": ["aalo", "aloo", "potato", "aaloo", "آلو"], "price": 80, "unit": "kilo"},
    {"id": 2, "name": "Dahi", "aliases": ["dahi", "yogurt", "yoghurt", "دہی"], "price": 200, "unit": "kilo"},
    {"id": 3, "name": "Chicken", "aliases": ["chicken", "murgi", "murghi", "چکن", "مرغی"], "price": 450, "unit": "kilo"},
    {"id": 4, "name": "Bhindi", "aliases": ["bhindi", "okra", "lady finger", "بھنڈی"], "price": 120, "unit": "kilo"},
    {"id": 5, "name": "Besan", "aliases": ["besan", "gram flour", "baysan", "بیسن"], "price": 150, "unit": "kilo"},
    {"id": 6, "name": "Tamatar", "aliases": ["tamatar", "tomato", "tamaatar", "ٹماٹر"], "price": 100, "unit": "kilo"},
    {"id": 7, "name": "Pyaz", "aliases": ["pyaz", "onion", "piaz", "پیاز"], "price": 90, "unit": "kilo"},
    {"id": 8, "name": "Anda", "aliases": ["anda", "ande", "egg", "eggs", "انڈے"], "price": 15, "unit": "piece"},
    {"id": 9, "name": "Gosht", "aliases": ["gosht", "meat", "mutton", "گوشت"], "price": 1200, "unit": "kilo"},
    {"id": 10, "name": "Chawal", "aliases": ["chawal", "rice", "چاول"], "price": 180, "unit": "kilo"},
]


def search_product(name: str) -> Optional[dict]:
    """Search product by name or alias (fuzzy matching)"""
    name_lower = name.lower().strip()
    
    # Exact match
    for product in PRODUCTS:
        if name_lower in [alias.lower() for alias in product['aliases']]:
            return product
    
    # Partial match
    for product in PRODUCTS:
        for alias in product['aliases']:
            if name_lower in alias.lower() or alias.lower() in name_lower:
                return product
    
    return None