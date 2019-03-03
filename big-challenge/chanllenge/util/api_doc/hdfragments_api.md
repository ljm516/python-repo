# hdfragments api document
## createTag

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
/api/hd-fragments/v1/tags
```
**parameters**

```
HDFragments.TagOption option
message TagOption { 
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;
}

```
**response**

```
message TagDTO { 
    optional Result result = 1;
    optional TagData data = 2;
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
message TagData{
    optional Tag tag = 1;
}
```
## updateTag

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
/api/hd-fragments/v1/tags/{tagId}
```
**parameters**

```
Long id
HDFragments.TagOption option
message TagOption { 
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;
}

```
**response**

```
message TagDTO { 
    optional Result result = 1;
    optional TagData data = 2;
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
message TagData{
    optional Tag tag = 1;
}
```
## deleteTag

**description**

```
this method not hava desc
```
**method**

```
DELETE
```
**URL**

```
/api/hd-fragments/v1/tags/{tagId}
```
**parameters**

```
Long id

```
**response**

```
message TagDTO { 
    optional Result result = 1;
    optional TagData data = 2;
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
message TagData{
    optional Tag tag = 1;
}
```
## getTagById

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
/api/hd-fragments/v1/tags/{tagId}
```
**parameters**

```
Long id

```
**response**

```
message TagDTO { 
    optional Result result = 1;
    optional TagData data = 2;
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
message TagData{
    optional Tag tag = 1;
}
```
## getChildrenOfOneTag

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
/api/hd-fragments/v1/tags/{tagId}/children
```
**parameters**

```
Long id

```
**response**

```
message TagListDTO { 
    optional Result result = 1;
    optional TagListData data = 2;
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
message TagListData{
    repeated Tag tags = 1;
}
```
## getNextLevelOfOneTag

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
/api/hd-fragments/v1/tags/{tagId}/daughter
```
**parameters**

```
Long id

```
**response**

```
message TagListDTO { 
    optional Result result = 1;
    optional TagListData data = 2;
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
message TagListData{
    repeated Tag tags = 1;
}
```
## getTags

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
/api/hd-fragments/v1/tags
```
**parameters**

```
Map<String, String> map

```
**response**

```
message TagListDTO { 
    optional Result result = 1;
    optional TagListData data = 2;
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
message TagListData{
    repeated Tag tags = 1;
}
```
## getTagsByDynamicMap

**description**

```
/**
     * 动态map组合查询，使用EntityManager的拼装sql而非jpa的Page Query.
     *
     * @param map
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/hd-fragments/v1/tags/query/dynamic-map
```
**parameters**

```
Map<String, String> map

```
**response**

```
message TagListDTO { 
    optional Result result = 1;
    optional TagListData data = 2;
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
message TagListData{
    repeated Tag tags = 1;
}
```
## getTagsAutoComplete

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
/api/hd-fragments/v1/tags/ac
```
**parameters**

```
String prefix
String ancestorIds

```
**response**

```
message TagNodeDTO { 
    optional Result result = 1;
    optional TagNodeData data = 2;
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
message TagNodeData{
    repeated TagNode nodes = 1;
}
```
## getTagPropertyListByTagId

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
/api/hd-fragments/v1/tags/{tagId}/tag-properties
```
**parameters**

```
Long tagId

```
**response**

```
message TagPropertiesDTO { 
    optional Result result = 1;
    optional TagPropertiesData data = 2;
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
message TagPropertiesData{
    repeated TagProperty properties = 1;
}
```
## transactionalTag

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
/api/hd-fragments/v1/tags/transactional
```
**parameters**

```
HDFragments.TransactionalTagOption option
message TransactionalTagOption { 
    optional TransactionalTagAddOption addOptions = 1;
    repeated TransactionalTagUpdateOption updateOptions = 2;
    repeated TagOption deleteOptions = 3;
}
message TransactionalTagAddOption{
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;

    repeated TagPropertyOption propertyOptions = 27;

    repeated TransactionalTagAddOption daughterOptions = 28;
}
message TransactionalTagUpdateOption{
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;

    repeated TagPropertyOption propertyOptions = 27;
}
message TagOption{
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;
}

```
**response**

```
message TransactionalTagDTO { 
    optional Result result = 1;
    optional TransactionalTagAddDTO addDTO = 2;
    repeated TransactionalTagUpdateDTO updateDTOs = 3;
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
message TransactionalTagAddDTO{
    optional TagDTO tag = 1;
    repeated TagPropertyDTO properties = 2;
    repeated TransactionalTagAddDTO daughters = 3;
}
message TransactionalTagUpdateDTO{
    optional TagDTO tag = 1;
    repeated TagPropertyDTO properties = 2;
}
```
## getTagAndPropertiesByTagId

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
/api/hd-fragments/v1/tags/{tagId}/tag-and-properties
```
**parameters**

```
Long tagId

```
**response**

```
message TagAndPropertyDTO { 
    optional Result result = 1;
    optional Tag tag = 2;
    repeated TagProperty properties = 3;
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
message Tag{
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;
}
message TagProperty{
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional string key = 4;
    optional string value = 5;
    optional int32 status = 6;
}
```
## getTagsAndPropertiesByTagIds

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
/api/hd-fragments/v1/tags/tags-and-properties
```
**parameters**

```
String tagIds

```
**response**

```
message TagsAndPropertiesDTO { 
    optional Result result = 1;
    repeated TagAndProperty tags = 2;
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
message TagAndProperty{
    optional Tag tag = 1;
    repeated TagProperty properties = 2;
}
```
## getTagAndPropertiesWithDaughtersByTagId

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
/api/hd-fragments/v1/tags/{tagId}/tag-and-properties-with-daughters
```
**parameters**

```
Long tagId

```
**response**

```
message TagAndPropertyWithDaughtersDTO { 
    optional Result result = 1;
    optional TagAndProperty selfTagAndProperty = 2;
    repeated TagAndProperty daughterTagAndProperties = 3;
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
message TagAndProperty{
    optional Tag tag = 1;
    repeated TagProperty properties = 2;
}
```
## getTagAndPropertiesByNameAndLevelAndParentId

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
/api/hd-fragments/v1/tags/tag-and-properties-by-name-level-parentId
```
**parameters**

```
String name
Integer level
Long parentId

```
**response**

```
message TagAndPropertyDTO { 
    optional Result result = 1;
    optional Tag tag = 2;
    repeated TagProperty properties = 3;
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
message Tag{
    optional int64 id = 1;
    optional string name = 2;
    optional int32 type = 3;
    optional int32 level = 4;
    optional int64 level1 = 5;
    optional int64 level2 = 6;
    optional int64 level3 = 7;
    optional int64 level4 = 8;
    optional int64 level5 = 9;
    optional int64 level6 = 10;
    optional int64 level7 = 11;
    optional int64 level8 = 12;
    optional int64 level9 = 13;
    optional int64 level10 = 14;
    optional int64 level11 = 15;
    optional int64 level12 = 16;
    optional int64 level13 = 17;
    optional int64 level14 = 18;
    optional int64 level15 = 19;
    optional int64 creatorId = 20;
    optional int32 creatorType = 21;
    optional int64 dptId = 22;
    optional int64 orgId = 23;
    optional bool isLeaf = 24;
    optional int64 createdAt = 25;
    optional int64 updatedAt = 26;
}
message TagProperty{
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional string key = 4;
    optional string value = 5;
    optional int32 status = 6;
}
```
## getTagsWithNameStructure

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
/api/hd-fragments/v1/tags/structure
```
**parameters**

```
Map<String, String> map

```
**response**

```
message TagNodeDTO { 
    optional Result result = 1;
    optional TagNodeData data = 2;
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
message TagNodeData{
    repeated TagNode nodes = 1;
}
```
## getTagsByDepIds

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
/api/hd-fragments/v1/tags/batch-departmentIds
```
**parameters**

```
Map<String, String> map

```
**response**

```
message TagListDTO { 
    optional Result result = 1;
    optional TagListData data = 2;
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
message TagListData{
    repeated Tag tags = 1;
}
```
## deleteTagsByIds

**description**

```
this method not hava desc
```
**method**

```
DELETE
```
**URL**

```
/api/hd-fragments/v1/tags/delete/batch-tag-ids/{tagIds}
```
**parameters**

```
String tagIds

```
**response**

```
message TagDTO { 
    optional Result result = 1;
    optional TagData data = 2;
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
message TagData{
    optional Tag tag = 1;
}
```
## createTagToObject

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
/api/hd-fragments/v1/tag-2-objects
```
**parameters**

```
HDFragments.TagToObjectOption option
message TagToObjectOption { 
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional int64 objectId = 4;
    optional int32 objectType = 5;
    optional int32 mappingType = 6;
    optional int64 creatorId = 7;
    optional int32 creatorType = 8;
    optional int64 creatorDptId = 9;
    optional int64 creatorOrgId = 10;
}

```
**response**

```
message TagToObjectDTO { 
    optional Result result = 1;
    optional TagToObjectData data = 2;
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
message TagToObjectData{
    optional TagToObject tag2Object = 1;
}
```
## updateTagToObject

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
/api/hd-fragments/v1/tag-2-objects/{id}
```
**parameters**

```
Long id
HDFragments.TagToObjectOption option
message TagToObjectOption { 
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional int64 objectId = 4;
    optional int32 objectType = 5;
    optional int32 mappingType = 6;
    optional int64 creatorId = 7;
    optional int32 creatorType = 8;
    optional int64 creatorDptId = 9;
    optional int64 creatorOrgId = 10;
}

```
**response**

```
message TagToObjectDTO { 
    optional Result result = 1;
    optional TagToObjectData data = 2;
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
message TagToObjectData{
    optional TagToObject tag2Object = 1;
}
```
## deleteTagToObject

**description**

```
this method not hava desc
```
**method**

```
DELETE
```
**URL**

```
/api/hd-fragments/v1/tag-2-objects/{id}
```
**parameters**

```
Long id

```
**response**

```
message TagToObjectDTO { 
    optional Result result = 1;
    optional TagToObjectData data = 2;
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
message TagToObjectData{
    optional TagToObject tag2Object = 1;
}
```
## getTagToObjectById

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
/api/hd-fragments/v1/tag-2-objects/{id}
```
**parameters**

```
Long id

```
**response**

```
message TagToObjectDTO { 
    optional Result result = 1;
    optional TagToObjectData data = 2;
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
message TagToObjectData{
    optional TagToObject tag2Object = 1;
}
```
## getTagToObjects

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
/api/hd-fragments/v1/tag-2-objects
```
**parameters**

```
Map<String, String> map

```
**response**

```
message TagToObjectsDTO { 
    optional Result result = 1;
    optional TagToObjectsData data = 2;
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
message TagToObjectsData{
    repeated TagToObject tag2Objects = 1;
}
```
## transactionalTagToObject

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
/api/hd-fragments/v1/tag-2-objects/transactional
```
**parameters**

```
HDFragments.TransactionalTagToObjectOption option
message TransactionalTagToObjectOption { 
    repeated TagToObjectOption addOptions = 1;
    repeated TagToObjectOption deleteOptions = 2;
}
message TagToObjectOption{
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional int64 objectId = 4;
    optional int32 objectType = 5;
    optional int32 mappingType = 6;
    optional int64 creatorId = 7;
    optional int32 creatorType = 8;
    optional int64 creatorDptId = 9;
    optional int64 creatorOrgId = 10;
}

```
**response**

```
message TransactionalTagToObjectDTO { 
    optional Result result = 1;
    repeated TagToObjectDTO addDTOs = 2;
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
message TagToObjectDTO{
    optional Result result = 1;
    optional TagToObjectData data = 2;
}
```
## createTagProperty

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
/api/hd-fragments/v1/tag-properties
```
**parameters**

```
HDFragments.TagPropertyOption option
message TagPropertyOption { 
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional string key = 4;
    optional string value = 5;
}

```
**response**

```
message TagPropertyDTO { 
    optional Result result = 1;
    optional TagPropertyData data = 2;
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
message TagPropertyData{
    optional TagProperty property = 1;
}
```
## createTagProperties

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
/api/hd-fragments/v1/tag-properties/batch
```
**parameters**

```
HDFragments.TagPropertiesOption option
message TagPropertiesOption { 
    repeated TagPropertyOption properties = 1;
}
message TagPropertyOption{
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional string key = 4;
    optional string value = 5;
}

```
**response**

```
message TagPropertiesDTO { 
    optional Result result = 1;
    optional TagPropertiesData data = 2;
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
message TagPropertiesData{
    repeated TagProperty properties = 1;
}
```
## updateTagProperty

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
/api/hd-fragments/v1/tag-properties/{tagPropertyId}
```
**parameters**

```
Long tagPropertyId
HDFragments.TagPropertyOption option
message TagPropertyOption { 
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional string key = 4;
    optional string value = 5;
}

```
**response**

```
message TagPropertyDTO { 
    optional Result result = 1;
    optional TagPropertyData data = 2;
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
message TagPropertyData{
    optional TagProperty property = 1;
}
```
## deleteTagProperty

**description**

```
this method not hava desc
```
**method**

```
DELETE
```
**URL**

```
/api/hd-fragments/v1/tag-properties/{tagPropertyId}
```
**parameters**

```
Long tagPropertyId

```
**response**

```
message TagPropertyDTO { 
    optional Result result = 1;
    optional TagPropertyData data = 2;
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
message TagPropertyData{
    optional TagProperty property = 1;
}
```
## getTagPropertyById

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
/api/hd-fragments/v1/tag-properties/{tagPropertyId}
```
**parameters**

```
Long tagPropertyId

```
**response**

```
message TagPropertyDTO { 
    optional Result result = 1;
    optional TagPropertyData data = 2;
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
message TagPropertyData{
    optional TagProperty property = 1;
}
```
## getTagPropertyByTagIdAndKey

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
/api/hd-fragments/v1/tag-properties/tagId-with-key
```
**parameters**

```
Long tagId
String key

```
**response**

```
message TagPropertyDTO { 
    optional Result result = 1;
    optional TagPropertyData data = 2;
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
message TagPropertyData{
    optional TagProperty property = 1;
}
```
## getTagPropertiesByTagId

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
/api/hd-fragments/v1/tag-properties
```
**parameters**

```
Long tagId

```
**response**

```
message TagPropertiesDTO { 
    optional Result result = 1;
    optional TagPropertiesData data = 2;
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
message TagPropertiesData{
    repeated TagProperty properties = 1;
}
```
## getTagProperties

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
/api/hd-fragments/v1/tag-properties/query
```
**parameters**

```
Map<String, String> map

```
**response**

```
message TagPropertiesDTO { 
    optional Result result = 1;
    optional TagPropertiesData data = 2;
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
message TagPropertiesData{
    repeated TagProperty properties = 1;
}
```
## transactionalTagProperty

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
/api/hd-fragments/v1/tag-properties/transactional
```
**parameters**

```
HDFragments.TransactionalTagPropertyOption option
message TransactionalTagPropertyOption { 
    repeated TagPropertyOption addOptions = 1;
    repeated TagPropertyOption updateOptions = 2;
    repeated TagPropertyOption deleteOptions = 3;
}
message TagPropertyOption{
    optional int64 id = 1;
    optional int64 tagId = 2;
    optional int32 tagType = 3;
    optional string key = 4;
    optional string value = 5;
}

```
**response**

```
message TransactionalTagPropertyDTO { 
    optional Result result = 1;
    repeated TagPropertyDTO addDTOs = 2;
    repeated TagPropertyDTO updateDTOs = 3;
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
message TagPropertyDTO{
    optional Result result = 1;
    optional TagPropertyData data = 2;
}
```
## deleteTagPropertiesByIds

**description**

```
this method not hava desc
```
**method**

```
DELETE
```
**URL**

```
/api/hd-fragments/v1/tag-properties/delete/batch-tag-property-ids/{tagPropertyIds}
```
**parameters**

```
String tagPropertyIds

```
**response**

```
message TagPropertyDTO { 
    optional Result result = 1;
    optional TagPropertyData data = 2;
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
message TagPropertyData{
    optional TagProperty property = 1;
}
```
## getTagPropertyListByTagIdsAndKey

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
/api/hd-fragments/v1/tag-properties/query/key/{keyValue}/byTagIds
```
**parameters**

```
COMMON.IdsOption option
message IdsOption { 
    repeated int64 ids = 1;
}
String keyValue

```
**response**

```
message TagPropertiesDTO { 
    optional Result result = 1;
    optional TagPropertiesData data = 2;
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
message TagPropertiesData{
    repeated TagProperty properties = 1;
}
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