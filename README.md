### Posts

| Método HTTP | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/careers/` | Lista todos os posts. |
| `POST` | `/careers/` | Cria um novo post. |
| `GET` | `/careers/{post_id}/` | Retorna os detalhes de um post específico. |
| `PUT` | `/careers/{post_id}/` | Atualiza um post específico. |
| `PATCH` | `/careers/{post_id}/` | Atualiza parcialmente um post específico. |
| `DELETE` | `/careers/{post_id}/` | Deleta um post específico. |
| `POST` | `/careers/{post_id}/like/` | Adiciona ou remove um "like" de um post. |
### Comentários (Aninhados sob Posts)

| Método HTTP | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/careers/{post_pk}/comments/` | Lista todos os comentários de um post específico. |
| `POST` | `/careers/{post_pk}/comments/` | Cria um novo comentário em um post específico. |
| `GET` | `/careers/{post_pk}/comments/{comment_id}/` | Retorna os detalhes de um comentário específico. |
| `PUT` | `/careers/{post_pk}/comments/{comment_id}/` | Atualiza um comentário específico. |
| `PATCH` | `/careers/{post_pk}/comments/{comment_id}/` | Atualiza parcialmente um comentário específico. |
| `DELETE` | `/careers/{post_pk}/comments/{comment_id}/` | Deleta um comentário específico. |
### Perfil de Usuário

| Método HTTP | Endpoint | Descrição                                  |
|-------------| --- |--------------------------------------------|
| `GET`       | `/careers/profile/` | Retorna o perfil do usuário autenticado.   |
| `PATCH`     | `/careers/profile/` | Usado para renomear o app_username (unico) |
