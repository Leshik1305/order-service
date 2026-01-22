from dependency_injector import containers, providers

from .db import Database
from .http.http_clients import CatalogServiceAPI
from .uow import UnitOfWork


class InfrastructureContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(
        Database,
        db_url=config.POSTGRES_CONNECTION_STRING,
    )

    uow = providers.Singleton(
        UnitOfWork,
        db=db,
    )

    catalog_api = providers.Singleton(
        CatalogServiceAPI,
        base_url=config.BASE_URL,
        api_key=config.API_KEY,
    )
