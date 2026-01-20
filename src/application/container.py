from dependency_injector import containers, providers

from src.application.use_cases.create_order_in_db import OrderPersister


class ApplicationContainer(containers.DeclarativeContainer):
    uow: providers.Dependency = providers.Dependency()

    create_order_in_db = providers.Factory(
        OrderPersister,
        uow=uow,
    )
