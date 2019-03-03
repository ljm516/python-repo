# civilization api document
## getArticleUserInteractionByUserId

**description**

```
/**
     * 获取患者对某篇文章的互动
     *
     * @param userId
     * @param articleId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/{articleId}/user-interaction/{userId}
```
**parameters**

```
Long userId
Long articleId

```
**response**

```
message ArticleUserInteractionDTO { 
    optional int64 articleId = 1;
    optional bool liked = 2;
    optional bool favored = 3;
    optional bool read = 4;
    optional Result result = 5;
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
## getArticleInteractionById

**description**

```
/**
     * 获取单篇文章的互动情况
     *
     * @param articleId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/{articleId}/interaction
```
**parameters**

```
Long articleId

```
**response**

```
message ArticleInteractionDTO { 
    optional int64 articleId = 1;
    optional int64 likeCount = 2;
    optional Result result = 3;
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
## getArticleContentById

**description**

```
/**
     * 获取单篇文章的详情
     *
     * @param articleId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/{articleId}/content
```
**parameters**

```
Long articleId

```
**response**

```
message ArticleContentDTO { 
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional Result result = 13;
    optional int64 updateAt = 14;
    optional int64 departmentId = 15;
    optional int64 statusValue = 16;
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
## getArticleUserInteractionListByUserId

**description**

```
/**
     * 获取患者和所有文章互动情况
     *
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/user-interaction/{userId}
```
**parameters**

```
Long userId

```
**response**

```
message ArticleUserInteractionListDTO { 
    message Article {
        optional int64 id = 1;
        optional string name = 2;
        optional string brief = 3;
        optional string bannerUrl = 4;
    }
    message ArticleUserInteraction {
        optional Article article = 1;
        optional bool liked = 2;
        optional bool favored = 3;
        optional bool read = 4;
    }
    optional Result result = 1;
    repeated ArticleUserInteraction articleUserInteraction = 2;
}
message Article{
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional int64 departmentId = 13;
    optional int64 statusValue = 14;
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
message ArticleUserInteraction{
    optional int64 articleId = 1;
    optional bool liked = 2;
    optional bool favored = 3;
    optional bool read = 4;
}
```
## getArticleInteractionListByIds

**description**

```
/**
     * 根据文章Id批量获取文章的互动情况
     *
     * @param option
     * @return
     */
```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/articles/interaction
```
**parameters**

```
Civilization.ArticleQueryBatchOption option
message ArticleQueryBatchOption { 
    repeated int64 articleId = 1;
}

```
**response**

```
message ArticleInteractionListDTO { 
    message ArticleInteraction {
        optional int64 articleId = 1;
        optional int64 likeCount = 2;
    }
    optional Result result = 1;
    repeated ArticleInteraction articleInteraction = 2;
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
message ArticleInteraction{
    optional int64 articleId = 1;
    optional int64 likeCount = 2;
}
```
## getArticleContentByIds

**description**

```
/**
     * /**
     * 根据文章Id批量获取文章详情
     *
     * @param option
     * @return
     */
```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/articles/content
```
**parameters**

```
Civilization.ArticleQueryBatchOption option
message ArticleQueryBatchOption { 
    repeated int64 articleId = 1;
}

```
**response**

```
message ArticleListDTO { 
    message Article {
        optional int64 id = 1;
        optional string name = 2;
        optional string brief = 3;
        optional int64 creatorId = 4;
        optional string creatorName = 5;
        optional string bannerUrl = 6;
        optional int64 departmentId = 7;
        optional int64 categoryId = 8;
        optional string categoryName = 9;
        optional int64 status = 10;
        optional int64 updateAt = 11;

    }
    optional Result result = 1;
    repeated Article article = 2;
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
message Article{
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional int64 departmentId = 13;
    optional int64 statusValue = 14;
}
```
## getArticlesByDepartmentId

**description**

```
/**
     * /**
     * 根据科室Id批量获取文章
     *
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/content/{departmentId}
```
**parameters**

```
Long departmentId

```
**response**

```
message ArticleListDTO { 
    message Article {
        optional int64 id = 1;
        optional string name = 2;
        optional string brief = 3;
        optional int64 creatorId = 4;
        optional string creatorName = 5;
        optional string bannerUrl = 6;
        optional int64 departmentId = 7;
        optional int64 categoryId = 8;
        optional string categoryName = 9;
        optional int64 status = 10;
        optional int64 updateAt = 11;

    }
    optional Result result = 1;
    repeated Article article = 2;
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
message Article{
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional int64 departmentId = 13;
    optional int64 statusValue = 14;
}
```
## getArticlesByDiseaseId

**description**

```
/**
     * 根据前台疾病Id获取所有文章
     *
     * @param diseaseId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/{diseaseId}
```
**parameters**

```
Long diseaseId

```
**response**

```
message ArticleListDTO { 
    message Article {
        optional int64 id = 1;
        optional string name = 2;
        optional string brief = 3;
        optional int64 creatorId = 4;
        optional string creatorName = 5;
        optional string bannerUrl = 6;
        optional int64 departmentId = 7;
        optional int64 categoryId = 8;
        optional string categoryName = 9;
        optional int64 status = 10;
        optional int64 updateAt = 11;

    }
    optional Result result = 1;
    repeated Article article = 2;
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
message Article{
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional int64 departmentId = 13;
    optional int64 statusValue = 14;
}
```
## getArticleStructureByDeparmentId

**description**

```
/**
     * 根据科室Id获取带疾病机构的文章列表
     *
     * @param departmentId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/{departmentId}/user-interaction
```
**parameters**

```
Long departmentId

```
**response**

```
message ArticleStructureListDTO { 
    message Content {
        message Structure {
            optional string name = 1;
            optional int64 levelOneId = 2;
            optional string levelOneName = 3;
            optional int64 levelTwoId = 4;
            optional string levelTwoName = 5;
        }
        optional int64 id = 1;
        optional string name = 2;
        optional string brief = 3;
        optional string creatorId = 4;
        optional string creatorName = 5;
        optional string bannerUrl = 6;
        optional Structure structure = 7;
    }
    optional Result result = 1;
    repeated Content content = 2;
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
## updateArticleInteractionById

**description**

```
/**
     * 更新用户与宣教的互动
     *
     * @param articleId
     * @param userId
     * @param option
     * @return
     */
```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/articles/{articleId}/user-interaction/{userId}
```
**parameters**

```
Long articleId
Long userId
Civilization.ArticleInteractionOption option
message ArticleInteractionOption { 
    optional int64 articleId = 1;
    optional bool liked = 2;
    optional bool favored = 3;
    optional bool read = 4;
}

```
**response**

```
message ArticleUserInteractionDTO { 
    optional int64 articleId = 1;
    optional bool liked = 2;
    optional bool favored = 3;
    optional bool read = 4;
    optional Result result = 5;
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
## getArticleCategories

**description**

```
/**
     * 获取科室下的文章分组信息
     *
     * @param departmentId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles/{departmentId}/categories
```
**parameters**

```
Long departmentId

```
**response**

```
message ArticleCategoryListDTO { 
    message ArticleCategoryInfo {
        message Article {
            optional int64 id = 1;
            optional string name = 2;
            optional int64 status = 3;
        }
        optional int64 id = 1;
        optional string name = 2;
        repeated Article article = 3;
    }

    optional Result result = 1;
    repeated ArticleCategoryInfo articleCategoryInfo = 2;
}
message Article{
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional int64 departmentId = 13;
    optional int64 statusValue = 14;
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
## addArticle

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/article
```
**parameters**

```
Civilization.ArticleAddOption option
message ArticleAddOption { 
    optional string name = 1;
    optional string brief = 2;
    optional int64 creatorId = 3;
    optional int64 creatorType = 4;
    optional string creatorName = 5;
    optional int64 departmentId = 6;
    optional string bannerUrl = 7;
    optional string content = 8;
    optional int64 categroyId = 9;
    optional int64 status = 10;
}

```
**response**

```
message ArticleContentDTO { 
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional Result result = 13;
    optional int64 updateAt = 14;
    optional int64 departmentId = 15;
    optional int64 statusValue = 16;
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
## updateArticleById

**description**

```

```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/articles/{articleId}
```
**parameters**

```
Long articleId
Civilization.ArticleUpdateOption option
message ArticleUpdateOption { 
    optional string name = 1;
    optional string brief = 2;
    optional string bannerUrl = 3;
    optional string content = 4;
    optional string classType = 5;
    optional int64 departmentId = 6;

}

```
**response**

```
message ArticleContentDTO { 
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional Result result = 13;
    optional int64 updateAt = 14;
    optional int64 departmentId = 15;
    optional int64 statusValue = 16;
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
## getArticleStructureByVirtualDisease

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/article/{departmentId}/virtual-disease
```
**parameters**

```
Long departmentId

```
**response**

```
message ArticleStructureListDTO { 
    message Content {
        message Structure {
            optional string name = 1;
            optional int64 levelOneId = 2;
            optional string levelOneName = 3;
            optional int64 levelTwoId = 4;
            optional string levelTwoName = 5;
        }
        optional int64 id = 1;
        optional string name = 2;
        optional string brief = 3;
        optional string creatorId = 4;
        optional string creatorName = 5;
        optional string bannerUrl = 6;
        optional Structure structure = 7;
    }
    optional Result result = 1;
    repeated Content content = 2;
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
## getArticles

**description**

```
/**
     * 组合查询
     * Map 参数请参考 com.youhujia.halo.civilization.ArticleQueryEnum
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/articles
```
**parameters**

```
Map<String, String> map

```
**response**

```
message GetArticleListDTO { 
    message Data {
        repeated ArticleBaseInfo article = 1;
    }
    optional Result result = 1;
    optional Data data = 2;
}
message ArticleBaseInfo{
    optional int64 id = 1;
    optional string name = 2;
    optional int64 status = 3;
    optional int64 authorId = 4;
    optional string authorName = 5;
    optional int64 authorType = 6;
    optional int64 createAt = 7;
    optional int64 updateAt = 8;
    optional int64 categoryId = 9;
    optional string categoryName = 10;
    optional int64 departmentId = 11;
    optional string departmentName = 12;
    optional int64 organizationId = 13;
    optional string organizationName = 14;
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
## updateArticleStatus

**description**

```
/**
     * 修改文章状态
     *
     * @param articleId
     * @param option
     * @return
     */
```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/articles/status/{articleId}
```
**parameters**

```
Long articleId
Civilization.UpdateArticleStatusOption option
message UpdateArticleStatusOption { 
    optional int64 status = 1;
}

```
**response**

```
message ArticleContentDTO { 
    optional int64 id = 1;
    optional string name = 2;
    optional string brief = 3;
    optional int64 creatorId = 4;
    optional string creatorName = 5;
    optional string creatorType = 6;
    optional string status = 7;
    optional string bannerUrl = 8;
    optional string content = 9;
    optional int64 categoryId = 10;
    optional string categoryName = 11;
    optional string classType = 12;
    optional Result result = 13;
    optional int64 updateAt = 14;
    optional int64 departmentId = 15;
    optional int64 statusValue = 16;
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
## getBundles

**description**

```
/**
     * 组合查询量表的基本信息(不包含content字段)
     * PS:查询优先级：
     * 1.ids + status
     * 2.ids
     * 3.除ids外的其它参数
     *
     * @param map 参数请参考 com.youhujia.halo.civilization.BundleStatusEnum
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/bundles
```
**parameters**

```
Map<String, String> map

```
**response**

```
message BundleListDTO { 
    message Bundle {
        optional int64 id = 1;
        optional string name = 2;
        optional string desc = 3;
        optional int64 creatorId = 4;
        optional int64 creatorType = 5;
        optional int64 type = 6;
        optional int64 departmentId = 7;
        optional int64 updateAt = 8;
        optional int64 status = 9;

    }
    optional Result result = 1;
    optional Data data = 2;
    message Data {
        repeated Bundle bundleList = 1;
    }
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
## getBundleContentList

**description**

```
/**
     * 组合查询量表(包含content字段).
     * PS:查询优先级：
     * 1.ids + status
     * 2.ids
     * 3.除ids外的其它参数
     *
     * @param map 参数请参考 com.youhujia.halo.civilization.BundleStatusEnum
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/bundles/content
```
**parameters**

```
Map<String, String> map

```
**response**

```
message BundleContentListDTO { 
    message Bundle {
        optional int64 id = 1;
        optional string name = 2;
        optional string desc = 3;
        optional int64 creatorId = 4;
        optional int64 creatorType = 5;
        optional int64 type = 6;
        optional int64 departmentId = 7;
        optional int64 updateAt = 8;
        optional int64 status = 9;
        optional string content = 10;
        optional BundleContent bundleContent = 11;

    }
    optional Result result = 1;
    optional Data data = 2;
    message Data {
        repeated Bundle bundleList = 1;
    }
}
message BundleContent{
    repeated ContentQuestion question = 1;
    repeated ConclusionChoiceLogic conclusionChoiceLogic = 2;
    repeated ChoiceWikiMappingLogic choiceWikiMappingLogic = 3;
    repeated CompletionMappingLogic completionMappingLogic = 4;
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
## createBundle

**description**

```
/**
     * 创建量表.
     *
     * @param addQuestionBundleOption
     * @return
     */
```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/bundles
```
**parameters**

```
Civilization.AddQuestionBundleOption addQuestionBundleOption
message AddQuestionBundleOption { 
    optional string name = 1;
    optional int64 authorId = 2;
    optional int64 authorType = 3;
    optional int64 status = 4;
    optional string bundleDesc = 5;
    optional int64 departmentId = 6;
    optional int64 bundleType = 7;
    optional BundleContent content = 8;
}
message BundleContent{
    repeated ContentQuestion question = 1;
    repeated ConclusionChoiceLogic conclusionChoiceLogic = 2;
    repeated ChoiceWikiMappingLogic choiceWikiMappingLogic = 3;
    repeated CompletionMappingLogic completionMappingLogic = 4;
}

```
**response**

```
message AddQuestionBundleDTO { 
    optional Result result = 1;
    optional QuestionBundleBaseInfo bundle = 2;
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
message QuestionBundleBaseInfo{
    optional int64 id = 1;
    optional string name = 2;
    optional string desc = 3;
    optional int64 creatorId = 4;
    optional int64 creatorType = 5;
    optional int64 type = 6;
    optional int64 departmentId = 7;
    optional int64 updateAt = 8;
    optional int64 status = 9;
}
```
## updateBundle

**description**

```
/**
     * 编辑量表.
     *
     * @param bundleId
     * @param updateQuestionBundleOption
     * @return
     */
```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/bundles/{bundleId}
```
**parameters**

```
Long bundleId
Civilization.UpdateQuestionBundleOption updateQuestionBundleOption
message UpdateQuestionBundleOption { 
     optional int64 id = 1;
     optional string name = 2;
     optional string bundleDesc = 3;
     optional int64 status = 4;
     optional int64 departmentId = 5;
     optional int64 bundleType = 6;
     optional BundleContent content = 7;
}
message BundleContent{
    repeated ContentQuestion question = 1;
    repeated ConclusionChoiceLogic conclusionChoiceLogic = 2;
    repeated ChoiceWikiMappingLogic choiceWikiMappingLogic = 3;
    repeated CompletionMappingLogic completionMappingLogic = 4;
}

```
**response**

```
message UpdateQuestionBundleDTO { 
    optional Result result = 1;
    optional QuestionBundleBaseInfo bundle = 2;
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
message QuestionBundleBaseInfo{
    optional int64 id = 1;
    optional string name = 2;
    optional string desc = 3;
    optional int64 creatorId = 4;
    optional int64 creatorType = 5;
    optional int64 type = 6;
    optional int64 departmentId = 7;
    optional int64 updateAt = 8;
    optional int64 status = 9;
}
```
## updateBundleStatus

**description**

```
/**
     * 修改量表状态
     *
     * @param bundleId
     * @param option
     * @return
     */
```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/bundles/status/{bundleId}
```
**parameters**

```
Long bundleId
Civilization.UpdateBundleStatusOption option
message UpdateBundleStatusOption { 
    optional int64 status = 1;
}

```
**response**

```
message UpdateBundleStatusDTO { 
    optional Result result = 1;
    optional QuestionBundleBaseInfo bundle = 2;
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
message QuestionBundleBaseInfo{
    optional int64 id = 1;
    optional string name = 2;
    optional string desc = 3;
    optional int64 creatorId = 4;
    optional int64 creatorType = 5;
    optional int64 type = 6;
    optional int64 departmentId = 7;
    optional int64 updateAt = 8;
    optional int64 status = 9;
}
```
## getEvaluations

**description**

```
/**
     * 组合查询评估、自测
     *
     * @param queryMap 参数请参考 com.youhujia.halo.civilization.EvaluationQueryEnum
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/evaluations
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message EvaluationListDTO { 
    message Data {
        repeated Evaluation evaluation = 1;
    }
    optional Result result = 1;
    optional Data data = 2;
}
message Evaluation{
    optional int64 id = 1;
    optional string name = 2;
    optional int64 authorId = 3;
    optional int64 authorType = 4;
    optional int64 departmentId = 5;
    optional int64 type = 6;
    optional int64 status = 7;
    optional string icon = 8;
    optional string iconColor = 9;
    optional string desc = 10;
    optional int64 createAt = 12;
    optional int64 updateAt = 13;
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
## getMappingEvaluationBundlesList

**description**

```
/**
     * 组合查询评估、自测(包括评估关联的量表，但没有量表的content字段)
     *
     * @param queryMap 参数请参考 com.youhujia.halo.civilization.EvaluationQueryEnum
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/evaluations/mapping-bundles
```
**parameters**

```
Map<String, String> queryMap

```
**response**

```
message MappingEvaluationBundleListDTO { 
    message Data {
        repeated MappingEvaluationBundle mappingEvaluationBundle = 1;
    }
    optional Result result = 1;
    optional Data data = 2;
}
message MappingEvaluationBundle{
    message Bundle {
        optional int64 id = 1;
        optional string name = 2;
        optional int64 status = 3;
        optional int64 order = 4;
    }
    optional Evaluation evaluation = 1;
    repeated Bundle bundle = 2;
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
## getResultTagIdsByRecordId

**description**

```
/**
     * 通过recordId 获取其对应产生的tagId集合.
     *
     * @param recordId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/evaluations/result-tagIds/{recordId}
```
**parameters**

```
Long recordId

```
**response**

```
message EvaluationResultTagIdsDTO { 
    message Data {
        optional int64 evaluationId = 1;
        optional int64 recordId = 2;
        repeated int64 tagIds = 3;
        repeated string evaluationConclusions = 4;
    }

    optional Result result = 1;
    optional Data data = 2;
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
## createEvaluation

**description**

```
/**
     * 创建 评估／自测
     *
     * @param addEvaluationOption
     * @return
     */
```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/evaluations
```
**parameters**

```
Civilization.AddEvaluationOption addEvaluationOption
message AddEvaluationOption { 
    optional string name = 1;
    optional int64 authorId = 2;
    optional int64 authorType = 3;
    optional string desc = 4;
    optional string iconColor = 5;
    optional string icon = 6;
    optional int64 departmentId = 7;
    optional int64 type = 8;
    optional int64 status = 9;
    repeated EvaluationBundle evaluationBundle = 10;
}
message EvaluationBundle{
    optional int64 bundleId = 1;
    optional int64 order = 2;
}

```
**response**

```
message EvaluationDTO { 
    optional Result result = 1;
    optional Data data = 2;
    message Data {
        optional Evaluation evaluation = 1;
    }
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
message Evaluation{
    optional int64 id = 1;
    optional string name = 2;
    optional int64 authorId = 3;
    optional int64 authorType = 4;
    optional int64 departmentId = 5;
    optional int64 type = 6;
    optional int64 status = 7;
    optional string icon = 8;
    optional string iconColor = 9;
    optional string desc = 10;
    optional int64 createAt = 12;
    optional int64 updateAt = 13;
}
```
## updateEvaluation

**description**

```
/**
     * 编辑 评估／自测
     *
     * @param updateEvaluationOption
     * @return
     */
```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/evaluations
```
**parameters**

```
Civilization.UpdateEvaluationOption updateEvaluationOption
message UpdateEvaluationOption { 

    optional int64 id = 1;
    optional string name = 2;
    optional string desc = 3;
    optional string iconColor = 4;
    optional string icon = 5;
    optional int64 departmentId = 6;
    optional int64 type = 7;
    optional int64 status = 8;
    repeated EvaluationBundle evaluationBundle = 9;
}
message EvaluationBundle{
    optional int64 bundleId = 1;
    optional int64 order = 2;
}

```
**response**

```
message EvaluationDTO { 
    optional Result result = 1;
    optional Data data = 2;
    message Data {
        optional Evaluation evaluation = 1;
    }
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
message Evaluation{
    optional int64 id = 1;
    optional string name = 2;
    optional int64 authorId = 3;
    optional int64 authorType = 4;
    optional int64 departmentId = 5;
    optional int64 type = 6;
    optional int64 status = 7;
    optional string icon = 8;
    optional string iconColor = 9;
    optional string desc = 10;
    optional int64 createAt = 12;
    optional int64 updateAt = 13;
}
```
## updateEvaluationStatus

**description**

```

```
**method**

```
PATCH
```
**URL**

```
/api/civilization/v1/evaluations/status/{evaluationId}
```
**parameters**

```
Long evaluationId
Civilization.UpdateEvaluationStatusOption updateEvaluationStatusOption
message UpdateEvaluationStatusOption { 
    optional int64 status = 1;
}

```
**response**

```
message EvaluationDTO { 
    optional Result result = 1;
    optional Data data = 2;
    message Data {
        optional Evaluation evaluation = 1;
    }
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
message Evaluation{
    optional int64 id = 1;
    optional string name = 2;
    optional int64 authorId = 3;
    optional int64 authorType = 4;
    optional int64 departmentId = 5;
    optional int64 type = 6;
    optional int64 status = 7;
    optional string icon = 8;
    optional string iconColor = 9;
    optional string desc = 10;
    optional int64 createAt = 12;
    optional int64 updateAt = 13;
}
```
## getProfessionalEvaluationById

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/{evaluationId}
```
**parameters**

```
Long evaluationId

```
**response**

```
message ProfessionalEvaluationDetailDTO { 

    message Question {
        message SingleChoice {
            optional string choice = 1;
            optional int64 order = 2;
        }

        message MultiChoice {
            optional string choice = 1;
            optional int64 order = 2;
        }

        message Completion {
            optional string content = 1; //"血压:${BLANK} mmHg；血糖:${BLANK} mmol/L;您的意见:${BLANK}"
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional Result result = 1;
    repeated Question question = 2;
    optional int64 evaluationId = 3;
    optional string evaluationName = 4;
    optional string iconColor = 5;
    optional string icon = 6;
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
## getProfessionalEvaluationResultById

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/records/{recordId}
```
**parameters**

```
Long recordId

```
**response**

```
message ProfessionalEvaluationResultDTO { 

    message QuestionAnswer {
        message SingleChoice {
            optional string choice = 1;
        }

        message MultiChoice {
            optional string choice = 1;
        }

        message Completion {
            optional string content = 1;
            optional string format = 2;
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional int64 recordId = 1;
    optional Result result = 2;
    optional int64 submitorId = 3;
    optional int64 submitorType = 4;
    optional int64 departmentId = 5;
    optional string departmentName = 6;
    optional int64 organizationId = 7;
    optional string organizationName = 8;
    optional int64 evaluationId = 9;
    optional string evaluationName = 10;
    optional string conclusion = 11; //bundle的结论
    repeated QuestionAnswer answer = 12;
    optional string iconColor = 13;
    optional string icon = 14;
    optional int64 updatedAt = 15;
    optional string evaluationConclusion = 16; //evaluation的结论
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
## getProfessionalEvaluationByIds

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/professional-evaluations/general-info
```
**parameters**

```
Civilization.EvaluationQueryBatchOption option
message EvaluationQueryBatchOption { 
    repeated int64 evaluationId = 1;
    optional string name = 2;
}

```
**response**

```
message ProfessionalEvaluationGeneralInfoListDTO { 
    message Data {
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional string iconColor = 3;
        optional string icon = 4;
        optional int64 departmentId = 5;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## getProfessionalEvaluationByDepartmentId

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/{departmentId}/professional-evaluations/general-info
```
**parameters**

```
Long departmentId

```
**response**

```
message ProfessionalEvaluationGeneralInfoListDTO { 
    message Data {
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional string iconColor = 3;
        optional string icon = 4;
        optional int64 departmentId = 5;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## getProfessinalEvaluationStructureByDepartmentId

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/structure/{departmentId}
```
**parameters**

```
Long departmentId

```
**response**

```
message ProfessionalStructureListDTO { 
    message Data {
        message Structure {
            optional string name = 1;
            optional int64 levelOneId = 2;
            optional string levelOneName = 3;
            optional int64 levelTwoId = 4;
            optional string levelTwoName = 5;
        }
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional Structure structure = 3;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## submitProfessionalEvaluation

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/professional-evaluation/{evaluationId}/submit
```
**parameters**

```
Civilization.ProfessionalEvaluationSubmitOption professionalOption
message ProfessionalEvaluationSubmitOption { 
    message Answer {
        optional int64 order = 1;
        repeated string content = 2;
    }
    optional int64 departmentId = 1;
    optional int64 nurseId = 2;
    optional int64 userId = 3;
    repeated Answer answer = 4;
    optional string source = 5;
}
Long evaluationId

```
**response**

```
message ProfessionalEvaluationResultDTO { 

    message QuestionAnswer {
        message SingleChoice {
            optional string choice = 1;
        }

        message MultiChoice {
            optional string choice = 1;
        }

        message Completion {
            optional string content = 1;
            optional string format = 2;
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional int64 recordId = 1;
    optional Result result = 2;
    optional int64 submitorId = 3;
    optional int64 submitorType = 4;
    optional int64 departmentId = 5;
    optional string departmentName = 6;
    optional int64 organizationId = 7;
    optional string organizationName = 8;
    optional int64 evaluationId = 9;
    optional string evaluationName = 10;
    optional string conclusion = 11; //bundle的结论
    repeated QuestionAnswer answer = 12;
    optional string iconColor = 13;
    optional string icon = 14;
    optional int64 updatedAt = 15;
    optional string evaluationConclusion = 16; //evaluation的结论
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
## getProfessionalEvaluationStructureByVirtualDisease

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/{departmentId}/virtual-disease
```
**parameters**

```
Long departmentId

```
**response**

```
message ProfessionalStructureListDTO { 
    message Data {
        message Structure {
            optional string name = 1;
            optional int64 levelOneId = 2;
            optional string levelOneName = 3;
            optional int64 levelTwoId = 4;
            optional string levelTwoName = 5;
        }
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional Structure structure = 3;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## getProfessionalEvaluationTodayResultScores

**description**

```
/**
     * 科研调用，获取 今日 护士给患者做的科研评估及结果分数
     *
     * @param nurseIds      查询的护士id范围，逗号拼接
     * @param evaluationIds 查询的评估id范围，逗号拼接
     * @param userId        限定用户id
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/result-scores-today
```
**parameters**

```
String nurseIds
String evaluationIds
Long userId

```
**response**

```
message EvaluationResultScoreDTO { 
    message ResultScore {
        optional int64 evaluationId = 1;
        optional int64 score = 2;
    }

    optional Result result = 1;
    repeated ResultScore resultScores = 2;
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
## getProfessionalEvaluationLastDayResultScores

**description**

```
/**
     * 科研调用，获取 昨日 护士给患者做的科研评估及结果分数(初次需求是查询昨日NIHSS分数和今日分数比对)
     *
     * @param nurseIds      查询的护士id范围，逗号拼接
     * @param evaluationIds 查询的评估id范围，逗号拼接
     * @param userId        限定用户id
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/result-scores-lastDay
```
**parameters**

```
String nurseIds
String evaluationIds
Long userId

```
**response**

```
message EvaluationResultScoreDTO { 
    message ResultScore {
        optional int64 evaluationId = 1;
        optional int64 score = 2;
    }

    optional Result result = 1;
    repeated ResultScore resultScores = 2;
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
## partialSaveEvaluation

**description**

```
/**
     * 照护评估部分保存
     *
     * @param evaluationPartialSaveOption
     * @param evaluationId
     * @return
     */
```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/professional-evaluation/{evaluationId}/partial-save
```
**parameters**

```
Civilization.EvaluationPartialSaveOption evaluationPartialSaveOption
message EvaluationPartialSaveOption { 
    message Answer {
        optional int64 order = 1;
        repeated string content = 2;
    }
    optional int64 departmentId = 1;
    optional int64 nurseId = 2;
    optional int64 userId = 3;
    repeated Answer answer = 4;
    optional string source = 5;
    optional int64 id = 6;
}
Long evaluationId

```
**response**

```
message EvaluationPartialSaveDTO { 
    optional int64 id = 1;
    optional Result result = 2;
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
## submitEvaluationBaseOnPartialSave

**description**

```
/**
     * 照护评估基于部分保存的全部提交.
     *
     * @return
     */
```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/professional-evaluation/submit-baseOnPartialSave
```
**parameters**

```
Civilization.EvaluationSubmitBaseOnPartialSaveOption option
message EvaluationSubmitBaseOnPartialSaveOption { 
    optional int64 partialSaveId = 6;
}

```
**response**

```
message ProfessionalEvaluationResultDTO { 

    message QuestionAnswer {
        message SingleChoice {
            optional string choice = 1;
        }

        message MultiChoice {
            optional string choice = 1;
        }

        message Completion {
            optional string content = 1;
            optional string format = 2;
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional int64 recordId = 1;
    optional Result result = 2;
    optional int64 submitorId = 3;
    optional int64 submitorType = 4;
    optional int64 departmentId = 5;
    optional string departmentName = 6;
    optional int64 organizationId = 7;
    optional string organizationName = 8;
    optional int64 evaluationId = 9;
    optional string evaluationName = 10;
    optional string conclusion = 11; //bundle的结论
    repeated QuestionAnswer answer = 12;
    optional string iconColor = 13;
    optional string icon = 14;
    optional int64 updatedAt = 15;
    optional string evaluationConclusion = 16; //evaluation的结论
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
## getProfessionalEvaluationResultByPartialSaveId

**description**

```
/**
     * 照护评估基于部分保存的结果提取.
     *
     * @param partialSaveId
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/professional-evaluations/partial-save-record/{partialSaveId}
```
**parameters**

```
Long partialSaveId

```
**response**

```
message ProfessionalEvaluationResultDTO { 

    message QuestionAnswer {
        message SingleChoice {
            optional string choice = 1;
        }

        message MultiChoice {
            optional string choice = 1;
        }

        message Completion {
            optional string content = 1;
            optional string format = 2;
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional int64 recordId = 1;
    optional Result result = 2;
    optional int64 submitorId = 3;
    optional int64 submitorType = 4;
    optional int64 departmentId = 5;
    optional string departmentName = 6;
    optional int64 organizationId = 7;
    optional string organizationName = 8;
    optional int64 evaluationId = 9;
    optional string evaluationName = 10;
    optional string conclusion = 11; //bundle的结论
    repeated QuestionAnswer answer = 12;
    optional string iconColor = 13;
    optional string icon = 14;
    optional int64 updatedAt = 15;
    optional string evaluationConclusion = 16; //evaluation的结论
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
## getSelfEvaluationById

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/self-evaluations/{evaluationId}
```
**parameters**

```
Long evaluationId

```
**response**

```
message SelfEvaluationDetailDTO { 

    message Question {
        message SingleChoice {
            optional string choice = 1;
            optional int64 order = 2;
        }

        message MultiChoice {
            optional string choice = 1;
            optional int64 order = 2;
        }

        message Completion {
            optional string content = 1; //"血压:${BLANK} mmHg；血糖:${BLANK} mmol/L;您的意见:${BLANK}"
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }
    optional Result result = 1;
    repeated Question question = 2;
    optional int64 evaluationId = 3;
    optional string evaluationName = 4;
    optional string iconColor = 5;
    optional string icon = 6;
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
## getSelfEvaluationResultById

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/self-evaluations/records/{recordId}
```
**parameters**

```
Long recordId

```
**response**

```
message SelfEvaluationResultDTO { 

    message QuestionAnswer {
        message SingleChoice {
            optional string choice = 1;
        }

        message MultiChoice {
            optional string choice = 1;
        }

        message Completion {
            optional string content = 1;
            optional string format = 2;
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional int64 recordId = 1;
    optional Result result = 2;
    optional int64 submitorId = 3;
    optional int64 submitorType = 4;
    optional int64 departmentId = 5;
    optional string departmentName = 6;
    optional int64 organizationId = 7;
    optional string organizationName = 8;
    optional int64 evaluationId = 9;
    optional string evaluationName = 10;
    optional string conclusion = 11; //bundle的结论
    repeated QuestionAnswer answer = 12;
    optional string iconColor = 13;
    optional string icon = 14;
    optional int64 updatedAt = 15;
    optional string evaluationConclusion = 16; //evaluation的结论
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
## getSelfEvaluationByIds

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/self-evaluations/general-info
```
**parameters**

```
Civilization.EvaluationQueryBatchOption option
message EvaluationQueryBatchOption { 
    repeated int64 evaluationId = 1;
    optional string name = 2;
}

```
**response**

```
message SelfEvaluationGeneralInfoListDTO { 
    message Data {
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional string iconColor = 5;
        optional string icon = 6;
        optional int64 departmentId = 7;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## getSelfEvaluationByDepartmentId

**description**

```

```
**method**

```

```
**URL**

```
/api/civilization/v1/{departmentId}/self-evaluations/general-info
```
**parameters**

```
Long departmentId

```
**response**

```
message SelfEvaluationGeneralInfoListDTO { 
    message Data {
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional string iconColor = 5;
        optional string icon = 6;
        optional int64 departmentId = 7;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## getSelfEvaluationStructureByDepartmentId

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/self-evaluations/structure/{departmentId}
```
**parameters**

```
Long departmentId

```
**response**

```
message SelfEvaluationStructureListDTO { 
    message Data {
        message Structure {
            optional string name = 1;
            optional int64 levelOneId = 2;
            optional string levelOneName = 3;
            optional int64 levelTwoId = 4;
            optional string levelTwoName = 5;
        }
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional Structure structure = 3;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## submitSelfEvaluation

**description**

```

```
**method**

```
POST
```
**URL**

```
/api/civilization/v1/self-evaluation/{evaluationId}/submit/{departmentId}/{userId}
```
**parameters**

```
Long evaluationId
Long departmentId
Long userId
Civilization.SelfEvaluationSubmitOption option
message SelfEvaluationSubmitOption { 
    message Answer {
        optional int64 order = 1;
        repeated string content = 2;
    }
    repeated Answer answer = 1;
    optional string source = 2;
}

```
**response**

```
message SelfEvaluationResultDTO { 

    message QuestionAnswer {
        message SingleChoice {
            optional string choice = 1;
        }

        message MultiChoice {
            optional string choice = 1;
        }

        message Completion {
            optional string content = 1;
            optional string format = 2;
        }

        message SingleChoiceMatrix {
            message OptionContent {
                optional int64 rank = 1;
                optional string content = 2;
                repeated string choice = 3;
            }
            optional OptionContent optionContent = 1;
        }

        optional string questionType = 1;
        optional string questionContent = 2;
        optional string questionDesc = 3;
        repeated string questionDescPicUrl = 4;
        repeated SingleChoice singleChoice = 5;
        repeated MultiChoice multiChoice = 6;
        repeated Completion completion = 7;
        repeated SingleChoiceMatrix singleChoiceMatrix = 8;
        optional int64 order = 9;
    }

    optional int64 recordId = 1;
    optional Result result = 2;
    optional int64 submitorId = 3;
    optional int64 submitorType = 4;
    optional int64 departmentId = 5;
    optional string departmentName = 6;
    optional int64 organizationId = 7;
    optional string organizationName = 8;
    optional int64 evaluationId = 9;
    optional string evaluationName = 10;
    optional string conclusion = 11; //bundle的结论
    repeated QuestionAnswer answer = 12;
    optional string iconColor = 13;
    optional string icon = 14;
    optional int64 updatedAt = 15;
    optional string evaluationConclusion = 16; //evaluation的结论
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
## getRecordGeneralInfoListBySubmitorInfo

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/self-evaluations/records/{submitorType}/{submitorId}
```
**parameters**

```
Long submitorType
Long submitorId

```
**response**

```
message RecordGeneralInfoListDTO { 
    message RecordGeneralInfo {
        optional int64 recordId = 1;
        optional int64 evaluationId = 2;
        optional int64 createdAt = 3;
    }
    optional Result result = 1;
    repeated RecordGeneralInfo info = 2;
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
## getSelfEvaluationStructureByVirtualDisease

**description**

```

```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/self-evaluations/{departmentId}/virtual-disease
```
**parameters**

```
Long departmentId

```
**response**

```
message SelfEvaluationStructureListDTO { 
    message Data {
        message Structure {
            optional string name = 1;
            optional int64 levelOneId = 2;
            optional string levelOneName = 3;
            optional int64 levelTwoId = 4;
            optional string levelTwoName = 5;
        }
        optional int64 evaluationId = 1;
        optional string evaluationName = 2;
        optional Structure structure = 3;
    }
    optional Result result = 1;
    repeated Data data = 2;
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
## getSelfEvaluationTodayResultScores

**description**

```
/**
     * 科研调用，获取 今日 患者做的科研自测及结果分数
     * @param evaluationIds 查询的自测id范围，逗号拼接
     * @param userId        用户id
     * @return
     */
```
**method**

```
GET
```
**URL**

```
/api/civilization/v1/self-evaluations/result-scores-today
```
**parameters**

```
String evaluationIds
Long userId

```
**response**

```
message EvaluationResultScoreDTO { 
    message ResultScore {
        optional int64 evaluationId = 1;
        optional int64 score = 2;
    }

    optional Result result = 1;
    repeated ResultScore resultScores = 2;
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