from dependency_injector import containers, providers

from .use_cases.create_order import CreateOrder


class ApplicationContainer(containers.DeclarativeContainer):
    uow: providers.Dependency = providers.Dependency()
    catalog_api = providers.Dependency()

    create_order = providers.Factory(CreateOrder, uow=uow, catalog=catalog_api)
