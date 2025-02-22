import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert_subscriber():
    subscriber_info = {
        "nome": "MeuNome",
        "email": "meunome@email.com",
        "link": "http://meulink.com",
        "evento_id": 1
    }
    
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "meunome@email.com"
    evento_id = 2
    
    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id) 
    print(resp.nome)
    
    