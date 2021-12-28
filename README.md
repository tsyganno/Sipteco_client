# Sipteco_client

Результатом задания должно быть успешно отправления сообщения в WhatsApp клиента.

Сервер API: https://dev.whatsapp.sipteco.ru/v3/

Метод  для получения нового чата chat/spare?crm=TEST&domain=test

Метод для работы с чатом instance{ID}/{METHOD}?token={TOKEN}

ID , TOKEN это данные полученные при получении чата

Пример https://dev.whatsapp.sipteco.ru/v3/instance23/me?token=123DYUUD

Документация по методам https://documenter.getpostman.com/view/16489057/TzzDLFp4#intro

При каждом запросе необходимо отправлять заголовок (header)
X-Tasktest-Token: f62cdf1e83bc324ba23aee3b113c6249

1. Получить свободный чат и записать данные в базу
2. Получить QR код
3. Получить статус что вацап подключен и записать имя и телефон
4. Отправить сообщение 
5. Залить код на github / bitbucket / gitlab
