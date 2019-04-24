from uuid import UUID

import flask_rebar
from flask_rebar import errors

from app.app import registry, db
from app.models.account import Account
from app.schemas.account import AccountSchema, CreateAccountSchema


@registry.handles(
    rule="/accounts",
    method="POST",
    marshal_schema={201: AccountSchema()},
    request_body_schema=CreateAccountSchema(),
)
def create_account():
    body = flask_rebar.get_validated_body()

    account = Account(**body)
    db.session.add(account)
    db.session.commit()

    return account, 201


@registry.handles(
    rule="/accounts/<uuid:account_id>", method="GET", marshal_schema=AccountSchema()
)
def get_account(account_id: UUID):
    account = Account.query.filter_by(id=account_id).first()
    if account is None:
        raise errors.NotFound()

    return account


@registry.handles(
    rule="/accounts/<uuid:account_id>",
    method="PUT",
    request_body_schema=CreateAccountSchema(),
)
def replace_account(account_id: UUID):
    body = flask_rebar.get_validated_body()

    account = Account.query.filter_by(id=account_id).update(body)
    if account is None:
        raise errors.NotFound()
    db.session.commit()

    return "", 204


@registry.handles(rule="/accounts/<uuid:account_id>", method="DELETE")
def delete_account(account_id: UUID):
    account = Account.query.filter_by(id=account_id).first()
    if account is None:
        raise errors.NotFound()
    db.session.delete(account)
    db.session.commit()

    return "", 204
