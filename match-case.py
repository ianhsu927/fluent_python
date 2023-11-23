"""析构嵌套元组(Python 3.10+)"""

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York City', 'US', 20.142, (40.714167, -74.005833)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f"{'':15} | {'lat.':>9} | {'long.':>9}")
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f"{name:15} | {lat:^9.4f} | {lon:^9.4f}")