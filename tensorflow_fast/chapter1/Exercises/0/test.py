import tensorflow as tf
import numpy as np
from tensorflow import keras


# Dense定义一层相连的神经元  里面只有一个单个神经元 
model=keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
# 优化函数sgd（随机梯度下降） 损失函数mean_squared_error（均方误差）
model.compile(optimizer="sgd",loss="mean_squared_error")

# 训练集的输入和输出
xs=np.array([-1.0,0.0,1.0,2.0,3.0,4.0],dtype=float)
ys=np.array([-3.0,-1.0,1.0,3.0,5.0,7.0],dtype=float)

# 训练数据在fit函数中进行训练
model.fit(xs,ys,epochs=500)
# 根据已经训练好的模型 进行相应的测试
print(model.predict([10.0]))
