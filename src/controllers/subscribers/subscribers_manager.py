from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersManager:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subscribers_repo
        
    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        
        subscribers = self.__subs_repo.select_subscribers_by_link(link, event_id)
        
        return self.__format_subs_by_link(subscribers)
    
    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event_ranking = self.__subs_repo.get_ranking(event_id)
        
        return self.__format_event_ranking(event_ranking)
    
    def __format_subs_by_link(self, subscribers: list) -> HttpResponse:
        formmated_subscriber = []
        for subscriber in subscribers:
            formmated_subscriber.append({
                "email": subscriber.email,
                "nome": subscriber.nome
            })
        
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formmated_subscriber),
                    "attributes": formmated_subscriber
                }
            },
            status_code=200
        ) 
        
    def __format_event_ranking(self, event_ranking: list) -> HttpResponse:
        formmated_event_ranking = []
        for position in event_ranking:
            formmated_event_ranking.append({
                "link": position.link,
                "total_subscribers": position.total
            })
        
        return HttpResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formmated_event_ranking),
                    "ranking": formmated_event_ranking
                }
            },
            status_code=200
        ) 
        