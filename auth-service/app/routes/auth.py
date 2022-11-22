from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


auth = APIRouter()


oath2_schema = OAuth2PasswordBearer(tokenUrl='token')


@auth.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {
        'access_token': form_data.username + 'token',

    }


@auth.route('/')
async def index(token: str = Depends(oath2_schema)):
    return {'the_token': token}

