# farmer api document
## getHomeOrderList

**description**

```
/**
*首页接口-返回待接单的List首页接口目前是别的应用调用，页面中的订单信息请求该接口。
*
*@paramqueryMap
*@return
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/workbench
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message OrderCenterDTO { 
    message Order {
        optional int64 orderId = 1;
        optional int64 nurseId = 2;
        optional int64 servingTime = 3;
        optional int64 orderTime = 4;
        message Status {
            optional int64 statusType = 1;
            optional string statusDisplayMsg = 2;
            optional string statusDescMsg = 3;
            optional string statusColor = 4;
            optional int64 amount = 5;
        }
        message Item {
            optional int64 itemId = 1;
            optional string name = 2;
            optional int64 price = 3;
            optional int64 period = 4;
            optional string pic = 5;
            optional string desc = 6;
        }
        message Patient {
            optional int64 patientId = 1;
            optional string phone = 2;
            optional string name = 3;
            optional int64 gender = 4;
            optional int64 age = 5;
            optional string address = 6;
            optional string avatarUrl = 7;
        }
        message Action {
            optional int64 actionId = 1;
            optional int64 actionType = 2;
            optional int64 order = 3;
            optional string title = 4;
            optional string desc = 5;
            message Progress {
                optional string msg = 1;
                optional string color = 2;
            }
            message Content {
                optional string title = 1;
                optional string desc = 2;
                optional int64 id = 3;
                message progress {
                    optional int64 status = 1;
                    optional string statusMsg = 2;
                    optional string color = 3;
                }
            }
        }
        message AvailableAction {
            optional string title = 1;
            optional string action = 2;
        }
        message ApplyRefund {
            optional string title = 1;
            optional string cause = 2;
            optional int64 money = 3;
            optional string desc = 4;
        }
        message Review {
            optional int64 reviewTime = 1;
            optional int64 score = 2;
            optional string reviewContent = 3;
            message Patient {
                optional int64 patientId = 1;
                optional string name = 2;
                optional string avatarUrl = 3;
            }
        }

        optional Status statusAction = 5;
        optional Item item = 6;
        optional Patient patient = 7;
        optional Action action = 8;
        optional AvailableAction availableAction = 9;
        optional ApplyRefund applyRefund = 10;
        optional Review review = 11;
        optional string orderNo = 12;
    }

    optional Result result = 1;
    repeated Order order = 2;
    optional string bannerURL = 3;
    optional int64 waitServingOrderNum = 4;
    optional bool openService = 5;
    optional int64 nurseId = 6;
    optional bool hasSickbedMonitor = 7;
}
```
## getAcceptedOrderList

**description**

```
/**
*获得已接单和待接单的列表
*
*@paramqueryMap
*@return
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message OrderCenterDTO { 
    message Order {
        optional int64 orderId = 1;
        optional int64 nurseId = 2;
        optional int64 servingTime = 3;
        optional int64 orderTime = 4;
        message Status {
            optional int64 statusType = 1;
            optional string statusDisplayMsg = 2;
            optional string statusDescMsg = 3;
            optional string statusColor = 4;
            optional int64 amount = 5;
        }
        message Item {
            optional int64 itemId = 1;
            optional string name = 2;
            optional int64 price = 3;
            optional int64 period = 4;
            optional string pic = 5;
            optional string desc = 6;
        }
        message Patient {
            optional int64 patientId = 1;
            optional string phone = 2;
            optional string name = 3;
            optional int64 gender = 4;
            optional int64 age = 5;
            optional string address = 6;
            optional string avatarUrl = 7;
        }
        message Action {
            optional int64 actionId = 1;
            optional int64 actionType = 2;
            optional int64 order = 3;
            optional string title = 4;
            optional string desc = 5;
            message Progress {
                optional string msg = 1;
                optional string color = 2;
            }
            message Content {
                optional string title = 1;
                optional string desc = 2;
                optional int64 id = 3;
                message progress {
                    optional int64 status = 1;
                    optional string statusMsg = 2;
                    optional string color = 3;
                }
            }
        }
        message AvailableAction {
            optional string title = 1;
            optional string action = 2;
        }
        message ApplyRefund {
            optional string title = 1;
            optional string cause = 2;
            optional int64 money = 3;
            optional string desc = 4;
        }
        message Review {
            optional int64 reviewTime = 1;
            optional int64 score = 2;
            optional string reviewContent = 3;
            message Patient {
                optional int64 patientId = 1;
                optional string name = 2;
                optional string avatarUrl = 3;
            }
        }

        optional Status statusAction = 5;
        optional Item item = 6;
        optional Patient patient = 7;
        optional Action action = 8;
        optional AvailableAction availableAction = 9;
        optional ApplyRefund applyRefund = 10;
        optional Review review = 11;
        optional string orderNo = 12;
    }

    optional Result result = 1;
    repeated Order order = 2;
    optional string bannerURL = 3;
    optional int64 waitServingOrderNum = 4;
    optional bool openService = 5;
    optional int64 nurseId = 6;
    optional bool hasSickbedMonitor = 7;
}
```
## gedOrderDetail

**description**

```
/**
*根据Order获得新订单详情
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/{orderId}/detail
```
**parameters**

```
Long orderId
Map<String, String> queryMap

```
**response**

```
message OrderDetailDTO { 

    message Order {
        message Status {
            optional int64 statusType = 1;
            optional string statusDisplayMsg = 2;
            optional string statusDescMsg = 3;
            optional string color = 4;
            optional int64 amount = 5;
        }
        message Item {
            optional int64 itemId = 1;
            optional string name = 2;
            optional int64 price = 3;
            optional int64 period = 4;
            optional string pic = 5;
            optional string desc = 6;
        }
        message Patient {
            optional int64 patientId = 1;
            optional string phone = 2;
            optional string name = 3;
            optional int64 gender = 4;
            optional int64 age = 5;
            optional string address = 6;
            optional string avatarUrl = 7;
        }
        message Action {
            optional int64 actionId = 1;
            optional int64 actionType = 2;
            optional int64 order = 3;
            optional string title = 4;
            optional string desc = 5;
            message Progress {
                optional string msg = 1;
                optional string color = 2;
            }
            message Content {
                optional string title = 1;
                optional int64 id = 2;
                message progress {
                    optional int64 status = 1;
                    optional string statusMsg = 2;
                    optional string color = 3;
                }
                optional progress pro = 3;
                message WindowInfo {
                    optional string title = 1;
                    optional string summary = 2;
                }
                optional WindowInfo windowInfo = 4;
            }
            optional Progress progress = 6;
            repeated Content content = 7;
            optional AvailableAction availableAction = 8;
        }
        message AvailableAction {
            optional string title = 1;
            optional string action = 2;
            optional int64 status = 3;
        }
        message ApplyRefund {
            optional string title = 1;
            optional string cause = 2;
            optional int64 money = 3;
            optional string desc = 4;
        }
        message Review {
            optional int64 reviewTime = 1;
            optional int64 score = 2;
            optional string reviewContent = 3;
            message Patient {
                optional int64 patientId = 1;
                optional string name = 2;
                optional string avatarUrl = 3;
            }
            optional Patient patient = 4;
        }

        optional int64 orderId = 1;
        optional int64 nurseId = 2;
        optional int64 servingTime = 3;
        optional int64 orderTime = 4;
        optional Status statusAction = 5;
        optional Item item = 6;
        optional Patient patient = 7;
        repeated Action action = 8;
        repeated AvailableAction availableAction = 9;
        optional ApplyRefund applyRefund = 10;
        optional Review review = 11;
        optional string orderNo = 12;
    }
    optional Result result = 1;
    optional Order order = 2;
}
```
## getServiceMessage

**description**

```
/**
*服务设置管理页面接口&&可服务项目接口
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/{nurseId}/serviceManager
```
**parameters**

```
Long nurseId
Map<String, String> queryMap

```
**response**

```
message ServiceCenterDTO { 
    message AvailableService {
        message Item {
            optional int64 itemId = 1;
            optional string name = 2;
            optional int64 status = 3;
            optional int64 price = 4;
            optional string pic = 5;
            optional string desc = 6;
        }
        repeated Item item = 1;
    }
    message Review {
        optional int64 reviewTime = 1;
        optional int64 score = 2;
        optional string reviewContent = 3;
        message Patient {
            optional int64 patientId = 1;
            optional string name = 2;
            optional string avatarUrl = 3;
        }
        optional Patient patient = 4;
    }
    optional Result result = 1;
    optional bool pushServiceStatus = 2;
    optional int64 orderIncome = 3;
    optional int64 nurseId = 4;
    repeated Review review = 5;
    optional AvailableService availableService = 6;
    optional int64 aveScore = 7;
    optional string hotline = 8;
}
```
## applyRefundEvent

**description**

```
/**
*护士申请进入运营介入
*
*@paramupdateOption
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
/api/nurses/order/v1/refund/{orderId}
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## getOpinionEvent

**description**

```
/**
*征求服务人员退款意见
*
*@paramupdateOption
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
api/nurses/order/v1/{orderId}/nurseOpinion
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## cancelOrder

**description**

```
/**
*服务人员主动取消订单
*
*@paramupdateOption
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
api/nurses/order/v1/{orderId}/nurseCancel
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## updateWouldProvideService

**description**

```
/**
*护士更新愿意服务的项目
*
*@paramupdateOption
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
api/nurses/order/v1/{itemId}/updateService
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## nurseCompleteOrder

**description**

```
/**
*详情页-护士确定完成订单
*
*@param
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
api/nurses/order/v1/{orderId}/nurseComplete
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## nurserCompleteService

**description**

```
/**
*详情页-护士确定完成订单的当前服务
*
*@param
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
api/nurses/order/v1/{orderId}/completeService
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## nurserPushService

**description**

```
/**
*接受推送接口
*
*@paramnurseId
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
api/nurses/order/v1/{nurseId}/pushService
```
**parameters**

```
Long nurseId

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## nurserAcceptOrder

**description**

```
/**
*接单
*
*@param
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
/api/nurses/order/v1/{orderId}/accept
```
**parameters**

```
RequestEntity<Farmer.OrderUpdateOption> updateOption
message OrderUpdateOption { 
    optional int64 nurseId = 1;
    optional int64 orderId = 2;
    optional int64 serviceId = 3;
    optional bool isAgree = 4;
    optional string content = 5;
    optional string cancelReason = 6;
    optional int64 status = 7;
    optional int64 pushServiceStatus = 8;
}

```
**response**

```
message OrderUpdateDTO { 
    optional Result result = 1;
}
```
## getUserDetail

**description**

```
/**
*新建
*/**二期
*查看用户详情
*
*@param
*@return
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/getUserDetail
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message UserInfoDTO { 
    optional UserInfo userInfo = 1;
    optional Result result = 2;
}
```
## getAllService

**description**

```
/**
*获取当前科室下的所有服务商品
*
*@param
*@return
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/getAllService
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message OrderServiceDTO { 
    repeated Item item = 1;
    optional Result result = 2;
}
```
## getAllServiceNurse

**description**

```
/**
*获取当前科室下的所有服务护士
*
*@param
*@return
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/getAllServiceNurse
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message ServiceNurseDTO { 
    repeated Nurse nurse = 1;
    optional Result result = 2;

}
```
## getServiceTime

**description**

```
/**
*获取当前科室下的所有服务时间
*
*@param
*@return
*/
```
**method**

```
GET
```
**URL**

```
/api/nurses/order/v1/getServiceTime
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message ServiceTimeDTO { 
    repeated ServiceTime serviceTime = 1;
    optional Result result = 2;
}
```
## createOrderUser

**description**

```
/**
*新建用户
*
*@param
*@return
*/
```
**method**

```
POST
```
**URL**

```
/api/nurses/order/v1/createUser
```
**parameters**

```
RequestEntity<Farmer.UserAddOption> addOption
message UserAddOption { 
    optional int64 userId = 1;
    optional string name = 2;
    optional int64 gender = 3;
    optional string birthday = 4;
    optional string phone = 5;
    optional string idCard = 6;
    optional Address address = 7;
}
Map<String, String> queryMap

```
**response**

```
message UserAddDTO { 
    optional Result result = 1;
    optional UserInfo userInfo = 2;
}
```
## addOrder

**description**

```
/**
*创建订单
*
*@param
*@return
*/
```
**method**

```
POST
```
**URL**

```
/api/nurses/order/v1/createAssistOrder
```
**parameters**

```
RequestEntity<Farmer.CreateOrderOption> createOrderOption
message CreateOrderOption { 
    optional int64 itemId = 1;
    optional int64 nurseId = 2;
    optional int64 servingTime = 3;
    optional int64 patientId = 4;
    optional int64 servingNurseId = 5;
}
Map<String, String> queryMap

```
**response**

```
message OrderAddDTO { 
    optional Result result = 1;
    optional int64 patientId = 2;
    optional int64 serviceNurseId = 3;
    optional int64 item = 4;
    optional ServiceTimeDTO serviceTime = 5;
    optional int64 nurseId = 6;
    optional int64 orderId = 7;
    optional int64 price = 8;
}
```
## changeUserMsg

**description**

```
/**
*选择并修改原有用户的信息
*
*@param
*@return
*/
```
**method**

```
PATCH
```
**URL**

```
/api/nurses/order/v1/updateUser
```
**parameters**

```
RequestEntity<Farmer.UpdateOption> updateOption
message UpdateOption { 
    optional int64 userId = 1;
    optional string name = 2;
    optional int64 gender = 3;
    optional string phone = 4;
    optional Address address = 5;
    optional string idCard = 6;
    optional string birthday = 7;

}
Map<String, String> queryMap

```
**response**

```
message ChangeResultDTO { 
    optional Result result = 1;

}
```
## initCharge

**description**

```
/**
*支付
*/
```
**method**

```
PATCH
```
**URL**

```
/api/nurses/order/v1/{nurseId}/nurse-pay
```
**parameters**

```
Long orderId
Map<String, String> queryMap

```
**response**

```
message InitiateChargeResultDTO { 
    optional Result result = 1;
    optional string chargeJson = 2;
}
```