"""
This file contains Pydantic model definitions for data validation.

Pydantic is a data validation library that uses Python type annotations.
It allows you to define data models with type hints that are validated
at runtime while providing static type checking.

Usage example:
```python
from my_model import MyModel

# Validates data at runtime
my_model = MyModel(name="John", age=30)

# Type-safe - my_model has correct type hints
print(my_model.name)

# Will raise error if validation fails
try:
    MyModel(name="", age=30)
except ValidationError as e:
    print(e)
```

For more information see:
https://docs.pydantic.dev/

WARNING: This is an auto-generated file.
Do not edit directly - any changes will be overwritten.
"""


## This is a generated file. Do not modify it manually!

from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Generic, TypeVar, Union
from enum import Enum
from uuid import uuid4
from datetime import date, datetime

# Filter Wrapper definition used to filter a list of objects
# based on their attributes
Cls = TypeVar("Cls")


class FilterWrapper(Generic[Cls]):
    """Wrapper class to filter a list of objects based on their attributes"""

    def __init__(self, collection: list[Cls], **kwargs):
        self.collection = collection
        self.kwargs = kwargs

    def filter(self) -> list[Cls]:
        for key, value in self.kwargs.items():
            self.collection = [
                item for item in self.collection if self._fetch_attr(key, item) == value
            ]
        return self.collection

    def _fetch_attr(self, name: str, item: Cls):
        try:
            return getattr(item, name)
        except AttributeError:
            raise AttributeError(f"{item} does not have attribute {name}")


# JSON-LD Helper Functions
def add_namespace(obj, prefix: str | None, iri: str | None):
    """Adds a namespace to the JSON-LD context

    Args:
        prefix (str): The prefix to add
        iri (str): The IRI to add
    """
    if prefix is None and iri is None:
        return
    elif prefix and iri is None:
        raise ValueError("If prefix is provided, iri must also be provided")
    elif iri and prefix is None:
        raise ValueError("If iri is provided, prefix must also be provided")

    obj.ld_context[prefix] = iri  # type: ignore


def validate_prefix(term: str | dict, prefix: str):
    """Validates that a term is prefixed with a given prefix

    Args:
        term (str): The term to validate
        prefix (str): The prefix to validate against

    Returns:
        bool: True if the term is prefixed with the prefix, False otherwise
    """

    if isinstance(term, dict) and not term["@id"].startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")
    elif isinstance(term, str) and not term.startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")


# Model Definitions


class Components(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    name: str = Field(
        default=...,
        description="""The name of the component can be either the
        trivial or trade name, the systematic
        designation according to IUPAC
        nomenclature, or any other means of
        identifying the substance.""",
    )
    smiles: str = Field(
        default=...,
        description="""SMILES (Simplified Molecular Input Line Entry
        System) is a chemical notation used
        to represent and describe molecular
        structures in a simplified and human-
        readable format.""",
    )
    persistent_identifier_PID: str = Field(
        default=...,
        description="""One or more identifiers that refer to the
        compound, such as CAS number, PubChem
        code, InChI code, etc.""",
    )
    concentration: float = Field(
        default=...,
        description="""Concentration of the component.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""The concentration of the component is typically
        expressed in M (Molar), mmol/L (millimoles
        per liter), or µmol/L (micromoles per
        liter).""",
    )
    supplier: str = Field(
        default=...,
        description="""Information about the source of the compound,
        usually a commercial supplier with perhaps
        product code, but could be preparation
        in a research lab. Should the component
        have been synthesized internally, please
        include a literature reference detailing
        its synthesis.""",
    )
    purity: float = Field(
        default=...,
        description="""Purity of a substance typically expressed in
        percentage (%). It is commonly defined
        as the percentage of the pure or desired
        compound relative to the total mass or
        volume of the substance.""",
    )
    formulation: str = Field(
        default=...,
        description="""The formulation encompass the nature of the
        component, whether it is in powder,
        liquid, gaseous form, or any other form,
        as well as the specific conditions under
        which it is presented.""",
    )
    solubility_limit: float = Field(
        default=...,
        description="""This limit represents the maximum concentration
        of a component, which might include gases,
        that can dissolve in a solution or gas
        phase. ( if_applicable )""",
    )
    solubility_limit_unit: str = Field(
        default=...,
        description="""The solubility limit of a component can be
        expressed in various units, including
        M (moles per liter), g/L (grams per
        liter), % (percentage concentration), or
        particles per volume, depending on the
        type of component and the solvent used.
        ( if_applicable )""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:Components/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:Components",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class StorageConditions(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    temperature: float = Field(
        default=...,
        description="""Temperature at which the component is stored.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    storage_start: date = Field(
        default=...,
        description="""The date since the component has been stored.""",
    )
    additives: str = Field(
        default=...,
        description="""Additives for the storage of components can
        include antioxidants, stabilizers,
        drying agent, or even inert gases (argon,
        nitrogen), among others.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific characteristics
        or aspects related to a component that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:StorageConditions/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:StorageConditions",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


# Rebuild all the classes within this file
for cls in [
    Components,
    StorageConditions,
]:
    cls.model_rebuild()
