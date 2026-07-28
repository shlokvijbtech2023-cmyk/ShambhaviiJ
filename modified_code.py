

# Import necessary libraries
# BY Shambhavii Jaiswal 23070521133
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
     

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
print("Train and Test datasets loaded successfully.")
print("Train data head:")
display(train.head())
print("\nTest data head:")
display(test.head())
     
Train and Test datasets loaded successfully.
Train data head:
Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	PoolArea	PoolQC	Fence	MiscFeature	MiscVal	MoSold	YrSold	SaleType	SaleCondition	SalePrice
0	1	60	RL	65.0	8450	Pave	NaN	Reg	Lvl	AllPub	...	0	NaN	NaN	NaN	0	2	2008	WD	Normal	208500
1	2	20	RL	80.0	9600	Pave	NaN	Reg	Lvl	AllPub	...	0	NaN	NaN	NaN	0	5	2007	WD	Normal	181500
2	3	60	RL	68.0	11250	Pave	NaN	IR1	Lvl	AllPub	...	0	NaN	NaN	NaN	0	9	2008	WD	Normal	223500
3	4	70	RL	60.0	9550	Pave	NaN	IR1	Lvl	AllPub	...	0	NaN	NaN	NaN	0	2	2006	WD	Abnorml	140000
4	5	60	RL	84.0	14260	Pave	NaN	IR1	Lvl	AllPub	...	0	NaN	NaN	NaN	0	12	2008	WD	Normal	250000
5 rows × 81 columns

Test data head:
Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	ScreenPorch	PoolArea	PoolQC	Fence	MiscFeature	MiscVal	MoSold	YrSold	SaleType	SaleCondition
0	1461	20	RH	80.0	11622	Pave	NaN	Reg	Lvl	AllPub	...	120	0	NaN	MnPrv	NaN	0	6	2010	WD	Normal
1	1462	20	RL	81.0	14267	Pave	NaN	IR1	Lvl	AllPub	...	0	0	NaN	NaN	Gar2	12500	6	2010	WD	Normal
2	1463	60	RL	74.0	13830	Pave	NaN	IR1	Lvl	AllPub	...	0	0	NaN	MnPrv	NaN	0	3	2010	WD	Normal
3	1464	60	RL	78.0	9978	Pave	NaN	IR1	Lvl	AllPub	...	0	0	NaN	NaN	NaN	0	6	2010	WD	Normal
4	1465	120	RL	43.0	5005	Pave	NaN	IR1	HLS	AllPub	...	144	0	NaN	NaN	NaN	0	1	2010	WD	Normal
5 rows × 80 columns


import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

train.info()
train.describe()
train.isnull().sum()
train.dtypes
X = train.drop("SalePrice", axis=1)
y = train["SalePrice"]
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns

num_imputer = SimpleImputer(strategy="median")
X[num_cols] = num_imputer.fit_transform(X[num_cols])

cat_imputer = SimpleImputer(strategy="most_frequent")
X[cat_cols] = cat_imputer.fit_transform(X[cat_cols])
X = pd.get_dummies(X, drop_first=True)

scaler = StandardScaler()

X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)
     
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1460 entries, 0 to 1459
Data columns (total 81 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             1460 non-null   int64  
 1   MSSubClass     1460 non-null   int64  
 2   MSZoning       1460 non-null   object 
 3   LotFrontage    1201 non-null   float64
 4   LotArea        1460 non-null   int64  
 5   Street         1460 non-null   object 
 6   Alley          91 non-null     object 
 7   LotShape       1460 non-null   object 
 8   LandContour    1460 non-null   object 
 9   Utilities      1460 non-null   object 
 10  LotConfig      1460 non-null   object 
 11  LandSlope      1460 non-null   object 
 12  Neighborhood   1460 non-null   object 
 13  Condition1     1460 non-null   object 
 14  Condition2     1460 non-null   object 
 15  BldgType       1460 non-null   object 
 16  HouseStyle     1460 non-null   object 
 17  OverallQual    1460 non-null   int64  
 18  OverallCond    1460 non-null   int64  
 19  YearBuilt      1460 non-null   int64  
 20  YearRemodAdd   1460 non-null   int64  
 21  RoofStyle      1460 non-null   object 
 22  RoofMatl       1460 non-null   object 
 23  Exterior1st    1460 non-null   object 
 24  Exterior2nd    1460 non-null   object 
 25  MasVnrType     588 non-null    object 
 26  MasVnrArea     1452 non-null   float64
 27  ExterQual      1460 non-null   object 
 28  ExterCond      1460 non-null   object 
 29  Foundation     1460 non-null   object 
 30  BsmtQual       1423 non-null   object 
 31  BsmtCond       1423 non-null   object 
 32  BsmtExposure   1422 non-null   object 
 33  BsmtFinType1   1423 non-null   object 
 34  BsmtFinSF1     1460 non-null   int64  
 35  BsmtFinType2   1422 non-null   object 
 36  BsmtFinSF2     1460 non-null   int64  
 37  BsmtUnfSF      1460 non-null   int64  
 38  TotalBsmtSF    1460 non-null   int64  
 39  Heating        1460 non-null   object 
 40  HeatingQC      1460 non-null   object 
 41  CentralAir     1460 non-null   object 
 42  Electrical     1459 non-null   object 
 43  1stFlrSF       1460 non-null   int64  
 44  2ndFlrSF       1460 non-null   int64  
 45  LowQualFinSF   1460 non-null   int64  
 46  GrLivArea      1460 non-null   int64  
 47  BsmtFullBath   1460 non-null   int64  
 48  BsmtHalfBath   1460 non-null   int64  
 49  FullBath       1460 non-null   int64  
 50  HalfBath       1460 non-null   int64  
 51  BedroomAbvGr   1460 non-null   int64  
 52  KitchenAbvGr   1460 non-null   int64  
 53  KitchenQual    1460 non-null   object 
 54  TotRmsAbvGrd   1460 non-null   int64  
 55  Functional     1460 non-null   object 
 56  Fireplaces     1460 non-null   int64  
 57  FireplaceQu    770 non-null    object 
 58  GarageType     1379 non-null   object 
 59  GarageYrBlt    1379 non-null   float64
 60  GarageFinish   1379 non-null   object 
 61  GarageCars     1460 non-null   int64  
 62  GarageArea     1460 non-null   int64  
 63  GarageQual     1379 non-null   object 
 64  GarageCond     1379 non-null   object 
 65  PavedDrive     1460 non-null   object 
 66  WoodDeckSF     1460 non-null   int64  
 67  OpenPorchSF    1460 non-null   int64  
 68  EnclosedPorch  1460 non-null   int64  
 69  3SsnPorch      1460 non-null   int64  
 70  ScreenPorch    1460 non-null   int64  
 71  PoolArea       1460 non-null   int64  
 72  PoolQC         7 non-null      object 
 73  Fence          281 non-null    object 
 74  MiscFeature    54 non-null     object 
 75  MiscVal        1460 non-null   int64  
 76  MoSold         1460 non-null   int64  
 77  YrSold         1460 non-null   int64  
 78  SaleType       1460 non-null   object 
 79  SaleCondition  1460 non-null   object 
 80  SalePrice      1460 non-null   int64  
dtypes: float64(3), int64(35), object(43)
memory usage: 924.0+ KB
(1168, 245)
(292, 245)
(1168,)
(292,)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()

model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))

model.add(Dense(64, activation='relu'))

model.add(Dense(32, activation='relu'))

model.add(Dense(1))
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)
model.summary()
     
/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/dense.py:106: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Model: "sequential_2"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ dense (Dense)                   │ (None, 128)            │        31,488 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 64)             │         8,256 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 1)              │            33 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 41,857 (163.50 KB)
 Trainable params: 41,857 (163.50 KB)
 Non-trainable params: 0 (0.00 B)

history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)
     
Epoch 1/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 1s 6ms/step - loss: 39145172992.0000 - mae: 181522.0625 - val_loss: 37836824576.0000 - val_mae: 181089.0938
Epoch 2/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 39126249472.0000 - mae: 181480.3438 - val_loss: 37793116160.0000 - val_mae: 180993.5000
Epoch 3/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 39000756224.0000 - mae: 181222.7188 - val_loss: 37549215744.0000 - val_mae: 180480.1719
Epoch 4/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 38486974464.0000 - mae: 180166.9219 - val_loss: 36716097536.0000 - val_mae: 178713.8125
Epoch 5/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 36963323904.0000 - mae: 177016.2812 - val_loss: 34595856384.0000 - val_mae: 174075.2969
Epoch 6/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 33621860352.0000 - mae: 169696.7344 - val_loss: 30367961088.0000 - val_mae: 164130.5469
Epoch 7/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 27770720256.0000 - mae: 155248.5312 - val_loss: 23983271936.0000 - val_mae: 146695.1250
Epoch 8/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 20168163328.0000 - mae: 132921.2500 - val_loss: 17036204032.0000 - val_mae: 121556.9688
Epoch 9/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 13408751616.0000 - mae: 104601.7812 - val_loss: 12171619328.0000 - val_mae: 95773.7656
Epoch 10/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 9760610304.0000 - mae: 84294.7734 - val_loss: 10134328320.0000 - val_mae: 85466.3281
Epoch 11/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 8152474112.0000 - mae: 76476.2422 - val_loss: 8974942208.0000 - val_mae: 80148.7891
Epoch 12/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 6951249408.0000 - mae: 69803.2734 - val_loss: 7907485184.0000 - val_mae: 74550.8906
Epoch 13/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 5886500864.0000 - mae: 63167.0625 - val_loss: 6929044992.0000 - val_mae: 68702.2656
Epoch 14/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 4947681792.0000 - mae: 56586.9062 - val_loss: 6088010240.0000 - val_mae: 62979.2461
Epoch 15/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 4156195328.0000 - mae: 50783.0586 - val_loss: 5361650688.0000 - val_mae: 57560.1523
Epoch 16/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 3519704320.0000 - mae: 45676.8477 - val_loss: 4779057664.0000 - val_mae: 52824.7656
Epoch 17/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 3032230400.0000 - mae: 41390.2930 - val_loss: 4349404672.0000 - val_mae: 48945.2344
Epoch 18/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2695108352.0000 - mae: 38262.7266 - val_loss: 4018061056.0000 - val_mae: 46112.4180
Epoch 19/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2437458688.0000 - mae: 36027.6328 - val_loss: 3775169024.0000 - val_mae: 44131.1211
Epoch 20/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2242836224.0000 - mae: 34322.7344 - val_loss: 3594416384.0000 - val_mae: 42530.0625
Epoch 21/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2104946176.0000 - mae: 33128.2539 - val_loss: 3462572800.0000 - val_mae: 41445.9062
Epoch 22/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1982301696.0000 - mae: 32089.4531 - val_loss: 3349223680.0000 - val_mae: 40501.0938
Epoch 23/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1875924224.0000 - mae: 31232.3477 - val_loss: 3247447040.0000 - val_mae: 39679.8828
Epoch 24/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1785157888.0000 - mae: 30475.1465 - val_loss: 3170808064.0000 - val_mae: 39111.4258
Epoch 25/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1701843584.0000 - mae: 29724.0039 - val_loss: 3088818432.0000 - val_mae: 38477.4531
Epoch 26/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1637311616.0000 - mae: 29086.5781 - val_loss: 3011324928.0000 - val_mae: 37845.3281
Epoch 27/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1562250368.0000 - mae: 28505.5410 - val_loss: 2949380352.0000 - val_mae: 37328.2578
Epoch 28/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1504053248.0000 - mae: 27900.4727 - val_loss: 2888376320.0000 - val_mae: 36845.6445
Epoch 29/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1458509696.0000 - mae: 27271.6855 - val_loss: 2844480768.0000 - val_mae: 36370.1953
Epoch 30/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1393636096.0000 - mae: 26837.7207 - val_loss: 2784705536.0000 - val_mae: 36019.7383
Epoch 31/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1337486336.0000 - mae: 26266.9609 - val_loss: 2741365248.0000 - val_mae: 35534.0352
Epoch 32/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1295181056.0000 - mae: 25787.7832 - val_loss: 2694961152.0000 - val_mae: 35192.2461
Epoch 33/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1256195840.0000 - mae: 25319.4062 - val_loss: 2657147136.0000 - val_mae: 34814.7773
Epoch 34/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1212693888.0000 - mae: 25056.3242 - val_loss: 2614485504.0000 - val_mae: 34473.6719
Epoch 35/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1175279872.0000 - mae: 24495.4375 - val_loss: 2584679424.0000 - val_mae: 34050.2969
Epoch 36/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1135257472.0000 - mae: 24136.9922 - val_loss: 2539358720.0000 - val_mae: 33813.9141
Epoch 37/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1103269248.0000 - mae: 23787.9043 - val_loss: 2505250304.0000 - val_mae: 33547.9102
Epoch 38/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1073762304.0000 - mae: 23466.0527 - val_loss: 2474533120.0000 - val_mae: 33251.7461
Epoch 39/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1043654464.0000 - mae: 23072.0508 - val_loss: 2451757056.0000 - val_mae: 32896.4297
Epoch 40/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1016381952.0000 - mae: 22758.2031 - val_loss: 2417927168.0000 - val_mae: 32679.4316
Epoch 41/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 993062720.0000 - mae: 22463.7324 - val_loss: 2397430784.0000 - val_mae: 32521.0371
Epoch 42/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 967494272.0000 - mae: 22162.4492 - val_loss: 2380113408.0000 - val_mae: 32229.5664
Epoch 43/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 944487424.0000 - mae: 21937.2051 - val_loss: 2338738688.0000 - val_mae: 31866.4570
Epoch 44/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 923200640.0000 - mae: 21651.0078 - val_loss: 2322615808.0000 - val_mae: 31612.1387
Epoch 45/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 903083008.0000 - mae: 21379.5684 - val_loss: 2310960384.0000 - val_mae: 31504.6914
Epoch 46/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 881674944.0000 - mae: 21169.6074 - val_loss: 2294376192.0000 - val_mae: 31287.5254
Epoch 47/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 869085696.0000 - mae: 20834.5703 - val_loss: 2279196416.0000 - val_mae: 31173.9238
Epoch 48/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 846933824.0000 - mae: 20753.9824 - val_loss: 2258199040.0000 - val_mae: 30941.6230
Epoch 49/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 827443520.0000 - mae: 20385.6816 - val_loss: 2241565184.0000 - val_mae: 30675.4551
Epoch 50/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 811246272.0000 - mae: 20194.8184 - val_loss: 2231581440.0000 - val_mae: 30600.1191
Epoch 51/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 798408448.0000 - mae: 20036.4746 - val_loss: 2226757632.0000 - val_mae: 30568.3477
Epoch 52/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 782358848.0000 - mae: 19886.2578 - val_loss: 2205971456.0000 - val_mae: 30305.0977
Epoch 53/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 765880832.0000 - mae: 19613.9297 - val_loss: 2196027648.0000 - val_mae: 30182.9727
Epoch 54/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 753427264.0000 - mae: 19433.2539 - val_loss: 2179381504.0000 - val_mae: 29965.0840
Epoch 55/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 739270336.0000 - mae: 19277.3867 - val_loss: 2165537792.0000 - val_mae: 29774.7637
Epoch 56/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 726459968.0000 - mae: 19037.7832 - val_loss: 2157576704.0000 - val_mae: 29679.0664
Epoch 57/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 713231168.0000 - mae: 18878.5586 - val_loss: 2143700608.0000 - val_mae: 29508.1348
Epoch 58/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 701581760.0000 - mae: 18713.3984 - val_loss: 2130503680.0000 - val_mae: 29364.5469
Epoch 59/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 688810240.0000 - mae: 18493.0859 - val_loss: 2129252992.0000 - val_mae: 29347.3379
Epoch 60/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 680401536.0000 - mae: 18381.0488 - val_loss: 2106348288.0000 - val_mae: 29185.7129
Epoch 61/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 669914688.0000 - mae: 18248.5352 - val_loss: 2090669440.0000 - val_mae: 28966.1113
Epoch 62/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 658011904.0000 - mae: 18176.3984 - val_loss: 2087247104.0000 - val_mae: 28958.2363
Epoch 63/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 646300736.0000 - mae: 17851.1641 - val_loss: 2075246336.0000 - val_mae: 28778.6621
Epoch 64/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 635110592.0000 - mae: 17745.7910 - val_loss: 2067952256.0000 - val_mae: 28758.4785
Epoch 65/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 626345344.0000 - mae: 17697.3770 - val_loss: 2056764416.0000 - val_mae: 28577.8535
Epoch 66/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 617836480.0000 - mae: 17421.7285 - val_loss: 2051190528.0000 - val_mae: 28416.2188
Epoch 67/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 605490816.0000 - mae: 17308.1348 - val_loss: 2040667520.0000 - val_mae: 28421.5742
Epoch 68/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 600454208.0000 - mae: 17215.5605 - val_loss: 2032000384.0000 - val_mae: 28223.4805
Epoch 69/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 594719360.0000 - mae: 17066.0410 - val_loss: 2025885440.0000 - val_mae: 28348.4258
Epoch 70/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 582126656.0000 - mae: 16982.0801 - val_loss: 2021311488.0000 - val_mae: 28064.3555
Epoch 71/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 573330112.0000 - mae: 16690.1230 - val_loss: 2013352960.0000 - val_mae: 28110.6504
Epoch 72/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 565315072.0000 - mae: 16703.1523 - val_loss: 2004644480.0000 - val_mae: 27914.2266
Epoch 73/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 560576576.0000 - mae: 16475.1602 - val_loss: 1998417792.0000 - val_mae: 27911.1953
Epoch 74/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 552213184.0000 - mae: 16392.8906 - val_loss: 1993586304.0000 - val_mae: 27758.2598
Epoch 75/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 544733120.0000 - mae: 16379.8428 - val_loss: 1986456192.0000 - val_mae: 27602.9121
Epoch 76/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 540574208.0000 - mae: 16143.6221 - val_loss: 1982416896.0000 - val_mae: 27782.2793
Epoch 77/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 529259936.0000 - mae: 16000.3584 - val_loss: 1975574272.0000 - val_mae: 27630.7734
Epoch 78/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 525333440.0000 - mae: 16053.5000 - val_loss: 1970935680.0000 - val_mae: 27344.4922
Epoch 79/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 518167680.0000 - mae: 15725.4463 - val_loss: 1962956544.0000 - val_mae: 27478.0430
Epoch 80/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 509897344.0000 - mae: 15740.8711 - val_loss: 1955299328.0000 - val_mae: 27282.5176
Epoch 81/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 505642720.0000 - mae: 15691.1064 - val_loss: 1946815872.0000 - val_mae: 27127.9316
Epoch 82/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 495004832.0000 - mae: 15406.8711 - val_loss: 1943927808.0000 - val_mae: 27280.4863
Epoch 83/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 491109216.0000 - mae: 15390.3535 - val_loss: 1943413504.0000 - val_mae: 26955.4512
Epoch 84/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 482185408.0000 - mae: 15132.7764 - val_loss: 1935734912.0000 - val_mae: 27114.3652
Epoch 85/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 477357792.0000 - mae: 15098.4248 - val_loss: 1925877632.0000 - val_mae: 26879.6367
Epoch 86/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 474887264.0000 - mae: 14989.6709 - val_loss: 1923661824.0000 - val_mae: 26795.4941
Epoch 87/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 465845440.0000 - mae: 14899.0938 - val_loss: 1918339968.0000 - val_mae: 26727.9121
Epoch 88/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 461716320.0000 - mae: 14761.9004 - val_loss: 1908152704.0000 - val_mae: 26645.0391
Epoch 89/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 456508544.0000 - mae: 14635.1768 - val_loss: 1909920768.0000 - val_mae: 26674.9902
Epoch 90/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 450200384.0000 - mae: 14597.5801 - val_loss: 1907779840.0000 - val_mae: 26592.9844
Epoch 91/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 445416064.0000 - mae: 14495.2002 - val_loss: 1902902144.0000 - val_mae: 26590.6387
Epoch 92/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 439935072.0000 - mae: 14402.0234 - val_loss: 1896397440.0000 - val_mae: 26452.6113
Epoch 93/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 435891904.0000 - mae: 14240.5586 - val_loss: 1891686656.0000 - val_mae: 26395.4629
Epoch 94/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 431526688.0000 - mae: 14258.5352 - val_loss: 1889847040.0000 - val_mae: 26357.5938
Epoch 95/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 426156160.0000 - mae: 14116.4590 - val_loss: 1886817024.0000 - val_mae: 26373.4277
Epoch 96/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 420636640.0000 - mae: 13929.0068 - val_loss: 1880990848.0000 - val_mae: 26227.5508
Epoch 97/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 418215872.0000 - mae: 13916.9111 - val_loss: 1881933184.0000 - val_mae: 26180.2129
Epoch 98/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 418646752.0000 - mae: 13989.0449 - val_loss: 1878681728.0000 - val_mae: 26183.4414
Epoch 99/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 6ms/step - loss: 410458880.0000 - mae: 13706.9932 - val_loss: 1863121664.0000 - val_mae: 25981.1875
Epoch 100/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 404699040.0000 - mae: 13706.7539 - val_loss: 1864543744.0000 - val_mae: 25986.6172

import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.xlabel("Training Epoch")
plt.ylabel("MSE Loss")
plt.title("Neural Network Learning Curve")
plt.legend()

plt.show()
     


y_pred = model.predict(X_test)
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
     
10/10 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step 
MAE : 26203.251953125
MSE : 1786924288.0
RMSE: 42272.02725207297

# Import necessary Keras components
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the Feedforward Neural Network model
model = Sequential()

model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1)) # Output layer for regression (single continuous value)

# Compile the model
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

print("Model defined and compiled successfully.")
model.summary()
     
Model defined and compiled successfully.
/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/dense.py:106: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Model: "sequential_3"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ dense_4 (Dense)                 │ (None, 128)            │        31,488 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_5 (Dense)                 │ (None, 64)             │         8,256 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_6 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_7 (Dense)                 │ (None, 1)              │            33 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 41,857 (163.50 KB)
 Trainable params: 41,857 (163.50 KB)
 Non-trainable params: 0 (0.00 B)

# Install pydot and graphviz for model visualization
!pip install pydot
!pip install graphviz

import pydot
import graphviz
from tensorflow.keras.utils import plot_model
     
Requirement already satisfied: pydot in /usr/local/lib/python3.12/dist-packages (4.0.1)
Requirement already satisfied: pyparsing>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from pydot) (3.3.2)
Requirement already satisfied: graphviz in /usr/local/lib/python3.12/dist-packages (0.21)

# Visualize the current model architecture
plot_model(
    model,
    to_file='current_model_architecture.png',
    show_shapes=True,
    show_layer_names=True,
    rankdir='LR', # 'TB' for top-to-bottom, 'LR' for left-to-right
    expand_nested=False,
    dpi=96
)

from IPython.display import Image
Image(filename='current_model_architecture.png')

     


# Train the model
history = model.fit(
    X_train,
    y_train,
    epochs=100, # Number of epochs can be adjusted
    batch_size=32, # Batch size can be adjusted
    validation_split=0.2, # 20% of training data used for validation
    verbose=1 # Show progress bar during training
)

print("Model training complete.")
     
Epoch 1/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 1s 13ms/step - loss: 39143370752.0000 - mae: 181517.4062 - val_loss: 37832269824.0000 - val_mae: 181077.2344
Epoch 2/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 39112007680.0000 - mae: 181446.3281 - val_loss: 37764214784.0000 - val_mae: 180923.7188
Epoch 3/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 38934183936.0000 - mae: 181061.8750 - val_loss: 37423493120.0000 - val_mae: 180184.3438
Epoch 4/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 38197043200.0000 - mae: 179530.5000 - val_loss: 36275310592.0000 - val_mae: 177679.2344
Epoch 5/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 36204789760.0000 - mae: 175210.1094 - val_loss: 33525563392.0000 - val_mae: 171463.1562
Epoch 6/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 32005646336.0000 - mae: 165726.9219 - val_loss: 28586745856.0000 - val_mae: 159231.7031
Epoch 7/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 25451089920.0000 - mae: 148399.7031 - val_loss: 21415909376.0000 - val_mae: 137993.8438
Epoch 8/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 17311285248.0000 - mae: 121733.9062 - val_loss: 14509422592.0000 - val_mae: 109340.1719
Epoch 9/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 11038746624.0000 - mae: 91730.3047 - val_loss: 10365821952.0000 - val_mae: 86549.5547
Epoch 10/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 8048146432.0000 - mae: 75408.6719 - val_loss: 8669276160.0000 - val_mae: 78262.0391
Epoch 11/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 6513613824.0000 - mae: 67138.8672 - val_loss: 7447448064.0000 - val_mae: 71439.6250
Epoch 12/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 5298039296.0000 - mae: 59120.4805 - val_loss: 6379414528.0000 - val_mae: 64516.9805
Epoch 13/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 4299275264.0000 - mae: 51816.7031 - val_loss: 5517852672.0000 - val_mae: 58106.9297
Epoch 14/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 3562668288.0000 - mae: 45686.4414 - val_loss: 4864013824.0000 - val_mae: 52967.3828
Epoch 15/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 3042020608.0000 - mae: 40948.1211 - val_loss: 4398096384.0000 - val_mae: 48807.0586
Epoch 16/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2656886528.0000 - mae: 37754.0469 - val_loss: 4059725312.0000 - val_mae: 46049.8555
Epoch 17/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2408656128.0000 - mae: 35542.2773 - val_loss: 3839387904.0000 - val_mae: 44208.8281
Epoch 18/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2257744896.0000 - mae: 34296.8555 - val_loss: 3635779072.0000 - val_mae: 42695.1445
Epoch 19/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 2083651840.0000 - mae: 32676.6934 - val_loss: 3521389568.0000 - val_mae: 41588.6172
Epoch 20/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1959696768.0000 - mae: 31693.1016 - val_loss: 3379429376.0000 - val_mae: 40521.6406
Epoch 21/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1852786688.0000 - mae: 30707.2148 - val_loss: 3271672832.0000 - val_mae: 39654.7188
Epoch 22/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1746382976.0000 - mae: 29833.0508 - val_loss: 3200231168.0000 - val_mae: 38985.6328
Epoch 23/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1667703296.0000 - mae: 29182.9824 - val_loss: 3107937536.0000 - val_mae: 38328.1094
Epoch 24/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1590253824.0000 - mae: 28384.0371 - val_loss: 3035558912.0000 - val_mae: 37650.8750
Epoch 25/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1518610432.0000 - mae: 27809.8047 - val_loss: 2959219712.0000 - val_mae: 37090.2188
Epoch 26/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1450907264.0000 - mae: 27131.9141 - val_loss: 2905478400.0000 - val_mae: 36592.8516
Epoch 27/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1395324032.0000 - mae: 26655.6758 - val_loss: 2850544128.0000 - val_mae: 36110.2305
Epoch 28/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1337571200.0000 - mae: 26085.4277 - val_loss: 2800331776.0000 - val_mae: 35673.6328
Epoch 29/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1285775360.0000 - mae: 25641.1387 - val_loss: 2741252096.0000 - val_mae: 35302.0625
Epoch 30/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1241613568.0000 - mae: 25149.4648 - val_loss: 2693330176.0000 - val_mae: 34901.5859
Epoch 31/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1195864960.0000 - mae: 24739.9238 - val_loss: 2643053312.0000 - val_mae: 34397.8359
Epoch 32/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1153489792.0000 - mae: 24242.7598 - val_loss: 2610453248.0000 - val_mae: 34083.8320
Epoch 33/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1123624192.0000 - mae: 23840.4277 - val_loss: 2584060160.0000 - val_mae: 33813.1250
Epoch 34/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1084235648.0000 - mae: 23379.5195 - val_loss: 2538213888.0000 - val_mae: 33388.8203
Epoch 35/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1055457024.0000 - mae: 23135.8965 - val_loss: 2500047360.0000 - val_mae: 33107.1562
Epoch 36/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 1021697024.0000 - mae: 22710.1719 - val_loss: 2476316928.0000 - val_mae: 32804.3477
Epoch 37/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 992113216.0000 - mae: 22392.2754 - val_loss: 2438624000.0000 - val_mae: 32498.3281
Epoch 38/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 965394624.0000 - mae: 22001.9570 - val_loss: 2409979136.0000 - val_mae: 32183.0234
Epoch 39/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 936178368.0000 - mae: 21695.0566 - val_loss: 2387127040.0000 - val_mae: 32004.2852
Epoch 40/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 915358848.0000 - mae: 21495.2676 - val_loss: 2364570880.0000 - val_mae: 31648.7852
Epoch 41/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 888965568.0000 - mae: 21056.2246 - val_loss: 2342630912.0000 - val_mae: 31530.2676
Epoch 42/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 869700416.0000 - mae: 20790.1719 - val_loss: 2317981440.0000 - val_mae: 31187.1973
Epoch 43/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 848223296.0000 - mae: 20598.8574 - val_loss: 2291675648.0000 - val_mae: 31027.1992
Epoch 44/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 824628416.0000 - mae: 20241.8652 - val_loss: 2278295040.0000 - val_mae: 30772.6055
Epoch 45/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 802819200.0000 - mae: 20011.4199 - val_loss: 2255484416.0000 - val_mae: 30575.9727
Epoch 46/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 785777472.0000 - mae: 19799.6758 - val_loss: 2239872000.0000 - val_mae: 30359.8848
Epoch 47/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 767842944.0000 - mae: 19504.5605 - val_loss: 2221832192.0000 - val_mae: 30223.1230
Epoch 48/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 749407936.0000 - mae: 19312.6680 - val_loss: 2203684864.0000 - val_mae: 30015.5039
Epoch 49/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 739743744.0000 - mae: 19253.3242 - val_loss: 2188974080.0000 - val_mae: 29792.0293
Epoch 50/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 718253184.0000 - mae: 18822.3926 - val_loss: 2168995072.0000 - val_mae: 29557.5840
Epoch 51/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 701715904.0000 - mae: 18610.5625 - val_loss: 2160020480.0000 - val_mae: 29522.6270
Epoch 52/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 686789632.0000 - mae: 18460.4297 - val_loss: 2147444480.0000 - val_mae: 29223.5586
Epoch 53/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 672176064.0000 - mae: 18177.2344 - val_loss: 2134600064.0000 - val_mae: 29253.1875
Epoch 54/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 660868736.0000 - mae: 18002.4844 - val_loss: 2118312576.0000 - val_mae: 29257.6406
Epoch 55/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 645889856.0000 - mae: 17884.7969 - val_loss: 2108583296.0000 - val_mae: 29028.7910
Epoch 56/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 633020480.0000 - mae: 17649.7520 - val_loss: 2094155776.0000 - val_mae: 28820.9238
Epoch 57/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 619805312.0000 - mae: 17486.4551 - val_loss: 2074112128.0000 - val_mae: 28816.8965
Epoch 58/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 607653568.0000 - mae: 17312.3008 - val_loss: 2061070336.0000 - val_mae: 28534.2812
Epoch 59/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 601348416.0000 - mae: 17189.6465 - val_loss: 2049816320.0000 - val_mae: 28458.6113
Epoch 60/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 588694016.0000 - mae: 16887.0293 - val_loss: 2048022784.0000 - val_mae: 28374.5918
Epoch 61/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 574312128.0000 - mae: 16736.8828 - val_loss: 2032832256.0000 - val_mae: 28294.9941
Epoch 62/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 567593920.0000 - mae: 16695.1094 - val_loss: 2025809664.0000 - val_mae: 28157.6895
Epoch 63/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 555489472.0000 - mae: 16400.2266 - val_loss: 2014448768.0000 - val_mae: 28126.2930
Epoch 64/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 544998912.0000 - mae: 16304.6045 - val_loss: 2009127168.0000 - val_mae: 27973.3867
Epoch 65/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 536952384.0000 - mae: 16056.8350 - val_loss: 1993413376.0000 - val_mae: 27781.7363
Epoch 66/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 528381760.0000 - mae: 15973.8770 - val_loss: 1989054848.0000 - val_mae: 27721.4316
Epoch 67/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 517524224.0000 - mae: 15736.7969 - val_loss: 1979634560.0000 - val_mae: 27685.6348
Epoch 68/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 509574848.0000 - mae: 15643.9473 - val_loss: 1973776512.0000 - val_mae: 27615.2070
Epoch 69/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 501316256.0000 - mae: 15479.2129 - val_loss: 1959693696.0000 - val_mae: 27462.2109
Epoch 70/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 506813664.0000 - mae: 15706.5801 - val_loss: 1950667648.0000 - val_mae: 27590.1973
Epoch 71/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 484016416.0000 - mae: 15231.6514 - val_loss: 1949475968.0000 - val_mae: 27414.2363
Epoch 72/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 476260672.0000 - mae: 15108.7598 - val_loss: 1938944896.0000 - val_mae: 27217.3672
Epoch 73/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 491064000.0000 - mae: 15115.6973 - val_loss: 1941513216.0000 - val_mae: 27316.6777
Epoch 74/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 464872000.0000 - mae: 15022.1133 - val_loss: 1932150656.0000 - val_mae: 27132.1191
Epoch 75/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 455361888.0000 - mae: 14703.2744 - val_loss: 1924317568.0000 - val_mae: 27007.1738
Epoch 76/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 448070848.0000 - mae: 14594.7822 - val_loss: 1918115456.0000 - val_mae: 26976.6191
Epoch 77/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 441683200.0000 - mae: 14464.8223 - val_loss: 1906166272.0000 - val_mae: 26857.0195
Epoch 78/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 434862016.0000 - mae: 14376.0146 - val_loss: 1904690176.0000 - val_mae: 26857.1680
Epoch 79/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 429907648.0000 - mae: 14225.9805 - val_loss: 1900994432.0000 - val_mae: 26720.1152
Epoch 80/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 425307776.0000 - mae: 14145.3369 - val_loss: 1895654144.0000 - val_mae: 26555.0938
Epoch 81/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 420395872.0000 - mae: 14018.0889 - val_loss: 1895508096.0000 - val_mae: 26632.7891
Epoch 82/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 411291456.0000 - mae: 13841.9043 - val_loss: 1882775424.0000 - val_mae: 26491.2559
Epoch 83/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 406430272.0000 - mae: 13813.1895 - val_loss: 1873335808.0000 - val_mae: 26443.8223
Epoch 84/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 402202592.0000 - mae: 13678.2900 - val_loss: 1873332224.0000 - val_mae: 26278.6133
Epoch 85/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 6ms/step - loss: 394124672.0000 - mae: 13519.8232 - val_loss: 1866341376.0000 - val_mae: 26421.7656
Epoch 86/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step - loss: 393572800.0000 - mae: 13535.4580 - val_loss: 1863687552.0000 - val_mae: 26307.7305
Epoch 87/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 387342048.0000 - mae: 13470.5420 - val_loss: 1858439168.0000 - val_mae: 26222.4805
Epoch 88/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 382923840.0000 - mae: 13230.8320 - val_loss: 1853777792.0000 - val_mae: 26258.4648
Epoch 89/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 374911872.0000 - mae: 13142.6328 - val_loss: 1850958976.0000 - val_mae: 26147.2305
Epoch 90/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 373547200.0000 - mae: 13032.9736 - val_loss: 1844870528.0000 - val_mae: 26040.7598
Epoch 91/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 369645696.0000 - mae: 13074.3994 - val_loss: 1842512512.0000 - val_mae: 26004.3262
Epoch 92/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 363621408.0000 - mae: 12867.9355 - val_loss: 1831423232.0000 - val_mae: 25838.8555
Epoch 93/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 360889568.0000 - mae: 12787.6006 - val_loss: 1826320256.0000 - val_mae: 25850.2246
Epoch 94/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 354520032.0000 - mae: 12639.6914 - val_loss: 1821060608.0000 - val_mae: 25666.9980
Epoch 95/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 351356032.0000 - mae: 12610.4951 - val_loss: 1814538496.0000 - val_mae: 25585.6211
Epoch 96/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 348593248.0000 - mae: 12496.5215 - val_loss: 1814413184.0000 - val_mae: 25625.2598
Epoch 97/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 343818848.0000 - mae: 12388.8115 - val_loss: 1806886912.0000 - val_mae: 25427.5078
Epoch 98/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 341239840.0000 - mae: 12304.7822 - val_loss: 1807476352.0000 - val_mae: 25470.5664
Epoch 99/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 337314848.0000 - mae: 12243.7793 - val_loss: 1806138496.0000 - val_mae: 25621.9316
Epoch 100/100
30/30 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step - loss: 335230816.0000 - mae: 12185.3145 - val_loss: 1794753792.0000 - val_mae: 25315.5605
Model training complete.

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel("Training Epoch")
plt.ylabel("MSE Loss")
plt.title("Neural Network Learning Curve")
plt.legend()
plt.grid(True)
plt.show()
     


# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

print("\nModel evaluation complete. You can now analyze these metrics to understand the model's performance.")
     
10/10 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step 
Mean Absolute Error (MAE): 26097.0117
Mean Squared Error (MSE): 1802902400.0000
Root Mean Squared Error (RMSE): 42460.5982

Model evaluation complete. You can now analyze these metrics to understand the model's performance.

def build_model(num_hidden_layers, neurons_per_layer_list, input_shape, activation='relu'):
    """
    Creates a Keras Sequential model with a specified number of hidden layers,
    neuron counts, input shape, and activation function.

    Args:
        num_hidden_layers (int): The number of hidden layers.
        neurons_per_layer_list (list): A list of integers, where each element
                                     represents the number of neurons in a
                                     corresponding hidden layer.
        input_shape (tuple): The input shape of the model.
        activation (str): The activation function for the hidden layers (default is 'relu').

    Returns:
        tf.keras.Model: The compiled Keras Sequential model.
    """
    model = keras.Sequential()

    # Add the input layer (which is technically the first hidden layer in Keras Sequential)
    # with input_shape. The number of neurons for this layer is the first in the list.
    if num_hidden_layers > 0:
        model.add(layers.Dense(neurons_per_layer_list[0], activation=activation, input_shape=input_shape))

        # Add subsequent hidden layers if any
        for i in range(1, num_hidden_layers):
            model.add(layers.Dense(neurons_per_layer_list[i], activation=activation))

    # Output layer for regression (single neuron, no activation)
    model.add(layers.Dense(1))

    # Compile the model
    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )
    return model

# Test the function: Create a model with 1 hidden layer (e.g., 64 neurons)
# using the input shape from our preprocessed data (X_train.shape[1])
input_dim = X_train.shape[1]
sample_model_1_layer = build_model(
    num_hidden_layers=1,
    neurons_per_layer_list=[64],
    input_shape=(input_dim,)
)

print("1-Hidden-Layer Model Summary:")
sample_model_1_layer.summary()
     
1-Hidden-Layer Model Summary:
/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/dense.py:106: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Model: "sequential_4"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ dense_8 (Dense)                 │ (None, 64)             │        15,744 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_9 (Dense)                 │ (None, 1)              │            65 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 15,809 (61.75 KB)
 Trainable params: 15,809 (61.75 KB)
 Non-trainable params: 0 (0.00 B)