from strawberry.types import Info

from templates.utils.dataclasses import AppContext
from templates.graphql.types.generic import ApiError


async def mutation_error_example(info: Info) -> ApiError:
    context: AppContext = info.context

    # Typical user check
    # current_user = check_user(settings.jwt_secret_key, info.context["request"].headers.get("Authorization"))

    return ApiError(message="Not Implemented")
