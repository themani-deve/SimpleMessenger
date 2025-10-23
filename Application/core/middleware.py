from urllib.parse import parse_qs

import jwt
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.conf import settings
from django.contrib.auth import get_user_model
from jwt import InvalidTokenError


class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token", None)

        if not token:
            return await send({"type": "websocket.close", "code": 4001})

        payload = self.decode_jwt(token=token[0])

        if not payload:
            return await send({"type": "websocket.close", "code": 4001})

        user = await self.get_user(user_id=payload["user_id"])

        if not user:
            return await send({"type": "websocket.close", "code": 4002})

        scope["user"] = user

        return await super().__call__(scope, receive, send)

    @staticmethod
    def decode_jwt(token):
        try:
            return jwt.decode(jwt=token, key=settings.JWT_PUBLIC_KEY, algorithms=[settings.JWT_ALGORITHM])
        except InvalidTokenError:
            return None

    @database_sync_to_async
    def get_user(self, user_id):
        return get_user_model().objects.filter(id=user_id).first()
