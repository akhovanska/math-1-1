import numpy as np


def is_equilateral_triangle(tri):
    # print(tri)
    tri_shifted = np.roll(tri, 1, axis=2)
    # print(tri_shifted)
    dis = np.sqrt(np.sum((tri - tri_shifted)**2, axis=1))
    # print(dis)
    rot90 = np.rot90(dis)
    # print(rot90)
    dis0 = np.full_like(rot90, rot90[0])
    # print(dis0)
    b = np.isclose(rot90, dis0)
    # print(b)
    res = np.all(b, axis=0)
    # print(res)
    return res


def count_equilateral_triangles(pts):
    n = pts.shape[1]
    arrays = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # print(i, j, k)
                arrays.append(
                    pts[:, np.array((i, j, k))]
                )
    triplets = np.stack(arrays)
    result = is_equilateral_triangle(triplets)
    # print(result)
    return np.sum(result)


if __name__ == "__main__":
    x = np.array([-1, 1, 0, 0])
    y = np.array([0, 0, np.sqrt(3), -np.sqrt(3)])
    points = np.vstack((x, y))
    # points = np.random.randn(2, 3)
    # print(points)
    print(count_equilateral_triangles(points))
