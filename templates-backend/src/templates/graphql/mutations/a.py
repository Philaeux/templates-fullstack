from strawberry.types import Info

from templates.graphql.types.generic import ApiError
from templates.utils.helpers import unpack_utilities


async def mutation_error_example(info: Info) -> ApiError:
    settings, session = unpack_utilities(info)

    # Typical user check
    # current_user = check_user(info.context["settings"].jwt_secret_key,
    #                           info.context["request"].headers.get("Authorization"))

    return ApiError(message="Not Implemented")
