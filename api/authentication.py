import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.conf import settings

try:
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': settings.FIREBASE_PROJECT_ID,
    })
except Exception as e:
    print(f"Firebase Admin SDK Error: {e}")
    print("Certifique-se de que a autenticação do Google Cloud está configurada ou use uma chave de serviço.")


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            raise exceptions.AuthenticationFailed('Cabeçalho de autorização mal formatado.')

        id_token = parts[1]

        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Token inválido: {e}')

        try:
            user, created = User.objects.get_or_create(username=uid)

            if created:
                if 'email' in decoded_token:
                    user.email = decoded_token['email']
                if 'name' in decoded_token:
                    user.first_name = decoded_token['name']
                user.save()

            return user, None

        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Erro ao buscar ou criar usuário: {e}')