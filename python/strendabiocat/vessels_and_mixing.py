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


class Vial(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    vial_size: float = Field(
        default=...,
        description="""The vial's size, which can be its volume or its
        dimensions.""",
    )
    vial_size_unit: str = Field(
        default=...,
        description="""For describing the vial size, you can use mL
        (milliliters) as the unit when referring
        to volume or cm (centimeters) when
        referring to dimensions.""",
    )
    vial_material: str = Field(
        default=...,
        description="""Specify the material of the vial, such as glass or
        plastic, as it can influence the reaction.""",
    )
    closure_type: str = Field(
        default=...,
        description="""Indicate the type of closure or stopper used for
        the vial, as it affects sealing and the
        course of the reaction. If no closure or
        seal was used for the vial, this should be
        noted as well.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the vial or its preparation
        for the reaction that are important for
        reproducibility and are not described by
        the aforementioned metadata, they should
        be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id", default_factory=lambda: "stbc:Vial/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:Vial",
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


class Plate(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    plate_type: str = Field(
        default=...,
        description="""The type of plate, such as microtiter plate, deep-
        well plate, or others.""",
    )
    plate_material: str = Field(
        default=...,
        description="""The material from which the plate is made, such as
        plastic (polystyrene), glass, or metal.""",
    )
    number_of_wells: str = Field(
        default=...,
        description="""The total number of wells or cavities in the
        plate.""",
    )
    well_shape: str = Field(
        default=...,
        description="""""",
    )
    well_volume: str = Field(
        default=...,
        description="""The volume of each well is, usually expressed in
        µL (microliters).""",
    )
    well_arrangement: str = Field(
        default=...,
        description="""The arrangement of the wells in the plate, for
        example, in rows and columns.""",
    )
    supplier: str = Field(
        default=...,
        description="""Information about the supplier from which the
        plate was purchased.""",
    )
    lot_number: float = Field(
        default=...,
        description="""The lot number, also known as a batch number or
        code, is a unique identifier assigned to a
        specific batch of a product. This makes it
        possible to check or track information on
        production.""",
    )
    sealing_method: str = Field(
        default=...,
        description="""Indicate if the wells were sealed with a sealing
        film or lid. ( if_applicable )""",
    )
    sealing_material: str = Field(
        default=...,
        description="""The material of the sealing film or lid.
        ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the plate or its preparation
        for the reaction that are important for
        reproducibility and are not described by
        the aforementioned metadata, they should
        be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id", default_factory=lambda: "stbc:Plate/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:Plate",
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


class StirredTankReactor(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    type: str = Field(
        default=...,
        description="""There are several types of Stirred Tank Reactors,
        differing in design and intended use. A
        detailed description is required.""",
    )
    material: str = Field(
        default=...,
        description="""Material the reactor is made of, e.g. glass,
        polypropylene etc.""",
    )
    volume: float = Field(
        default=...,
        description="""Indicate the total volume capacity of the Stirred
        Tank Reactor.""",
    )
    volume_unit: str = Field(
        default=...,
        description="""The volume is typically expressed in L (liters).""",
    )
    geometry: str = Field(
        default=...,
        description="""The geometry of the reactor, in particular of
        interest is the ratio of height to width.""",
    )
    bottom_type: str = Field(
        default=...,
        description="""Shape of the bottom of the reactor, e.g. a round
        bottom or a flat bottom.""",
    )
    gas_consumption: str = Field(
        default=...,
        description="""Common gases that are supplied to the reactor
        include, e.g., air, oxygen, hydrogen, etc.""",
    )
    gas_supply: str = Field(
        default=...,
        description="""Gas can be supplied to a Stirred Tank Reactor in
        various ways, such as through sparging
        using a tube or an aeration basket,
        bubbling, or direct injection into the
        reactor vessel.""",
    )
    gas_supply_rate: float = Field(
        default=...,
        description="""Specification of the gas supply rate.""",
    )
    gas_supply_rate_unit: str = Field(
        default=...,
        description="""The units for the gas supply rate in a Stirred
        Tank Reactor can be L/min (liters per
        minute), m³/h (cubic meters per hour), or
        other volume units per unit of time.""",
    )
    temperature_control: str = Field(
        default=...,
        description="""The temperature in a Stirred Tank Reactor can
        be controlled through various methods,
        typically using external heat sources or
        cooling systems such as heating jackets,
        cooling coils, or external temperature
        control units.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the Stirred Tank Reactor or
        its preparation for the reaction that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:StirredTankReactor/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:StirredTankReactor",
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


class TubularFlowContinuousReactor(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    volume: float = Field(
        default=...,
        description="""Indicate the total volume capacity of the tubular
        flow/continuous reactor.""",
    )
    volume_unit: str = Field(
        default=...,
        description="""The volume is typically expressed in L (liters).""",
    )
    geometry: str = Field(
        default=...,
        description="""The exact geometry of the tubular flow/continuous
        reactor.""",
    )
    reactor_type: str = Field(
        default=...,
        description="""There are several types of tubular flow/continuous
        reactors, e.g. packed bed reactor, or a
        plug flow reactor, differing in design
        and intended use. A detailed description
        is required.""",
    )
    material: str = Field(
        default=...,
        description="""Material the reactor is made of, e.g. glass,
        stainless steel or other materials.""",
    )
    tubing: str = Field(
        default=...,
        description="""When using tubing in a tubular flow/continuous
        reactor, various pieces of information
        can be provided, such as tubing material,
        diameter, length, connections, etc.""",
    )
    localisation_of_the_catalyst: str = Field(
        default=...,
        description="""Specify the exact location of the catalyst in
        the tubular flow/continuous reactor. The
        biocatalyst is typically present in the
        liquid phase or immobilized on a support
        matrix (such as particles or membranes).""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or
        aspects related to the tubular flow/
        continuous reactor or its preparation
        for the reaction that are important for
        reproducibility and are not described by
        the aforementioned metadata, they should
        be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:TubularFlowContinuousReactor/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:TubularFlowContinuousReactor",
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


class Shaking(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    shaking_type: str = Field(
        default=...,
        description="""The type of shaking used to mix the reaction
        (e.g., horizontal, vertical, back-and-
        forth or circulatory).""",
    )
    deflection: float = Field(
        default=...,
        description="""Information about the extent of deflection or
        bending of the agitator from its original
        position of the horizontal shaking system.""",
    )
    deflection_unit: str = Field(
        default=...,
        description="""Units such as mm (millimeters) or μm (micrometers)
        could be used to describe deflection in
        relation to the movement of the shaking
        system.""",
    )
    speed: float = Field(
        default=...,
        description="""Specify the speed or frequency at which the
        shaking was conducted.""",
    )
    speed_unit: str = Field(
        default=...,
        description="""The shaking speed or frequency could be expressed
        in units such as rpm (rounds per minute)
        or Hz (cycles per second).""",
    )
    position: str = Field(
        default=...,
        description="""Information regarding the orientation of the
        vessel in the shaking system relative to
        deflection.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the shaking that are important
        for reproducibility and are not described
        by the aforementioned metadata, they
        should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:Shaking/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:Shaking",
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


class MechanicallyImpelledMixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    stirring_type: str = Field(
        default=...,
        description="""There are several types of stirring methods used
        in laboratory and industrial settings,
        including magnetic stirring (from vessel
        bottom), mechanical stirring, overhead
        stirring and other methods.""",
    )
    stirrer_material: str = Field(
        default=...,
        description="""The specific composition or nature of the material
        should be indicated, e.g. whether it
        is made of magnetic material, a PTFE
        (polytetrafluoroethylene) coating,
        stainless steel or other relevant
        features that determine its structural
        or functional properties within the
        experimental setup.""",
    )
    supplier: str = Field(
        default=...,
        description="""If available, details of the specific designation
        or manufacturer's name of the stirrer
        should be provided for precise
        identification.""",
    )
    number_of_stirrers: float = Field(
        default=...,
        description="""The number of stirrers available in the system.""",
    )
    distance_between_stirrers: float = Field(
        default=...,
        description="""Information about the distance, spacing or
        separation between the stirring rods or
        impellers within a reaction vessel or
        container.""",
    )
    distance_between_stirrers_unit: str = Field(
        default=...,
        description="""The distance between stirrers can be specified in
        mm (millimeters), cm (centimeters), or m
        (meters), depending on the size and scale
        of the stirring system.""",
    )
    stirrer_blade_pitch_angle: float = Field(
        default=...,
        description="""The pitch angle at which the blades or paddles
        of a stirring mechanism are positioned
        relative to the plane of rotation. It's
        typically expressed in ° (degrees).""",
    )
    number_of_stirrer_blades: float = Field(
        default=...,
        description="""The number of blades on each stirrer.""",
    )
    stirrer_blade_size: float = Field(
        default=...,
        description="""The size of the impeller blades in a stirred tank
        reactor.""",
    )
    stirrer_blade_size_unit: str = Field(
        default=...,
        description="""In the case of impellers in a stirred tank
        reactor, the diameter of the impeller
        blades is typically specified. This
        diameter can be measured in millimeters
        (mm) or centimeters (cm).""",
    )
    stirrer_geometry: str = Field(
        default=...,
        description="""There are various morphologies or geometries,
        such as radial impellers, axial impellers,
        helical ribbon impellers, paddle
        impellers, and more, depending on its
        design and intended purpose.""",
    )
    stirrer_speed: float = Field(
        default=...,
        description="""Specify the speed or frequency at which the
        stirring was conducted.""",
    )
    speed_unit: str = Field(
        default=...,
        description="""The unit for stirring speed can be expressed in
        RPM (revolutions per minute), Hz (Hertz),
        or rad/s (radians per second), depending
        on the measurement instruments and
        scientific conventions used.""",
    )
    height_of_stirrer_above_vessel_base: float = Field(
        default=...,
        description="""The vertical distance between the bottom of the
        vessel or container (where the reaction
        takes place) and the lowest point of the
        stirring element or stirrer, which is
        usually located just above the vessel
        base.""",
    )
    height_of_stirrer_above_vessel_base_unit: str = Field(
        default=...,
        description="""Common units for defining the vertical distance
        between the bottom of the vessel and
        the lowest point of the stirrer include:
        mm (millimeters), cm (centimeters) and
        m (meters).""",
    )
    power_per_volume: float = Field(
        default=...,
        description="""The amount of stirring power or energy input into
        a system per unit volume.""",
    )
    power_per_volume_unit: str = Field(
        default=...,
        description="""The units commonly used for expressing the
        stirring power are W/L (watts per liter)
        or kW/m³ (kilowatts per cubic meter).""",
    )
    stir_bar_size: float = Field(
        default=...,
        description="""""",
    )
    stir_bar_size_unit: float = Field(
        default=...,
        description="""""",
    )
    stir_bar_shape: str = Field(
        default=...,
        description="""The shape or configuration of the stir bar,
        whether it's cylindrical, octagonal,
        oval, or another shape. Different shapes
        can interact with the reaction mixture
        differently, influencing mixing patterns
        and efficiency.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the mechanically impelled
        mixing (stirring) that are important for
        reproducibility and are not described by
        the aforementioned metadata, they should
        be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:MechanicallyImpelledMixing/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:MechanicallyImpelledMixing",
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


class LiquidOrGasImpelledMixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    volume_of_liquid_solid_phase: str = Field(
        default=...,
        description="""In the context of enzymatic reactions or any
        chemical processes involving heterogeneous
        mixtures like a liquid and solid phase,
        essential parameters for describing the
        system involve the composition of the
        phases, the percentage or fraction of the
        total volume occupied by the liquid-solid
        phase mixture, and further information.""",
    )
    residence_time: float = Field(
        default=...,
        description="""The residence time, often denoted as "τ" (tau),
        refers to the average amount of time a
        substance or component spends inside a
        specific system or reactor and is to be
        specified.""",
    )
    residence_time_unit: str = Field(
        default=...,
        description="""The units for residence time can vary depending on
        the system and the units used for volume
        and flow rate. Common units include s
        (seconds), min (minutes), h (hours), or
        any time-related units.""",
    )
    reynolds_number: str = Field(
        default=...,
        description="""The Reynolds number (Re) is a dimensionless
        quantity used in fluid dynamics to predict
        the flow regime of a fluid within a
        specific system. It helps to determine
        whether the flow is laminar, turbulent, or
        somewhere in between.""",
    )
    passive_mixing: str = Field(
        default=...,
        description="""The design of the coils and the flow patterns
        created by the geometry of the tubing
        can lead to passive mixing as the fluid
        flows through the reactor without the
        need for external agitation. More detailed
        information must be provided to describe
        the process.""",
    )
    active_T_or_Y_mixer: str = Field(
        default=...,
        description="""Key features for describing an active Y or T mixer
        can include inlet ports, mixer chamber,
        outlet port, control, materials amon
        others.""",
    )
    pulsing: str = Field(
        default=...,
        description="""The pulsing process involves periodically
        injecting or introducing specific
        components, such as reactants or
        additives, into a reaction system at
        regular intervals or in a pulsatile
        manner. More detailed information must be
        provided to describe the process.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or
        aspects related to the liquid or gas
        impelled mixing that are important for
        reproducibility and are not described by
        the aforementioned metadata, they should
        be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:LiquidOrGasImpelledMixing/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:LiquidOrGasImpelledMixing",
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
    Vial,
    Plate,
    StirredTankReactor,
    TubularFlowContinuousReactor,
    Shaking,
    MechanicallyImpelledMixing,
    LiquidOrGasImpelledMixing,
]:
    cls.model_rebuild()
