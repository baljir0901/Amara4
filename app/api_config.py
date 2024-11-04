from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from datetime import timedelta

# Rate limiting configuration
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"],
    storage_uri="memory://"
)

# JWT configuration
jwt = JWTManager()
JWT_SECRET_KEY = "your-secret-key-change-this"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

# Cache configuration
cache = Cache(config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300
})

# API Versions
API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# Custom error messages
ERROR_MESSAGES = {
    'rate_limit_exceeded': 'Rate limit exceeded. Please try again later.',
    'token_expired': 'Authentication token has expired.',
    'invalid_token': 'Invalid authentication token.',
    'missing_token': 'Authentication token is missing.',
    'invalid_request': 'Invalid request parameters.',
    'server_error': 'Internal server error occurred.'
}
