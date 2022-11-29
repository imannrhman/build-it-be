from fastapi import FastAPI, status, Request, Response, APIRouter

from app.core.route import route
from app.core.settings import settings
from app.models.orders import OrderForm
from app.models.users import UsernamePasswordForm, UserForm, UserUpdateForm

app = FastAPI()

order = APIRouter(
    prefix='/v1/api/orders',
    tags=['Order']
)

auth = APIRouter(
    prefix='/v1/api/auth',
    tags=['Auth']
)


@route(
    request_method=app.post,
    path='/api/login',
    status_code=status.HTTP_201_CREATED,
    payload_key='username_password',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func='app.core.post_processing.access_token_generate_handler',
    response_model='app.models.users.LoginResponse'
)
async def login(username_password: UsernamePasswordForm,
                request: Request, response: Response):
    pass


@route(
    request_method=app.post,
    path='/api/users',
    status_code=status.HTTP_201_CREATED,
    payload_key='user',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    service_header_generator='app.core.auth.generate_request_header',
    response_model='app.models.users.UserResponse',
)
async def create_user(user: UserForm, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path='/api/users',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    service_header_generator='app.core.auth.generate_request_header',
    response_model='app.models.users.UserResponse',
    response_list=True
)
async def get_users(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path='/api/users/{user_id}',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    service_header_generator='app.core.auth.generate_request_header',
    response_model='app.models.users.UserResponse',
)
async def get_user(user_id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.delete,
    path='/api/users/{user_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    service_header_generator='app.core.auth.generate_request_header',
)
async def delete_user(user_id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.put,
    path='/api/users/{user_id}',
    status_code=status.HTTP_200_OK,
    payload_key='user',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    service_header_generator='app.core.auth.generate_request_header',
    response_model='app.models.users.UserResponse',
)
async def update_user(user_id: int, user: UserUpdateForm,
                      request: Request, response: Response):
    pass


@route(
    request_method=order.get,
    path='',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.ORDERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    service_header_generator='app.core.auth.generate_request_header',
    response_model='app.models.orders.OrderResponse',
    response_list=True,
)
async def get_orders(request: Request, response: Response):
    pass


@route(
    request_method=order.post,
    path='',
    status_code=status.HTTP_200_OK,
    payload_key='order',
    service_url=settings.ORDERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    service_header_generator='app.core.auth.generate_request_header',
    response_model='app.models.orders.OrderResponse',
)
async def create_order(order: OrderForm, request: Request, response: Response):
    pass


app.include_router(order)
