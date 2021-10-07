from . models import UserToken

def is_authenticated(request) -> bool:
    if "authorization" in request.headers:
        token_str = request.headers.get("authorization")
        user_token= UserToken.objects.filter(token=token_str).first()
        if user_token:
            request.user = user_token.user
            return True