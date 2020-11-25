# 人脸解析


## 一、接口描述 
### 1. 功能描述  
人脸解析（Face Parsing）是将人的头及五官构成分解成若干区域。
本API为用户提供人脸解析以及分割功能，输入一张人脸图片，返回人的脸部分割结果，一共为11类(括号中为区域分类ID):
背景(0), 脸部皮肤(1), 左眉毛(2), 右眉毛(3), 左眼(4), 右眼(5), 鼻子(6), 上唇(7), 口中(8), 下唇(9), 头发(10)

做为可选项(optionally), 本API提供了一个着色盘可以进行不同部位的对应着色标注，详情请见本页五。


### 2. 能力说明：   
输入图像限定为人脸图片。为获得最优分割效果，场景为单人头像，而且头部需在输入图片的中间部分，并占比至少50%以上。多人头像或占比较低的场景效果不能保证最优.如有需要可以考虑与[人像分割(selfie_segmentation)](https://git.jd.com/doc-neuhub/api-docs/blob/master/image/selfie_segmentation.md)联合使用。

### 3. 接口数据要求：  
- 图片格式：base64编码
- 图片类型：JPG, JPEG, PNG
- 图片文件大小：最小 50\*50 像素，最大 2048\*2048 像素之间
- 图片大小：图片小于2M

### 4. 接口使用： 
使用接口前，需要先完成API的下单购买，然后可使用已经封装好的SDK/参照[接口鉴权](https://aidoc.jd.com/user/auth.html)规则进行相应开发，整体流程详见   [接入流程](https://aidoc.jd.com/user/flow.html)

## 二、请求说明
### 1. 接口地址 ：

```
https://aiapi.jd.com/jdai/face_parser
```

### 2. 请求方式：  
```
 post
```

### 3. 请求参数  
#### （1）query请求参数  
公共请求参数
<table>
   <tr>
      <th>名称</th>
      <th>类型</th>
      <th>必填</th>
      <th>示例值</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>appkey</td>
      <td>string</td>
      <td>是</td>
      <td>80d2b762ecb86593f9668526920f46c</td>
      <td>您的appkey，可在买家中心控制台中获</td>
   </tr>
   <tr>
      <td>timestamp</td>
      <td>long</td>
      <td>是</td>
      <td>1541491668060</td>
      <td>请求的时间戳，精确到毫秒，timestamp有效期5分钟</td>
   </tr>
   <tr>
      <td>sign</td>
      <td>string</td>
      <td>是</td>
      <td>2e148773a0337a8f2200ba90d445f083</td>
      <td>签名，根据规则MD5(sectetkey+timestamp)</td>
   </tr>
</table>



#### （2）body请求参数
业务请求参数
<table>
   <tr>
      <th>名称</th>
      <th>类型</th>
      <th>必填</th>
      <th>示例值</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>无</td>
      <td>string</td>
      <td>是</td>
      <td>Python列表(List), List中每个entry为图像Base64编码值，去掉图片头"data:image/png;base64,", <br> [{"image":"4AAQSk..."}, {"image":"9j/4AA..."}, ...{"image":"4AAQSk..."}]<br>（由于过长，不给出完全示例）</td> <td>图像base64编码的列表</td>
   </tr>
</table>

### 4、请求代码示例
建议您使用我们提供的SDK进行调用，SDK获取及调用方式详见本页一接口描述中的4接口使用



## 三、返回说明
### 1、返回参数
#### （1）公共返回参数

<table>
   <tr>
      <th>名称</th>
      <th>类型</th>
      <th>示例值</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>code</td>
      <td>string</td>
      <td>10000</td>
      <td>参见下方错误码-系统级错误码</td>
   </tr>
      <tr>
      <td>charge</td>
      <td>boolean</td>
      <td>false 或 true</td>
      <td>false：不扣费， true：扣费</td>
   </tr>
   <tr>
         <td>remainTimes</td>
         <td>long</td>
         <td>1305</td>
         <td>剩余调用次数；免费api：每天剩余调用次数；收费api：剩余次数；无限制时为-1</td>
      </tr>
      <tr>
         <td>remainSeconds</td>
         <td>long</td>
         <td>1223456</td>
         <td>剩余调用时间（s）；免费api：-1；收费api：剩余调用时间；无限制时为-1</td>
         </tr>
      </tr>
      <tr>
      <td>msg</td>
      <td>string</td>
      <td>查询成功</td>
      <td>参见下方错误码-系统级错误码数</td>
   </tr>
      </tr>
      <tr>
      <td>result</td>
      <td>object</td>
      <td>{...}</td>
      <td>查询结果</td>
   </tr>
</table>

#### （2）业务返回参数

<table>
   <tr>
      <th>名称</th>
      <th>类型</th>
      <th>示例值</th>
      <th>描述</th>
   </tr>
   <tr>
      <td>status</td>
      <td>int</td>
      <td>200</td>
      <td>参照四、错误码-业务错误码</td>
   </tr>
   <tr>
      <td>message</td>
      <td>string</td>
      <td>OK</td>
      <td>参照四、错误码-业务错误码</td>
   </tr>
   <tr>
      <td>image</td>
      <td>string</td>
      <td>iVBORw0KGgoAAAANSUh</td>
      <td>返回分割图像的base64编码, 像素值为对应区域分类ID(详见本页五）</td>
   </tr>
   <tr>
      <td>used_time</td>
      <td>int</td>
      <td>129</td>
      <td>整个请求花费的时间，单位为毫秒</td>
   </tr>
</table>

### 2、返回示例  


```
{
    "code": "10000",
    "charge": false,
    "remainTimes": 4998,
    "remainSeconds": -1,
    "msg": "查询成功",
    "result": {
   			"message":"ok ",
   			"status": 200,
   			"used_time": 129 
   			"image": "iVBORw0KGgoAAAANSUh..."
    }
}
```

### 2、返回示例

## 四、错误码

### 1.系统级错误码
[详见返回码](https://aidoc.jd.com/user/returncode.html)  
### 2.业务错误码


<table>
   <tr>
      <th>业务错误码（status）</th>
      <th>message</th>
      <th>说明</th>
   </tr>
   <tr>
      <td>1002</td>
      <td>"parameter error, \"image\" is required"</td>
      <td>缺少必要参数</td>
   </tr>
   <tr>
      <td>1003</td>
      <td>"invalid image base64 data"</td>
      <td>base64图像解析失败</td>
   </tr>
   <tr>
      <td>1004</td>
      <td>"incorrect image size"</td>
      <td>图像大小超过限制</td>
   </tr>
   <tr>
      <td>1005</td>
      <td>"not valid json string"</td>
      <td>非法的json字符串</td>
   </tr>
   <tr>
      <td>1006</td>
      <td>"other error"</td>
      <td>其他错误</td>
   </tr>
   <tr>
      <td>1007</td>
      <td>"image format error"</td>
      <td>图像格式错误</td>
   </tr>
</table>

## 五、人脸各个部分对应Mask及其调色盘(palette)
<table>
   <tr>
      <th>区域分类ID (Mask Index)</th>
      <th>头部区域(Head Parts)</th>
      <th>着色盘(Palette RGB)</th>
   </tr>
   <tr>
      <td>0</td>
      <td>"背景(background)"</td>
      <td>[0, 0, 0]</td>
   </tr>
   <tr>
      <td>1</td>
      <td>"脸部皮肤(face_skin)"</td>
      <td>[0, 153, 255]</td>
   </tr>
   <tr>
      <td>2</td>
      <td>"左眉毛(left_eyebrow)"</td>
      <td>[102, 255, 153]</td>
   </tr>
   <tr>
      <td>3</td>
      <td>"右眉毛(right_eyebrow)"</td>
      <td>[0, 204, 153]</td>
   </tr>
   <tr>
      <td>4</td>
      <td>" 左眼(left_eye)"</td>
      <td>[255, 255, 102]</td>
   </tr>
   <tr>
      <td>5</td>
      <td>"右眼(right_eye)"</td>
      <td>[255, 255, 204]</td>
   </tr>
   <tr>
      <td>6</td>
      <td>" 鼻子(nose)"</td>
      <td>[255, 153, 0]</td>
   </tr>
   <tr>
      <td>7</td>
      <td>"上唇(upper_lip)"</td>
      <td>[255, 204, 255]</td>
   </tr>
   <tr>
      <td>8</td>
      <td>"口中(inner_mouth)"</td>
      <td>[102, 0, 51]</td>
   </tr>
   <tr>
      <td>9</td>
      <td>"下唇(lower_lip)"</td>
      <td>[255, 102, 255]</td>
   </tr>
   <tr>
      <td>10</td>
      <td>"头发(hair)"</td>
      <td>[255, 0, 102]</td>
   </tr>
</table>
