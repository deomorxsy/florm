# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related utilities."""

from .extensions import db
from .compat import basestring

# Alias common SQLAlchemy names
Column = db.Column
relationship = db.relationship

from typing import Optional, Type, TypeVar
T = TypeVar("T", bound="PkModel")

# The Mixin concept uses the dependency inversion principle to inject code into a class
class crudMixin(object):
    """convenience mixin for crud operations"""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            return self.save()
        return self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit: bool = True) -> None:
        """Remove the record from the database."""
        db.session.delete(self)
        if commit:
            return db.session.commit()
        return


class Model(crudMixin, db.Model):
    """ Base Model class that includes CRUD convenience methods. """
    __abstract__ = True
    id = Column(db.Integer, primary_key=True)


class PkModel(Model):
    """ Base model class with basic CRUD operations which
    includes id as primary_key"""
    __abstract__ = True
    id = Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls: Type[T], record_id) -> Optional[T]:
        """ Get record by id """
        if any((
            isinstance(record_id, basestring) and record_id.isdigit(),
            isinstance(record_id, (int, float))
            )):
            return cls.query.get(int(record_id))
        return None


def reference_col(
        tablename,
        nullable=False,
        pk_name="id",
        foreign_key_kwargs=None,
        column_kwargs=None):
    foreign_key_kwargs = foreign_key_kwargs or {}
    column_kwargs = column_kwargs or {}

    return Column(
            db.ForeignKey(f'{tablename}.{pk_name}', **foreign_key_kwargs),
            nullable=nullable,
            **column_kwargs
            )


