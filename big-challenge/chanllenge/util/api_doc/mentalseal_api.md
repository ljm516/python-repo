# mentalseal api document
## getAdminByAdminIdAndApp

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/authority/admin
```
**parameters**

```
MentalSeal.CheckPermissionOption option
message CheckPermissionOption { 
    optional int64 id = 1;
    optional int64 appId = 2;
    optional string appSecret = 3;
}

```
**response**

```
message AdminDTO { 
    optional Data data = 1;
    message Data{
        optional Admin admin = 1;
    }
    optional Result result = 2;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getNurseByNurseIdAndApp

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/authority/nurse
```
**parameters**

```
MentalSeal.CheckPermissionOption option
message CheckPermissionOption { 
    optional int64 id = 1;
    optional int64 appId = 2;
    optional string appSecret = 3;
}

```
**response**

```
message NurseDTO { 
    optional Data data = 1;
    message Data{
        optional Nurse nurse = 1;
    }
    optional Result result = 2;
}
message Nurse{
    optional int64 nurseId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional int64 personId = 5;
    optional int64 organizationId = 6;
    optional int64 departmentId = 7;
    optional string idCard = 8;
    optional int64 personType = 9;
    optional string title = 10;
    optional int64 birthday = 11;
    optional int64 gender = 12;
    optional string avatarUrl = 13;
    optional string token = 14;
    optional int64 updatedAt = 15;
    optional int64 createdAt = 16;
    repeated App app = 17;
    optional bool active = 18;
    optional string certs = 19;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getAdmins

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/admin
```
**parameters**

```
Map<String, String> map

```
**response**

```
message AdminListDTO { 
    optional Data data = 1;
    optional int64 draw = 2;
    optional int64 recordsTotal = 3;
    optional int64 recordsFiltered = 4;
    message Data{
        repeated Admin admin = 1;
    }
    optional Result result = 5;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getAdminByIds

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/admin/ids
```
**parameters**

```
String adminIds

```
**response**

```
message AdminListDTO { 
    optional Data data = 1;
    optional int64 draw = 2;
    optional int64 recordsTotal = 3;
    optional int64 recordsFiltered = 4;
    message Data{
        repeated Admin admin = 1;
    }
    optional Result result = 5;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## saveAdmin

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/admin
```
**parameters**

```
MentalSeal.AdminSaveOption adminSaveOption
message AdminSaveOption { 
    optional string name = 1;
    optional string phone = 2;
    optional string remark = 3;
}
Map<String, String> map

```
**response**

```
message AdminDTO { 
    optional Data data = 1;
    message Data{
        optional Admin admin = 1;
    }
    optional Result result = 2;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getAdmin

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/admin/{id}
```
**parameters**

```
Long adminId
Map<String, String> map

```
**response**

```
message AdminDTO { 
    optional Data data = 1;
    message Data{
        optional Admin admin = 1;
    }
    optional Result result = 2;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## updateAdmin

**description**

```
this method not hava desc
```
**method**

```
PATCH
```
**URL**

```
/api/mentalseal/v1/admin/{id}
```
**parameters**

```
Long adminId
Map<String, String> map
MentalSeal.AdminUpdateOption adminUpdateOption
message AdminUpdateOption { 
    optional string name = 1;
    optional int64 status = 2;
    optional string remark = 3;
    optional string avatarUrl = 4;
    repeated AppId app = 5;
}
message AppId{
    optional int64 appId = 1;
    repeated RoleId role = 2;
    message RoleId{
        optional int64 roleId = 1;
    }
}

```
**response**

```
message AdminDTO { 
    optional Data data = 1;
    message Data{
        optional Admin admin = 1;
    }
    optional Result result = 2;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getAdminListByRoleIds

**description**

```
/**
     * 通过 roleIds 获取 AdminList
     *
     * @param roleIds 如 1,2,3 用逗号隔开
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/admin/role
```
**parameters**

```
String roleIds

```
**response**

```
message AdminListDTO { 
    optional Data data = 1;
    optional int64 draw = 2;
    optional int64 recordsTotal = 3;
    optional int64 recordsFiltered = 4;
    message Data{
        repeated Admin admin = 1;
    }
    optional Result result = 5;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getAppList

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/admin/app
```
**parameters**

```

```
**response**

```
message AppListDTO { 
    optional Data data = 1;
    message Data{
        repeated App app = 1;
    }
    optional Result result = 2;
}
message App{
    optional int64 appId = 1;
    optional string appName = 2;
    optional string appSecret = 3;
    optional string appPath = 4;
    optional string appDescription = 5;
    repeated Role role = 6;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## saveApp

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/app
```
**parameters**

```
MentalSeal.AppSaveOption appSaveOption
message AppSaveOption { 
    optional string appName = 1;
    optional string appPath = 2;
    optional string appDescription = 3;
}
Map<String, String> map

```
**response**

```
message AppDTO { 
    optional Data data = 1;
    message Data{
        optional App app = 1;
    }
    optional Result result = 2;
}
message App{
    optional int64 appId = 1;
    optional string appName = 2;
    optional string appSecret = 3;
    optional string appPath = 4;
    optional string appDescription = 5;
    repeated Role role = 6;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getApp

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/app/{id}
```
**parameters**

```
Long appId
Map<String, String> map

```
**response**

```
message AppDTO { 
    optional Data data = 1;
    message Data{
        optional App app = 1;
    }
    optional Result result = 2;
}
message App{
    optional int64 appId = 1;
    optional string appName = 2;
    optional string appSecret = 3;
    optional string appPath = 4;
    optional string appDescription = 5;
    repeated Role role = 6;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## updateApp

**description**

```
this method not hava desc
```
**method**

```
PUT
```
**URL**

```
/api/mentalseal/v1/app/{id}
```
**parameters**

```
Long appId
Map<String, String> map
MentalSeal.AppUpdateOption appUpdateOption
message AppUpdateOption { 
    optional string appName = 1;
    optional string appDescription = 2;
}

```
**response**

```
message AppDTO { 
    optional Data data = 1;
    message Data{
        optional App app = 1;
    }
    optional Result result = 2;
}
message App{
    optional int64 appId = 1;
    optional string appName = 2;
    optional string appSecret = 3;
    optional string appPath = 4;
    optional string appDescription = 5;
    repeated Role role = 6;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## addRoleToApp

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/app/{id}/role
```
**parameters**

```
Long appId
Map<String, String> map
MentalSeal.RoleSaveOption roleSaveOption
message RoleSaveOption { 
    optional string roleName = 1;
    optional string roleDescription = 2;
    optional Scope scope = 3;
}
message Scope{
      repeated int64 organizationId = 1;
      repeated int64 departmentId = 2;
      optional bool isYHJ = 3;
}

```
**response**

```
message RoleDTO { 
    optional Data data = 1;
    message Data{
        optional int64 roleId = 1;
        optional string roleName = 2;
        optional string roleDescription = 3;
        optional Scope scope = 4;
    }
    optional Result result = 2;
    repeated string permission = 3;
}
message Scope{
      repeated int64 organizationId = 1;
      repeated int64 departmentId = 2;
      optional bool isYHJ = 3;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getPermissionBundlesOfApp

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/app/{id}/permission-bundles
```
**parameters**

```
Long appId

```
**response**

```
PermissionBundles
```
## getPermissionBundlesOfRole

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/app/role/{id}/permission-bundles
```
**parameters**

```
Long roleId

```
**response**

```
List
```
## heartbeat

**description**

```
this method not hava desc
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
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## login

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/login/password
```
**parameters**

```
MentalSeal.LoginOption loginOption
message LoginOption { 
    optional string phone = 1;
    optional string password = 2;
}

```
**response**

```
message AdminDTO { 
    optional Data data = 1;
    message Data{
        optional Admin admin = 1;
    }
    optional Result result = 2;
}
message Admin{
    optional int64 adminId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional string remark = 5;
    optional string avatarUrl = 6;
    optional string token = 7;
    optional int64 updatedAt = 8;
    optional int64 createdAt = 9;
    repeated App app = 10;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## createNurseRole

**description**

```
this method not hava desc
```
**method**

```
POST
```
**URL**

```
/api/mentalseal/v1/admin/app
```
**parameters**

```
MentalSeal.NurseRoleOption body
message NurseRoleOption { 
    optional int64 nurse_id = 1;
    optional int64 app_id = 2;
    optional int64 role_id = 3;
}

```
**response**

```
message NurseRoleDTO { 
    optional Data data = 1;
    message Data{
        optional NurseRole NurseRole = 1;
    }
    optional Result result = 2;
}
message NurseRole{
    optional int64 id = 1;
    optional int64 nurse_id = 2;
    optional int64 role_id = 3;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getNurseById

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/nurse/{id}
```
**parameters**

```
Long nurseId
Map<String, String> map

```
**response**

```
message NurseDTO { 
    optional Data data = 1;
    message Data{
        optional Nurse nurse = 1;
    }
    optional Result result = 2;
}
message Nurse{
    optional int64 nurseId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional int64 personId = 5;
    optional int64 organizationId = 6;
    optional int64 departmentId = 7;
    optional string idCard = 8;
    optional int64 personType = 9;
    optional string title = 10;
    optional int64 birthday = 11;
    optional int64 gender = 12;
    optional string avatarUrl = 13;
    optional string token = 14;
    optional int64 updatedAt = 15;
    optional int64 createdAt = 16;
    repeated App app = 17;
    optional bool active = 18;
    optional string certs = 19;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## getNurseListByIds

**description**

```
this method not hava desc
```
**method**

```
GET
```
**URL**

```
/api/mentalseal/v1/nurse
```
**parameters**

```
String nurseIds

```
**response**

```
message NurseListDTO { 
    optional Data data = 1;
    message Data{
        repeated Nurse nurse = 1;
    }
    optional Result result = 2;
}
message Nurse{
    optional int64 nurseId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional int64 personId = 5;
    optional int64 organizationId = 6;
    optional int64 departmentId = 7;
    optional string idCard = 8;
    optional int64 personType = 9;
    optional string title = 10;
    optional int64 birthday = 11;
    optional int64 gender = 12;
    optional string avatarUrl = 13;
    optional string token = 14;
    optional int64 updatedAt = 15;
    optional int64 createdAt = 16;
    repeated App app = 17;
    optional bool active = 18;
    optional string certs = 19;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```
## updateRoleToNurse

**description**

```
this method not hava desc
```
**method**

```
PATCH
```
**URL**

```
/api/mentalseal/v1/admin/role/nurse
```
**parameters**

```
MentalSeal.NurseRoleUpdateOption nurseRoleUpdateOption
message NurseRoleUpdateOption { 
    optional int64 nurseId = 1;
    repeated AppId app = 2;
}
message AppId{
    optional int64 appId = 1;
    repeated RoleId role = 2;
    message RoleId{
        optional int64 roleId = 1;
    }
}

```
**response**

```
message NurseDTO { 
    optional Data data = 1;
    message Data{
        optional Nurse nurse = 1;
    }
    optional Result result = 2;
}
message Nurse{
    optional int64 nurseId = 1;
    optional string name = 2;
    optional string phone = 3;
    optional int64 status = 4;
    optional int64 personId = 5;
    optional int64 organizationId = 6;
    optional int64 departmentId = 7;
    optional string idCard = 8;
    optional int64 personType = 9;
    optional string title = 10;
    optional int64 birthday = 11;
    optional int64 gender = 12;
    optional string avatarUrl = 13;
    optional string token = 14;
    optional int64 updatedAt = 15;
    optional int64 createdAt = 16;
    repeated App app = 17;
    optional bool active = 18;
    optional string certs = 19;
}
message Result{
    optional bool success = 1;
    optional int64 code = 2;
    optional string msg = 3;
    optional string displaymsg = 4;
    optional string message4Log = 5;
    optional string message4Show = 6;
    optional string info = 7;
    optional string resetToken = 8;
}
```