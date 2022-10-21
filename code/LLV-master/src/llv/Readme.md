## Python-LiveLink(UE4)

在`LLV`库的基础上进行开发的，原仓库地址为：https://github.com/think-biq/LLV

仅在UE4.27版本上进行了测试，是可行的。

**主要函数**

1、生成帧

`gesicht.py/FaceFrame`：

```python
# 功能：给定BS值以及帧编号，返回一个可以直接发送给LiveLink的动画帧、
# 输入：
	1、blendshapes: dict({'bs_name':bs_value.....})  # ARKit格式
	2、frame_number: int  # 帧编号
# 输出：
	FaceFrame Object
def from_default_blendshapes(blendshapes,frame_number,fps=60)

```

2、发送帧

`cli.py/send_one_frame`

```python
# 功能：发送帧，这个函数内部调用了生成帧的函数
# 输入：
	1、buchse对象：buchse = Buchse(host, port, as_server = False)
	1、blendshapes: dict({'bs_name':bs_value.....})  # ARKit格式
	2、frame_number: int  # 帧编号
# 输出：发送是否成功
def send_one_frame(buchse,blendshapes,frame_number)
```



##### 注意

本地测试时`host`使用`127.0.0.1`

测试命令：

```
python llv.py play --host 10.0.0.69 examples/dao.gesichter
```









##### 现有的问题

1、blendshape值导出问题：按照facegood的流程是从maya软件里导出116个blendshape值，现在不知道怎么导出，是否可以从其他软件导出ARKit格式的52个点的值？

maya源文件里的各个blendshape的组织形式，能用export_weights.py直接导出

2、数据集生成pipeline问题，数据集应该是数字人的语音和数字人表情的匹配对，就算真人来录数据，如何保证语音帧和表情帧的匹配？

用演员的音色去训练合成音模型，训练数据是演员的原声和表情，可以保证音频和表情一一对应，然后应用的时候，给合成音模型输入文字，然后得到和演员音色相同的合成音，用这个合成音去得到表情。





