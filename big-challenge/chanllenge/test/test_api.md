# yolar api doc

## queryAdmin

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/admins
```
**parameters**

```
Map<String, String> map

```
**response**

```
message AdminListDTO { 
    optional Result result = 1;
    repeated Admin admin = 2;
}
```
## saveAdmin

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/admins
```
**parameters**

```
Yolar.AdminCreateOption option
message AdminCreateOption { 
    optional string name = 1;
    optional string phone = 2;
    optional string remark = 3;
    optional string avatarUrl = 6;
    optional int64 status = 7;
}

```
**response**

```
message AdminDTO { 
    optional Result result = 1;
    optional Admin admin = 2;
}
```
## getAdminById

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/admins/{adminId}
```
**parameters**

```
Long adminId

```
**response**

```
message AdminDTO { 
    optional Result result = 1;
    optional Admin admin = 2;
}
```
## getAdminByPhone

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/admins/phone/{phone}
```
**parameters**

```
String phone

```
**response**

```
message AdminDTO { 
    optional Result result = 1;
    optional Admin admin = 2;
}
```
## resetToken

**description**

```
/重置护士的tokenparamnurseIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/reset-token
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## updateAdmin

**description**

```

```
**method**

```
PATCH
```
**URL**

```
/api/yolar/v3/admins/{adminId}
```
**parameters**

```
Long adminId
Yolar.AdminUpdateOption option
message AdminUpdateOption { 
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional string remark = 4;
    optional int64 type = 5;
    optional int64 status = 6;
    optional string password = 7;
    optional string avatarUrl = 8;
}

```
**response**

```
message AdminDTO { 
    optional Result result = 1;
    optional Admin admin = 2;
}
```
## sendPhoneCaptcha

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/captcha/phone
```
**parameters**

```
Yolar.SendPhoneCaptchaOption option
message SendPhoneCaptchaOption { 
    optional string phone = 1;
}

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## validatePhoneCaptcha

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/captcha/phone/validate
```
**parameters**

```
Yolar.PhoneCaptchaOption option
message PhoneCaptchaOption { 
    optional string phone = 1;
    optional string captcha = 2;
}

```
**response**

```
message ValidateDTO { 
    optional Result result = 1;
    optional bool validate = 2;
}
```
## heartbeat

**description**

```

```
**method**

```
GET
```
**URL**

```
/guard/heartbeat
```
**parameters**

```

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## loginByPhoneAndPassword

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/login/phone-password
```
**parameters**

```
Yolar.PhonePasswordLoginOption option
message PhonePasswordLoginOption { 
    optional string phone = 1;
    optional string password = 2;
    optional LoginRole loginRole = 3;
}

```
**response**

```
message SimpleLoginDTO { 
    optional Data data = 1;
    message Data {
        optional string token = 1;
        optional int64 id = 2;
        optional LoginRole loginRole = 3;
        optional string redirectUrl = 4;
    }
    optional Result result = 2;
}
```
## loginByPhoneAndCaptcha

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/login/phone-captcha
```
**parameters**

```
Yolar.PhoneCaptchaLoginOption option
message PhoneCaptchaLoginOption { 
    optional string phone = 1;
    optional string captcha = 2;
    optional LoginRole loginRole = 3;
}

```
**response**

```
message SimpleLoginDTO { 
    optional Data data = 1;
    message Data {
        optional string token = 1;
        optional int64 id = 2;
        optional LoginRole loginRole = 3;
        optional string redirectUrl = 4;
    }
    optional Result result = 2;
}
```
## resetPasswordByPhoneCaptcha

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/login/reset-password
```
**parameters**

```
Yolar.SimpleLoginOption option
message SimpleLoginOption { 
    optional string phone = 1;
    optional string password = 2;
    optional string captcha = 3;
    optional LoginRole loginRole = 4;
}

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## loginByWeChat

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/login/wx/{code}
```
**parameters**

```
String code
Yolar.SimpleLoginOption option
message SimpleLoginOption { 
    optional string phone = 1;
    optional string password = 2;
    optional string captcha = 3;
    optional LoginRole loginRole = 4;
}

```
**response**

```
message SimpleLoginDTO { 
    optional Data data = 1;
    message Data {
        optional string token = 1;
        optional int64 id = 2;
        optional LoginRole loginRole = 3;
        optional string redirectUrl = 4;
    }
    optional Result result = 2;
}
```
## logOut

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/logout
```
**parameters**

```
Yolar.SimpleLogOutOption option
message SimpleLogOutOption { 
    optional int64 id = 1;
    optional LoginRole loginRole = 2;
}

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## createNurse

**description**

```
/创建护士paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses
```
**parameters**

```
Yolar.NurseCreateOption option
message NurseCreateOption { 
    optional int64 departmentId = 1;
    optional string name = 2;
    optional string idCard = 3;
    optional string certs = 4;
    optional string photos = 5;
    optional string title = 6;
    optional string phone = 7;
    optional string avatarUrl = 8;
    optional int64 birthday = 9;
    optional int64 gender = 10;
    optional int64 status = 11;
}

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## queryNurse

**description**

```
/护士查询接口parammap参数请参考com.youhujia.halo.yolar.YolarNurseQueryEnumreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/nurses
```
**parameters**

```
Map<String, String> map

```
**response**

```
message NurseListDTO { 
    optional Result result = 1;
    repeated Nurse nurse = 2;
}
```
## getNurseById

**description**

```
/通过nurseId查找护士paramnurseIdreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## getNurseByIds

**description**

```
/通过nurseIds查找护士nurseIds=1,2,3paramnurseIdsreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/nurses/ids
```
**parameters**

```
String nurseIds

```
**response**

```
message NurseListDTO { 
    optional Result result = 1;
    repeated Nurse nurse = 2;
}
```
## getNurseByPhone

**description**

```
/通过phone查找护士paramphonereturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/nurses/phone/{phone}
```
**parameters**

```
String phone

```
**response**

```
message NurseListDTO { 
    optional Result result = 1;
    repeated Nurse nurse = 2;
}
```
## updateNurse

**description**

```
/更新护士信息paramoptionreturn/
```
**method**

```
PATCH
```
**URL**

```
/api/yolar/v3/nurses
```
**parameters**

```
Yolar.NurseUpdateOption option
message NurseUpdateOption { 
    optional int64 nurseId = 1;
    optional string name = 2;
    optional string idCard = 3;
    optional string certs = 4;
    optional string photos = 5;
    optional string title = 6;
    optional string phone = 7;
    optional string avatarUrl = 8;
    optional int64 birthday = 9;
    optional int64 gender = 10;
}

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## getNursesByName

**description**

```
/根据护士名字获取护士paramnamereturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/nurses/name/{name}
```
**parameters**

```
String name

```
**response**

```
message NurseListDTO { 
    optional Result result = 1;
    repeated Nurse nurse = 2;
}
```
## getNurseChangeableDepartmentList

**description**

```
/获取护士可切换的科室列表paramnurseIdreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/changeable-departments
```
**parameters**

```
Long nurseId

```
**response**

```
message DepartmentListDTO { 
    optional Result result = 1;
    repeated Department department = 2;
}
```
## changeNurseDepartment

**description**

```
/更换护士科室1.并不会修改nurse.departmentId，而是找到目标科室下的护士，激活active为true2.并将其余该护士在别的科室下的身份active变为falseparamoptionreturn当前的active护士/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/change-department
```
**parameters**

```
Yolar.ChangeDepartmentOption option
message ChangeDepartmentOption { 
    optional int64 nurseId = 1;
    optional int64 fromDepartmentId = 2;
    optional int64 toDepartmentId = 3;
}

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## changeStatusNurseCompleteInfo

**description**

```
/更改护士状态-护士完善个人信息paramnurseIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/change-status/nurse-complete-info
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## changeStatusAdminPermitAuthorized

**description**

```
/更改护士状态-运营允许护士认证paramnurseIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/change-status/admin-permit-authorized
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## changeStatusAdminPermitMaster

**description**

```
/更改护士状态-运营允许护士成为护士管理员paramnurseIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/change-status/admin-permit-master
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## changeStatusAdminPermitAssistant

**description**

```
/更改护士状态-运营允许护士成为科密paramnurseIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/change-status/admin-permit-assistant
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## changeStatusNurseFailOfAuthorization

**description**

```
/更改护士状态-护士认证失败paramnurseIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/change-status/nurse-fail-of-authorization
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## changeStatusNurseUpdateInfo

**description**

```
/更改护士状态-护士重新提交认证信息paramnurseIdreturn/
```
**method**

```

```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/change-status/nurse-update-info
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## getActiveNurseListByDepartmentId

**description**

```
/获取科室下的活动护士paramdepartmentIdreturn/
```
**method**

```

```
**URL**

```
/api/yolar/v3/nurses/departments/{departmentId}/active
```
**parameters**

```
Long departmentId

```
**response**

```
message NurseListDTO { 
    optional Result result = 1;
    repeated Nurse nurse = 2;
}
```
## setNurseActive

**description**

```
/将护士置为活动paramnurseIdreturn/
```
**method**

```

```
**URL**

```
/api/yolar/v3/nurses/{nurseId}/set-active
```
**parameters**

```
Long nurseId

```
**response**

```
message NurseDTO { 
    optional Result result = 1;
    optional Nurse nurse = 2;
}
```
## resetPassword

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/password
```
**parameters**

```
Yolar.PasswordOption option
message PasswordOption { 
    optional string phone = 1;
    optional string email = 2;
    optional string password = 3;
    optional Role role = 4;

    enum Role {
        NURSE = 1;
        USER = 2;
        ADMIN = 3;
    }
}

```
**response**

```
message PasswordDTO { 
    optional int64 passwordId = 1;
    optional string phone = 2;
    optional string email = 3;
    optional string password = 4;
    optional int64 createdAt = 5;
    optional int64 updatedAt = 6;
    optional Result result = 7;
}
```
## updatePasswordRelation

**description**

```

```
**method**

```
PUT
```
**URL**

```
/api/yolar/v3/password
```
**parameters**

```
Yolar.PasswordRelationOption option
message PasswordRelationOption { 
    optional string phone = 1;
    optional string email = 2;
}

```
**response**

```
message PasswordDTO { 
    optional int64 passwordId = 1;
    optional string phone = 2;
    optional string email = 3;
    optional string password = 4;
    optional int64 createdAt = 5;
    optional int64 updatedAt = 6;
    optional Result result = 7;
}
```
## validatePassword

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/password/validate
```
**parameters**

```
Yolar.PasswordOption option
message PasswordOption { 
    optional string phone = 1;
    optional string email = 2;
    optional string password = 3;
    optional Role role = 4;

    enum Role {
        NURSE = 1;
        USER = 2;
        ADMIN = 3;
    }
}

```
**response**

```
message ValidatePasswordDTO { 
    optional Result result = 1;
    optional bool validate = 2;
}
```
## checkExistByShadowId

**description**

```
/tocheckuser"sexistinShadowWxbyuserIdandshadowWxIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/shadow-wx/exist
```
**parameters**

```
Yolar.ShadowWxAccountOption option
message ShadowWxAccountOption { 
    optional string shadowWxId = 1;
    optional string departmentId = 2;
}
Long userId

```
**response**

```
message RedirectResponseDTO { 
    optional Result result = 1;
    optional string redirectUrl = 2;
}
```
## redirectToDestinationUrl

**description**

```
/tosaveuser"sopenIdwhofromShadowWxAccountandredirectreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/shadow-wx
```
**parameters**

```
Yolar.ShadowWxAuthOption wxProfile
message ShadowWxAuthOption { 
    optional string code = 1;
    optional string state = 2;
}
Long userId

```
**response**

```
message RedirectResponseDTO { 
    optional Result result = 1;
    optional string redirectUrl = 2;
}
```
## findShadowWxAccountByDepartmentId

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/shadow/{departmentId}
```
**parameters**

```
Long departmentId

```
**response**

```
message ShadowWxAccountDTO { 
    optional int64 shadowWxAccountId = 1;
    optional string destination_url = 2;
    optional string appid = 3;
    optional string secret = 4;
    optional string note = 5;
    optional int64 createdAt = 6;
    optional int64 updatedAt = 7;
    optional Result result = 8;
    repeated int64 departmentId = 9;
    optional WxTemplateInfo info = 10;
}
```
## findByShadowWxAccountIdAndUserId

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/shadow/{shadowWxId}/user/{userId}
```
**parameters**

```
Long shadowWxId
Long userId

```
**response**

```
message ShadowWxProfileDTO { 
    optional int64 shadowWxProfileId = 1;
    optional int64 userId = 2;
    optional string openId = 3;
    optional int64 shadowWxAccountId = 4;
    optional bool isSubscribed = 5;
    optional int64 createdAt = 6;
    optional int64 updatedAt = 7;
    optional Result result = 8;
}
```
## createUser

**description**

```
/创建患者paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users
```
**parameters**

```
Yolar.UserCreateOption option
message UserCreateOption { 
    optional string nickname = 1;
    optional string avatarUrl = 2;
    optional int64 gender = 3;
    optional int64 birthday = 4;
    optional string idCard = 5;
    optional string phone = 6;
}

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## archiveUser

**description**

```
/Archive患者paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/archive
```
**parameters**

```
Yolar.ArchiveUserOption option
message ArchiveUserOption { 
    optional int64 departmentId = 1;
    repeated int64 user = 2;
}

```
**response**

```
message UserListDTO { 
    optional Result result = 1;

    repeated User user = 2;
}
```
## unarchiveUser

**description**

```
/Unarchive患者paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/unarchive
```
**parameters**

```
Yolar.UnarchiveUserOption option
message UnarchiveUserOption { 
    optional int64 departmentId = 1;
    repeated int64 user = 2;
}

```
**response**

```
message UserListDTO { 
    optional Result result = 1;

    repeated User user = 2;
}
```
## addUserToDepartment

**description**

```
/患者关注(加入)科室（批量）paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/add-to-department
```
**parameters**

```
Yolar.UserAddToDepartmentOption option
message UserAddToDepartmentOption { 
    repeated UserDepartment userDepartment = 1;

    message UserDepartment {
        optional int64 userId = 1;
        optional int64 departmentId = 2;
    }
}

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## removeUserFromDepartment

**description**

```
/删除患者和科室的关联（批量），即删除关联关系paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/remove-from-department
```
**parameters**

```
Yolar.RemoveUserFromDepartmentOption option
message RemoveUserFromDepartmentOption { 
    repeated UserDepartment userDepartment = 1;

    message UserDepartment {
        optional int64 userId = 1;
        optional int64 departmentId = 2;
    }
}

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## getUserDepartmentListByUserId

**description**

```
/查询患者关注的科室列表paramuserIdreturn/
```
**method**

```

```
**URL**

```
/api/yolar/v3/users/{userId}/departments
```
**parameters**

```
Long userId

```
**response**

```
message UserDepartmentListDTO { 
    optional Result result = 1;

    repeated UserDepartment userDepartment = 2;
}
```
## getUserListByDepartmentId

**description**

```
/查询科室下的患者列表parammap参考com.youhujia.halo.yolar.YolarUserDepartmentQueryEnumreturn/
```
**method**

```

```
**URL**

```
/api/yolar/v3/users/departments
```
**parameters**

```
Map<String, String> map

```
**response**

```
message UserListDTO { 
    optional Result result = 1;

    repeated User user = 2;
}
```
## createUserByWxInfo

**description**

```
/通过微信信息创建患者paramoptionreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/wx
```
**parameters**

```
Yolar.WechatInfoOption option
message WechatInfoOption { 
    optional string openId = 1;
    optional string nickname = 2;
    optional string avatarUrl = 3;
    optional int64 gender = 4;
    optional string unionid = 5;
}

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## getUserById

**description**

```
/通过userId获取患者paramuserIdreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/users/{userId}
```
**parameters**

```
Long userId

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## getUserByOpenId

**description**

```
/通过微信openid获取患者paramopenIdreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/users/open-id/{openId}
```
**parameters**

```
String openId

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## updateUser

**description**

```
/更新患者信息paramoptionreturn/
```
**method**

```
PATCH
```
**URL**

```
/api/yolar/v3/users
```
**parameters**

```
Yolar.UserUpdateOption option
message UserUpdateOption { 
    optional int64 userId = 1;
    optional string nickname = 2;
    optional string realname = 3;
    optional string avatarUrl = 4;
    optional int64 gender = 5;
    optional int64 birthday = 6;
    optional string idCard = 7;
    optional string phone = 8;
    optional string flag = 9;
}

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## getUserByPhone

**description**

```
/通过phone查找患者paramphonereturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/users/phone/{phone}
```
**parameters**

```
String phone

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## getUsersByNickname

**description**

```
/通过nickname查找患者paramnamereturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/users/nickname/{nickname}
```
**parameters**

```
String name

```
**response**

```
message UserListDTO { 
    optional Result result = 1;

    repeated User user = 2;
}
```
## migrateUserFromDeprecatedWxAccount

**description**

```
/迁移公众号患者paramcurrentUserIdparamoldOpenIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/{currentUserId}/migrate-from-deprecated-wx-account/{oldOpenId}
```
**parameters**

```
Long currentUserId
String oldOpenId

```
**response**

```
message MigResponse { 
    optional Result result = 1;
    optional string token = 2;
}
```
## mergeUser

**description**

```
/用户注册phone之后，可能发现已存在对应User记录，需要对应做merge处理<p>现在只处理了对应的openid不一致的情况，用于处理用户更换了，paramfromUserIdparamtoUserIdreturn/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/users/merge-user/{fromUserId}/to/{toUserId}
```
**parameters**

```
Long fromUserId
Long toUserId

```
**response**

```
message UserDTO { 
    optional Result result = 1;
    optional User user = 2;
}
```
## getUserListByIds

**description**

```
/batch接口paramuserIdsreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/users/batch/{ids}
```
**parameters**

```
String userIds

```
**response**

```
message UserListDTO { 
    optional Result result = 1;

    repeated User user = 2;
}
```
## createUserAddress

**description**

```
/createUserAddress/
```
**method**

```
POST
```
**URL**

```
/api/yolar/v3/user-addresses
```
**parameters**

```
Yolar.UserAddressCreateOption userAddressCreateOption
message UserAddressCreateOption { 
    optional string name = 1;
    optional int64 gender = 2;
    optional int64 birthday = 3;
    optional string idCard = 4;
    optional int64 relation = 5;
    optional Address address = 6;
    optional string phone = 7;
    optional bool default = 8;
    optional int64 userId = 9;
}

```
**response**

```
message UserAddressDTO { 
    optional Result result = 1;
    optional UserAddress userAddress = 2;
}
```
## getUserAddress

**description**

```
/getUserAddress/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/user-addresses/{userAddressId}
```
**parameters**

```
Long userAddressId

```
**response**

```
message UserAddressDTO { 
    optional Result result = 1;
    optional UserAddress userAddress = 2;
}
```
## updateUserAddress

**description**

```
/updateUserAddress/
```
**method**

```
PATCH
```
**URL**

```
/api/yolar/v3/user-addresses/{userAddressId}
```
**parameters**

```
Long userAddressId
Yolar.UserAddressUpdateOption userAddressUpdateOption
message UserAddressUpdateOption { 
    optional int64 userAddressId = 1;
    optional string name = 2;
    optional int64 gender = 3;
    optional int64 birthday = 4;
    optional string idCard = 5;
    optional int64 relation = 6;
    optional Address address = 7;
    optional string phone = 8;
    optional bool default = 9;
    optional int64 userId = 10;
}

```
**response**

```
message UserAddressDTO { 
    optional Result result = 1;
    optional UserAddress userAddress = 2;
}
```
## deleteUserAddress

**description**

```
/deleteUserAddress/
```
**method**

```
DELETE
```
**URL**

```
/api/yolar/v3/user-addresses/{userAddressId}
```
**parameters**

```
Long userAddressId

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## setUserAddressDefault

**description**

```
/根据userAddress设置default的默认值/
```
**method**

```
PATCH
```
**URL**

```
/api/yolar/v3/user-addresses/{userAddressId}/set-default
```
**parameters**

```
Long userAddressId
Yolar.UserAddressUpdateOption userAddressUpdateOption
message UserAddressUpdateOption { 
    optional int64 userAddressId = 1;
    optional string name = 2;
    optional int64 gender = 3;
    optional int64 birthday = 4;
    optional string idCard = 5;
    optional int64 relation = 6;
    optional Address address = 7;
    optional string phone = 8;
    optional bool default = 9;
    optional int64 userId = 10;
}

```
**response**

```
message SimpleResponse { 
    optional Result result = 1;
}
```
## getUserAddressListByUserId

**description**

```
/获取患者所有地址paramuserIdreturn/
```
**method**

```
GET
```
**URL**

```
/api/yolar/v3/user-addresses/users/{userId}
```
**parameters**

```
Long userId

```
**response**

```
message UserAddressListDTO { 
    optional Result result = 1;
    repeated UserAddress userAddress = 2;
}
```