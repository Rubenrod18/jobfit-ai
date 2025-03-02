from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def welcome_route():
    return {'Hello': 'World'}
