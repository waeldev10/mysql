def gradient_search(start, end, learning_rate, num_iterations):
    x = start
    for _ in range(num_iterations):
        gradient = compute_gradient(x)
        x -= learning_rate * gradient
        # تحديد حدود النقطة x بين start و end
        x = max(start, min(x, end))
    return x

# مثال على استخدام الخوارزمية:
def compute_gradient(x):
    # حساب المشتقة للدالة في نقطة x
    return 2*x

start = 0
end = 10
learning_rate = 0.1
num_iterations = 100

optimal_x = gradient_search(start, end, learning_rate, num_iterations)
print("القيمة المثلى لـ x هي:", optimal_x)