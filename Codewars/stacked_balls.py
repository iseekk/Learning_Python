def stack_height_3d(layers):
    return layers if layers < 2 else 1 + (layers-1) * (2/3)**(1/2)


print(stack_height_3d(10))
