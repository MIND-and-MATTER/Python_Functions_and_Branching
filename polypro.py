# Compute a polynomial via a product.

def poly(x, roots):
    poly = 1
    for r in roots:
        poly *= (x - r)

    return poly