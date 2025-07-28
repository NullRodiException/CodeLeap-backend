---
title: CodeLeap-api
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.30"

---

# CodeLeap-api

### Base URLs:
- `https://codeleap-front.onrender.com/` Frontend URL for generating firebase token
- `https://codeleap-backend-qog7.onrender.com/` Backend URL for API requests

# Authentication
- The API uses Firebase for authentication. To authenticate, you need to obtain a Firebase token from the frontend URL. This token should be included in the `Authorization` header of your requests.

# Career

## GET Posts

GET /careers/

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|author|query|integer| yes |filters posts from a author with id|
|cursor|query|string| yes |comes from pagination on the bopdy of the response (next and previous)|
|ordering|query|string| yes |filter ordering (-comments_count, comments_count, -likes_count, likes_count, created_datetime, -created_datetime)|

> Response Examples

> 200 Response

```json
{
  "next": "http://localhost:8000/careers/?author=&cursor=cD0yMDI1LTA3LTI4KzAxJTNBMzglM0E1NC4wNTYzNTklMkIwMCUzQTAw&ordering=",
  "previous": "http://localhost:8000/careers/?author=&cursor=cD0yMDI1LTA3LTI4KzAxJTNBMzglM0E1NC4wNTYzNTklMkIwMCUzQTAw&ordering=",
  "results": []
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|string|

## POST Post

POST /careers/

> Body Parameters

```json
{
  "title": "test",
  "content": "Mention to @Rodrigo_123654"
}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|Authorization|header|string| no ||Obteined from the basic front end|
|body|body|object| no | Rodrigo|none|
|» title|body|string| yes ||none|
|» content|body|string| yes ||none|

> Response Examples

> 201 Response

```json
{
  "id": 33,
  "name": "Rodrigo Oliveira",
  "username": "Rodrigo_123654",
  "created_datetime": "2025-07-28T21:01:00.020559Z",
  "title": "titulo",
  "content": "Mention to @Rodrigo_123654",
  "comments_count": 0,
  "likes_count": 0,
  "mentions": [
    "Rodrigo_123654"
  ]
}
```

> 403 Response

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|none|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||none|
|» name|string|true|none||none|
|» username|string|true|none||none|
|» created_datetime|string|true|none||none|
|» title|string|true|none||none|
|» content|string|true|none||none|
|» comments_count|integer|true|none||none|
|» likes_count|integer|true|none||none|
|» mentions|[string]|true|none||none|

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

### Response Header

|Status|Header|Type|Format|Description|
|---|---|---|---|---|
|201|Authorization|string||none|
|403|Authorization|string||No Bearer value|

## GET Post

GET /careers/{postId}/

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|integer| yes ||Id from the Post|
|author|query|string| yes ||filters posts from a author with id|
|cursor|query|string| yes ||comes from pagination on the bopdy of the response (next and previous)|
|ordering|query|string| yes ||filter ordering ( created_datetime, -created_datetime)|

> Response Examples

> 200 Response

```json
{
  "id": 35,
  "name": "Rodrigo Oliveira",
  "username": "Rodrigo_123654",
  "created_datetime": "2025-07-28T21:18:29.529791Z",
  "title": "titulo",
  "content": "Mention to @Rodrigo_123654",
  "comments_count": 0,
  "likes_count": 0,
  "mentions": [
    "Rodrigo_123654"
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

*aqui tem um teste*

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||none|
|» name|string|true|none||none|
|» username|string|true|none||none|
|» created_datetime|string|true|none||none|
|» title|string|true|none||none|
|» content|string|true|none||none|
|» comments_count|integer|true|none||none|
|» likes_count|integer|true|none||none|
|» mentions|[string]|true|none||none|

## PATCH Post

PATCH /careers/{postID}/

> Body Parameters

```json
{
  "title": "test update",
  "content": "contente update no mention"
}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postID|path|string| yes ||none|
|Authorization|header|string| no ||none|
|body|body|object| no ||none|
|» title|body|string| yes ||none|
|» content|body|string| yes ||none|

> Response Examples

> 200 Response

```json
{
  "id": 33,
  "name": "Rodrigo Oliveira",
  "username": "Rodrigo_123654",
  "created_datetime": "2025-07-28T21:01:00.020559Z",
  "title": "test update",
  "content": "contente update no mention",
  "comments_count": 0,
  "likes_count": 0,
  "mentions": []
}
```

> 403 Response

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Different user trying to patch posts from others|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||none|
|» name|string|true|none||none|
|» username|string|true|none||none|
|» created_datetime|string|true|none||none|
|» title|string|true|none||none|
|» content|string|true|none||none|
|» comments_count|integer|true|none||none|
|» likes_count|integer|true|none||none|
|» mentions|[string]|true|none||none|

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## DELETE Post

DELETE /careers/{postID}/

> Body Parameters

```json
{}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postID|path|string| yes ||none|
|Authorization|header|string| no ||none|
|body|body|object| no ||none|

> Response Examples

> 204 Response

```json
{}
```

> 403 Response

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Different user trying to delete posts from others|Inline|

### Responses Data Schema

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

# Career/Comment

## GET Comments

GET /careers/{postId}/comments/

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|string| yes ||none|
|cursor|query|string| yes ||none|

> Response Examples

> 200 Response

```json
{
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 27,
      "name": "Rodrigo Oliveira",
      "username": "rodrigo_123",
      "content": "this is a good comment @rodrigo_123",
      "created_datetime": "2025-07-28T21:34:36.317264Z",
      "mentions": [
        "rodrigo_123"
      ]
    },
    {
      "id": 26,
      "name": "Rodrigo Oliveira",
      "username": "rodrigo_123",
      "content": "this is a good comment @rodrigo_123",
      "created_datetime": "2025-07-28T21:34:35.260028Z",
      "mentions": [
        "rodrigo_123"
      ]
    },
    {
      "id": 25,
      "name": "Rodrigo Oliveira",
      "username": "rodrigo_123",
      "content": "this is a good comment @rodrigo_123",
      "created_datetime": "2025-07-28T21:34:34.297644Z",
      "mentions": [
        "rodrigo_123"
      ]
    },
    {
      "id": 24,
      "name": "Rodrigo Oliveira",
      "username": "rodrigo_123",
      "content": "this is a good comment @rodrigo_123",
      "created_datetime": "2025-07-28T21:34:33.370942Z",
      "mentions": [
        "rodrigo_123"
      ]
    },
    {
      "id": 23,
      "name": "Rodrigo Oliveira",
      "username": "rodrigo_123",
      "content": "this is a good comment @rodrigo_123",
      "created_datetime": "2025-07-28T21:34:32.179269Z",
      "mentions": [
        "rodrigo_123"
      ]
    },
    {
      "id": 22,
      "name": "Rodrigo Oliveira",
      "username": "rodrigo_123",
      "content": "this is a good comment @rodrigo_123",
      "created_datetime": "2025-07-28T21:34:29.436872Z",
      "mentions": [
        "rodrigo_123"
      ]
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» next|null|true|none||none|
|» previous|null|true|none||none|
|» results|[string]|true|none||none|

## POST Comment

POST /careers/{postId}/comments/

> Body Parameters

```json
{
  "content": "this is a good comment @rodrigo_123"
}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|string| yes ||none|
|Authorization|header|string| yes ||none|
|body|body|object| no ||none|
|» content|body|string| yes ||none|

> Response Examples

> 200 Response

```json
{
  "id": 27,
  "name": "Rodrigo Oliveira",
  "username": "rodrigo_123",
  "content": "this is a good comment @rodrigo_123",
  "created_datetime": "2025-07-28T21:34:36.317264Z",
  "mentions": [
    "rodrigo_123"
  ]
}
```

> 400 Response

```json
{
  "content": [
    "This field is required."
  ]
}
```

> 403 Response

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||none|
|» name|string|true|none||none|
|» username|string|true|none||none|
|» content|string|true|none||none|
|» created_datetime|string|true|none||none|
|» mentions|[string]|true|none||none|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» content|[string]|true|none||none|

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## GET Comment

GET /careers/{postId}/comments/{commentId}/

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|string| yes ||none|
|commentId|path|string| yes ||none|
|Authorization|header|string| no ||none|

> Response Examples

> 200 Response

```json
{
  "id": 27,
  "name": "Rodrigo Oliveira",
  "username": "rodrigo_123",
  "content": "this is a good comment @rodrigo_123",
  "created_datetime": "2025-07-28T21:34:36.317264Z",
  "mentions": [
    "rodrigo_123"
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||none|
|» name|string|true|none||none|
|» username|string|true|none||none|
|» content|string|true|none||none|
|» created_datetime|string|true|none||none|
|» mentions|[string]|true|none||none|

## PATCH Comment

PATCH /careers/{postId}/comments/{commentId}/

> Body Parameters

```json
{
  "content": "this is a comment"
}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|string| yes ||none|
|commentId|path|string| yes ||none|
|Authorization|header|string| yes ||none|
|body|body|object| no ||none|
|» content|body|string| yes ||none|

> Response Examples

> 200 Response

```json
{
  "id": 27,
  "name": "Rodrigo Oliveira",
  "username": "rodrigo_123",
  "content": "this is a comment",
  "created_datetime": "2025-07-28T21:34:36.317264Z",
  "mentions": []
}
```

> 403 Response

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|User trying to patch a comment from other user|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||none|
|» name|string|true|none||none|
|» username|string|true|none||none|
|» content|string|true|none||none|
|» created_datetime|string|true|none||none|
|» mentions|[string]|true|none||none|

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## DELETE Comment

DELETE /careers/{postId}/comments/{commentId}/

> Body Parameters

```json
{}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|string| yes ||none|
|commentId|path|string| yes ||none|
|Authorization|header|string| yes ||none|
|body|body|object| no ||none|

> Response Examples

> 204 Response

```json
{}
```

> 403 Response

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|User trying to delete a comment from other user|Inline|

### Responses Data Schema

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

# Career/Like

## POST Like-a-post

POST /careers/{postId}/like/

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|postId|path|string| yes ||none|
|Authorization|header|string| no ||none|

> Response Examples

> 201 Response

```json
{}
```

> 403 Response

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|User gives a like in a post|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|User removes a like in a post|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|none|Inline|

### Responses Data Schema

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

# Career/Profile

## PATCH Profile

PATCH /careers/profile/

> Body Parameters

```json
{
  "app_username": "rodrigo_123"
}
```

### Params

|Name|Location|Type|Required|Title|Description|
|---|---|---|---|---|---|
|Authorization|header|string| yes ||none|
|body|body|object| no ||none|
|» app_username|body|string| yes ||none|

> Response Examples

> 200 Response

```json
{
  "name": "Rodrigo Oliveira",
  "email": "rodrigo.silva.oliveira369@gmail.com",
  "app_username": "rodrigo_123"
}
```

> 400 Response

```json
{
  "app_username": [
    "O nome de usuário pode conter apenas letras, números e underscores (_)."
  ]
}
```

> 403 Response

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|name and email get from firebase auth|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|none|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» name|string|true|none||none|
|» email|string|true|none||none|
|» app_username|string|true|none||none|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» app_username|[string]|true|none||app_username with " ". Ex: "user user"|

HTTP Status Code **403**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

### Response Header

|Status|Header|Type|Format|Description|
|---|---|---|---|---|
|200|Authorization|string||none|


