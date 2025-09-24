from strawberry.types import Info

from templates.utils.dataclasses import AppContext
from templates.graphql.types.generic import ApiError, ApiSuccess


async def query_error_example(info: Info) -> ApiError:
    context: AppContext = info.context

    return ApiError(message="Not Implemented")


async def query_success_example(info: Info) -> ApiSuccess:
    context: AppContext = info.context

    return ApiSuccess(message="Nice")
