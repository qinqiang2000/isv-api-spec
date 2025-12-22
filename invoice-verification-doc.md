### 1.发票查验（单张发票实时查询下载接口）

#### 1.1接口说明

企业端业务系统通过接口对开具、取得的各类发票发起查验申请，系统根据查验申请反馈查验结果。

#### 1.2请求方式

请求方式为POST

path 指该参数为路径参数

query 指该参数需在请求URL传参

body 指该参数需在请求JSON传参

#### 1.3请求参数

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **序号** | **数据项标识** | **数据项名称** | **字段类型** | **长度** | **必须** | **说明** |
| 1   | fplx | 发票类型 | String | 2   | 是   | 01：增值税专用发票<br><br>02：货物运输业增值税专用发票<br><br>03：机动车销售统一发票<br><br>04：增值税普通发票<br><br>08：增值税电子专用发票<br><br>10：增值税电子普通发票<br><br>11：卷式发票<br><br>14：通行费发票<br><br>15：二手车销售统一发票<br><br>81：电子发票（增值税专用发票）<br><br>82：电子发票（普通发票）<br><br>85：纸质发票（增值税专用发票）<br><br>86：纸质发票（普通发票）<br><br>51：电子发票（铁路电子客票）<br><br>61：电子发票（航空运输客票电子行程单）<br><br>83：机动车销售电子统一发票<br><br>84：二手车销售电子统一发票<br><br>87：纸质发票（机动车销售统一发票）<br><br>88：纸质发票（二手车销售统一发票） |
| 2   | fpdm | 发票代码 | String | 12  | 否   | 发票类型为：01、02、03、04、08、10、11、14、15、85、86、87、88传纸质发票代码 |
| 3   | fphm | 发票号码 | String | 20  | 是   | 发票类型为：01、02、03、04、08、10、11、14、15、85、86、87、88传纸质发票号码<br><br>发票类型为：81、82、51、61、83、84传20位数字化电子发票号码 |
| 4   | kprq | 开票日期 | String | 8   | 是   | YYYYMMDD |
| 5   | jym | 校验码 | String | 32  | 否   | 校验码（后六位） |
| 6   | kpje | 开票金额 | Number | 18,2 | 否   | 08：增值税电子专用发票、01：增值税专用发票、85：纸质发票（增值税专用发票）、02：货物运输业增值税专用发票，传开具金额(不含税)；<br><br>03：机动车销售统一发票、87：纸质发票（机动车销售统一发票），传不含税价；<br><br>15：二手车销售统一发票、<br><br>84：二手车销售电子统一发票、88：纸质发票（二手车销售统一发票），传车价合计；<br><br>81：电子发票（增值税专用发票）、82：电子发票（普通发票）、51：电子发票（铁路电子客票）、61：电子发票（航空运输客票电子行程单），传价税合计<br><br>83：机动车销售电子统一发票，传价税合计 |
| 7   | nsrsbh | 纳税人识别号 | String | 20  | 是   |     |

#### 1.4请求报文示例

{

"fplx": "01",

"fpdm": "5101\*\*\*\*\*111",

"fphm": "00000001",

"kprq": "20250101",

"jym": "123456",

"kpje": "10000.00",

"nsrsbh": "915100\*\*\*\*\*\*\*\*\*\*\*\*"

}

#### 1.5返回参数

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **序号** | **数据项标识** | **数据项名称** | **字段类型** | **长度** | **必须** | **说明** |
| 1   | returncode | 结果代码 | String | 2   | 是   | 00：成功<br><br>01：失败<br><br>02：查无数据<br><br>03：查验不一致<br><br>04：此发票非本单位开具或取得 |
| 2   | returnmsg | 返回信息 | String | 2000 | 否   | 错误信息说明 |
| 3   | cyjgxx | 查验结果信息 | String | 20000 | 否   | 压缩包文件流（gzip+base64），原始数据为json报文<br><br>Json报文格式详见：六、附件：（一）发票票面信息数据说明” |

#### 1.6返回报文示例

成功返回：

{

"Response": {

"RequestId": "16位随机数字和字母组合",

"Data": {

"returncode": "00",

"returnmsg": "返回信息",

"cyjgxx": "查验结果信息"

}

}

}

失败返回：

{

"Response": {

"RequestId": "16位随机数字和字母组合",

"Error": {

"Code": "01",

"Message": "错误说明"

}

}

}

# 六、附件

## （一）发票票面信息数据说明

### 1.取得数字化电子发票-增值税发票数据

包含以下发票类型：

81：电子发票（增值税专用发票）

82：电子发票（普通发票）

85：纸质发票（增值税专用发票）

86：纸质发票（普通发票）

原始数据为json报文字段说明

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 2   | 纸质发票代码 | zzfpDm | Y   | VARCHAR | 12  |     |
| 3   | 纸质发票号码 | zzfphm | Y   | VARCHAR | 20  |     |
| 4   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 5   | 发票票种代码 | fppzDm | N   | CHAR | 2   |     |
| 6   | 特定要素类型代码 | tdyslxDm | Y   | CHAR | 2   |     |
| 7   | 是否蓝字发票 | sflzfp | N   | CHAR | 1   | Y：是<br><br>N：否 |
| 8   | 开具红字发票对应的蓝字发票号码 | kjhzfpdydlzfphm | Y   | VARCHAR | 20  |     |
| 9   | 开具红字发票对应的纸质发票代码 | kjhzfpdydzzfpDm | Y   | VARCHAR | 12  |     |
| 10  | 开具红字发票对应的纸质发票号码 | kjhzfpdydzzfphm | Y   | VARCHAR | 20  |     |
| 11  | 销售方识别号 | xsfnsrsbh | Y   | VARCHAR | 20  |     |
| 12  | 销售方名称 | xsfmc | N   | VARCHAR | 150 |     |
| 13  | 销货方地址 | xhfdz | Y   | VARCHAR | 250 |     |
| 14  | 购买方识别号 | gmfnsrsbh | Y   | VARCHAR | 20  |     |
| 15  | 购买方名称 | gmfmc | N   | VARCHAR | 150 |     |
| 16  | 购买方地址 | gmfdz | Y   | VARCHAR | 300 |     |
| 17  | 合计金额 | hjje | N   | DECIMAL | 18,2 |     |
| 18  | 合计税额 | hjse | N   | DECIMAL | 18,2 |     |
| 19  | 价税合计 | jshj | N   | DECIMAL | 18,2 |     |
| 20  | 价税合计(大写) | jshjdx | N   | VARCHAR | 300 |     |
| 21  | 扣除额 | kce | Y   | DECIMAL | 18,2 |     |
| 22  | 结算方式 | jsfsDm | Y   | CHAR | 2   |     |
| 23  | 开票人 | kpr | Y   | VARCHAR | 300 |     |
| 24  | 备注  | bz  | Y   | VARCHAR | 450 |     |
| 25  | 明细条数 | xmmxhs | Y   | BIGINT | 20  |     |
| 26  | 增值税即征即退代码 | zzsjzjtDm | Y   | VARCHAR | 2   |     |
| 27  | 出口退税类代码 | cktslDm | Y   | CHAR | 2   |     |
| 28  | 复核人姓名 | fhrxm | Y   | VARCHAR | 75  |     |
| 29  | 收款人姓名 | skrxm | Y   | VARCHAR | 150 |     |
| 30  | 销售方电话 | xsfdh | Y   | VARCHAR | 60  |     |
| 31  | 销售方开户行 | xsfkhh | Y   | VARCHAR | 120 |     |
| 32  | 销售方账号 | xsfzh | Y   | VARCHAR | 100 |     |
| 33  | 购买方电话 | gmfdh | Y   | VARCHAR | 60  |     |
| 34  | 购买方开户行 | gmfkhh | Y   | VARCHAR | 120 |     |
| 35  | 购买方账号 | gmfzh | Y   | VARCHAR | 100 |     |
| 36  | 销方纳税人类型代码 | xfnsrlxdm | Y   | VARCHAR | 1   | 1：一般纳税人<br><br>2：小规模纳税人<br><br>3：转登记小规模纳税人<br><br>4：辅导期一般纳税人<br><br>5：自然人 |
| 37  | 成品油异常标识 | cpyycbs | Y   | VARCHAR | 1   | 9：正常<br><br>1：成品油单价异常<br><br>2：成品油超库存异常 |
| 38  | 附加要素信息 | fjysxx | Y   | JSON |     |     |
| hwxx（**货物信息）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 项目名称 | xmmc | Y   | VARCHAR | 600 |     |
| 3   | 商品服务简称 | spfwjc | Y   | VARCHAR | 120 |     |
| 4   | 货物或应税劳务、服务名称 | hwhyslwfwmc | Y   | VARCHAR | 300 |     |
| 5   | 商品和服务税收分类合并编码 | sphfwssflhbbm | Y   | VARCHAR | 19  |     |
| 6   | 规格型号 | ggxh | Y   | VARCHAR | 150 |     |
| 7   | 单位  | dw  | Y   | VARCHAR | 300 |     |
| 8   | 发票交易数量 | fpjysl | Y   | VARCHAR | 25  |     |
| 9   | 发票交易单价 | fpjydj | Y   | VARCHAR | 25  |     |
| 10  | 税率  | slv | N   | DECIMAL | 16,6 |     |
| 11  | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 12  | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 13  | 扣除额 | kce | Y   | DECIMAL | 18,2 |     |
| 14  | 商品条码 | sptm | Y   | VARCHAR | 300 |     |
| **jzfwtdys（特定要素类型代码为03：建筑服务发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 土地增值税项目编号 | tdzzsxmbh | Y   | VARCHAR | 40  |     |
| 2   | 跨地（市）标志 | kdsbz | Y   | CHAR | 1   | Y：是<br><br>N：否 |
| **jzfwtdysList（特定要素类型代码为03：建筑服务发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 建筑服务发生地 | jzfwfsd | N   | VARCHAR | 300 |     |
| 3   | 建筑项目名称 | jzxmmc | N   | VARCHAR | 300 |     |
| 4   | 项目名称 | xmmc | Y   | VARCHAR | 600 |     |
| 5   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 6   | 税率  | sl1 | N   | DECIMAL | 16,6 |     |
| 7   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| **hwysfwtdysList（特定要素类型代码为04：货物运输服务发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 运输工具种类 | ysgjzl | Y   | VARCHAR | 30  |     |
| 3   | 运输工具牌号 | ysgjph | Y   | VARCHAR | 40  |     |
| 4   | 起运地 | qyd | N   | VARCHAR | 300 |     |
| 5   | 到达地 | ddd | N   | VARCHAR | 300 |     |
| 6   | 运输货物名称 | yshwmc | Y   | VARCHAR | 150 |     |
| **bdcxsfwtdysList（特定要素类型代码为05：不动产销售服务发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 产权证书编号 | cqzsbh | Y   | VARCHAR | 40  | 产权证书/不动产权证号 |
| 3   | 不动产单位代码 | bdcdwdm | Y   | VARCHAR | 30  | 不动产单元代码 |
| 4   | 网签合同备案编号 | wqhtbabh | Y   | VARCHAR | 30  |     |
| 5   | 不动产坐落地址 | bdczldz | Y   | VARCHAR | 300 | 不动产地址 |
| 6   | 跨地（市）标志 | kdsbz | Y   | CHAR | 1   | Y：是<br><br>N：否 |
| 7   | 土地增值税项目编号 | tdzzsxmbh | Y   | VARCHAR | 40  |     |
| 8   | 核定计税价格 | hdjsjg | Y   | DECIMAL | 18,2 |     |
| 9   | 实际成交含税金额 | sjcjhsje | Y   | DECIMAL | 18,2 |     |
| **bdcjyzltdysList（特定要素类型代码为06：不动产经营租赁服务时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 产权证书编号 | cqzsbh | Y   | VARCHAR | 40  | 产权证书/不动产权证号 |
| 3   | 不动产坐落地址 | bdczldz | Y   | VARCHAR | 300 | 不动产地址 |
| 4   | 租赁期起 | zlqq | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 5   | 租赁期止 | zlqz | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 6   | 跨地（市）标志 | kdsbz | Y   | CHAR | 1   | Y：是<br><br>N：否 |
| **dsccstdys（特定要素类型代码为07：代收车船税时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 保险单号 | bxdh | N   | VARCHAR | 40  |     |
| 2   | 车牌号/船舶登记号 | cphcbdjh | N   | VARCHAR | 40  |     |
| 3   | 税款所属期 | skssq | N   | VARCHAR | 60  |     |
| 4   | 车架号 | cjh | N   | VARCHAR | 60  |     |
| 5   | 代收车船税金额 | dsccsje | N   | DECIMAL | 18,2 |     |
| 6   | 滞纳金 | znj | N   | DECIMAL | 18,2 | 滞纳金金额 |
| 7   | 金额合计 | jehj | N   | DECIMAL | 18,2 |     |
| **lkysfwtdysList（特定要素类型代码为09：旅客运输服务发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 出行人 | cxr | N   | VARCHAR | 300 |     |
| 3   | 出行人证件类型代码 | cxrzjlxDm | N   | CHAR | 3   | 详见“六、附件：（二）代码表”1.身份证件类型代码 |
| 4   | 身份证件号码 | sfzjhm | N   | VARCHAR | 30  | 有效身份证件号 |
| 5   | 出行日期 | chuxrq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 6   | 出发地 | cfd | N   | VARCHAR | 300 |     |
| 7   | 到达地 | ddd | N   | VARCHAR | 300 |     |
| 8   | 座位等级 | zwdj | Y   | VARCHAR | 20  | 等级  |
| 9   | 交通工具类型代码 | jtgjlxDm | Y   | CHAR | 1   | 交通工具类型<br><br>1：飞机<br><br>2：火车<br><br>3：长途汽车<br><br>4：公共交通<br><br>5：出租车<br><br>6：汽车<br><br>7：船舶<br><br>9：其他 |
| **ylfwzytdys（特定要素类型代码为10：医疗服务（住院）发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 医疗业务流水号 | ylywlsh | N   | VARCHAR | 40  | 业务流水号 |
| 2   | 患者姓名 | hzxm | N   | VARCHAR | 150 |     |
| 3   | 患者身份证件类型代码 | hzsfzjlxDm | N   | CHAR | 3   | 详见“六、附件：（二）代码表”1.身份证件类型代码 |
| 4   | 患者身份证件号码 | hzsfzjhm | N   | VARCHAR | 30  |     |
| 5   | 病例号 | blh | Y   | VARCHAR | 20  |     |
| 6   | 住院号 | zyh | N   | VARCHAR | 20  |     |
| 7   | 住院科别 | zykb | N   | VARCHAR | 100 |     |
| 8   | 住院时间起 | zysjq | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 9   | 住院时间止 | zysjz | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 10  | 医疗预缴金额 | ylyjje | Y   | DECIMAL | 18,4 | 预缴金额 |
| 11  | 医疗补缴金额 | ylbjje | Y   | DECIMAL | 18,4 | 补缴金额 |
| 12  | 医疗退费金额 | yltfje | Y   | DECIMAL | 18,4 | 退费金额 |
| 13  | 医疗机构类型代码 | yljglxDm | Y   | VARCHAR | 4   | 医疗机构类型<br><br>详见“六、附件：（二）代码表”2.医疗机构类型代码 |
| 14  | 其他医疗机构类型 | qtyljglx | Y   | VARCHAR | 100 | 不在医疗机构类型代码中的医疗机构类型 |
| 15  | 医保类型代码 | yblxDm | Y   | CHAR | 2   | 医保类型<br><br>01：职工基本医疗保险<br><br>02：城乡居民基本医疗保险<br><br>03：离休<br><br>04：其他医疗保险<br><br>05：自费 |
| 16  | 其他医保类型 | qtyblx | Y   | VARCHAR | 100 | 不在医保类型代码中的医保类型 |
| 17  | 医保编号 | ybbh | Y   | VARCHAR | 20  |     |
| 18  | 性别代码 | xbDm | N   | CHAR | 1   | 性别<br><br>1：男<br><br>2：女 |
| 19  | 医保统筹基金支付金额 | ybtcjjzfje | Y   | DECIMAL | 18,4 | 医保统筹基金支付 |
| 20  | 其他支付金额 | qtzfje | Y   | DECIMAL | 18,4 | 其他支付 |
| 21  | 个人账户支付金额 | grzhzfje | Y   | DECIMAL | 18,4 | 个人账户支付 |
| 22  | 个人现金支付金额 | grxjzfje | Y   | DECIMAL | 18,4 | 个人现金支付 |
| 23  | 个人支付金额 | grzfje | Y   | DECIMAL | 18,4 | 个人支付 |
| 24  | 个人自费金额 | grzfje1 | Y   | DECIMAL | 18,4 | 个人自费 |
| 25  | 交款人 | jkr | Y   | VARCHAR | 100 |     |
| 26  | 收款单位 | skdw | Y   | VARCHAR | 100 |     |
| 27  | 省市自定义要素数量 | sszdyyssl | Y   | INT | 11  |     |
| 28  | 省市自定义要素json | sszdyysjson | Y   | JSON |     |     |
| **ylfwzytdysList（特定要素类型代码为10：医疗服务（住院）发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 医疗服务住院发票明细序号 | ylfwzyfpmxxh | N   | INT | 11  |     |
| 2   | 项目名称 | xmmc | N   | VARCHAR | 600 |     |
| 3   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 4   | 税率  | sl1 | Y   | DECIMAL | 16,6 |     |
| 5   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 6   | 备注  | bz5 | Y   | VARCHAR | 450 |     |
| **ylfwzysftdysList（特定要素类型代码为10：医疗服务（住院）发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 住院收费明细序号 | zysfmxxh | N   | INT | 11  |     |
| 2   | 医疗服务住院发票明细序号 | ylfwzyfpmxxh | N   | INT | 11  | 明细序号 |
| 3   | 费用明细 | fymx | N   | VARCHAR | 100 |     |
| 4   | 发票商品数量 | fpspsl | Y   | VARCHAR | 25  | 数量  |
| 5   | 单位  | dw  | Y   | VARCHAR | 300 |     |
| 6   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 7   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 8   | 税率  | sl1 | N   | DECIMAL | 16,6 | 增值税税率/征收率 |
| 9   | 医疗服务贯标码 | ylfwgbm | Y   | VARCHAR | 50  |     |
| 10  | 备注  | bz5 | Y   | VARCHAR | 450 |     |
| **ylfwmztdys（特定要素类型代码为11：医疗服务（门诊）发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 医疗业务流水号 | ylywlsh | N   | VARCHAR | 40  | 业务流水号 |
| 2   | 患者姓名 | hzxm | N   | VARCHAR | 150 |     |
| 3   | 患者身份证件类型代码 | hzsfzjlxDm | N   | CHAR | 3   | 详见“六、附件：（二）代码表”1.身份证件类型代码 |
| 4   | 患者身份证件号码 | hzsfzjhm | N   | VARCHAR | 30  |     |
| 5   | 门诊号 | mzh | N   | VARCHAR | 30  |     |
| 6   | 门诊就诊时间 | mzjzsj | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss<br><br>就诊日期 |
| 7   | 医疗机构类型代码 | yljglxDm | Y   | VARCHAR | 4   | 医疗机构类型<br><br>详见“六、附件：（二）代码表”2.医疗机构类型代码 |
| 8   | 其他医疗机构类型 | qtyljglx | Y   | VARCHAR | 100 | 不在医疗机构类型代码中的医疗机构类型 |
| 9   | 医保类型代码 | yblxDm | Y   | CHAR | 2   | 医保类型<br><br>01：职工基本医疗保险<br><br>02：城乡居民基本医疗保险<br><br>03：离休<br><br>04：其他医疗保险<br><br>05：自费 |
| 10  | 其他医保类型 | qtyblx | Y   | VARCHAR | 100 | 不在医保类型代码中的医保类型 |
| 11  | 医保编号 | ybbh | Y   | VARCHAR | 30  |     |
| 12  | 性别代码 | xbDm | N   | CHAR | 1   | 性别<br><br>1：男<br><br>2：女 |
| 13  | 医保统筹基金支付金额 | ybtcjjzfje | Y   | DECIMAL | 18,4 | 医保统筹基金支付 |
| 14  | 其他支付金额 | qtzfje | Y   | DECIMAL | 18,4 | 其他支付 |
| 15  | 个人账户支付金额 | grzhzfje | Y   | DECIMAL | 18,4 | 个人账户支付 |
| 16  | 个人现金支付金额 | grxjzfje | Y   | DECIMAL | 18,4 | 个人现金支付 |
| 17  | 个人支付金额 | grzfje | Y   | DECIMAL | 18,4 | 个人支付 |
| 18  | 个人自费金额 | grzfje1 | Y   | DECIMAL | 18,4 | 个人自费 |
| 19  | 省市自定义要素数量 | sszdyyssl | Y   | INT | 11  |     |
| 20  | 省市自定义要素json | sszdyysjson | Y   | JSON |     |     |
| **ylfwmztdysList（特定要素类型代码为11：医疗服务（门诊）发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 项目名称 | xmmc | N   | VARCHAR | 600 |     |
| 3   | 费用明细 | fymx | Y   | VARCHAR | 100 |     |
| 4   | 单位  | dw  | Y   | VARCHAR | 300 |     |
| 5   | 发票商品数量 | fpspsl | Y   | VARCHAR | 25  | 数量  |
| 6   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 7   | 税率  | sl1 | N   | DECIMAL | 16,6 | 增值税税率/征收率 |
| 8   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 9   | 备注  | bz5 | Y   | VARCHAR | 450 |     |
| 10  | 医疗服务贯标码 | ylfwgbm | Y   | VARCHAR | 50  |     |
| **tljhlhsgjtdys（特定要素类型代码为13：拖拉机和联合收割机发票时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发动机号码 | fdjhm | Y   | VARCHAR | 40  |     |
| 2   | 底盘合格证编号 | dphgzbh | Y   | VARCHAR | 40  | 底盘号/机架号 |
| **esctdys（特定要素类型代码为15：二手车、31：二手车\*时返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 二手车销售统一发票号码 | escxstyfphm | Y   | VARCHAR | 30  | 二手车销售统一发票数电票号码 |
| 2   | 二手车销售统一纸质发票号码 | escxstyzzfphm | Y   | VARCHAR | 30  | 二手车销售统一发票号码 |
| 3   | 二手车销售统一纸质发票代码 | escxstyzzfpDm | Y   | VARCHAR | 12  | 二手车销售统一发票代码 |
| **txftdysList（特定要素类型代码为08：通行费返回）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 项目名称 | xmmc | N   | VARCHAR | 600 |     |
| 2   | 车牌号码 | cphm | N   | VARCHAR | 20  |     |
| 3   | 车辆类型代码 | cllxDm | N   | VARCHAR | 5   |     |
| 4   | 车辆类型名称 | cllxmc | N   | VARCHAR | 75  |     |
| 5   | 通行日期起 | txrqq | Y   | VARCHAR | 19  | yyyy-MM-dd HH:mm:ss |
| 6   | 通行日期止 | txrqz | Y   | VARCHAR | 19  | yyyy-MM-dd HH:mm:ss |
| 7   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 8   | 税率  | sl1 | N   | DECIMAL | 16,6 |     |
| 9   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 10  | 序号  | xh  | N   | INT | 10  |     |

原始数据为json报文示例

```json
{
    "fphm": "发票号码",
    "zzfpDm": "纸质发票代码",
    "zzfphm": "纸质发票号码",
    "kprq": "开票日期",
    "fppzDm": "发票票种代码",
    "tdyslxDm": "特定要素类型代码",
    "sflzfp": "是否蓝字发票",
    "kjhzfpdydlzfphm": "开具红字发票对应的蓝字发票号码",
    "kjhzfpdydzzfpDm": "开具红字发票对应的纸质发票代码",
    "kjhzfpdydzzfphm": "开具红字发票对应的纸质发票号码",
    "xsfnsrsbh": "销售方识别号",
    "xsfmc": "销售方名称",
    "xhfdz": "销货方地址",
    "gmfnsrsbh": "购买方识别号",
    "gmfmc": "购买方名称",
    "gmfdz": "购买方地址",
    "hjje": "合计金额",
    "hjse": "合计税额",
    "jshj": "价税合计",
    "jshjdx": "价税合计(大写)",
    "kce": "扣除额",
    "jsfsDm": "结算方式",
    "kpr": "开票人",
    "bz": "备注",
    "xmmxhs": "明细条数",
    "zzsjzjtDm": "增值税即征即退代码",
    "cktslDm": "出口退税类代码",
    "fhrxm": "复核人姓名",
    "skrxm": "收款人姓名",
    "xsfdh": "销售方电话",
    "xsfkhh": "销售方开户行",
    "xsfzh": "销售方账号",
    "gmfdh": "购买方电话",
    "gmfkhh": "购买方开户行",
    "gmfzh": "购买方账号",
    "xfnsrlxdm": "销方纳税人类型代码",
    "cpyycbs": "成品油异常标识",
    "fjysxx": {
        "fjysList": [
            {
                "sjlx": "附加要素类型",
                "fjysKey": "附加要素名称",
                "fjysValue": "附加要素值"
            },
            {
                "sjlx": "附加要素类型",
                "fjysKey": "附加要素名称",
                "fjysValue": "附加要素值"
            }
        ]
    },
    "hwxx": [
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "spfwjc": "商品服务简称",
            "hwhyslwfwmc": "货物或应税劳务、服务名称",
            "sphfwssflhbbm": "商品和服务税收分类合并编码",
            "ggxh": "规格型号",
            "dw": "单位",
            "fpjysl": "发票交易数量",
            "fpjydj": "发票交易单价",
            "slv": "税率",
            "se": "税额",
            "je": "金额",
            "kce": "扣除额",
            "sptm": "商品条码"
        },
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "spfwjc": "商品服务简称",
            "hwhyslwfwmc": "货物或应税劳务、服务名称",
            "sphfwssflhbbm": "商品和服务税收分类合并编码",
            "ggxh": "规格型号",
            "dw": "单位",
            "fpjysl": "发票交易数量",
            "fpjydj": "发票交易单价",
            "slv": "税率",
            "se": "税额",
            "je": "金额",
            "kce": "扣除额",
            "sptm": "商品条码"
        }
    ],
    "jzfwtdys": {
        "tdzzsxmbh": "土地增值税项目编号",
        "kdsbz": "跨地（市）标志"
    },
    "jzfwtdysList": [
        {
            "xh": "序号",
            "jzfwfsd": "建筑服务发生地",
            "jzxmmc": "建筑项目名称",
            "xmmc": "项目名称",
            "je": "金额",
            "sl1": "税率",
            "se": "税额"
        }
    ],
    "hwysfwtdysList": [
        {
            "xh": "序号",
            "ysgjzl": "运输工具种类",
            "ysgjph": "运输工具牌号",
            "qyd": "起运地",
            "ddd": "到达地",
            "yshwmc": "运输货物名称"
        }
    ],
    "bdcxsfwtdysList": [
        {
            "xh": "序号",
            "cqzsbh": "产权证书编号",
            "bdcdwdm": "不动产单位代码",
            "wqhtbabh": "网签合同备案编号",
            "bdczldz": "不动产坐落地址",
            "kdsbz": "跨地（市）标志",
            "tdzzsxmbh": "土地增值税项目编号",
            "hdjsjg": "核定计税价格",
            "sjcjhsje": "实际成交含税金额"
        }
    ],
    "bdcjyzltdysList": [
        {
            "xh": "序号",
            "cqzsbh": "产权证书编号",
            "bdczldz": "不动产坐落地址",
            "zlqq": "租赁期起",
            "zlqz": "租赁期止",
            "kdsbz": "跨地（市）标志"
        }
    ],
    "dsccstdys": {
        "bxdh": "保险单号",
        "cphcbdjh": "车牌号/船舶登记号",
        "skssq": "税款所属期",
        "cjh": "车架号",
        "dsccsje": "代收车船税金额",
        "znj": "滞纳金",
        "jehj": "金额合计"
    },
    "lkysfwtdysList": [
        {
            "xh": "序号",
            "cxr": "出行人",
            "cxrzjlxDm": "出行人证件类型代码",
            "sfzjhm": "身份证件号码",
            "chuxrq": "出行日期",
            "cfd": "出发地",
            "ddd": "到达地",
            "zwdj": "座位等级",
            "jtgjlxDm": "交通工具类型代码"
        }
    ],
    "ylfwzytdys": {
        "ylywlsh": "医疗业务流水号",
        "hzxm": "患者姓名",
        "hzsfzjlxDm": "患者身份证件类型代码",
        "hzsfzjhm": "患者身份证件号码",
        "blh": "病例号",
        "zyh": "住院号",
        "zykb": "住院科别",
        "zysjq": "住院时间起",
        "zysjz": "住院时间止",
        "ylyjje": "医疗预缴金额",
        "ylbjje": "医疗补缴金额",
        "yltfje": "医疗退费金额",
        "yljglxDm": "医疗机构类型代码",
        "qtyljglx": "其他医疗机构类型",
        "yblxDm": "医保类型代码",
        "qtyblx": "其他医保类型",
        "ybbh": "医保编号",
        "xbDm": "性别代码",
        "ybtcjjzfje": "医保统筹基金支付金额",
        "qtzfje": "其他支付金额",
        "grzhzfje": "个人账户支付金额",
        "grxjzfje": "个人现金支付金额",
        "grzfje": "个人支付金额",
        "grzfje1": "个人自费金额",
        "jkr": "交款人",
        "skdw": "收款单位",
        "sszdyyssl": "省市自定义要素数量",
        "sszdyysjson": {
            "sszdyysList": [
                {
                    "sszdyysxh": "省市自定义要素序号",
                    "sszdyysmc": "省市自定义要素名称",
                    "sszdyysnr": "省市自定义要素内容"
                },
                {
                    "sszdyysxh": "省市自定义要素序号",
                    "sszdyysmc": "省市自定义要素名称",
                    "sszdyysnr": "省市自定义要素内容"
                }
            ]
        }
    },
    "ylfwzytdysList": [
        {
            "ylfwzyfpmxxh": "医疗服务住院发票明细序号",
            "xmmc": "项目名称",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "bz5": "备注"
        }
    ],
    "ylfwzysftdysList": [
        {
            "zysfmxxh": "住院收费明细序号",
            "ylfwzyfpmxxh": "医疗服务住院发票明细序号",
            "fymx": "费用明细",
            "fpspsl": "发票商品数量",
            "dw": "单位",
            "je": "金额",
            "se": "税额",
            "sl1": "税率",
            "ylfwgbm": "医疗服务贯标码",
            "bz5": "备注"
        }
    ],
    "ylfwmztdys": {
        "ylywlsh": "医疗业务流水号",
        "hzxm": "患者姓名",
        "hzsfzjlxDm": "患者身份证件类型代码",
        "hzsfzjhm": "患者身份证件号码",
        "mzh": "门诊号",
        "mzjzsj": "门诊就诊时间",
        "yljglxDm": "医疗机构类型代码",
        "qtyljglx": "其他医疗机构类型",
        "yblxDm": "医保类型代码",
        "qtyblx": "其他医保类型",
        "ybbh": "医保编号",
        "xbDm": "性别代码",
        "ybtcjjzfje": "医保统筹基金支付金额",
        "qtzfje": "其他支付金额",
        "grzhzfje": "个人账户支付金额",
        "grxjzfje": "个人现金支付金额",
        "grzfje": "个人支付金额",
        "grzfje1": "个人自费金额",
        "sszdyyssl": "省市自定义要素数量",
        "sszdyysjson": {
            "sszdyysList": [
                {
                    "sszdyysxh": "省市自定义要素序号",
                    "sszdyysmc": "省市自定义要素名称",
                    "sszdyysnr": "省市自定义要素内容"
                },
                {
                    "sszdyysxh": "省市自定义要素序号",
                    "sszdyysmc": "省市自定义要素名称",
                    "sszdyysnr": "省市自定义要素内容"
                }
            ]
        }
    },
    "ylfwmztdysList": [
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "fymx": "费用明细",
            "dw": "单位",
            "fpspsl": "发票商品数量",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "bz5": "备注",
            "ylfwgbm": "医疗服务贯标码"
        }
    ],
    "tljhlhsgjtdys": {
        "fdjhm": "发动机号码",
        "dphgzbh": "底盘合格证编号"
    },
    "esctdys": {
        "escxstyfphm": "二手车销售统一发票号码",
        "escxstyzzfphm": "二手车销售统一纸质发票号码",
        "escxstyzzfpDm": "二手车销售统一纸质发票代码"
    },
    "txftdysList": [
        {
            "xmmc": "项目名称",
            "cphm": "车牌号码",
            "cllxDm": "车辆类型代码",
            "cllxmc": "车辆类型名称",
            "txrqq": "通行日期起",
            "txrqz": "通行日期止",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "xh": "序号"
        }
    ]
}
```

附加要素信息（fjysxx）的json的key值格式

|     |     |     |     |
| --- | --- | --- | --- |
| 附加要素信息（fjysxx） | **key** | **value** | **备注** |
| fjysList |     |     |
| sjlx | 附加要素类型 | 子节点 |
| fjysKey | 附加要素名称 | 子节点 |
| fjysValue | 附加要素值 | 子节点 |

省市自定义要素JSON（sszdyysjson）的json的key值格式

|     |     |     |     |
| --- | --- | --- | --- |
| 省市自定义要素JSON（sszdyysjson） | **key** | **value** | **备注** |
| sszdyysList |     |     |
| sszdyysxh | 省市自定义要素序号 | 子节点 |
| sszdyysmc | 省市自定义要素名称 | 子节点 |
| sszdyysnr | 省市自定义要素内容 | 子节点 |

### 2.取得增值税发票数据

包含以下发票类型：

01：增值税专用发票

02：货物运输业增值税专用发票

04：增值税普通发票

08：增值税电子专用发票

10：增值税电子普通发票

注：特殊票种为02：农产品收购时，购方、销方信息为反向存储，如有需要请自行进行反转。

原始数据为json报文字段说明

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票代码 | fpdm | N   | VARCHAR | 12  |     |
| 2   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 3   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 4   | 特殊票种 | tspz | Y   | VARCHAR | 2   | 02：农产品收购<br><br>03：稀土矿产品发票<br><br>04：稀土产成品发票<br><br>05：石脑油<br><br>08：成品油发票；<br><br>20：会员单位投资性黄金<br><br>21：会员单位非投资性黄金<br><br>22：客户标准黄金 |
| 5   | 发票状态标识 | fpztbz | N   | CHAR | 1   | 0：正数票<br><br>1：负数票<br><br>2：空白作废发票<br><br>3：正数作废发票<br><br>4：负数作废发票 |
| 6   | 校验码 | jym | Y   | VARCHAR | 32  |     |
| 7   | 销售方识别号 | xsfsbh | N   | VARCHAR | 20  |     |
| 8   | 销售方名称 | xsfmc | Y   | VARCHAR | 300 |     |
| 9   | 购买方税号 | gmfsbh | Y   | VARCHAR | 20  |     |
| 10  | 购买方名称 | gmfmc | Y   | VARCHAR | 300 |     |
| 11  | 代开发票真实销售方识别号 | dkXsfsbh | Y   | VARCHAR | 20  |     |
| 12  | 代开发票真实销售方名称 | dkXsfmc | Y   | VARCHAR | 300 |     |
| 13  | 作废日期 | zfrq | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 14  | 金额  | je  | Y   | DECIMAL | 18,2 |     |
| 15  | 税额  | se  | Y   | DECIMAL | 18,2 |     |
| 16  | 税率  | slv | Y   | DECIMAL | 8,5 |     |
| 17  | 价税合计 | jshj | Y   | DECIMAL | 18,2 |     |
| 18  | 备注  | bz  | Y   | VARCHAR | 610 |     |
| 19  | 开具类型（代开标识） | kjlx | N   | CHAR | 1   | 1：自开<br><br>2：代开<br><br>3：代办退税 |
| 20  | 含税税率标识 | hsslbz | Y   | CHAR | 1   | 0：不含税税率<br><br>1：含税税率<br><br>2：差额征税 |
| 21  | 适用税率标识 | syslbs | N   | VARCHAR | 1   | 0：不是<br><br>1：是<br><br>其他：不是 |
| 22  | 明细条数 | mxts | Y   | VARCHAR | 30  |     |
| 23  | 不征税金额 | bzsje | Y   | DECIMAL | 18,2 |     |
| 24  | 销售方地址电话 | xsfdzdh | Y   | VARCHAR | 190 |     |
| 25  | 销售方银行账号 | xsfyhzh | Y   | VARCHAR | 300 |     |
| 26  | 购买方地址电话 | gmfdzdh | Y   | VARCHAR | 190 |     |
| 27  | 购买方银行账号 | gmfyhzh | Y   | VARCHAR | 300 |     |
| 28  | 销方纳税人类型代码 | xfnsrlxdm | Y   | VARCHAR | 1   | 当查询发票类型为01、08时返回<br><br>1：一般纳税人<br><br>2：小规模纳税人<br><br>3：转登记小规模纳税人<br><br>4：辅导期一般纳税人<br><br>5：自然人 |
| 29  | 机动车异常标识 | jdcycbs | Y   | VARCHAR | 1   | 0：无风险<br><br>1：低风险<br><br>2：中风险<br><br>3：高风险 |
| **hwxx（货物信息）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 货物明细序号 | mxxh | N   | NUMBER | 30,0 |     |
| 2   | 货物名称 | mc  | Y   | VARCHAR | 310 |     |
| 3   | 规格型号 | ggxh | Y   | VARCHAR | 64  |     |
| 4   | 计量单位 | jldw | Y   | VARCHAR | 52  |     |
| 5   | 数量  | sl  | Y   | VARCHAR | 25  |     |
| 6   | 单价  | dj  | Y   | VARCHAR | 25  |     |
| 7   | 税率  | slv | Y   | NUMBER | 8,5 |     |
| 8   | 税额  | se  | N   | NUMBER | 18,2 |     |
| 9   | 金额  | je  | N   | NUMBER | 18,2 |     |
| 10  | 商品编码 | spbm | Y   | VARCHAR | 45  |     |
| 11  | 零税率标识 | lslbs | Y   | VARCHAR | 10  | 当查询发票类型为04、10时返回<br><br>空：代表无<br><br>0：出口退税<br><br>1：出口免税和其他免税政策<br><br>2：不征税措施<br><br>3：普通零税率 |

原始数据为json报文示例

```json
{
    "fpdm": "发票代码",
    "fphm": "发票号码",
    "kprq": "开票日期",
    "tspz": "特殊票种",
    "fpztbz": "发票状态标识",
    "jym": "校验码",
    "xsfsbh": "销售方识别号",
    "xsfmc": "销售方名称",
    "gmfsbh": "购买方税号",
    "gmfmc": "购买方名称",
    "dkXsfsbh": "代开发票真实销售方识别号",
    "dkXsfmc": "代开发票真实销售方名称",
    "zfrq": "作废日期",
    "je": "金额",
    "se": "税额",
    "slv": "税率",
    "jshj": "价税合计",
    "bz": "备注",
    "kjlx": "开具类型（代开标识）",
    "hsslbz": "含税税率标识",
    "syslbs": "适用税率标识",
    "mxts": "明细条数",
    "bzsje": "不征税金额",
    "xsfdzdh": "销售方地址电话",
    "xsfyhzh": "销售方银行账号",
    "gmfdzdh": "购买方地址电话",
    "gmfyhzh": "购买方银行账号",
    "xfnsrlxdm": "销方纳税人类型代码",
    "jdcycbs": "机动车异常标识",
    "hwxx": [
        {
            "mxxh": "货物明细序号",
            "mc": "货物名称",
            "ggxh": "规格型号",
            "jldw": "计量单位",
            "sl": "数量",
            "dj": "单价",
            "slv": "税率",
            "se": "税额",
            "je": "金额",
            "spbm": "商品编码",
            "lslbs": "零税率标识"
        },
        {
            "mxxh": "货物明细序号",
            "mc": "货物名称",
            "ggxh": "规格型号",
            "jldw": "计量单位",
            "sl": "数量",
            "dj": "单价",
            "slv": "税率",
            "se": "税额",
            "je": "金额",
            "spbm": "商品编码",
            "lslbs": "零税率标识"
        }
    ]
}
```



### 3.取得增值税普通发票（卷式）数据

包含以下发票类型：

11：卷式发票

原始数据为json报文字段说明

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **关联关系输入信息及数据说明** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票代码 | fpdm | N   | VARCHAR | 12  |     |
| 2   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 3   | 报税纳税人识别号 | bsNsrsbh | N   | VARCHAR | 20  |     |
| 4   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 5   | 销售方识别号 | xfsbh | N   | VARCHAR | 20  |     |
| 6   | 销售方名称 | xfmc | Y   | VARCHAR | 300 |     |
| 7   | 购买方税号 | gfsbh | Y   | VARCHAR | 20  |     |
| 8   | 购买方名称 | gfmc | Y   | VARCHAR | 300 |     |
| 9   | 代开发票真实销售方识别号 | dkXsfsbh | Y   | VARCHAR | 20  |     |
| 10  | 代开发票真实销售方名称 | dkXsfmc | Y   | VARCHAR | 300 |     |
| 11  | 完税凭证号 | wspzh | Y   | VARCHAR | 200 |     |
| 12  | 作废日期 | zfrq | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 13  | 特殊票种 | tspz | Y   | VARCHAR | 2   | 08：成品油发票 |
| 14  | 发票状态标识 | fpztbz | N   | CHAR | 1   | 0：正数票<br><br>1：负数票<br><br>2：空白作废发票<br><br>3：正数作废发票<br><br>4：负数作废发票 |
| 15  | 金额，单位：元 | je  | Y   | DECIMAL | 18,2 |     |
| 16  | 税额，单位：元 | se  | Y   | DECIMAL | 18,2 |     |
| 17  | 税率  | slv | Y   | DECIMAL | 8,5 |     |
| 18  | 价税合计，单位：元 | jshj | Y   | DECIMAL | 18,2 |     |
| 19  | 备注  | bz  | Y   | VARCHAR | 610 |     |
| 20  | 校验码 | jym | Y   | VARCHAR | 32  |     |
| 21  | 明细条数 | mxts | Y   | VARCHAR | 30  |     |
| 22  | 不征税金额 | bzsje | Y   | DECIMAL | 18,2 |     |
| 23  | 销售方地址电话 | xsfdzdh | Y   | VARCHAR | 190 |     |
| 24  | 销售方银行账号 | xsfyhzh | Y   | VARCHAR | 300 |     |
| 25  | 购买方地址电话 | gmfdzdh | Y   | VARCHAR | 190 |     |
| 26  | 购买方银行账号 | gmfyhzh | Y   | VARCHAR | 300 |     |
| **hwxx（货物信息）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 货物明细序号 | mxxh | Y   | NUMBER | 30,0 |     |
| 2   | 项目  | xm  | Y   | VARCHAR | 160 |     |
| 3   | 数量  | sl  | Y   | VARCHAR | 25  |     |
| 4   | 不含税单价 | dj  | Y   | VARCHAR | 25  |     |
| 5   | 不含税金额 | je  | Y   | NUMBER | 18,2 |     |
| 6   | 含税单价 | hsdj | Y   | VARCHAR | 25  |     |
| 7   | 含税金额 | hsje | Y   | NUMBER | 18,2 |     |
| 8   | 税率  | slv | Y   | NUMBER | 8,5 |     |
| 9   | 税额  | se  | N   | NUMBER | 18,2 |     |
| 10  | 商品编码 | spbm | Y   | VARCHAR | 45  |     |

原始数据为json报文示例

```json
{
    "fpdm": "发票代码",
    "fphm": "发票号码",
    "bsNsrsbh": "报税纳税人识别号",
    "kprq": "开票日期",
    "xfsbh": "销售方识别号",
    "xfmc": "销售方名称",
    "gfsbh": "购买方税号",
    "gfmc": "购买方名称",
    "dkXsfsbh": "代开发票真实销售方识别号",
    "dkXsfmc": "代开发票真实销售方名称",
    "wspzh": "完税凭证号",
    "zfrq": "作废日期",
    "tspz": "特殊票种",
    "fpztbz": "发票状态标识",
    "je": "金额，单位：元",
    "se": "税额，单位：元",
    "slv": "税率",
    "jshj": "价税合计，单位：元",
    "bz": "备注",
    "jym": "校验码",
    "mxts": "明细条数",
    "bzsje": "不征税金额",
    "xsfdzdh": "销售方地址电话",
    "xsfyhzh": "销售方银行账号",
    "gmfdzdh": "购买方地址电话",
    "gmfyhzh": "购买方银行账号",
    "hwxx": [
        {
            "mxxh": "货物明细序号",
            "xm": "项目",
            "sl": "数量",
            "dj": "不含税单价",
            "je": "不含税金额",
            "hsdj": "含税单价",
            "hsje": "含税金额",
            "slv": "税率",
            "se": "税额",
            "spbm": "商品编码"
        },
        {
            "mxxh": "货物明细序号",
            "xm": "项目",
            "sl": "数量",
            "dj": "不含税单价",
            "je": "不含税金额",
            "hsdj": "含税单价",
            "hsje": "含税金额",
            "slv": "税率",
            "se": "税额",
            "spbm": "商品编码"
        }
    ]
}
```



### 4.取得增值税普通发票（通行费）数据

包含以下发票类型：

14：通行费发票

原始数据为json报文字段说明

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **关联关系输出信息及数据说明** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票代码 | fpdm | N   | VARCHAR | 12  |     |
| 2   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 3   | 报税纳税人识别号 | bsNsrsbh | N   | VARCHAR | 20  |     |
| 4   | 开票日期 | kprq | N   | VARCHAR2 | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 5   | 特殊票种 | tspz | Y   | VARCHAR | 2   | 06：通行费（可抵扣）<br><br>07：通行费（不可抵扣） |
| 6   | 发票状态标识 | fpztbz | N   | CHAR | 1   | 0：正数票<br><br>1：负数票<br><br>2：空白作废发票<br><br>3：正数作废发票<br><br>4负数作废发票 |
| 7   | 税控码 | skm | Y   | VARCHAR | 200 |     |
| 8   | 校验码 | jym | Y   | VARCHAR | 32  |     |
| 9   | 销售方识别号 | xfsbh | N   | VARCHAR | 20  |     |
| 10  | 销售方名称 | xfmc | Y   | VARCHAR | 300 |     |
| 11  | 销售方地址电话 | xsfdzdh | Y   | VARCHAR | 190 |     |
| 12  | 销售方银行账号 | xsfyhzh | Y   | VARCHAR | 300 |     |
| 13  | 购买方税号 | gfsbh | Y   | VARCHAR | 20  |     |
| 14  | 购买方名称 | gfmc | Y   | VARCHAR | 300 |     |
| 15  | 购买方地址电话 | gmfdzdh | Y   | VARCHAR | 190 |     |
| 16  | 购买方银行账号 | gmfyhzh | Y   | VARCHAR | 300 |     |
| 17  | 代开发票真实销售方识别号 | dkXsfsbh | Y   | VARCHAR | 20  |     |
| 18  | 代开发票真实销售方名称 | dkXsfmc | Y   | VARCHAR | 300 |     |
| 19  | 完税凭证号 | wspzh | Y   | VARCHAR | 200 |     |
| 20  | 作废日期 | zfrq | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 21  | 金额，单位：元 | je  | Y   | DECIMAL | 18,2 |     |
| 22  | 税额，单位：元 | se  | Y   | DECIMAL | 18,2 |     |
| 23  | 税率  | slv | Y   | DECIMAL | 8,5 |     |
| 24  | 价税合计，单位：元 | jshj | Y   | DECIMAL | 18,2 |     |
| 25  | 备注  | bz  | Y   | VARCHAR | 610 |     |
| 26  | 不征税金额 | bzsje | Y   | DECIMAL | 18,2 |     |
| **hwxx（货物信息）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 货物明细序号 | mxxh | Y   | NUMBER | 30,0 |     |
| 2   | 货物名称 | mc  | Y   | VARCHAR | 310 | 项目名称 |
| 3   | 规格型号 | ggxh | Y   | VARCHAR | 64  | 车牌号 |
| 4   | 计量单位 | jldw | Y   | VARCHAR | 52  | 类型  |
| 5   | 数量  | sl  | Y   | VARCHAR | 25  | 通行日期起 |
| 6   | 单价  | dj  | Y   | VARCHAR | 25  | 通行日期止 |
| 7   | 税率  | slv | Y   | NUMBER | 8,5 |     |
| 8   | 税额  | se  | N   | NUMBER | 18,2 |     |
| 9   | 金额  | je  | N   | NUMBER | 18,2 |     |
| 10  | 商品编码 | spbm | Y   | STRING | 45  |     |

原始数据为json报文示例

```json
{
    "fpdm": "发票代码",
    "fphm": "发票号码",
    "bsNsrsbh": "报税纳税人识别号",
    "kprq": "开票日期",
    "tspz": "特殊票种",
    "fpztbz": "发票状态标识",
    "skm": "税控码",
    "jym": "校验码",
    "xfsbh": "销售方识别号",
    "xfmc": "销售方名称",
    "xsfdzdh": "销售方地址电话",
    "xsfyhzh": "销售方银行账号",
    "gfsbh": "购买方税号",
    "gfmc": "购买方名称",
    "gmfdzdh": "购买方地址电话",
    "gmfyhzh": "购买方银行账号",
    "dkXsfsbh": "代开发票真实销售方识别号",
    "dkXsfmc": "代开发票真实销售方名称",
    "wspzh": "完税凭证号",
    "zfrq": "作废日期",
    "je": "金额，单位：元",
    "se": "税额，单位：元",
    "slv": "税率",
    "jshj": "价税合计，单位：元",
    "bz": "备注",
    "bzsje": "不征税金额",
    "hwxx": [
        {
            "mxxh": "货物明细序号",
            "mc": "货物名称",
            "ggxh": "规格型号",
            "jldw": "计量单位",
            "sl": "数量",
            "dj": "单价",
            "slv": "税率",
            "se": "税额",
            "je": "金额",
            "spbm": "商品编码"
        },
        {
            "mxxh": "货物明细序号",
            "mc": "货物名称",
            "ggxh": "规格型号",
            "jldw": "计量单位",
            "sl": "数量",
            "dj": "单价",
            "slv": "税率",
            "se": "税额",
            "je": "金额",
            "spbm": "商品编码"
        }
    ]
}
```



### 5.取得机动车销售统一发票数据

包含以下发票类型：

03：机动车销售统一发票

原始数据为json报文字段说明

| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | 发票代码 | fpdm | Y   | VARCHAR | 12  | 数字化电子发票纸票、税控纸票 |
| 2   | 纸质发票号码 | zzfphm | Y   | VARCHAR | 8   | 税控纸质票号码 |
| 3   | 发票号码 | fphm | Y   | VARCHAR | 20  | 数字化电子发票电票号码 |
| 4   | 报税纳税人识别号 | bsNsrsbh | N   | VARCHAR | 20  |     |
| 5   | 开票日期 | kprq | N   | VARCHAR |     | YYYY-MM-DD<br><br>HH:mm:ss |
| 6   | 税控码 | skm | Y   | VARCHAR | 200 |     |
| 7   | 发票状态标识 | fpztbz | N   | CHAR | 1   | 0：正数票<br><br>1：负数票<br><br>2：空白作废发票<br><br>3：正数作废发票<br><br>4：负数作废发票 |
| 8   | 购货单位 | ghdw | Y   | VARCHAR | 370 |     |
| 9   | 购买方纳税人识别号 | gfsbh | Y   | VARCHAR | 20  |     |
| 10  | 身份证号码/组织机构代码 | sfzhm | Y   | VARCHAR | 70  |     |
| 11  | 销货单位名称 | xhdwmc | Y   | VARCHAR | 300 |     |
| 12  | 纳税人识别号 | nsrsbh | N   | VARCHAR | 20  |     |
| 13  | 地址  | dz  | Y   | VARCHAR | 250 |     |
| 14  | 电话  | dh  | Y   | VARCHAR | 120 |     |
| 15  | 开户银行 | khyhzh | Y   | VARCHAR | 250 |     |
| 16  | 帐号  | zh  | Y   | VARCHAR | 300 |     |
| 17  | 厂牌型号 | cpxh | Y   | VARCHAR | 210 |     |
| 18  | 车辆类型 | cllx | Y   | VARCHAR | 128 |     |
| 19  | 合格证书 | hgzs | Y   | VARCHAR | 160 |     |
| 20  | 进口证明书号 | jkzmsh | Y   | VARCHAR | 128 |     |
| 21  | 产地  | cd  | Y   | VARCHAR | 128 |     |
| 22  | 商检单号 | sjdh | Y   | VARCHAR | 128 |     |
| 23  | 发动机号码 | fdjhm | Y   | VARCHAR | 190 |     |
| 24  | 车架号码/车辆识别号 | cjhm | Y   | VARCHAR | 40  |     |
| 25  | 车价及价外费用(不含增值税)单位：元 | cjfy | Y   | DECIMAL | 18,2 |     |
| 26  | 增值税税率或征收率如：0.17、0.13、0.00等 | slv | Y   | DECIMAL | 8,5 |     |
| 27  | 增值税税额:单位：元 | zzsse | Y   | DECIMAL | 18,2 |     |
| 28  | 价税合计:单位：元 | jshj | Y   | DECIMAL | 18,2 |     |
| 29  | 代开单位代码 | dkdwdm | Y   | VARCHAR | 20  |     |
| 30  | 代开单位名称 | dkdwmc | Y   | VARCHAR | 300 |     |
| 31  | 开票人:开票人名称 | kpr | Y   | VARCHAR | 150 |     |
| 32  | 开票类型 | kjlx | N   | CHAR | 1   |     |
| 33  | 吨位  | dw  | Y   | VARCHAR | 64  |     |
| 34  | 限乘人数 | xcrs | Y   | VARCHAR | 40  |     |
| 35  | 抵扣标志 | dkbz | N   | CHAR | 1   |     |
| 36  | 作废日期 | zfrq | Y   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 37  | 作废人 | zfr | Y   | VARCHAR | 150 |     |
| 38  | 接收人 | jsrDm | Y   | VARCHAR | 16  |     |
| 39  | 接收人名称 | jsrMc | Y   | VARCHAR | 150 |     |
| 40  | 接收时间 | jssj | N   | DATETIME |     |     |
| 41  | 主管税务机关代码:纳税人主管税务机关 | swjgDm | Y   | VARCHAR | 11  |     |
| 42  | 接收税务机关代码 | jsswjgDm | N   | VARCHAR | 11  |     |
| 43  | 主管税务机关名称 | swjgMc | Y   | VARCHAR | 300 |     |
| 44  | 完税凭证号码 | wspzhm | Y   | VARCHAR | 200 |     |
| 45  | 报送方式 | bsfs | N   | CHAR | 1   |     |
| 46  | 编码表版本号 | bmbBbh | Y   | VARCHAR | 21  |     |
| 47  | 商品编码 | spbm | Y   | VARCHAR | 20  |     |
| 48  | 自行编码 | zxbm | Y   | VARCHAR | 40  |     |
| 49  | 优惠政策标识 | yhzcbs | Y   | CHAR | 1   |     |
| 50  | 增值税特殊管理 | zzstsgl | Y   | VARCHAR | 760 |     |
| 51  | 零税率标识 | lslbs | Y   | VARCHAR | 10  |     |
| 52  | 适用税率标识 | syslbs | Y   | VARCHAR | 1   |     |
| 53  | 3%税率开具理由 | sslkjly | Y   | VARCHAR | 2   |     |
| 54  | 机动车异常标识 | jdcycbs | Y   | VARCHAR | 1   | 0：无风险<br><br>1：低风险<br><br>2：中风险<br><br>3：高风险 |

原始数据为json报文示例

```json
{
    "fpdm": "发票代码",
    "zzfphm ": "纸质发票号码",
    "fphm": "发票号码",
    "bsNsrsbh": "报税纳税人识别号",
    "kprq": "开票日期",
    "skm": "税控码",
    "fpztbz": "发票状态标识",
    "ghdw": "购货单位",
    "gfsbh": "购买方纳税人识别号",
    "sfzhm": "身份证号码/组织机构代码",
    "xhdwmc": "销货单位名称",
    "nsrsbh": "纳税人识别号",
    "dz": "地址",
    "dh": "电话",
    "khyhzh": "开户银行",
    "zh": "帐号",
    "cpxh": "厂牌型号",
    "cllx": "车辆类型",
    "hgzs": "合格证书",
    "jkzmsh": "进口证明书号",
    "cd": "产地",
    "sjdh": "商检单号",
    "fdjhm": "发动机号码",
    "cjhm": "车架号码/车辆识别号",
    "cjfy": "车价及价外费用(不含增值税)",
    "slv": "增值税税率或征收率",
    "zzsse": "增值税税额",
    "jshj": "价税合计",
    "dkdwdm": "代开单位代码",
    "dkdwmc": "代开单位名称",
    "kpr": "开票人/开票人名称",
    "kjlx": "开票类型",
    "dw": "吨位",
    "xcrs": "限乘人数",
    "dkbz": "抵扣标志",
    "zfrq": "作废日期",
    "zfr": "作废人",
    "jsrDm": "接收人",
    "jsrMc": "接收人名称",
    "jssj": "接收时间",
    "swjgDm": "主管税务机关代码/纳税人主管税务机关",
    "jsswjgDm": "接收税务机关代码",
    "swjgMc": "主管税务机关名称",
    "wspzhm": "完税凭证号码",
    "bsfs": "报送方式",
    "bmbBbh": "编码表版本号",
    "spbm": "商品编码",
    "zxbm": "自行编码",
    "yhzcbs": "优惠政策标识",
    "zzstsgl": "增值税特殊管理",
    "lslbs": "零税率标识",
    "syslbs": "适用税率标识",
    "sslkjly": "3%税率开具理由",
    "jdcycbs": "机动车异常标识"
}
```



### 6.取得二手车销售统一发票数据

包含以下发票类型：

15：二手车销售统一发票

原始数据为json报文字段说明

| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | 发票代码 | fpdm | Y   | VARCHAR | 12  | 数字化电子发票纸票、税控纸票 |
| 2   | 纸质发票号码 | zzfphm | Y   | VARCHAR | 8   | 税控纸质票号码 |
| 3   | 发票号码 | fphm | Y   | VARCHAR | 20  | 数字化电子发票电票号码 |
| 4   | 报税纳税人识别号 | bsNsrsbh | Y   | VARCHAR | 20  |     |
| 5   | 开票日期 | kprq | Y   | VARCHAR |     | YYYY-MM-DD<br><br>HH:mm:ss |
| 6   | 税控码 | skm | Y   | VARCHAR | 32  |     |
| 7   | 买方单位/个人名称（购方名称） | gfMc | Y   | VARCHAR | 300 |     |
| 8   | 买方单位/个人代码（购方识别号） | gfDm | Y   | VARCHAR | 20  |     |
| 9   | 买方单位/个人地址 | gfDz | Y   | VARCHAR | 310 |     |
| 10  | 买方单位/个人电话 | gfDh | Y   | VARCHAR | 80  |     |
| 11  | 开票方纳税人识别号（销方识别号） | kpfNsrsbh | Y   | VARCHAR | 20  |     |
| 12  | 卖方单位/个人名称 | xfMc | Y   | VARCHAR | 300 |     |
| 13  | 卖方单位/个人代码 | xfDm | Y   | VARCHAR | 20  |     |
| 14  | 卖方单位/个人地址 | xfDz | Y   | VARCHAR | 310 |     |
| 15  | 卖方单位/个人电话 | xfDh | Y   | VARCHAR | 80  |     |
| 16  | 车牌照号 | cphm | Y   | VARCHAR | 32  |     |
| 17  | 登记证号 | djzh | Y   | VARCHAR | 32  |     |
| 18  | 车辆类型 | cllx | Y   | VARCHAR | 128 |     |
| 19  | 车架号/车辆识别号 | clsbh | Y   | VARCHAR | 64  |     |
| 20  | 厂牌型号 | cpxh | Y   | VARCHAR | 210 |     |
| 21  | 转入地车辆管理所名称 | zrdclglsMc | Y   | VARCHAR | 310 |     |
| 22  | 经营、拍卖单位名称 | jyPmMc | Y   | VARCHAR | 300 |     |
| 23  | 经营、拍卖单位地址 | jyPmDz | Y   | VARCHAR | 310 |     |
| 24  | 经营、拍卖单位纳税人识别号 | jyPmSbh | Y   | VARCHAR | 20  |     |
| 25  | 经营、拍卖单位开户行、账号 | jyPmYhZh | Y   | VARCHAR | 250 |     |
| 26  | 经营、拍卖单位电话 | jyPmDh | Y   | VARCHAR | 80  |     |
| 27  | 二手车市场名称 | escMc | Y   | VARCHAR | 300 |     |
| 28  | 二手车市场识别号 | escSbh | Y   | VARCHAR | 20  |     |
| 29  | 二手车市场地址 | escDz | Y   | VARCHAR | 310 |     |
| 30  | 二手车市场开户行、账号 | escYhZh | Y   | VARCHAR | 250 |     |
| 31  | 二手车市场电话 | escDh | Y   | VARCHAR | 80  |     |
| 32  | 车价合计：单位：元 | cjhj | Y   | DECIMAL | 18,2 |     |
| 33  | 开票人 | kpr | Y   | VARCHAR | 150 |     |
| 34  | 备注  | bz  | Y   | VARCHAR | 610 |     |
| 35  | 开票类型 | kjlx | Y   | CHAR | 1   |     |
| 36  | 商品编码 | spbm | Y   | VARCHAR | 20  |     |
| 37  | 纳税人自行编码 | zxbm | Y   | VARCHAR | 40  |     |
| 38  | 优惠政策标识 | yhzcbs | Y   | CHAR | 1   |     |
| 39  | 零税率标识 | lslbs | Y   | VARCHAR | 10  | 空：代表无<br><br>0：出口退税<br><br>1：出口免税和其他免税政策<br><br>2：不征税措施<br><br>3：普通零税率 |
| 40  | 增值税特殊管理 | zzstsgl | Y   | VARCHAR | 760 |     |
| 41  | 适用税率标识 | syslbs | Y   | VARCHAR | 1   |     |

原始数据为json报文示例

```json
{
    "fpdm": "发票代码",
    "zzfphm ": "纸质发票号码",
    "fphm": "发票号码",
    "bsNsrsbh": "报税纳税人识别号",
    "kprq": "开票日期",
    "skm": "税控码",
    "gfMc": "买方单位/个人名称（购方名称）",
    "gfDm": "买方单位/个人代码（购方识别号）",
    "gfDz": "买方单位/个人地址",
    "gfDh": "买方单位/个人电话",
    "kpfNsrsbh": "开票方纳税人识别号（销方识别号）",
    "xfMc": "卖方单位/个人名称",
    "xfDm": "卖方单位/个人代码",
    "xfDz": "卖方单位/个人地址",
    "xfDh": "卖方单位/个人电话",
    "cphm": "车牌照号",
    "djzh": "登记证号",
    "cllx": "车辆类型",
    "clsbh": "车架号/车辆识别号",
    "cpxh": "厂牌型号",
    "zrdclglsMc": "转入地车辆管理所名称",
    "jyPmMc": "经营、拍卖单位名称",
    "jyPmDz": "经营、拍卖单位地址",
    "jyPmSbh": "经营、拍卖单位纳税人识别号",
    "jyPmYhZh": "经营、拍卖单位开户行、账号",
    "jyPmDh": "经营、拍卖单位电话",
    "escMc": "二手车市场名称",
    "escSbh": "二手车市场识别号",
    "escDz": "二手车市场地址",
    "escYhZh": "二手车市场开户行、账号",
    "escDh": "二手车市场电话",
    "cjhj": "车价合计：单位：元",
    "kpr": "开票人",
    "bz": "备注",
    "kjlx": "开票类型",
    "spbm": "商品编码",
    "zxbm": "纳税人自行编码",
    "yhzcbs": "优惠政策标识",
    "lslbs": "零税率标识",
    "zzstsgl": "增值税特殊管理",
    "syslbs": "适用税率标识"
}
```



### 7.取得航空运输客票电子行程单发票数据

包含以下发票类型：

61：电子发票（航空运输客票电子行程单）

原始数据为json报文字段说明

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 2   | 是否为纸质发票 | sfwzzfp | N   | CHAR | 1   |     |
| 3   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 4   | 开具红字发票对应的蓝字发票号码 | kjhzfpdydlzfphm | Y   | VARCHAR | 30  |     |
| 5   | 发票票种代码 | fppzDm | N   | CHAR | 2   |     |
| 6   | 特定要素类型代码 | tdyslxDm | Y   | CHAR | 2   |     |
| 7   | 购买方纳税人识别号 | gmfnsrsbh | Y   | VARCHAR | 20  |     |
| 8   | 购买方名称 | gmfmc | N   | VARCHAR | 300 |     |
| 9   | 购买方地址 | gmfdz | Y   | VARCHAR | 300 |     |
| 10  | 购买方联系电话 | gmflxdh | Y   | VARCHAR | 60  |     |
| 11  | 销售方纳税人识别号 | xsfnsrsbh | N   | VARCHAR | 20  |     |
| 12  | 销售方名称 | xsfmc | N   | VARCHAR | 300 |     |
| 13  | 销售方地址 | xsfdz | Y   | VARCHAR | 300 |     |
| 14  | 销售方联系电话 | xsflxdh | Y   | VARCHAR | 60  |     |
| 15  | 购买方经办人 | gmfjbr | Y   | VARCHAR | 150 |     |
| 16  | 经办人身份证件号码 | jbrsfzjhm | Y   | VARCHAR | 30  |     |
| 17  | 经办人联系电话 | jbrlxdh | Y   | VARCHAR | 60  |     |
| 18  | 开票人 | kpr | N   | VARCHAR | 300 |     |
| 19  | 收款人 | skr | Y   | VARCHAR | 300 |     |
| 20  | 付汇人 | fhr | Y   | VARCHAR | 300 |     |
| 21  | 价税合计 | jshj | N   | DECIMAL | 18,2 |     |
| 22  | 价税合计（大写） | jshjdx | N   | VARCHAR | 100 |     |
| 23  | 结算方式代码 | jsfsDm | Y   | CHAR | 2   |     |
| 24  | 合计金额（合计不含税金额） | hjje | N   | DECIMAL | 18,2 |     |
| 25  | 合计税额 | hjse | N   | DECIMAL | 18,2 |     |
| 26  | 开票人实人认证地址信息 | kprsrrzdzxx | Y   | VARCHAR | 100 |     |
| 27  | 手机开票地址信息 | sjkpdzxx | Y   | VARCHAR | 100 |     |
| 28  | 合同编号 | htbh | Y   | VARCHAR | 60  |     |
| 29  | 纳税义务发生时间 | nsywfssj | Y   | DATETIME | 17  | YYYY-MM-DD HH:MI:SS |
| 30  | 经办人身份证件种类 | jbrsfzjzlDm | Y   | VARCHAR | 30  |     |
| 31  | 是否蓝字发票标志 | sflzfpbz | N   | CHAR | 1   | Y：是<br><br>N：否 |
| 32  | 增值税即征即退代码 | zzsjzjtDm | Y   | VARCHAR | 2   |     |
| 33  | 备注  | bz  | Y   | MEDIUMTEXT | 300 |     |
| 34  | 商品数量 | spsl | Y   | DECIMAL | 18,4 |     |
| 35  | 出口退税类代码 | cktslDm | Y   | CHAR | 2   |     |
| **hwxx（货物信息）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 项目名称 | xmmc | Y   | VARCHAR | 600 |     |
| 3   | 货物或应税劳务、服务名称 | hwhyslwfwmc | Y   | MEDIUMTEXT | 300 |     |
| 4   | 商品服务简称 | spfwjc | Y   | VARCHAR | 120 |     |
| 5   | 商品和服务税收分类合并编码 | sphfwssflhbbm | N   | CHAR | 19  |     |
| 6   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 7   | 税率  | sl1 | N   | DECIMAL | 16,6 |     |
| 8   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 9   | 扣除额 | kce | Y   | DECIMAL | 18,2 |     |
| **民航行程单电子发票特定要素信息** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票号码 | fphm | N   | VARCHAR | 30  |     |
| 2   | 国内国际标识 | gngjbz | Y   | CHAR | 1   |     |
| 3   | GP单号 | gpdh | Y   | VARCHAR | 20  |     |
| 4   | 是否蓝字发票标志 | sflzfpbz | N   | CHAR | 1   | Y：是<br><br>N：否 |
| 5   | 姓名  | xm  | Y   | VARCHAR | 49  |     |
| 6   | 证件号码 | zjhm | Y   | VARCHAR | 30  |     |
| 7   | 签注  | qz  | Y   | VARCHAR | 200 |     |
| 8   | 电子客票号码 | dzkphm | Y   | VARCHAR | 30  |     |
| 9   | 验证码 | yzm | Y   | VARCHAR | 20  |     |
| 10  | 提示信息 | tsxx | Y   | VARCHAR | 100 |     |
| 11  | 保险费 | bxf | Y   | VARCHAR | 20  |     |
| 12  | 销售网点代号 | xswddh | Y   | VARCHAR | 20  |     |
| 13  | 填开单位 | tkdw | Y   | VARCHAR | 300 |     |
| 14  | 开票日期 | kprq | N   | DATETIME |     |     |
| 15  | 销售方名称 | xsfmc | N   | VARCHAR | 300 |     |
| 16  | 销售方纳税人识别号 | xsfnsrsbh | N   | VARCHAR | 20  |     |
| 17  | 购买方名称 | gmfmc | N   | VARCHAR | 300 |     |
| 18  | 购买方纳税人识别号 | gmfnsrsbh | Y   | VARCHAR | 20  |     |
| **特定要素明细（tdysmx）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 始发站 | sfz | Y   | VARCHAR | 50  |     |
| 2   | 目的站 | mdz | Y   | VARCHAR | 50  |     |
| 3   | 航段  | hd  | Y   | NUMBER | 4   |     |
| 4   | 承运人 | cyr | Y   | VARCHAR | 20  |     |
| 5   | 航班号 | hbh | Y   | VARCHAR | 20  |     |
| 6   | 座位等级 | zwdj | Y   | VARCHAR | 20  |     |
| 7   | 承运日期 | cyrq | Y   | DATE | 8   | YYYYYMMDD |
| 8   | 起飞时间 | qfsj | Y   | DATETIME | 17  | YYYY-MM-DD HH:MI:SS |
| 9   | 客票级别/客票类别 | kpjbkplb | Y   | VARCHAR | 20  |     |
| 10  | 客票生效日期 | kpsxrq | Y   | DATE | 8   | YYYYYMMDD |
| 11  | 有效截止日期 | yxjzrq | Y   | DATE | 8   | YYYYYMMDD |
| 12  | 免费行李额 | mfxle | Y   | VARCHAR | 20  |     |

原始数据为json报文示例

```json
{
    "fphm": "发票号码",
    "sfwzzfp": "是否为纸质发票",
    "kprq": "开票日期",
    "kjhzfpdydlzfphm": "开具红字发票对应的蓝字发票号码",
    "fppzDm": "发票票种代码",
    "tdyslxDm": "特定要素类型代码",
    "gmfnsrsbh": "购买方纳税人识别号",
    "gmfmc": "购买方名称",
    "gmfdz": "购买方地址",
    "gmflxdh": "购买方联系电话",
    "xsfnsrsbh": "销售方纳税人识别号",
    "xsfmc": "销售方名称",
    "xsfdz": "销售方地址",
    "xsflxdh": "销售方联系电话",
    "gmfjbr": "购买方经办人",
    "jbrsfzjhm": "经办人身份证件号码",
    "jbrlxdh": "经办人联系电话",
    "kpr": "开票人",
    "skr": "收款人",
    "fhr": "付汇人",
    "jshj": "价税合计",
    " jshjdx ": "价税合计（大写）",
    "jsfsDm": "结算方式代码",
    "hjje": "合计金额（合计不含税金额）",
    "hjse": "合计税额",
    "kprsrrzdzxx": "开票人实人认证地址信息",
    "sjkpdzxx": "手机开票地址信息",
    "htbh": "合同编号",
    "nsywfssj": "纳税义务发生时间",
    "jbrsfzjzlDm": "经办人身份证件种类",
    "sflzfpbz": "是否蓝字发票标志",
    "zzsjzjtDm": "增值税即征即退代码",
    "bz": "备注",
    "spsl": "商品数量",
    "cktslDm ": "出口退税类代码",
    "hwxx": [
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "hwhyslwfwmc": "货物或应税劳务、服务名称",
            "spfwjc": "商品服务简称",
            "sphfwssflhbbm": "商品和服务税收分类合并编码",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "kce": "扣除额"
        },
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "hwhyslwfwmc": "货物或应税劳务、服务名称",
            "spfwjc": "商品服务简称",
            "sphfwssflhbbm": "商品和服务税收分类合并编码",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "kce": "扣除额"
        }
    ],
    "tdys": {
        "fphm": "发票号码",
        "gngjbz": "国内国际标识",
        "gpdh": "GP单号",
        "sflzfpbz": "是否蓝字发票标志",
        "xm": "姓名",
        "zjhm": "证件号码",
        "qz": "签注",
        "dzkphm": "电子客票号码",
        "yzm": "验证码",
        "tsxx": "提示信息",
        "bxf": "保险费",
        "xswddh": "销售网点代号",
        "tkdw": "填开单位",
        "kprq": "开票日期",
        "xsfmc": "销售方名称",
        "xsfnsrsbh": "销售方纳税人识别号",
        "gmfmc": "购买方名称",
        "gmfnsrsbh": "购买方纳税人识别号",
        "tdysmx": [
            {
                "sfz": "始发站",
                "mdz": "目的站",
                "hd": "航段",
                "cyr": "承运人",
                "hbh": "航班号",
                "zwdj": "座位等级",
                "cyrq": "承运日期",
                "qfsj": "起飞时间",
                "kpjbkplb": "客票级别/客票类别",
                "kpsxrq": "客票生效日期",
                "yxjzrq": "有效截止日期",
                "mfxle": "免费行李额"
            },
            {
                "sfz": "始发站",
                "mdz": "目的站",
                "hd": "航段",
                "cyr": "承运人",
                "hbh": "航班号",
                "zwdj": "座位等级",
                "cyrq": "承运日期",
                "qfsj": "起飞时间",
                "kpjbkplb": "客票级别/客票类别",
                "kpsxrq": "客票生效日期",
                "yxjzrq": "有效截止日期",
                "mfxle": "免费行李额"
            }
        ]
    }
}
```



### 8.取得铁路电子客票发票数据

包含以下发票类型：

51：电子发票（铁路电子客票）

原始数据为json报文字段说明

| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 2   | 是否为纸质发票 | sfwzzfp | N   | CHAR | 1   |     |
| 3   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 4   | 开具红字发票对应的蓝字发票号码 | kjhzfpdydlzfphm | Y   | VARCHAR | 30  |     |
| 5   | 发票票种代码 | fppzDm | N   | CHAR | 2   |     |
| 6   | 特定要素类型代码 | tdyslxDm | Y   | CHAR | 2   |     |
| 7   | 购买方纳税人识别号 | gmfnsrsbh | Y   | VARCHAR | 20  |     |
| 8   | 购买方名称 | gmfmc | N   | VARCHAR | 300 |     |
| 9   | 购买方地址 | gmfdz | Y   | VARCHAR | 300 |     |
| 10  | 购买方联系电话 | gmflxdh | Y   | VARCHAR | 60  |     |
| 11  | 销售方纳税人识别号 | xsfnsrsbh | N   | VARCHAR | 20  |     |
| 12  | 销售方名称 | xsfmc | N   | VARCHAR | 300 |     |
| 13  | 销售方地址 | xsfdz | Y   | VARCHAR | 300 |     |
| 14  | 销售方联系电话 | xsflxdh | Y   | VARCHAR | 60  |     |
| 15  | 购买方经办人 | gmfjbr | Y   | VARCHAR | 150 |     |
| 16  | 经办人身份证件号码 | jbrsfzjhm | Y   | VARCHAR | 30  |     |
| 17  | 经办人联系电话 | jbrlxdh | Y   | VARCHAR | 60  |     |
| 18  | 开票人 | kpr | N   | VARCHAR | 300 |     |
| 19  | 收款人 | skr | Y   | VARCHAR | 300 |     |
| 20  | 付汇人 | fhr | Y   | VARCHAR | 300 |     |
| 21  | 价税合计 | jshj | N   | DECIMAL | 18,2 |     |
| 22  | 价税合计（大写） | jshjdx | N   | VARCHAR | 100 |     |
| 23  | 结算方式代码 | jsfsDm | Y   | CHAR | 2   |     |
| 24  | 合计金额（合计不含税金额） | hjje | N   | DECIMAL | 18,2 |     |
| 25  | 合计税额 | hjse | N   | DECIMAL | 18,2 |     |
| 26  | 开票人实人认证地址信息 | kprsrrzdzxx | Y   | VARCHAR | 100 |     |
| 27  | 手机开票地址信息 | sjkpdzxx | Y   | VARCHAR | 100 |     |
| 28  | 合同编号 | htbh | Y   | VARCHAR | 60  |     |
| 29  | 纳税义务发生时间 | nsywfssj | Y   | DATETIME | 17  | YYYY-MM-DD HH:MI:SS |
| 30  | 经办人身份证件种类 | jbrsfzjzlDm | Y   | VARCHAR | 30  |     |
| 31  | 是否蓝字发票标志 | sflzfpbz | N   | CHAR | 1   | Y：是<br><br>N：否 |
| 32  | 增值税即征即退代码 | zzsjzjtDm | Y   | VARCHAR | 2   |     |
| 33  | 备注  | bz  | Y   | MEDIUMTEXT | 300 |     |
| 34  | 商品数量 | spsl | Y   | DECIMAL | 18,4 |     |
| 35  | 出口退税类代码 | cktslDm | Y   | CHAR | 2   |     |
| **hwxx（货物信息）** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 序号  | xh  | N   | INT | 11  |     |
| 2   | 项目名称 | xmmc | Y   | VARCHAR | 600 |     |
| 3   | 货物或应税劳务、服务名称 | hwhyslwfwmc | Y   | MEDIUMTEXT | 300 |     |
| 4   | 商品服务简称 | spfwjc | Y   | VARCHAR | 120 |     |
| 5   | 商品和服务税收分类合并编码 | sphfwssflhbbm | N   | CHAR | 19  |     |
| 6   | 金额  | je  | N   | DECIMAL | 18,2 |     |
| 7   | 税率  | sl1 | N   | DECIMAL | 16,6 |     |
| 8   | 税额  | se  | N   | DECIMAL | 18,6 |     |
| 9   | 扣除额 | kce | Y   | DECIMAL | 18,2 |     |
| **铁路电子客票特定要素信息表** |     |     |     |     |     |     |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票号码 | fphm | N   | VARCHAR | 30  |     |
| 2   | 开票日期 | kprq | N   | DATETIME |     |     |
| 3   | 业务类型名称 | ywlxmc | N   | VARCHAR | 300 |     |
| 4   | 出发站 | cfz | Y   | VARCHAR | 60  |     |
| 5   | 出发站拼音 | cfzpy | Y   | VARCHAR | 60  |     |
| 6   | 到达站 | ddz | Y   | VARCHAR | 60  |     |
| 7   | 到达站拼音 | ddzpy | Y   | VARCHAR | 60  |     |
| 8   | 乘车车次 | cccc | Y   | VARCHAR | 20  |     |
| 9   | 日期  | rq  | Y   | DATETIME |     |     |
| 10  | 出发时间 | cfsj1 | Y   | VARCHAR | 5   |     |
| 11  | 铁路电子客票票种名称 | tldzkppzmc | Y   | VARCHAR | 60  |     |
| 12  | 空调特征 | kttz | Y   | VARCHAR | 20  |     |
| 13  | 席别  | xb1 | Y   | VARCHAR | 20  |     |
| 14  | 车厢  | cx  | Y   | VARCHAR | 20  |     |
| 15  | 席位  | xw  | Y   | VARCHAR | 60  |     |
| 16  | 支付金额 | zfje | N   | DECIMAL | 18,2 |     |
| 17  | 已退金额 | ytje | Y   | DECIMAL | 18,2 |     |
| 18  | 原票票价 | yppj | Y   | DECIMAL | 18,2 |     |
| 19  | 原票出发站 | ypcfz | Y   | VARCHAR | 60  |     |
| 20  | 原票到达站 | ypddz | Y   | VARCHAR | 60  |     |
| 21  | 电子客票号 | dzkph | Y   | VARCHAR | 30  |     |
| 22  | 证件号码 | zjhm | Y   | VARCHAR | 30  |     |
| 23  | 姓名  | xm  | Y   | VARCHAR | 150 |     |
| 24  | 铁路客票优惠类型 | tlkpyhlx | Y   | VARCHAR | 30  |     |
| 25  | 原发票号码 | yfphm | Y   | VARCHAR | 30  |     |

原始数据为json报文示例

```json
{
    "fphm": "发票号码",
    "sfwzzfp": "是否为纸质发票",
    "kprq": "开票日期",
    "kjhzfpdydlzfphm": "开具红字发票对应的蓝字发票号码",
    "fppzDm": "发票票种代码",
    "tdyslxDm": "特定要素类型代码",
    "gmfnsrsbh": "购买方纳税人识别号",
    "gmfmc": "购买方名称",
    "gmfdz": "购买方地址",
    "gmflxdh": "购买方联系电话",
    "xsfnsrsbh": "销售方纳税人识别号",
    "xsfmc": "销售方名称",
    "xsfdz": "销售方地址",
    "xsflxdh": "销售方联系电话",
    "gmfjbr": "购买方经办人",
    "jbrsfzjhm": "经办人身份证件号码",
    "jbrlxdh": "经办人联系电话",
    "kpr": "开票人",
    "skr": "收款人",
    "fhr": "付汇人",
    "jshj": "价税合计",
    "jshjdx ": "价税合计（大写）",
    "jsfsDm": "结算方式代码",
    "hjje": "合计金额（合计不含税金额）",
    "hjse": "合计税额",
    "kprsrrzdzxx": "开票人实人认证地址信息",
    "sjkpdzxx": "手机开票地址信息",
    "htbh": "合同编号",
    "nsywfssj": "纳税义务发生时间",
    "jbrsfzjzlDm": "经办人身份证件种类",
    "sflzfpbz": "是否蓝字发票标志",
    "zzsjzjtDm": "增值税即征即退代码",
    "bz": "备注",
    "spsl": "商品数量",
    "cktslDm ": "出口退税类代码",
    "hwxx": [
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "hwhyslwfwmc": "货物或应税劳务、服务名称",
            "spfwjc": "商品服务简称",
            "sphfwssflhbbm": "商品和服务税收分类合并编码",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "kce": "扣除额"
        },
        {
            "xh": "序号",
            "xmmc": "项目名称",
            "hwhyslwfwmc": "货物或应税劳务、服务名称",
            "spfwjc": "商品服务简称",
            "sphfwssflhbbm": "商品和服务税收分类合并编码",
            "je": "金额",
            "sl1": "税率",
            "se": "税额",
            "kce": "扣除额"
        }
    ],
    "tdys": {
        "fphm": "发票号码",
        "kprq": "开票日期",
        "ywlxmc": "业务类型名称",
        "cfz": "出发站",
        "cfzpy": "出发站拼音",
        "ddz": "到达站",
        "ddzpy": "到达站拼音",
        "cccc": "乘车车次",
        "rq": "日期",
        "cfsj1": "出发时间",
        "tldzkppzmc": "铁路电子客票票种名称",
        "kttz": "空调特征",
        "xb1": "席别",
        "cx": "车厢",
        "xw": "席位",
        "zfje": "支付金额",
        "ytje": "已退金额",
        "yppj": "原票票价",
        "ypcfz": "原票出发站",
        "ypddz": "原票到达站",
        "dzkph": "电子客票号",
        "zjhm": "证件号码",
        "xm": "姓名",
        "tlkpyhlx": "铁路客票优惠类型",
        "yfphm": "原发票号码"
    }
}
```



### 9.取得数字化电子发票-机动车销售统一发票数据

包含以下发票类型：

83：机动车销售电子统一发票

87：纸质发票（机动车销售统一发票）

原始数据为json报文字段说明

| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 2   | 纸质发票代码 | zzfpDm | Y   | VARCHAR | 12  |     |
| 3   | 纸质发票号码 | zzfphm | Y   | VARCHAR | 20  |     |
| 4   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 5   | 发票票种代码 | fppzDm | N   | CHAR | 2   |     |
| 6   | 特定要素类型代码 | tdyslxDm | Y   | CHAR | 2   |     |
| 7   | 是否蓝字发票 | sflzfp | N   | CHAR | 1   | Y：是<br><br>N：否 |
| 8   | 开具红字发票对应的蓝字发票号码 | kjhzfpdydlzfphm | Y   | VARCHAR | 20  |     |
| 9   | 开具红字发票对应的纸质发票代码 | kjhzfpdydzzfpDm | Y   | VARCHAR | 12  |     |
| 10  | 开具红字发票对应的纸质发票号码 | kjhzfpdydzzfphm | Y   | VARCHAR | 20  |     |
| 11  | 销售方识别号 | xsfnsrsbh | Y   | VARCHAR | 20  | 纳税人识别号 |
| 12  | 销售方名称 | xsfmc | N   | VARCHAR | 150 | 销货单位名称 |
| 13  | 销货方地址 | xhfdz | Y   | VARCHAR | 250 | 地址  |
| 14  | 销售方电话 | xsfdh | Y   | VARCHAR | 60  | 电话  |
| 15  | 销售方开户行 | xsfkhh | Y   | VARCHAR | 120 | 开户银行 |
| 16  | 销售方账号 | xsfzh | Y   | VARCHAR | 100 | 账号  |
| 17  | 购买方识别号 | gmfnsrsbh | Y   | VARCHAR | 20  | 统一社会信用代码/纳税人识别号/身份证号 |
| 18  | 购买方名称 | gmfmc | N   | VARCHAR | 150 |     |
| 19  | 购买方地址 | gmfdz | Y   | VARCHAR | 300 |     |
| 20  | 购买方电话 | gmfdh | Y   | VARCHAR | 60  |     |
| 21  | 购买方开户行 | gmfkhh | Y   | VARCHAR | 120 |     |
| 22  | 购买方账号 | gmfzh | Y   | VARCHAR | 100 |     |
| 23  | 合计金额 | hjje | N   | DECIMAL | 18,2 |     |
| 24  | 合计税额 | hjse | N   | DECIMAL | 18,2 |     |
| 25  | 价税合计 | jshj | N   | DECIMAL | 18,2 |     |
| 26  | 价税合计(大写) | jshjdx | N   | VARCHAR | 300 |     |
| 27  | 开票人 | kpr | N   | VARCHAR | 300 |     |
| 28  | 备注  | bz  | Y   | VARCHAR | 450 |     |
| 29  | 车辆类型 | cllx | N   | VARCHAR | 600 |     |
| 30  | 厂牌型号 | cpxh1 | N   | VARCHAR | 150 |     |
| 31  | 产地  | cd  | Y   | VARCHAR | 300 |     |
| 32  | 合格证号 | hgzh | Y   | VARCHAR | 50  |     |
| 33  | 进口证明书号 | jkzmsh | Y   | VARCHAR | 30  |     |
| 34  | 商检单号 | sjdh | Y   | VARCHAR | 30  |     |
| 35  | 发动机号码 | fdjhm | Y   | VARCHAR | 160 |     |
| 36  | 车辆识别代号/车价号码 | clsbdh | N   | VARCHAR | 30  |     |
| 37  | 税率  | sl1 | N   | DECIMAL | 16,6 | 增值税税率或征收率 |
| 38  | 税额  | se  | N   | DECIMAL | 18,6 | 增值税税额 |
| 39  | 主管税务机关代码 | zgswjgDm | Y   | VARCHAR | 11  |     |
| 40  | 主管税务机关名称 | zgswjgmc | Y   | VARCHAR | 150 |     |
| 41  | 不含税价 | bhsj | N   | DECIMAL | 18,2 |     |
| 42  | 完税凭证号码 | wspzhm | Y   | VARCHAR | 40  |     |
| 43  | 车辆吨位 | cldw | Y   | DECIMAL | 16,4 | 吨位  |
| 44  | 限乘人数 | xcrs | Y   | VARCHAR | 4   |     |
| 45  | 商品和服务税收分类合并编码 | sphfwssflhbbm | Y   | VARCHAR | 19  |     |

原始数据为json报文示例

```json
{
    "fphm": "发票号码",
    "zzfpDm": "纸质发票代码",
    "zzfphm": "纸质发票号码",
    "kprq": "开票日期",
    "fppzDm": "发票票种代码",
    "tdyslxDm": "特定要素类型代码",
    "sflzfp": "是否蓝字发票",
    "kjhzfpdydlzfphm": "开具红字发票对应的蓝字发票号码",
    "kjhzfpdydzzfpDm": "开具红字发票对应的纸质发票代码",
    "kjhzfpdydzzfphm": "开具红字发票对应的纸质发票号码",
    "xsfnsrsbh": "销售方识别号",
    "xsfmc": "销售方名称",
    "xhfdz": "销货方地址",
    "xsfdh": "销售方电话",
    "xsfkhh": "销售方开户行",
    "xsfzh": "销售方账号",
    "gmfnsrsbh": "购买方识别号",
    "gmfmc": "购买方名称",
    "gmfdz": "购买方地址",
    "gmfdh": "购买方电话",
    "gmfkhh": "购买方开户行",
    "gmfzh": "购买方账号",
    "hjje": "合计金额",
    "hjse": "合计税额",
    "jshj": "价税合计 ",
    "jshjdx": "价税合计(大写)",
    "kpr": "开票人",
    "bz": "备注",
    "cllx": "车辆类型",
    "cpxh1": "厂牌型号",
    "cd": "产地",
    "hgzh": "合格证号",
    "jkzmsh": "进口证明书号",
    "sjdh": "商检单号",
    "fdjhm": "发动机号码",
    "clsbdh": "车辆识别代号/车价号码",
    "sl1": "税率",
    "se": "税额",
    "zgswjgDm": "主管税务机关代码",
    "zgswjgmc": "主管税务机关名称",
    "bhsj": "不含税价",
    "wspzhm": "完税凭证号码",
    "cldw": "车辆吨位",
    "xcrs": "限乘人数",
    "sphfwssflhbbm": "商品和服务税收分类合并编码"
}
```



### 10.取得数字化电子发票-二手车销售统一发票数据

包含以下发票类型：

84：二手车销售电子统一发票

88：纸质发票（二手车销售统一发票）

原始数据为json报文字段说明

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **序号** | **数据项名称** | **数据项标识符** | **是否可空** | **字段类型** | **字段长度** | **备注** |
| 1   | 发票号码 | fphm | N   | VARCHAR | 20  |     |
| 2   | 纸质发票代码 | zzfpDm | Y   | VARCHAR | 12  |     |
| 3   | 纸质发票号码 | zzfphm | Y   | VARCHAR | 20  |     |
| 4   | 开票日期 | kprq | N   | VARCHAR | 19  | YYYY-MM-DD<br><br>HH:mm:ss |
| 5   | 发票票种代码 | fppzDm | N   | CHAR | 2   |     |
| 6   | 特定要素类型代码 | tdyslxDm | Y   | CHAR | 2   | 51：正常开具<br><br>52：反向开具 |
| 7   | 是否蓝字发票 | sflzfp | N   | CHAR | 1   | Y：是<br><br>N：否 |
| 8   | 开具红字发票对应的蓝字发票号码 | kjhzfpdydlzfphm | Y   | VARCHAR | 20  |     |
| 9   | 开具红字发票对应的纸质发票代码 | kjhzfpdydzzfpDm | Y   | VARCHAR | 12  |     |
| 10  | 开具红字发票对应的纸质发票号码 | kjhzfpdydzzfphm | Y   | VARCHAR | 20  |     |
| 11  | 销售方识别号 | xsfnsrsbh | Y   | VARCHAR | 20  | 纳税人识别号/身份证号 |
| 12  | 销售方名称 | xsfmc | N   | VARCHAR | 150 | 销货单位名称 |
| 13  | 销货方地址 | xhfdz | Y   | VARCHAR | 250 | 卖方单位/个人住址 |
| 14  | 销售方电话 | xsfdh | Y   | VARCHAR | 60  | 电话  |
| 15  | 销售方开户行 | xsfkhh | Y   | VARCHAR | 120 |     |
| 16  | 销售方账号 | xsfzh | Y   | VARCHAR | 100 |     |
| 17  | 购买方识别号 | gmfnsrsbh | Y   | VARCHAR | 20  | 单位代码/税号 |
| 18  | 购买方名称 | gmfmc | N   | VARCHAR | 150 | 卖方单位/个人 |
| 19  | 购买方地址 | gmfdz | Y   | VARCHAR | 300 | 购买单位/个人住址 |
| 20  | 购买方电话 | gmfdh | Y   | VARCHAR | 60  | 电话  |
| 21  | 购买方开户行 | gmfkhh | Y   | VARCHAR | 120 |     |
| 22  | 购买方账号 | gmfzh | Y   | VARCHAR | 100 |     |
| 23  | 合计金额 | hjje | N   | DECIMAL | 18,2 |     |
| 24  | 合计税额 | hjse | N   | DECIMAL | 18,2 |     |
| 25  | 价税合计 | jshj | N   | DECIMAL | 18,2 |     |
| 26  | 价税合计(大写) | jshjdx | N   | VARCHAR | 300 |     |
| 27  | 开票人 | kpr | N   | VARCHAR | 300 |     |
| 28  | 备注  | bz  | Y   | VARCHAR | 450 |     |
| 29  | 车牌照号 | cpzh | N   | VARCHAR | 20  |     |
| 30  | 登记证号 | djzh | N   | VARCHAR | 20  |     |
| 31  | 车辆类型 | cllx | N   | VARCHAR | 600 |     |
| 32  | 车辆识别代号/车价号码 | clsbdh | N   | VARCHAR | 30  |     |
| 33  | 厂牌型号 | cpxh1 | N   | VARCHAR | 150 |     |
| 34  | 转入地车辆管理所名称 | zrdclglsmc | N   | VARCHAR | 80  |     |
| 35  | 车价合计大写 | cjhjdx | N   | VARCHAR | 300 |     |
| 36  | 车价合计小写 | cjhjxx | N   | DECIMAL | 18,2 |     |
| 37  | 拍卖单位纳税人识别号 | pmdwnsrsbh | Y   | VARCHAR | 20  |     |
| 38  | 拍卖单位纳税人名称 | pmdwnsrmc | Y   | VARCHAR | 300 |     |
| 39  | 拍卖单位开户银行 | pmdwkhyh | Y   | VARCHAR | 120 |     |
| 40  | 拍卖单位银行账号 | pmdwyhzh | Y   | VARCHAR | 50  |     |
| 41  | 拍卖单位地址 | pmdwdz | Y   | VARCHAR | 300 |     |
| 42  | 拍卖单位电话 | pwdwdh | Y   | VARCHAR | 60  |     |
| 43  | 经营单位纳税人识别号 | dwnsrsbh | Y   | VARCHAR | 20  |     |
| 44  | 经营单位纳税人名称 | jydwnsrmc | Y   | VARCHAR | 300 |     |
| 45  | 经营单位开户银行 | jydwkhyh | Y   | VARCHAR | 120 |     |
| 46  | 经营单位银行账号 | jydwyhzh | Y   | VARCHAR | 50  |     |
| 47  | 经营单位地址 | jydwdz | Y   | VARCHAR | 300 |     |
| 48  | 经营单位电话 | jydwdh | Y   | VARCHAR | 60  |     |
| 49  | 二手车市场纳税人识别号 | escscnsrsbh | Y   | VARCHAR | 20  |     |
| 50  | 二手车市场纳税人名称 | escscnsrmc | Y   | VARCHAR | 300 |     |
| 51  | 二手车市场开户银行 | escsckhyh | Y   | VARCHAR | 120 |     |
| 52  | 二手车市场银行账号 | escscyhzh | Y   | VARCHAR | 50  |     |
| 53  | 二手车市场地址 | escscdz | Y   | VARCHAR | 300 |     |
| 54  | 二手车市场电话 | escscdh | Y   | VARCHAR | 60  |     |
| 55  | 商品和服务税收分类合并编码 | sphfwssflhbbm | Y   | VARCHAR | 19  |     |

原始数据为json报文示例

```json
{
    "fphm": "发票号码",
    "zzfpDm": "纸质发票代码",
    "zzfphm": "纸质发票号码",
    "kprq": "开票日期",
    "fppzDm": "发票票种代码",
    "tdyslxDm": "特定要素类型代码",
    "sflzfp": "是否蓝字发票",
    "kjhzfpdydlzfphm": "开具红字发票对应的蓝字发票号码",
    "kjhzfpdydzzfpDm": "开具红字发票对应的纸质发票代码",
    "kjhzfpdydzzfphm": "开具红字发票对应的纸质发票号码",
    "xsfnsrsbh": "销售方识别号",
    "xsfmc": "销售方名称",
    "xhfdz": "销货方地址",
    "xsfdh": "销售方电话",
    "xsfkhh": "销售方开户行",
    "xsfzh": "销售方账号",
    "gmfnsrsbh": "购买方识别号",
    "gmfmc": "购买方名称",
    "gmfdz": "购买方地址",
    "gmfdh": "购买方电话",
    "gmfkhh": "购买方开户行",
    "gmfzh": "购买方账号",
    "hjje": "合计金额",
    "hjse": "合计税额",
    "jshj": "价税合计",
    "jshjdx": "价税合计(大写)",
    "kpr": "开票人",
    "bz": "备注",
    "cpzh": "车牌照号",
    "djzh": "登记证号",
    "cllx": "车辆类型",
    "clsbdh": "车辆识别代号/车价号码",
    "cpxh1": "厂牌型号",
    "zrdclglsmc": "转入地车辆管理所名称",
    "cjhjdx": "车价合计大写",
    "cjhjxx": "车价合计小写",
    "pmdwnsrsbh": "拍卖单位纳税人识别号",
    "pmdwnsrmc": "拍卖单位纳税人名称",
    "pmdwkhyh": "拍卖单位开户银行",
    "pmdwyhzh": "拍卖单位银行账号",
    "pmdwdz": "拍卖单位地址",
    "pwdwdh": "拍卖单位电话",
    "dwnsrsbh": "经营单位纳税人识别号",
    "jydwnsrmc": "经营单位纳税人名称",
    "jydwkhyh": "经营单位开户银行",
    "jydwyhzh": "经营单位银行账号",
    "jydwdz": "经营单位地址",
    "jydwdh": "经营单位电话",
    "escscnsrsbh": "二手车市场纳税人识别号",
    "escscnsrmc": "二手车市场纳税人名称",
    "escsckhyh": "二手车市场开户银行",
    "escscyhzh": "二手车市场银行账号",
    "escscdz": "二手车市场地址",
    "escscdh": "二手车市场电话",
    "sphfwssflhbbm": "商品和服务税收分类合并编码"
}
```



## （二）代码表

### 1.身份证件类型代码

|     |     |
| --- | --- |
| 身份证件类型码值 | 身份证件类型名称 |
| 100 | 单位  |
| 101 | 组织机构代码证 |
| 102 | 营业执照 |
| 103 | 税务登记证 |
| 199 | 其他单位证件 |
| 200 | 个人  |
| 201 | 居民身份证 |
| 202 | 军官证 |
| 203 | 武警警官证 |
| 204 | 士兵证 |
| 205 | 军队离退休干部证 |
| 206 | 残疾人证 |
| 207 | 残疾军人证（1-8级） |
| 208 | 外国护照 |
| 209 | 港澳同胞回乡证 |
| 210 | 港澳居民来往内地通行证 |
| 211 | 台胞证 |
| 212 | 中华人民共和国往来港澳通行证 |
| 213 | 台湾居民来往大陆通行证 |
| 214 | 大陆居民往来台湾通行证 |
| 215 | 外国人居留证 |
| 216 | 外交官证 |
| 217 | 使（领事）馆证 |
| 218 | 海员证 |
| 219 | 香港永久性居民身份证 |
| 220 | 台湾身份证 |
| 221 | 澳门特别行政区永久性居民身份证 |
| 222 | 外国人身份证件 |
| 223 | 高校毕业生自主创业证 |
| 224 | 就业失业登记证 |
| 225 | 退休证 |
| 226 | 离休证 |
| 227 | 中国护照 |
| 228 | 城镇退役士兵自谋职业证 |
| 229 | 随军家属身份证明 |
| 230 | 中国人民解放军军官转业证书 |
| 231 | 中国人民解放军义务兵退出现役证 |
| 232 | 中国人民解放军士官退出现役证 |
| 233 | 外国人永久居留身份证（外国人永久居留证） |
| 234 | 就业创业证 |
| 235 | 香港特别行政区护照 |
| 236 | 澳门特别行政区护照 |
| 237 | 中华人民共和国港澳居民居住证 |
| 238 | 中华人民共和国台湾居民居住证 |
| 239 | 《中华人民共和国外国人工作许可证》（A类） |
| 240 | 《中华人民共和国外国人工作许可证》（B类） |
| 241 | 《中华人民共和国外国人工作许可证》（C类） |
| 291 | 出生医学证明 |
| 299 | 其他个人证件 |

### 2.医疗机构类型代码

| 医疗机构类型码值 | 医疗机构类型 |
| --- | --- |
| A   | 医院  |
| A1  | 综合医院 |
| A100 | 综合医院 |
| A2  | 中医医院 |
| A210 | 中医（综合）医院 |
| A220 | 中医专科医院 |
| A221 | 肛肠医院 |
| A222 | 骨伤医院 |
| A223 | 针炙医院 |
| A224 | 按摩医院 |
| A229 | 其他中医专科医院 |
| A3  | 中西医结合医院 |
| A300 | 中西医结合医院 |
| A4  | 民族医院 |
| A411 | 蒙医院 |
| A412 | 藏医院 |
| A413 | 维医院 |
| A414 | 傣医院 |
| A419 | 其他民族医院 |
| A5  | 专科医院 |
| A511 | 口腔医院 |
| A512 | 眼科医院 |
| A513 | 鼻喉科医院 |
| A514 | 肿瘤医院 |
| A515 | 心血管病医院 |
| A516 | 胸科医院 |
| A517 | 血液病医院 |
| A518 | 妇产（科）医院 |
| A519 | 儿童医院 |
| A520 | 精神病医院 |
| A521 | 传染病医院 |
| A522 | 皮肤病医院 |
| A523 | 结核病及院 |
| A524 | 麻风病医院 |
| A525 | 职业病医院 |
| A526 | 骨科医院 |
| A527 | 康复医院 |
| A528 | 整形外科医院 |
| A529 | 美容医院 |
| A539 | 其他专科医院 |
| A6  | 疗养院 |
| A600 | 疗养院 |
| A7  | 护理院（站） |
| A710 | 护理院 |
| A720 | 护理站 |
| B   | 社区卫生服务中心（站） |
| B1  | 社区卫生服务中心 |
| B100 | 社区卫生服务中心 |
| B2  | 社区卫生服务站 |
| B200 | 社区卫生服务站 |
| C   | 卫生院 |
| C2  | 乡镇卫生院 |
| C210 | 中心卫生院 |
| C220 | 乡卫生院 |
| D   | 门诊部、诊所、医务室、村卫生室 |
| D1  | 门诊部 |
| D110 | 综合门诊部 |
| D120 | 中医门诊部 |
| D121 | 中医（席合）门诊部 |
| D122 | 中医专科门诊部 |
| D130 | 中西医结合门诊部 |
| D140 | 民族医门诊部 |
| D150 | 专科门诊部 |
| D151 | 并通专科门诊部 |
| D152 | 口腔门诊部 |
| D153 | 眼科门诊部 |
| D154 | 医疗美容门诊部 |
| D155 | 精神卫生门诊部 |
| D159 | 其他专科门诊部 |
| D2  | 诊所  |
| D211 | 普通诊所 |
| D212 | 中医诊所 |
| D213 | 中西医结合诊所 |
| D214 | 民族医诊所 |
| D215 | 口腔诊所 |
| D216 | 医疗美容诊所 |
| D217 | 精神卫生诊所 |
| D229 | 其他诊所 |
| D3  | 卫生所（室） |
| D300 | 卫生所（室） |
| D4  | 医务室 |
| D400 | 医务室 |
| D5  | 中小学卫生保健所 |
| D500 | 中小学卫生保健所 |
| D6  | 村卫生室 |
| D600 | 村卫生室 |
| E   | 急救中心（站） |
| E1  | 急救中心 |
| E100 | 急救中心 |
| E2  | 急救中心站 |
| E200 | 急救中心站 |
| E3  | 急救站 |
| E300 | 急救站 |
| F   | 采供血机构 |
| F1  | 血站  |
| F110 | 血液中心 |
| F120 | 中心血站 |
| F130 | 基层血站、中心血库 |
| F2  | 单采血浆站 |
| F200 | 单采血浆站 |
| G   | 妇幼保健院（所、站） |
| G1  | 妇幼保健院 |
| G100 | 妇幼保健院 |
| G2  | 妇幼保健所 |
| G200 | 妇幼保健所 |
| G3  | 妇幼保健站 |
| G300 | 妇幼保健站 |
| G4  | 生殖保健中心 |
| G400 | 生殖保健中心 |
| H   | 专科疾病防治院（所、站） |
| H1  | 专科疾病防治院 |
| H111 | 传染病防治院 |
| H112 | 结核病防治院 |
| H113 | 职业病防治院 |
| H119 | 其他专科疾病防治院 |
| H2  | 专科疾病防治所（站、中心） |
| H211 | 口腔病防治所（站、中心） |
| H212 | 精神病防治所（站、中心） |
| H213 | 皮肤病防治所（站、中心） |
| H214 | 结核病防治所（站、中心） |
| H215 | 麻凤病防治所（站、中心） |
| H216 | 职业病防治所（站、中心） |
| H217 | 寄生虫病防治所（站、中心） |
| H218 | 地方病防治所（站，中心） |
| H219 | 血吸虫病防治所（站、中心） |
| H220 | 药物戒毒所（中心） |
| H229 | 其他专科疾病防治所（站、中心） |
| J   | 疾病预防控制中心（防疫站） |
| J1  | 疾病预防控制中心 |
| J100 | 疾病预防控制中心 |
| J2  | 卫生防疫站 |
| J200 | 卫生防疫站 |
| J3  | 卫生防病中心 |
| J300 | 卫生防病中心 |
| J4  | 预防保健中心 |
| J400 | 预防保健中心 |
| K   | 卫生监督所（局） |
| K1  | 卫生监督所（局） |
| K100 | 卫生监督所（局） |
| L   | 卫生监督检验（监测、检测）所（站） |
| L1  | 卫生（综合）监督检验（监测，检测）所（站） |
| L100 | 卫生（综合）监督检验（监测，检测）所（站） |
| L2  | 环境卫生监悴检验（监测、检测）所（站） |
| L200 | 坏境卫生监督检验（监测、检测）所（站） |
| L3  | 放射卫生监督检验（监测、检测）所（站） |
| L300 | 放射卫生监督检验（监测、检测）所（站） |
| L4  | 劳动（职业、工业）卫生监督检验（监测、检测）所（站） |
| L400 | 劳动（职业、工业）卫生监督检验（监测、检测）所（站） |
| L5  | 食品卫生监督检验（监测、检测）所（站） |
| L500 | 食品卫生监督检验（监测、检测）所（站） |
| L6  | 学校卫生监督检验（监测、检测）所（站） |
| L600 | 学校卫生监督检验（监测、检测）所（站） |
| L9  | 其他卫生监督检验（监测，检测）所（站） |
| L900 | 其他卫生监督检验（监测，检测）所（站） |
| M   | 医学科学研究机构 |
| M1  | 医学科学（研究）院（所） |
| M100 | 医学科学（研究）院（所） |
| M2  | 预防医学研究院（所） |
| M200 | 预防医学研究院（所） |
| M3  | 中医（药）研究院（所） |
| M300 | 中医（药）研究院（所） |
| M4  | 中西医结合研究所 |
| M400 | 中西医结合研究所 |
| M5  | 民族医（药）学研究所 |
| M500 | 民族医（药）学研究所 |
| M6  | 医学专科研究所 |
| M611 | 基础医学研究所 |
| M612 | 病毒学研究所 |
| M613 | 老年医学研究所 |
| M614 | 肿瘤（防治）研究所 |
| M615 | 心血管病研究所 |
| M616 | 血液学研究所 |
| M617 | 整形外科研究所 |
| M618 | 特种卫生研究所 |
| M619 | 放射医学研究所 |
| M620 | 医学生物学研究所 |
| M621 | 生物医学工程研究所 |
| M622 | 实验动物研究所 |
| M623 | 结核病防治研究所 |
| M624 | 皮肤病与性病防治研究所 |
| M625 | 寄生虫病防治研允所 |
| M626 | 地方病防治研究所 |
| M627 | 血吸虫病防治研究所 |
| M628 | 流行病学研究所 |
| M629 | 医学微生物学研究所 |
| M630 | 环境卫生研究所 |
| M631 | 劳动卫生（职业病）研究所 |
| M632 | 营养与食品卫生研究所 |
| M633 | 儿少卫生研究所 |
| M634 | 医学信息研究所 |
| M649 | 其他医学专科研究所 |
| M7  | 药学研究所 |
| M700 | 药学研究所 |
| N   | 医学教育机构 |
| N1  | 医学普通高中等学校 |
| N110 | 医学普通高等学校 |
| N111 | 医学院 |
| N112 | 中医（药）学院 |
| N113 | 民族医（药）学院 |
| N119 | 其他医学普通高等学校 |
| N120 | 医学普通中等专业学校 |
| N121 | 卫生学校 |
| N122 | 中医（药）学校 |
| N123 | 民族医（药）学校 |
| N124 | 护士学校 |
| N129 | 其他医学普通中等专业学校 |
| N2  | 医学成人学校 |
| N210 | 医学成人高等学校 |
| N211 | 职工医学院 |
| N212 | 卫生管理干部学院 |
| N219 | 其他医学成人高等学校 |
| N220 | 医学成人中等学校 |
| N221 | 卫生职业（工）中等专业学校 |
| N222 | 中医（药）职业中等专业学校 |
| N223 | 卫生进修学校 |
| N229 | 其他医学成人中等学校 |
| N3  | 医学在职培训机构 |
| N300 | 医学在职培训机构 |
| O   | 健康教育所（站、中心） |
| O1  | 健康教育所 |
| O100 | 健康教育所 |
| O2  | 健康教育站（中心） |
| O200 | 健康教育站（中心） |
| P   | 其他卫生机构 |
| P1  | 临床检验中心（所、站） |
| P110 | 临床检验中心 |
| P120 | 临床检验所（站） |
| P2  | 卫生新闻出版杜 |
| P210 | 卫生图书出版社 |
| P220 | 卫生报纸出版社 |
| P230 | 卫生杂志社 |
| P290 | 其他卫生新闻出版社 |
| P9  | 其他卫生事业机构 |
| P911 | 精神病收容所 |