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


class KineticParameters(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    michaelis_constant: float = Field(
        default=...,
        description="""The Michaelis-Menten constant (Km​) represents the
        substrate concentration at which an enzyme
        achieves half of its maximum reaction
        rate.""",
    )
    michaelis_constant_unit: str = Field(
        default=...,
        description="""The unit of the Michaelis-Menten constant (Km​) is
        typically expressed as moles per liter (M
        or mM).""",
    )
    maximum_reaction_rate: float = Field(
        default=...,
        description="""Vmax, the maximum reaction rate, represents
        the speed at which an enzyme-catalyzed
        reaction reaches saturation, indicating
        the maximum achievable rate of product
        formation under optimal substrate
        concentration (where enzymes are
        predominantly saturated with substrates).""",
    )
    maximum_reaction_rate_unit: str = Field(
        default=...,
        description="""The unit of Vmax (maximum reaction rate) is
        typically represented as concentration per
        time, such as moles per liter per second
        (mol/L/s or mM/s).""",
    )
    turnover_number: float = Field(
        default=...,
        description="""The turnover number (kcat) measures the number of
        substrate molecules converted to product
        per active site of an enzyme per unit
        time when the enzyme is fully saturated
        with substrate.""",
    )
    turnover_number_unit: str = Field(
        default=...,
        description="""The unit of turnover number (kcat) is typically
        expressed as moles of product per mole of
        enzyme per second or per minute (time-1).""",
    )
    catalytic_efficiency: float = Field(
        default=...,
        description="""Catalytic efficiency (kcat/Km) is a measure of how
        effectively an enzyme converts substrate
        into product, often quantified as the
        ratio of the turnover number (kcat) to the
        Michaelis-Menten constant (Km).""",
    )
    catalytic_efficiency_unit: str = Field(
        default=...,
        description="""The typical unit for catalytic efficiency (kcat/
        Km) is M-1s-1.""",
    )
    dissociation_constant: float = Field(
        default=...,
        description="""The dissociation constant (Kd) is a measure that
        represents the equilibrium between a
        complex and its dissociated components.""",
    )
    dissociation_constant_unit: str = Field(
        default=...,
        description="""The dissociation constant (Kd) is typically
        expressed in M (mol per liter) or its
        derivatives, such as nM (nanomoles per
        liter).""",
    )
    inhibition_type: str = Field(
        default=...,
        description="""Enzyme inhibition encompasses various forms,
        including competitive, non-competitive,
        uncompetitive, mixed, and irreversible
        inhibition. Each type has different
        effects on the enzyme's function and plays
        a crucial role in regulating biochemical
        processes.""",
    )
    inhibition_constant: float = Field(
        default=...,
        description="""The inhibition constant (Ki) describes the
        affinity of an inhibitor for an enzyme.
        It indicates how effectively an inhibitor
        influences enzyme activity. A lower Ki
        value suggests a strong binding of the
        inhibitor to the enzyme.""",
    )
    inhibition_constant_unit: str = Field(
        default=...,
        description="""The units for the inhibition constant (Ki) are
        commonly expressed in M (mol per liter) or
        related units.""",
    )
    hill_coefficient: float = Field(
        default=...,
        description="""The Hill coefficient is a parameter used to
        describe cooperativity in the binding
        of molecules to proteins. It is employed
        in enzyme reactions, e.g. oxygen binding
        to hemoglobin, to indicate whether there
        is positive (cooperative) or negative
        (anticooperative) binding. A Hill
        coefficient greater than 1 indicates
        positive cooperativity, while a value less
        than 1 indicates negative cooperativity.
        A value of exactly 1 indicates no
        cooperativity.""",
    )
    enzyme_stability: str = Field(
        default=...,
        description="""The stability of enzymes is often characterized
        by various parameters such as the enzyme's
        half-life under specific conditions, the
        decline in activity over time, or the
        preservation of catalytic activity under
        different environmental conditions.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific metrics,
        parameters, characteristics or aspects
        related to the kinetics that are important
        to document the results accurately and
        are not described by the aforementioned
        metadata, they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:KineticParameters/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:KineticParameters",
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


class YieldAndConversion(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    c_yield: float = Field(
        default=...,
        description="""Yield represents the amount of the desired
        product obtained from a reaction. It is
        the number of synthesized molecules of
        product per number of starting molecules.
        The following formula can be used: $$Y_p
        = \frac{n_p - n _ {p0}}{n _ {s0}} \cdot
        \frac{|v_s|}{|v_p|}$$ where, Yp - yield
        of the product p (-), np0 - amount of
        product p at the start of the reaction
        (mol), np - amount of product p at the end
        of the reaction (mol), vs - stoichiometric
        factor for the substrate s (-), vp -
        stoichiometric factor for the product
        p (-). Note: The reported yield relies
        on analytical findings. Typically, the
        isolated yield is more common in practice
        as it reflects the precise quantity
        of product acquired post downstream
        processing (DSP).""",
    )
    yield_unit: str = Field(
        default=...,
        description="""The yield is typically expressed in percentages
        (%), reflecting the ratio of the
        actual obtained product quantity to the
        theoretical maximum product quantity that
        could be obtained under ideal conditions.""",
    )
    space_time_yield: float = Field(
        default=...,
        description="""Space-time yield in biocatalysis refers to the
        mass of product obtained per unit volume
        of the reactor per unit time. Other
        terms commonly used in the literature are
        volumetric productivity or the reactor
        productivity . The following formula can
        be used: $$STY = \frac{m_p}{𝜏 \cdot V_R}$$
        where, STY - space-time yield (g L-1 h-1),
        mp - mass of the synthesized product (g),
        𝜏 - residence time r reaction time (h), VR
        - reactor volume.""",
    )
    space_time_yield_unit: str = Field(
        default=...,
        description="""Space-time yield is commonly expressed in g/L/
        h (grams per liter per hour) or mol/L/h
        (moles per liter per hour).""",
    )
    conversion: float = Field(
        default=...,
        description="""The term "conversion" refers to the percentage of
        substrate that undergoes transformation
        into the desired product during a
        reaction. It is the number of converted
        molecules per number of starting
        molecules. The following formula can be
        used: $$X_s = \frac{n _ {s0} - n_s}{n
        _ {s0}}$$ where, Xs - conversion of the
        substrate s (-), ns0 - amount of substrate
        s at the start of the reaction (mol), ns
        - amount of substrate s at the end of the
        reaction (mol).""",
    )
    conversion_unit: str = Field(
        default=...,
        description="""The conversion is commonly expressed as a
        percentage (%) to indicate the proportion
        of substrate converted to the desired
        product during a specific reaction.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific metrics,
        parameters, characteristics or aspects
        related to the conversion or yield that
        are important to document the results
        accurately and are not described by the
        aforementioned attributes, they should be
        explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:YieldAndConversion/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:YieldAndConversion",
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


class ActivityAndInitialReactionRate(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    specific_activity: float = Field(
        default=...,
        description="""The specific activity refers to the amount of
        product formed or substrate consumed per
        unit of enzyme per unit of time.""",
    )
    specific_activity_unit: str = Field(
        default=...,
        description="""The specific activity is typically expressed in
        µmol/min/mg (micromoles per minute per
        milligram of protein).""",
    )
    initial_reaction_rate: float = Field(
        default=...,
        description="""The initial reaction rate refers to the rate
        at which the product is formed in the
        first 10% of the enzymatic reaction under
        specific initial substrate concentrations
        and reaction conditions.""",
    )
    initial_reaction_rate_unit: str = Field(
        default=...,
        description="""Typically, the initial reaction rate is expressed
        as mol/L/min (moles per liter per minute)
        or µmol/mL/min (micromoles per milliliter
        per minute).""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific metrics,
        parameters, characteristics or aspects
        related to the activity or initial
        reaction rate that are important to
        document the results accurately and
        are not described by the aforementioned
        attributes, they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:ActivityAndInitialReactionRate/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:ActivityAndInitialReactionRate",
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


class SelectivityAndSpecificity(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    stereoselectivity: str = Field(
        default=...,
        description="""Stereoselectivity refers to the preference of a
        chemical reaction to produce a specific
        stereoisomer or a particular spatial
        arrangement of atoms within a molecule.
        It describes the ability of a reaction to
        favor the formation of one stereoisomer
        over others or to create a specific
        stereochemical outcome.""",
    )
    enantioselectivity: float = Field(
        default=...,
        description="""Enantioselectivity, or enantiomeric ratio (E),
        defines the enzyme's capability to
        preferentially catalyze the transformation
        of one enantiomer over its mirror-image
        counterpart. This trait highlights the
        enzyme's ability to favor a specific
        enantiomer either as a product or as the
        preferred substrate for a reaction.""",
    )
    enantiomeric_excess: float = Field(
        default=...,
        description="""The enantiomeric excess ( ee ) measures the degree
        of purity and efficiency in a chiral
        catalysis process, representing the excess
        of one enantiomer over the other in a
        reaction product. The following formula
        can be used: $$ee_R = \frac{n_R - n_S}
        {n_R + n_S}$$ where, eeR - enantiomeric
        excess of the ( R )-enantiomer (-), nR -
        amount of the ( R )-enatiomer (mol) and nS
        - amount of the ( S )-enatiomer (mol).""",
    )
    enantiomeric_excess_unit: str = Field(
        default=...,
        description="""The primary unit used for enantiomeric excess
        ( ee ) is percent (%).""",
    )
    diastereomeric_excess: float = Field(
        default=...,
        description="""The diasteriomeric excess ( de ) represents the
        difference in the concentration of one
        diastereomer over another in a reaction
        product. The following formula can be
        used: $$de_1 = \frac{n_1 - n_2}{n_1 +
        n_2}$$ where, de - diasteriomeric excess
        of the major diasteriomer (-), n1 - amount
        of the major diasteriomer (mol) and n2 -
        amount of the minor diasteriomer (mol).""",
    )
    diasteriomeric_excess_unit: str = Field(
        default=...,
        description="""The primary unit used for diasteriomeric excess
        ( ee ) is percent (%).""",
    )
    isomeric_content: float = Field(
        default=...,
        description="""The isomeric content ( ic ) refers to the
        percentage distribution or ratio of
        different isomers within a mixture
        resulting from a reaction or process.
        It describes how various isomers are
        represented in a product or mixture.
        The following formula can be used: $$ic
        = I_1 / \sum _ {i=1}^n I_i$$ where, ic
        - proportion of a specific isomer in a
        mixture of isomers (-), I1 - amount of the
        specific isomer (mol) and Ii - quantity of
        all isomers (mol).""",
    )
    isomeric_content_unit: str = Field(
        default=...,
        description="""The primary unit used for isomeric content ( ic )
        is percent (%).""",
    )
    chemoselectivity: str = Field(
        default=...,
        description="""Chemoselectivity refers to the ability of a
        chemical reaction to target a specific
        functional group or site within a molecule
        without affecting other reactive groups
        present. It highlights the preference
        of a reaction for one type of chemical
        bond or functional group over others in
        a molecule.""",
    )
    regioselectivity: str = Field(
        default=...,
        description="""Regioselectivity refers to the preference of
        a reaction to occur at a specific site
        within a molecule or compound that has
        multiple potential reaction sites. It
        describes the tendency of a reaction to
        selectively take place at a particular
        position of the molecule, considering
        its structural arrangement of atoms or
        functional groups, rather than at other
        possible sites.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific metrics,
        parameters, characteristics or aspects
        related to the selectivity and specificity
        that are important to document the results
        accurately and are not described by the
        aforementioned attributes, they should be
        explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:SelectivityAndSpecificity/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:SelectivityAndSpecificity",
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


class ThermodynamicParameters(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    gibbs_free_energy_change: str = Field(
        default=...,
        description="""The Gibbs free energy ( G ) represents the portion
        of energy capable of performing work in
        a reaction under constant temperature
        and pressure, providing insights into the
        spontaneity of the reaction. While the
        absolute value of the free energy cannot
        be measured directly, the change in free
        energy (Δ G ) throughout the reaction,
        known as free reaction enthalpy, is
        measurable. As indicated by the Gibbs-
        Helmholtz equation, it depends on changes
        in enthalpy (heat content) and entropy
        (system disorder) during the reaction. Δ G
        Δ G = 0: The system is at equilibrium; no
        work is performed. Δ G > 0: The reaction
        does not proceed spontaneously; it is
        endergonic . A supply of free energy is
        required to drive the reaction.""",
    )
    enthalpy_change: str = Field(
        default=...,
        description="""The enthalpy ( H ) represents the heat content
        within a system, expressing the quantity
        and nature of chemical bonds. This
        thermodynamic property cannot be measured
        independently. However, measurable is
        the change in enthalpy (Δ H ), which
        refers to the amount of heat absorbed or
        released during a chemical reaction (under
        constant pressure), also known as the
        reaction enthalpy. Δ H > 0: Heat energy
        is supplied; the reaction is endothermic .
        Δ H Δ S > 0: The disorder of the system
        increases. Δ S""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific metrics,
        parameters, characteristics or aspects
        related to the thermodynamic parameters
        that are important to document the results
        accurately and are not described by the
        aforementioned attributes, they should be
        explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:ThermodynamicParameters/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:ThermodynamicParameters",
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
    KineticParameters,
    YieldAndConversion,
    ActivityAndInitialReactionRate,
    SelectivityAndSpecificity,
    ThermodynamicParameters,
]:
    cls.model_rebuild()
