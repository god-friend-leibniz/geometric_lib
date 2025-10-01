# Geometric_lib Documentation

> [!NOTE]
> In code examples we'll manually specify data types
> for all variables to achieve clear understanding

## Supported shapes

- [Circle](#circle)
- [Square](#square)
- [Rectangle](#rectangle)

### Circle

#### Perimeter

##### Signature

```Python
def circle_perimeter(
    radius: float
) -> float:
```

##### Example

To calculate perimeter of a circle with radius 3.7, we call

```Python
cp: float = circle_perimeter(3.7)
```

#### Area

##### Signature

```Python
def circle_area(
    radius: float
) -> float:
```

##### Example

To calculate area of a circle with radius 3.7, we call

```Python
ca: float = circle_area(3.7)
```

### Square

#### Perimeter

##### Signature

```Python
def square_perimeter(
    length: float
) -> float:
```

##### Example

To calculate perimeter of a square with size 3.7, we call

```Python
sp: float = square_perimeter(3.7)
```

#### Area

##### Signature

```Python
def square_area(
    length: float
) -> float:
```

##### Example

To calculate area of a square with size 3.7, we call

```Python
sa: float = square_area(4.2, 3.7)
```

### Rectangle

#### Perimeter

##### Signature

```Python
def rectangle_perimeter(
    length: float,
    width: float
) -> float:
```

##### Example

To calculate perimeter of a rectangle with size 4.2 by 3.7, we call

```Python
rp: float = rectangle_perimeter(4.2, 3.7)
```

#### Area

##### Signature

```Python
def rectangle_area(
    length: float,
    width: float
) -> float:
```

##### Example

To calculate area of a rectangle with size 4.2 by 3.7, we call

```Python
ra: float = rectangle_area(4.2, 3.7)
```
