from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager
from flask_caching import Cache

# API configuration
API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# Rate limiting
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

# JWT configuration
jwt = JWTManager()

# Cache configuration
cache = Cache(config={
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
})
