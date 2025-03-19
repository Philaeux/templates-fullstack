from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyLoader

from templates.graphql.schema import schema
from templates.settings import Settings
from templates.utils.helpers import check_migration


def make_app(settings: Settings):
    # Database
    engine = create_engine(settings.database_uri)
    check_migration(settings.database_uri)

    # Session dependency
    def get_session():
        with Session(engine, expire_on_commit=False) as session:
            yield session
    SessionDep = Annotated[Session, Depends(get_session)]

    # App creation
    @asynccontextmanager
    async def lifespan(fast_app: FastAPI):
        # Add startup functions here
        yield
        # Add shutdown functions here

    app = FastAPI(lifespan=lifespan)
    app.engine = engine
    app.settings = settings

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            settings.frontend_uri,
            "http://localhost:4200"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # GraphQL
    async def get_context(session: SessionDep):
        """Contexte passed to all GraphQL functions. Give database access"""
        return {
            "settings": settings,
            "session": session,
            "sqlalchemy_loader": StrawberrySQLAlchemyLoader(bind=session),
        }

    graphql_app = GraphQLRouter(
        schema,
        graphql_ide="graphiql" if settings.debug else None,
        context_getter=get_context,
    )
    app.include_router(graphql_app, prefix="/graphql")

    # Static files
    # app.mount("/aaa, StaticFiles(directory=any path), name="data")

    # Classic REST endpoints
    @app.get('/hello')
    async def hello(request: Request):
        return {"message": "Hello World"}

    return app
