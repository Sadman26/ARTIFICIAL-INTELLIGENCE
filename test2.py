import numpy as np
Input = np.array(
    [[0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])
Label = np.array(
    [
    0,
    0,
    0, 
    1]
    )
Weight = [1, 0.5]
Bias = 2.5
LearningRate = 0.1
epoch = 9
for j in range(0, epoch):
    print("Epoch: ", j)
    count = 0
    for i in range(0, Input.shape[0]):
        T = Label[i]
        instance = Input[i]
        x0 = instance[0]
        x1 = instance[1]
        net = (Weight[0]*x0)+(Weight[1]*x1)-Bias
        if net > 0:
            y = 1
        else:
            y = 0
        delta = T-y
        if delta != 0:
            Weight[0] = Weight[0]+(LearningRate*delta*x0)
            Weight[1] = Weight[1]+(LearningRate*delta*x1)
            Bias = Bias+(LearningRate*delta*(-1))
        else:
            count = count+1
        print("Calculated Value:", y, "actual value", delta)
    if count == Input.shape[0]:
        break
    print(".............")


