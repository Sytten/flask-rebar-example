from flask_rebar import errors

from app.app import registry
from app.schemas import HealthSchema


@registry.handles(rule="/health", method="GET", marshal_schema=HealthSchema())
def get_health():
    return {"status": "OK"}
