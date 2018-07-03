"""
y_pred = w1*x + w0
f(x) = sum( y_pred - y_true)^2 )
     = y_pred^2 - 2*y_pred*y_true + y_true^2
     = (w1*x + w0)^2 - 2*(w1*x + w0)*y_true + y_true^2
     = (w1*x)^2 + 2*w1*x*w0 + w0^2 - 2*y_true*w1*x - 2*y_true*w0 + y_true^2
f'(x) wrt w0 = 2*w1*x + 2*w0 - 2*y_true
             = 2*sum((w1*x + w0) - y_true)
             = 2 * sum(y_pred - y_true)
             = 2 * sum(error)
f'(x) wrt w1 = 2*x^2*w1 + 2*x*w0 - 2*y_true*x
             = 2 * sum(((w1*x + w0) - y_true)*x)
             = 2 * sum((y_pred - y_true)*x)
             = 2 * sum(error*x)
"""

points = [
    [0, 0], 
    [1, 0],
]

learning_rate = 0.01
w0 = 0.5
w1 = 0.5

for i in range(100):
    # Calculate
    y_pred = [w1*point[0] + w0 for point in points]
    y_true = [point[1] for point in points]
    zipped = list(zip(y_pred, y_true))
    errors = [(y[0] - y[1]) for y in zipped]
    print(zipped)
    print(errors)
    print([w1, w0])

    # Update
    # w0_new = w0 - learning_rate * gradient
    w0 = w0 - learning_rate * (2 * sum(errors))
    zipped = list(zip(errors, points))
    w1 = w1 - learning_rate * (2 * sum([error*point[0] for error, point in zipped]))