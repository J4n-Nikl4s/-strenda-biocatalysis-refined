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


class MonoliquidSystemDescription_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    solvent_description: str = Field(
        default=...,
        description="""The solvent used in the reaction system, e.g. a
        buffered aqueous solution or an organic
        solvent.""",
    )
    ionic_strength: float = Field(
        default=...,
        description="""Ionic strength calculated according to the
        dissolved ions in the solvent. The
        following formula can be used: $$I =
        \frac{1}{2} \sum _ {i=1}^n C_i Z_i^2$
        $ where, I - ionic strength, Ci - ionic
        concentration and Zi - ion charges.
        ( if_applicable )""",
    )
    ionic_strength_unit: str = Field(
        default=...,
        description="""The unit of ionic strength is usually expressed
        in mol/L (moles per liter), or in mmol/L
        (millimoles per liter). ( if_applicable )""",
    )
    further_additives: str = Field(
        default=...,
        description="""Further additive like cosolvents used to increase
        solubility of components, e.g. DMSO.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the monoliquid system that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:MonoliquidSystemDescription_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:MonoliquidSystemDescription_WMRS",
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


class MultiphasicSystemDescription_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    phases_number: float = Field(
        default=...,
        description="""Number of phases present in the system, if there
        is an aqueous and a gas phase present, the
        number is 2.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the multiphasic system that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:MultiphasicSystemDescription_WMRS/"
        + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:MultiphasicSystemDescription_WMRS",
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


class LiquidPhase_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    liquid_type: str = Field(
        default=...,
        description="""Information about the type of liquid used, whether
        it is an organic solvent,an aqueous buffer
        or are mixture of both.""",
    )
    liquid_amount: float = Field(
        default=...,
        description="""Amount of the liquid added to the reaction.""",
    )
    liquid_unit: str = Field(
        default=...,
        description="""In case of aqueous liquids, mL (milliliter) is
        often used as unit, in case of organic
        solvents, volume percentage (Vol %) or
        volume fraction (Vol/Vol) is utilized.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:LiquidPhase_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:LiquidPhase_WMRS",
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


class SolidPhase_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    solid_type: str = Field(
        default=...,
        description="""Information about the type of solid used, whether
        it is a support material, solid catalyst,
        or any other solid compound.""",
    )
    solid_amount: float = Field(
        default=...,
        description="""Mass of the solid compound used in the reaction
        solution.""",
    )
    solid_unit: str = Field(
        default=...,
        description="""In the case of a solid compound, common units
        like grams, milligrams, or micrograms can
        be used.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:SolidPhase_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:SolidPhase_WMRS",
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


class GasPhase_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    gas_type: str = Field(
        default=...,
        description="""Information about the type of gas used, whether it
        is nitrogen, carbon dioxide, argon, oxygen
        or other gases.""",
    )
    gas_amount: float = Field(
        default=...,
        description="""Concentration of the gas in the gas phase.""",
    )
    gas_unit: str = Field(
        default=...,
        description="""In the case of gases, common units are volume
        percentage (Vol %), volume fraction (Vol/
        Vol), mole percentage (Mol %) or molar
        fraction (Mol/Mol).""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:GasPhase_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:GasPhase_WMRS",
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


class TemperatureConstant_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    temperature: float = Field(
        default=...,
        description="""Temperature during the reaction.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the temperature that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:TemperatureConstant_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:TemperatureConstant_WMRS",
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


class EventBasedTemperatureShift_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    temperature_beginning: float = Field(
        default=...,
        description="""The initial temperature, prior to the start of the
        reaction, should be specified.""",
    )
    temperature_after_event: float = Field(
        default=...,
        description="""The temperature that is present after a specific
        event has occurred.""",
    )
    event_description: str = Field(
        default=...,
        description="""Information regarding the event that caused the
        temperature change. In the case of a fed-
        batch reaction protocol, this event can
        also be the planned adjustment of the
        temperature to another specific value
        based on the current progress of the
        reaction process.""",
    )
    temperature_at_XY: float = Field(
        default=...,
        description="""The temperature can also be measured at a variably
        chosen time point XY during the reaction.""",
    )
    time_at_XY: float = Field(
        default=...,
        description="""Specification of the exact time point XY at which
        the temperature was measured.""",
    )
    time_unit: str = Field(
        default=...,
        description="""Common units for specifying time can be s
        (seconds), min (minutes) or h (hours).""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the temperature that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:EventBasedTemperatureShift_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:EventBasedTemperatureShift_WMRS",
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


class pHConstant_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    pH_value: float = Field(
        default=...,
        description="""Value of the pH.""",
    )
    detected_when: str = Field(
        default=...,
        description="""Specification of the timepoint at which the pH was
        measured. It includes whether the pH value
        was measured before, during, or after the
        reaction and whether all components of the
        reaction solution were already present or
        if some were added after the measurement.""",
    )
    detected_how: str = Field(
        default=...,
        description="""The pH value of a reaction can be determined in
        various ways, such as using a pH meter, pH
        paper, titration, electrochemical sensors,
        or other methods.""",
    )
    temperature: float = Field(
        default=...,
        description="""The temperature at the time of pH measurement.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    calibration_pH_electrode: str = Field(
        default=...,
        description="""Usually, a pH electrode is calibrated using
        standard buffers at 20-25 °C. If the
        conditions in the reaction mixture
        differ from this, it should be specified.
        ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the pH value that are important
        for reproducibility and are not described
        by the aforementioned metadata, they
        should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:pHConstant_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:pHConstant_WMRS",
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


class EventBasedpHShift_WMRS(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    pH_beginning: float = Field(
        default=...,
        description="""The initial pH, prior to the start of the
        reaction, should be specified.""",
    )
    pH_after_event: float = Field(
        default=...,
        description="""The pH that is present after a specific event
        has occurred.""",
    )
    event_description: str = Field(
        default=...,
        description="""Information regarding the event that caused the
        pH change. In the case of a fed-batch
        reaction protocol, this event can also
        be the planned adjustment of the pH value
        to another specific value based on the
        current progress of the reaction process.""",
    )
    pH_at_XY: float = Field(
        default=...,
        description="""The pH can also be measured at a variably chosen
        time point XY during the reaction.""",
    )
    time_at_XY: float = Field(
        default=...,
        description="""Specification of the exact time point XY at which
        the pH was measured.""",
    )
    time_unit: str = Field(
        default=...,
        description="""Common units for specifying time can be s
        (seconds) or min (minutes).""",
    )
    detected_when: str = Field(
        default=...,
        description="""Specification whether all components of the
        reaction solution were already present or
        if some were added after the measurement
        at the timepoint of the pH measurement.""",
    )
    detected_how: str = Field(
        default=...,
        description="""The pH value of a reaction can be determined in
        various ways, such as using a pH meter, pH
        paper, titration, electrochemical sensors,
        or other methods.""",
    )
    temperature: float = Field(
        default=...,
        description="""The temperature at the time of pH measurement.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    calibration_pH_electrode: str = Field(
        default=...,
        description="""Usually, a pH electrode is calibrated using
        standard buffers at 20-25 °C. If the
        conditions in the reaction mixture
        differ from this, it should be specified.
        ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the pH value that are important
        for reproducibility and are not described
        by the aforementioned metadata, they
        should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:EventBasedpHShift_WMRS/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:EventBasedpHShift_WMRS",
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


class MonoliquidSystemDescription_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    solvent_description: str = Field(
        default=...,
        description="""The solvent used in the reaction system, e.g. a
        buffered aqueous solution or an organic
        solvent.""",
    )
    ionic_strength: float = Field(
        default=...,
        description="""Ionic strength calculated according to the
        dissolved ions in the solvent. The
        following formula can be used: $$I =
        \frac{1}{2} \sum _ {1}^n C_i Z_i^2$
        $ where, I - ionic strength, Ci - ionic
        concentration and Zi - ion charges
        ( if_applicable )""",
    )
    ionic_strength_unit: str = Field(
        default=...,
        description="""The unit of ionic strength is usually expressed
        in mol/L (moles per liter), or in mmol/L
        (millimoles per liter). ( if_applicable )""",
    )
    further_additives: str = Field(
        default=...,
        description="""Further additive like cosolvents used to increase
        solubility of reactants, e.g. DMSO.""",
    )
    Flow_rate: float = Field(
        default=...,
        description="""The flow rate must be specified to determine how
        fast a liquid or gas is flowing through a
        reactor or system.""",
    )
    Flow_rate_unit: str = Field(
        default=...,
        description="""Common units for describing flow rate include L/
        min (liters per minute), mL/h (milliliters
        per hour), m³/h (cubic meters per hour),
        or other volume units per unit of time.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the monoliquid system that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:MonoliquidSystemDescription_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:MonoliquidSystemDescription_TFCR",
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


class MultiphasicSystemDescription_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    phases_number: float = Field(
        default=...,
        description="""Number of phases present in the system, if there
        is an aqueous and a gas phase present, the
        number is 2.""",
    )
    Flow_rate: float = Field(
        default=...,
        description="""The flow rate must be specified to determine how
        fast a liquid or gas is flowing through a
        reactor or system.""",
    )
    Flow_rate_unit: str = Field(
        default=...,
        description="""Common units for describing flow rate include L/
        min (liters per minute), mL/h (milliliters
        per hour), m³/h (cubic meters per hour),
        or other volume units per unit of time.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the multiphasic system that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:MultiphasicSystemDescription_TFCR/"
        + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:MultiphasicSystemDescription_TFCR",
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


class LiquidPhase_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    liquid_type: str = Field(
        default=...,
        description="""Information about the type of liquid used, whether
        it is an organic solvent, an aqueous
        buffer or a mixture of both.""",
    )
    liquid_amount: float = Field(
        default=...,
        description="""Amount of the liquid added to the reaction.""",
    )
    liquid_unit: str = Field(
        default=...,
        description="""In case of aqueous liquids, mL (milliliter) is
        often used as unit, in case of organic
        solvents, volume percentage (Vol %) or
        volume fraction (Vol/Vol) is utilized.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:LiquidPhase_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:LiquidPhase_TFCR",
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


class SolidPhase_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    solid_type: str = Field(
        default=...,
        description="""Information about the type of solid used, whether
        it is a support material, solid catalyst,
        or any other solid compound.""",
    )
    solid_amount: float = Field(
        default=...,
        description="""Mass of the solid used in the reaction solution.""",
    )
    solid_unit: str = Field(
        default=...,
        description="""In the case of solids, common units like grams,
        milligrams, or micrograms can be used.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:SolidPhase_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:SolidPhase_TFCR",
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


class GasPhase_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    gas_type: str = Field(
        default=...,
        description="""Information about the type of gas used, whether
        it's nitrogen dioxide, argon, oxygen or
        other gases.""",
    )
    gas_amount: float = Field(
        default=...,
        description="""Concentration of the gas in the gas phase.""",
    )
    gas_unit: str = Field(
        default=...,
        description="""In the case of gases, common units are volume
        percentage (Vol %), volume fraction (Vol/
        Vol), mole percentage (Mol %) or molar
        fraction (Mol/Mol).""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:GasPhase_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:GasPhase_TFCR",
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


class TemperatureConstant_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    temperature: float = Field(
        default=...,
        description="""Temperature during the reaction.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the temperature that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:TemperatureConstant_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:TemperatureConstant_TFCR",
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


class DynamicTemperature_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    temperature_beginning: float = Field(
        default=...,
        description="""The initial temperature, prior to the start of the
        reaction, should be specified.""",
    )
    temperature_after_event: float = Field(
        default=...,
        description="""The temperature that is present after a specific
        event has occurred.""",
    )
    event_description: str = Field(
        default=...,
        description="""Information regarding the event that caused the
        temperature change. In the case of a fed-
        batch reaction protocol, this event can
        also be the planned adjustment of the
        temperature to another specific value
        based on the current progress of the
        reaction process.""",
    )
    temperature_at_XY: float = Field(
        default=...,
        description="""The temperature can also be measured at a variably
        chosen time point XY during the reaction.""",
    )
    time_at_XY: float = Field(
        default=...,
        description="""Specification of the exact time point XY at which
        the temperature was measured.""",
    )
    time_unit: str = Field(
        default=...,
        description="""Common units for specifying time can be s
        (seconds), min (minutes) h (hours).""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    temperature_gradient_beginning: float = Field(
        default=...,
        description="""The initial temperature from which the temperature
        gradient begins. ( if_applicable )""",
    )
    temperature_gradient_end: float = Field(
        default=...,
        description="""The target temperature reached after the
        temperature gradient is applied.
        ( if_applicable )""",
    )
    gradient_length: float = Field(
        default=...,
        description="""The distance or time span over which the
        temperature gradient is applied.
        ( if_applicable )""",
    )
    gradient_length_unit: str = Field(
        default=...,
        description="""The gradient length can be specified either as
        the physical distance (e.g. in meters)
        or as the time span (e.g. in minutes).
        ( if_applicable )""",
    )
    measurement_points: str = Field(
        default=...,
        description="""Information about the locations or time points
        where temperature measurements are taken
        to monitor the gradient. This can be
        important to ensure that the gradient
        behaves as intended. ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the temperature profile that
        are important for reproducibility and
        are not described by the aforementioned
        metadata, they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:DynamicTemperature_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:DynamicTemperature_TFCR",
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


class pHConstant_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    pH_value: float = Field(
        default=...,
        description="""The value of the pH.""",
    )
    detected_when: str = Field(
        default=...,
        description="""Specification of the timepoint at which the pH was
        measured. It includes whether the pH value
        was measured before, during, or after the
        reaction and whether all components of the
        reaction solution were already present or
        if some were added after the measurement.""",
    )
    detected_how: str = Field(
        default=...,
        description="""The pH value of a reaction can be determined in
        various ways, such as using a pH meter, pH
        paper, titration, electrochemical sensors,
        or other methods.""",
    )
    temperature: float = Field(
        default=...,
        description="""The temperature at the time of pH measurement.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    calibration_pH_electrode: str = Field(
        default=...,
        description="""Usually, a pH electrode is calibrated using
        standard buffers at 20-25 °C. If the
        conditions in the reaction mixture
        differ from this, it should be specified.
        ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the pH value that are important
        for reproducibility and are not described
        by the aforementioned metadata, they
        should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:pHConstant_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:pHConstant_TFCR",
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


class DynamicpH_TFCR(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    pH_beginning: float = Field(
        default=...,
        description="""The initial pH, prior to the start of the
        reaction, should be specified.""",
    )
    pH_after_event: float = Field(
        default=...,
        description="""The pH that is present after a specific event
        has occurred.""",
    )
    event_description: str = Field(
        default=...,
        description="""Information regarding the event that caused the
        pH change. In the case of a fed-batch
        reaction protocol, this event can also
        be the planned adjustment of the pH value
        to another specific value based on the
        current progress of the reaction process.""",
    )
    pH_at_XY: float = Field(
        default=...,
        description="""The pH can also be measured at a variably chosen
        time point XY during the reaction.""",
    )
    time_at_XY: float = Field(
        default=...,
        description="""Specification of the exact time point XY at which
        the pH was measured.""",
    )
    time_unit: str = Field(
        default=...,
        description="""Common units for specifying time can be s
        (seconds) or min (minutes).""",
    )
    detected_when: str = Field(
        default=...,
        description="""Specification whether all components of the
        reaction solution were already present or
        if some were added after the measurement
        at the timepoint of the pH measurement.""",
    )
    detected_how: str = Field(
        default=...,
        description="""The pH value of a reaction can be determined in
        various ways, such as using a pH meter, pH
        paper, titration, electrochemical sensors,
        or other methods.""",
    )
    temperature: float = Field(
        default=...,
        description="""The temperature at the time of pH measurement.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    calibration_pH_electrode: str = Field(
        default=...,
        description="""Usually, a pH electrode is calibrated using
        standard buffers at 20-25 °C. If the
        conditions in the reaction mixture
        differ from this, it should be specified.
        ( if_applicable )""",
    )
    pH_gradient_beginning: float = Field(
        default=...,
        description="""The initial pH from which the pH gradient begins.
        ( if_applicable )""",
    )
    pH_gradient_end: float = Field(
        default=...,
        description="""The target pH reached after the pH gradient is
        applied. ( if_applicable )""",
    )
    gradient_length: float = Field(
        default=...,
        description="""The distance or time span over which the pH
        gradient is applied. ( if_applicable )""",
    )
    gradient_length_unit: str = Field(
        default=...,
        description="""The gradient length can be specified either as
        the physical distance (e.g. in meters)
        or as the time span (e.g. in minutes).
        ( if_applicable )""",
    )
    measurement_points: str = Field(
        default=...,
        description="""Information about the locations or time points
        where pH measurements are taken to monitor
        the gradient. This can be important
        to ensure that the gradient behaves as
        intended. ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the pH value that are important
        for reproducibility and are not described
        by the aforementioned metadata, they
        should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:DynamicpH_TFCR/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:DynamicpH_TFCR",
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
    MonoliquidSystemDescription_WMRS,
    MultiphasicSystemDescription_WMRS,
    LiquidPhase_WMRS,
    SolidPhase_WMRS,
    GasPhase_WMRS,
    TemperatureConstant_WMRS,
    EventBasedTemperatureShift_WMRS,
    pHConstant_WMRS,
    EventBasedpHShift_WMRS,
    MonoliquidSystemDescription_TFCR,
    MultiphasicSystemDescription_TFCR,
    LiquidPhase_TFCR,
    SolidPhase_TFCR,
    GasPhase_TFCR,
    TemperatureConstant_TFCR,
    DynamicTemperature_TFCR,
    pHConstant_TFCR,
    DynamicpH_TFCR,
]:
    cls.model_rebuild()
