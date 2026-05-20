import os
from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.jwt_access_token import JWTAccessToken


jwt_access_token = JWTAccessToken()

bearer_scheme = HTTPBearer(
    scheme_name="Bearer",
    description="Informe apenas o token JWT. O Swagger adiciona o prefixo Bearer automaticamente.",
)

async def protect(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict[str, Any]:
    
    token = credentials.credentials
    payload = jwt_access_token.decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    admin_email = os.getenv("ADMIN_EMAIL")

    if not admin_email:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="ADMIN_EMAIL is not configured",
        )

    payload_email = getattr(payload, "email", None)

    if payload_email != admin_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions",
        )

    if hasattr(payload, "to_dict"):
        return payload.to_dict()

    if isinstance(payload, dict):
        return payload

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token payload",
    )